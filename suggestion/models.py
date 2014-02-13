from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from django.db import models
from django_extensions.db.models import TimeStampedModel
from snapshot.models import CosmosDir
# Create your models here.

STATUS_CHOICES = (
        (0, 'PENDING'),
        (1, 'COMPLETED'),
        (2, 'CANCELLED'),
        )

CERTAINTY_CHOICES = (
        (10, 'Highly aggressive'),
        (40, 'Aggressive'),
        (60, 'Conservative'),
        (90, 'Highly conservative'),
        (100, 'Absolutely sure'),
        )

class Suggestion(TimeStampedModel):
    """
    Suggestions are a way to recommend changes to directories.

    These are recursively considered to apply to subdirectories. Suggestions on subdirectories will be ignored.
    """
    cosmosdir = models.ForeignKey(CosmosDir, related_name='suggestions')

    certainty = models.IntegerField(choices=CERTAINTY_CHOICES, default=40)

    ignore = models.BooleanField(default=True, verbose_name="At least some subdirectories are efficiently utilized. If so, you're done here.")
    delete_all = models.BooleanField(default=False, verbose_name='Delete this directory and its subdirectories.')
    replication = models.IntegerField(default=3)
    retention_percent = models.FloatField(blank=True, null=True, verbose_name='Retention as a percentage of current (i.e. 0.5).')

    proposed_by = models.CharField(max_length=200, default='coffen')
    required_signoffs = models.CharField(max_length=400, null=True, blank=True)
    signoffs = models.CharField(max_length=400, null=True, blank=True)

    notes = models.TextField(null=True, blank=True)

    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    savings = models.FloatField(default=0)

    def __unicode__(self):
        return '%s suggestion to save %s TiBs: %s' % (self.certainty, self.savings, self.cosmosdir.path)

    @classmethod
    def set_savings_all(cls):
        for s in cls.objects.all():
            s.set_savings()

    def set_savings(self):
        if self.ignore:
            self.savings = 0
        elif self.delete_all:
            self.savings = self.cosmosdir.total
        else:
            if self.retention_percent and self.replication == 3:
                self.savings = self.cosmosdir.total * (1 - self.retention_percent)
            if self.retention_percent and self.replication != 3:
                self.savings = self.cosmosdir.total * (1 - self.retention_percent) + (self.cosmosdir.total * self.retention_percent * self.replication / 3.0)
            if not self.retention_percent and self.replication != 3:
                self.savings = self.cosmosdir.total * (3 - self.replication) / 3.0
        
        self.save()

    @classmethod
    def calculate_savings(cls, suggestions):
        """Calculate savings for a group of suggestions.
        Key here is that in the current implementation, do NOT count
        children's contributions to the total. Only count parents. This 
        is not strictly true but it is better to undercount at the moment,
        and this should definitively do that.
        
        When in doubt, use the more aggressive suggestion.
        
        This method is very inefficient at the moment, may choke on 
        high numbers of suggestions."""

        all_children_pks = []

        # We want to skip the pks of all dirs where suggestions are active on a parent
        for s in suggestions.filter(ignore=False):
            all_children_pks.extend(s.cosmosdir.all_children_pks())

        total = 0
        for s in suggestions.filter(ignore=False).order_by('cosmosdir', 'certainty').distinct('cosmosdir'):
            print s.cosmosdir.pk, all_children_pks
            if s.cosmosdir.pk not in all_children_pks:
                total += s.savings

        return total

    def verbose(self):
        if self.ignore:
            return "This directory is said to be well-utilized."
        elif self.delete_all:
            return "This directory is a candidate for total deletion."

#class SuggestionSet(TimeStampedModel):
#    name = models.CharField(max_length=200)
#    suggestions = models.ManyToManyField(Suggestion)

class SuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        exclude = ('savings',)

    def __init__(self, *args, **kwargs):
        super(SuggestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class='col-lg-2'
        self.helper.field_class='col-lg-8'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn-success col-lg-offset-2'))
