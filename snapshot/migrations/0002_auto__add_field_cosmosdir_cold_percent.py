# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CosmosDir.cold_percent'
        db.add_column(u'snapshot_cosmosdir', 'cold_percent',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CosmosDir.cold_percent'
        db.delete_column(u'snapshot_cosmosdir', 'cold_percent')


    models = {
        u'snapshot.cosmosdir': {
            'Meta': {'object_name': 'CosmosDir'},
            'cold': ('django.db.models.fields.FloatField', [], {}),
            'cold_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'direct_children'", 'null': 'True', 'to': u"orm['snapshot.CosmosDir']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'snapshot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['snapshot.Snapshot']"}),
            'total': ('django.db.models.fields.FloatField', [], {})
        },
        u'snapshot.snapshot': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Snapshot'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        }
    }

    complete_apps = ['snapshot']