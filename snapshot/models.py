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
                    if float(row[2]) > 0:
                        CosmosDirTree.objects.get_or_create(snapshot = s, path = row[0], cold = row[1], total = row[2])

        print 'Deduping'
        CosmosDirTree.dedupe()

        print 'Creating graph'
        CosmosDirTree.create_graph()

class CosmosDirTree(models.Model):
    snapshot = models.ForeignKey('Snapshot')
    path = models.CharField(max_length=500)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
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
        return CosmosDirTree.objects.filter(
                Q(parent = self) |
                Q(parent__parent = self) | 
                Q(parent__parent__parent = self) | 
                Q(parent__parent__parent__parent = self) |
                Q(parent__parent__parent__parent__parent = self) 
                )
    def all_children_pks(self):
        return [a.pk for a in self.all_children()]

    def dedupe(self):
        CosmosDirTree.objects.filter(path = self.path).exclude(pk = self.pk).delete()

    def find_parent(self):
        p = '/'.join(self.path.split('/')[:-2]) + '/'
        par = CosmosDirTree.objects.filter(path=p)
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
            return 'cosmos11'

    def other_dc(self):
        if self.dc() == 'cosmos08':
            return 'cosmos11'
        else:
            return 'cosmos08'

    def other_cluster(self):
        search = self.path.replace(self.dc(), self.other_dc())
        dirs = CosmosDirTree.objects.filter(path = search)
        if dirs:
            return dirs[0]
        else:
            return False
