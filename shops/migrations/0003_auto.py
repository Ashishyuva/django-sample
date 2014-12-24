# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field products on 'Shop'
        m2m_table_name = db.shorten_name(u'shops_shop_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('shop', models.ForeignKey(orm[u'shops.shop'], null=False)),
            ('product', models.ForeignKey(orm[u'shops.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['shop_id', 'product_id'])


    def backwards(self, orm):
        # Removing M2M table for field products on 'Shop'
        db.delete_table(db.shorten_name(u'shops_shop_products'))


    models = {
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