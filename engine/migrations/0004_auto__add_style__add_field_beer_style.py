# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Style'
        db.create_table(u'engine_style', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'engine', ['Style'])

        # Adding field 'Beer.style'
        db.add_column(u'engine_beer', 'style',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Style'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Style'
        db.delete_table(u'engine_style')

        # Deleting field 'Beer.style'
        db.delete_column(u'engine_beer', 'style_id')


    models = {
        u'engine.beer': {
            'Meta': {'object_name': 'Beer'},
            'brewery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Brewery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['engine']