# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Beer.description'
        db.add_column(u'engine_beer', 'description',
                      self.gf('django.db.models.fields.CharField')(default='No description provided.', max_length=2000),
                      keep_default=False)

        # Adding field 'Beer.abv'
        db.add_column(u'engine_beer', 'abv',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Beer.ibu'
        db.add_column(u'engine_beer', 'ibu',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Beer.srm'
        db.add_column(u'engine_beer', 'srm',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Beer.description'
        db.delete_column(u'engine_beer', 'description')

        # Deleting field 'Beer.abv'
        db.delete_column(u'engine_beer', 'abv')

        # Deleting field 'Beer.ibu'
        db.delete_column(u'engine_beer', 'ibu')

        # Deleting field 'Beer.srm'
        db.delete_column(u'engine_beer', 'srm')


    models = {
        u'engine.beer': {
            'Meta': {'object_name': 'Beer'},
            'abv': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'brewery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Brewery']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'No description provided.'", 'max_length': '2000'}),
            'ibu': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'srm': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
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