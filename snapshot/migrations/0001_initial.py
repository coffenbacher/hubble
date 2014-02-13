# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Snapshot'
        db.create_table(u'snapshot_snapshot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'snapshot', ['Snapshot'])

        # Adding model 'CosmosDir'
        db.create_table(u'snapshot_cosmosdir', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('snapshot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['snapshot.Snapshot'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='direct_children', null=True, to=orm['snapshot.CosmosDir'])),
            ('cold', self.gf('django.db.models.fields.FloatField')()),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'snapshot', ['CosmosDir'])


    def backwards(self, orm):
        # Deleting model 'Snapshot'
        db.delete_table(u'snapshot_snapshot')

        # Deleting model 'CosmosDir'
        db.delete_table(u'snapshot_cosmosdir')


    models = {
        u'snapshot.cosmosdir': {
            'Meta': {'object_name': 'CosmosDir'},
            'cold': ('django.db.models.fields.FloatField', [], {}),
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