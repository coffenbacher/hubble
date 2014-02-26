# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CosmosDirTree.rght'
        db.delete_column(u'snapshot_cosmosdirtree', u'rght')

        # Deleting field 'CosmosDirTree.tree_id'
        db.delete_column(u'snapshot_cosmosdirtree', u'tree_id')

        # Deleting field 'CosmosDirTree.lft'
        db.delete_column(u'snapshot_cosmosdirtree', u'lft')

        # Deleting field 'CosmosDirTree.level'
        db.delete_column(u'snapshot_cosmosdirtree', u'level')


        # Changing field 'CosmosDirTree.parent'
        db.alter_column(u'snapshot_cosmosdirtree', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['snapshot.CosmosDirTree']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'CosmosDirTree.rght'
        raise RuntimeError("Cannot reverse this migration. 'CosmosDirTree.rght' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CosmosDirTree.rght'
        db.add_column(u'snapshot_cosmosdirtree', u'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CosmosDirTree.tree_id'
        raise RuntimeError("Cannot reverse this migration. 'CosmosDirTree.tree_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CosmosDirTree.tree_id'
        db.add_column(u'snapshot_cosmosdirtree', u'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CosmosDirTree.lft'
        raise RuntimeError("Cannot reverse this migration. 'CosmosDirTree.lft' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CosmosDirTree.lft'
        db.add_column(u'snapshot_cosmosdirtree', u'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CosmosDirTree.level'
        raise RuntimeError("Cannot reverse this migration. 'CosmosDirTree.level' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CosmosDirTree.level'
        db.add_column(u'snapshot_cosmosdirtree', u'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True),
                      keep_default=False)


        # Changing field 'CosmosDirTree.parent'
        db.alter_column(u'snapshot_cosmosdirtree', 'parent_id', self.gf('mptt.fields.TreeForeignKey')(null=True, to=orm['snapshot.CosmosDirTree']))

    models = {
        u'snapshot.cosmosdirtree': {
            'Meta': {'object_name': 'CosmosDirTree'},
            'cold': ('django.db.models.fields.FloatField', [], {}),
            'cold_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'exclude_from_analysis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['snapshot.CosmosDirTree']"}),
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
        }
    }

    complete_apps = ['snapshot']