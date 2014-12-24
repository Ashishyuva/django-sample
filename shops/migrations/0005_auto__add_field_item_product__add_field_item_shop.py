# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.product'
        db.add_column(u'shops_item', 'product',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['shops.Product']),
                      keep_default=False)

        # Adding field 'Item.shop'
        db.add_column(u'shops_item', 'shop',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['shops.Shop']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.product'
        db.delete_column(u'shops_item', 'product_id')

        # Deleting field 'Item.shop'
        db.delete_column(u'shops_item', 'shop_id')


    models = {
        u'shops.item': {
            'Meta': {'object_name': 'Item'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shops.Product']"}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shops.Shop']"})
        },
        u'shops.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'shops.shop': {
            'Meta': {'object_name': 'Shop'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['shops.Product']", 'symmetrical': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['shops']