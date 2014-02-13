import csv
from django.db.models.query import Q
from django_extensions.db.models import TimeStampedModel
from django.db import models

# Create your models here.
class Snapshot(TimeStampedModel):

    @classmethod
    def load_csv(cls, filename):
        s = cls.objects.create()
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] != 'path':
                    CosmosDir.objects.get_or_create(snapshot = s, path = row[0], cold = row[1], total = row[2])

        print 'Deduping'
        CosmosDir.dedupe()

        print 'Creating graph'
        CosmosDir.create_graph()

class CosmosDir(models.Model):
    snapshot = models.ForeignKey('Snapshot')
    path = models.CharField(max_length=500)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    cold = models.FloatField()
    total = models.FloatField()
    exclude_from_analysis = models.BooleanField(default=False)
    cold_percent = models.FloatField(blank=True, null=True)
    score_deletion = models.FloatField(blank=True, null=True)

    @classmethod
    def calculate_scores(cls):
        for o in cls.objects.all():
            o.__calculate_scores()

    @classmethod
    def create_graph(cls):
        for o in cls.objects.all():
            o.find_parent()

    @classmethod
    def dedupe_all(cls):
        for o in cls.objects.all():
            o.dedupe()

    def all_children(self):
        # This is a hack to avoid doing something smarter tonight
        children = CosmosDir.objects.filter(
                Q(parent = self) |
                Q(parent__parent = self) |
                Q(parent__parent__parent = self) |
                Q(parent__parent__parent__parent = self)
                )
        return children

    def all_children_pks(self):
        allcs = self.all_children()
        return [a.pk for a in allcs]

    def dedupe(self):
        CosmosDir.objects.filter(path = self.path).exclude(pk = self.pk).delete()

    def find_parent(self):
        p = '/'.join(self.path.split('/')[:-2]) + '/'
        par = CosmosDir.objects.filter(path=p)
        if par.exists():
            self.parent = par[0]
            if par[0].pk == self.pk:
                print par[0].path, self.path
                raise Exception
            self.save()
        else:
            self.parent = None
            self.save()
            print 'no parent found for path %s' % p

    def __calculate_scores(self):
        self.cold_percent = self.cold / self.total
        self.score_deletion = self.cold_percent * 100 + self.cold
        self.save()

    def __unicode__(self):
        return self.path

    def dc(self):
        if 'http://cosmos08' in self.path:
            return 'cosmos08'
        else:
            return 'cosmos10'

    def other_dc(self):
        if self.dc() == 'cosmos08':
            return 'cosmos10'
        else:
            return 'cosmos08'

    def other_cluster(self):
        search = self.path.replace(self.dc(), self.other_dc())
        dirs = CosmosDir.objects.filter(path = search)
        if dirs:
            return dirs[0]
        else:
            return False
