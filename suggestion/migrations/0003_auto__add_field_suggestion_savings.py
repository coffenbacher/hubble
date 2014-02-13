# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Suggestion.savings'
        db.add_column(u'suggestion_suggestion', 'savings',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Suggestion.savings'
        db.delete_column(u'suggestion_suggestion', 'savings')


    models = {
        u'snapshot.cosmosdir': {
            'Meta': {'object_name': 'CosmosDir'},
            'cold': ('django.db.models.fields.FloatField', [], {}),
            'cold_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['snapshot.CosmosDir']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'score_deletion': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'snapshot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['snapshot.Snapshot']"}),
            'total': ('django.db.models.fields.FloatField', [], {})
        },
        u'snapshot.snapshot': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Snapshot'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'suggestion.suggestion': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Suggestion'},
            'certainty': ('django.db.models.fields.IntegerField', [], {'default': '40'}),
            'cosmosdir': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'suggestions'", 'to': u"orm['snapshot.CosmosDir']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'delete_all': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignore': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'proposed_by': ('django.db.models.fields.CharField', [], {'default': "'coffen'", 'max_length': '200'}),
            'replication': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'required_signoffs': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'retention_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'savings': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'signoffs': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['suggestion']