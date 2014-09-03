# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TrackProduct'
        db.create_table(u'producttracker_trackproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lcbo_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('track', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'producttracker', ['TrackProduct'])

        # Adding model 'Product'
        db.create_table(u'producttracker_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lcbo_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('is_dead', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('is_discontinued', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('price_in_cents', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('regular_price_in_cents', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('limited_time_offer_savings_in_cents', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('limited_time_offer_ends_on', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bonus_reward_miles', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bonus_reward_miles_ends_on', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('stock_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('primary_category', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('secondary_category', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('package', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('package_unit_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('package_unit_volume_in_milliliters', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_package_units', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volume_in_milliliters', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('alcohol_content', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('price_per_liter_of_alcohol_in_cents', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('price_per_liter_in_cents', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('inventory_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('inventory_volume_in_milliliters', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('inventory_price_in_cents', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sugar_content', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('producer_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('released_on', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('has_value_added_promotion', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('has_limited_time_offer', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('has_bonus_reward_miles', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('is_seasonal', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('is_vqa', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('is_kosher', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('value_added_promotion_description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('serving_suggestion', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('tasting_note', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('updated_at', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image_thumb_url', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('varietal', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tertiary_category', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sugar_in_grams_per_liter', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('clearance_sale_savings_in_cents', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('has_clearance_sale', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('product_no', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'producttracker', ['Product'])

        # Adding model 'StoreInventory'
        db.create_table(u'producttracker_storeinventory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lcbo_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('store_no', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('updated_on', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('updated_at', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'producttracker', ['StoreInventory'])


    def backwards(self, orm):
        # Deleting model 'TrackProduct'
        db.delete_table(u'producttracker_trackproduct')

        # Deleting model 'Product'
        db.delete_table(u'producttracker_product')

        # Deleting model 'StoreInventory'
        db.delete_table(u'producttracker_storeinventory')


    models = {
        u'producttracker.product': {
            'Meta': {'object_name': 'Product'},
            'alcohol_content': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bonus_reward_miles': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bonus_reward_miles_ends_on': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'clearance_sale_savings_in_cents': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'has_bonus_reward_miles': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'has_clearance_sale': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'has_limited_time_offer': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'has_value_added_promotion': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_thumb_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'inventory_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'inventory_price_in_cents': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'inventory_volume_in_milliliters': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_dead': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_discontinued': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_kosher': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_seasonal': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_vqa': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'lcbo_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'limited_time_offer_ends_on': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'limited_time_offer_savings_in_cents': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'package': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'package_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'package_unit_volume_in_milliliters': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price_in_cents': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price_per_liter_in_cents': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price_per_liter_of_alcohol_in_cents': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'primary_category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'producer_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'product_no': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'regular_price_in_cents': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'released_on': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'secondary_category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'serving_suggestion': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'stock_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sugar_content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sugar_in_grams_per_liter': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'tasting_note': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'tertiary_category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'total_package_units': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'value_added_promotion_description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'varietal': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'volume_in_milliliters': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'producttracker.storeinventory': {
            'Meta': {'object_name': 'StoreInventory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcbo_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'store_no': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_on': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'producttracker.trackproduct': {
            'Meta': {'object_name': 'TrackProduct'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcbo_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'track': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['producttracker']