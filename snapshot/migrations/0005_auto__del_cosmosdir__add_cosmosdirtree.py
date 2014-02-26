# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CosmosDir'
        db.delete_table(u'snapshot_cosmosdir')

        # Adding model 'CosmosDirTree'
        db.create_table(u'snapshot_cosmosdirtree', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('snapshot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['snapshot.Snapshot'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['snapshot.CosmosDirTree'])),
            ('cold', self.gf('django.db.models.fields.FloatField')()),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('exclude_from_analysis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cold_percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('score_deletion', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'snapshot', ['CosmosDirTree'])


    def backwards(self, orm):
        # Adding model 'CosmosDir'
        db.create_table(u'snapshot_cosmosdir', (
            ('cold_percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('snapshot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['snapshot.Snapshot'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', null=True, to=orm['snapshot.CosmosDir'], blank=True)),
            ('exclude_from_analysis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('cold', self.gf('django.db.models.fields.FloatField')()),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score_deletion', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'snapshot', ['CosmosDir'])

        # Deleting model 'CosmosDirTree'
        db.delete_table(u'snapshot_cosmosdirtree')


    models = {
        u'snapshot.cosmosdirtree': {
            'Meta': {'object_name': 'CosmosDirTree'},
            'cold': ('django.db.models.fields.FloatField', [], {}),
            'cold_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'exclude_from_analysis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['snapshot.CosmosDirTree']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'score_deletion': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'snapshot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['snapshot.Snapshot']"}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'snapshot.snapshot': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Snapshot'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        }
    }

    complete_apps = ['snapshot']