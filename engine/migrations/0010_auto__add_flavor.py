# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Flavor'
        db.create_table(u'engine_flavor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Beer'])),
            ('acidity', self.gf('django.db.models.fields.IntegerField')()),
            ('alcohol', self.gf('django.db.models.fields.IntegerField')()),
            ('balance', self.gf('django.db.models.fields.IntegerField')()),
            ('biscuit', self.gf('django.db.models.fields.IntegerField')()),
            ('bitter', self.gf('django.db.models.fields.IntegerField')()),
            ('body', self.gf('django.db.models.fields.IntegerField')()),
            ('bread', self.gf('django.db.models.fields.IntegerField')()),
            ('burnt', self.gf('django.db.models.fields.IntegerField')()),
            ('butter', self.gf('django.db.models.fields.IntegerField')()),
            ('caramel', self.gf('django.db.models.fields.IntegerField')()),
            ('chocolate', self.gf('django.db.models.fields.IntegerField')()),
            ('citrus', self.gf('django.db.models.fields.IntegerField')()),
            ('clove', self.gf('django.db.models.fields.IntegerField')()),
            ('coconut', self.gf('django.db.models.fields.IntegerField')()),
            ('coffee', self.gf('django.db.models.fields.IntegerField')()),
            ('crisp', self.gf('django.db.models.fields.IntegerField')()),
            ('dark_fruit', self.gf('django.db.models.fields.IntegerField')()),
            ('dry', self.gf('django.db.models.fields.IntegerField')()),
            ('earthy', self.gf('django.db.models.fields.IntegerField')()),
            ('finish', self.gf('django.db.models.fields.IntegerField')()),
            ('fruit', self.gf('django.db.models.fields.IntegerField')()),
            ('graham_cracker', self.gf('django.db.models.fields.IntegerField')()),
            ('grass', self.gf('django.db.models.fields.IntegerField')()),
            ('herbal', self.gf('django.db.models.fields.IntegerField')()),
            ('hop', self.gf('django.db.models.fields.IntegerField')()),
            ('licorice', self.gf('django.db.models.fields.IntegerField')()),
            ('malt', self.gf('django.db.models.fields.IntegerField')()),
            ('nutty', self.gf('django.db.models.fields.IntegerField')()),
            ('oak', self.gf('django.db.models.fields.IntegerField')()),
            ('pine', self.gf('django.db.models.fields.IntegerField')()),
            ('refreshing', self.gf('django.db.models.fields.IntegerField')()),
            ('resin', self.gf('django.db.models.fields.IntegerField')()),
            ('richness', self.gf('django.db.models.fields.IntegerField')()),
            ('roast', self.gf('django.db.models.fields.IntegerField')()),
            ('robust', self.gf('django.db.models.fields.IntegerField')()),
            ('salt', self.gf('django.db.models.fields.IntegerField')()),
            ('silk', self.gf('django.db.models.fields.IntegerField')()),
            ('smoke', self.gf('django.db.models.fields.IntegerField')()),
            ('sour', self.gf('django.db.models.fields.IntegerField')()),
            ('spice', self.gf('django.db.models.fields.IntegerField')()),
            ('sweet', self.gf('django.db.models.fields.IntegerField')()),
            ('syrup', self.gf('django.db.models.fields.IntegerField')()),
            ('tart', self.gf('django.db.models.fields.IntegerField')()),
            ('toast', self.gf('django.db.models.fields.IntegerField')()),
            ('toffee', self.gf('django.db.models.fields.IntegerField')()),
            ('vanilla', self.gf('django.db.models.fields.IntegerField')()),
            ('vinous', self.gf('django.db.models.fields.IntegerField')()),
            ('warmth', self.gf('django.db.models.fields.IntegerField')()),
            ('wheat', self.gf('django.db.models.fields.IntegerField')()),
            ('yeast', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'engine', ['Flavor'])


    def backwards(self, orm):
        # Deleting model 'Flavor'
        db.delete_table(u'engine_flavor')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'engine.beer': {
            'Meta': {'object_name': 'Beer'},
            'abv': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'brewery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Brewery']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'No description provided.'", 'max_length': '2000'}),
            'dislikes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ibu': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'saves': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'srm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Style']", 'null': 'True'})
        },
        u'engine.brewery': {
            'Meta': {'object_name': 'Brewery'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'engine.flavor': {
            'Meta': {'object_name': 'Flavor'},
            'acidity': ('django.db.models.fields.IntegerField', [], {}),
            'alcohol': ('django.db.models.fields.IntegerField', [], {}),
            'balance': ('django.db.models.fields.IntegerField', [], {}),
            'beer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Beer']"}),
            'biscuit': ('django.db.models.fields.IntegerField', [], {}),
            'bitter': ('django.db.models.fields.IntegerField', [], {}),
            'body': ('django.db.models.fields.IntegerField', [], {}),
            'bread': ('django.db.models.fields.IntegerField', [], {}),
            'burnt': ('django.db.models.fields.IntegerField', [], {}),
            'butter': ('django.db.models.fields.IntegerField', [], {}),
            'caramel': ('django.db.models.fields.IntegerField', [], {}),
            'chocolate': ('django.db.models.fields.IntegerField', [], {}),
            'citrus': ('django.db.models.fields.IntegerField', [], {}),
            'clove': ('django.db.models.fields.IntegerField', [], {}),
            'coconut': ('django.db.models.fields.IntegerField', [], {}),
            'coffee': ('django.db.models.fields.IntegerField', [], {}),
            'crisp': ('django.db.models.fields.IntegerField', [], {}),
            'dark_fruit': ('django.db.models.fields.IntegerField', [], {}),
            'dry': ('django.db.models.fields.IntegerField', [], {}),
            'earthy': ('django.db.models.fields.IntegerField', [], {}),
            'finish': ('django.db.models.fields.IntegerField', [], {}),
            'fruit': ('django.db.models.fields.IntegerField', [], {}),
            'graham_cracker': ('django.db.models.fields.IntegerField', [], {}),
            'grass': ('django.db.models.fields.IntegerField', [], {}),
            'herbal': ('django.db.models.fields.IntegerField', [], {}),
            'hop': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licorice': ('django.db.models.fields.IntegerField', [], {}),
            'malt': ('django.db.models.fields.IntegerField', [], {}),
            'nutty': ('django.db.models.fields.IntegerField', [], {}),
            'oak': ('django.db.models.fields.IntegerField', [], {}),
            'pine': ('django.db.models.fields.IntegerField', [], {}),
            'refreshing': ('django.db.models.fields.IntegerField', [], {}),
            'resin': ('django.db.models.fields.IntegerField', [], {}),
            'richness': ('django.db.models.fields.IntegerField', [], {}),
            'roast': ('django.db.models.fields.IntegerField', [], {}),
            'robust': ('django.db.models.fields.IntegerField', [], {}),
            'salt': ('django.db.models.fields.IntegerField', [], {}),
            'silk': ('django.db.models.fields.IntegerField', [], {}),
            'smoke': ('django.db.models.fields.IntegerField', [], {}),
            'sour': ('django.db.models.fields.IntegerField', [], {}),
            'spice': ('django.db.models.fields.IntegerField', [], {}),
            'sweet': ('django.db.models.fields.IntegerField', [], {}),
            'syrup': ('django.db.models.fields.IntegerField', [], {}),
            'tart': ('django.db.models.fields.IntegerField', [], {}),
            'toast': ('django.db.models.fields.IntegerField', [], {}),
            'toffee': ('django.db.models.fields.IntegerField', [], {}),
            'vanilla': ('django.db.models.fields.IntegerField', [], {}),
            'vinous': ('django.db.models.fields.IntegerField', [], {}),
            'warmth': ('django.db.models.fields.IntegerField', [], {}),
            'wheat': ('django.db.models.fields.IntegerField', [], {}),
            'yeast': ('django.db.models.fields.IntegerField', [], {})
        },
        u'engine.history': {
            'Meta': {'object_name': 'History'},
            'beer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Beer']"}),
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'engine.style': {
            'Meta': {'object_name': 'Style'},
            'description': ('django.db.models.fields.CharField', [], {'default': "'No description provided.'", 'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['engine']