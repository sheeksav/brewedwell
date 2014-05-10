# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Beer'
        db.create_table(u'engine_beer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brewery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Brewery'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'engine', ['Beer'])


    def backwards(self, orm):
        # Deleting model 'Beer'
        db.delete_table(u'engine_beer')


    models = {
        u'engine.beer': {
            'Meta': {'object_name': 'Beer'},
            'brewery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Brewery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'engine.brewery': {
            'Meta': {'object_name': 'Brewery'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['engine']