# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Beer.srm'
        db.alter_column(u'engine_beer', 'srm', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Beer.abv'
        db.alter_column(u'engine_beer', 'abv', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Beer.ibu'
        db.alter_column(u'engine_beer', 'ibu', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'Beer.srm'
        db.alter_column(u'engine_beer', 'srm', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Beer.abv'
        db.alter_column(u'engine_beer', 'abv', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Beer.ibu'
        db.alter_column(u'engine_beer', 'ibu', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'engine.beer': {
            'Meta': {'object_name': 'Beer'},
            'abv': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'brewery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Brewery']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'No description provided.'", 'max_length': '2000'}),
            'ibu': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'srm': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Style']", 'null': 'True'})
        },
        u'engine.brewery': {
            'Meta': {'object_name': 'Brewery'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'engine.style': {
            'Meta': {'object_name': 'Style'},
            'description': ('django.db.models.fields.CharField', [], {'default': "'No description provided.'", 'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['engine']