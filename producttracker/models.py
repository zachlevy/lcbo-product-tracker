from django.db import models

# Create your models here.

class TrackProduct(models.Model):
	lcbo_id = models.IntegerField(default=0)
	track = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
	lcbo_id = models.IntegerField(default=0)
	name = models.CharField(max_length=200) #Sage Cranberry Blackcurrant
	tags = models.CharField(max_length=1000) #sage cranberry blackcurrant ready to drinkcoolers ready-to-drinkcoolers readytodrinkcoolers one pour cocktails canada ontario mixology bottle
	is_dead = models.NullBooleanField(default=False) #false
	is_discontinued = models.NullBooleanField(default=False) #false
	price_in_cents = models.IntegerField(default=0) #1395
	regular_price_in_cents = models.IntegerField(default=0) #1395
	limited_time_offer_savings_in_cents = models.IntegerField(default=0) #0
	limited_time_offer_ends_on = models.CharField(max_length=200) #null
	bonus_reward_miles = models.IntegerField(default=0) #0
	bonus_reward_miles_ends_on = models.CharField(max_length=200) #null
	stock_type = models.CharField(max_length=200) #LCBO
	primary_category = models.CharField(max_length=200) #Ready-to-Drink/Coolers
	secondary_category = models.CharField(max_length=200) #One Pour Cocktails
	origin = models.CharField(max_length=200) #Canada Ontario
	package = models.CharField(max_length=200) #750 mL bottle
	package_unit_type = models.CharField(max_length=200) #bottle
	package_unit_volume_in_milliliters = models.IntegerField(default=0) #750
	total_package_units = models.IntegerField(default=0) #1
	volume_in_milliliters = models.IntegerField(default=0) #750
	alcohol_content = models.IntegerField(default=0) #1000
	price_per_liter_of_alcohol_in_cents = models.IntegerField(default=0) #1860
	price_per_liter_in_cents = models.IntegerField(default=0) #1860
	inventory_count = models.IntegerField(default=0) #785
	inventory_volume_in_milliliters = models.IntegerField(default=0) #588750
	inventory_price_in_cents = models.IntegerField(default=0) #1095075
	sugar_content = models.CharField(max_length=200) #null
	producer_name = models.CharField(max_length=200) #Sage Mixology
	released_on = models.CharField(max_length=200) #null
	has_value_added_promotion = models.NullBooleanField(default=False) #false
	has_limited_time_offer = models.NullBooleanField(default=False) #false
	has_bonus_reward_miles = models.NullBooleanField(default=False) #false
	is_seasonal = models.NullBooleanField(default=False) #false
	is_vqa = models.NullBooleanField(default=False) #false
	is_kosher = models.NullBooleanField(default=False) #false
	value_added_promotion_description = models.CharField(max_length=2000) #null
	description = models.CharField(max_length=2000) #null
	serving_suggestion = models.CharField(max_length=2000) #null
	tasting_note = models.CharField(max_length=2000) #null
	updated_at = models.CharField(max_length=200) #2014-09-02T14:27:30.335Z
	image_thumb_url = models.CharField(max_length=1000) #null
	image_url = models.CharField(max_length=1000) #null
	varietal = models.CharField(max_length=200) #Medium Sweet
	style = models.CharField(max_length=200) #null
	tertiary_category = models.CharField(max_length=200) #Fruity
	sugar_in_grams_per_liter = models.CharField(max_length=200) #null
	clearance_sale_savings_in_cents = models.IntegerField(default=0) #0
	has_clearance_sale = models.NullBooleanField(default=False) #false
	product_no = models.IntegerField(default=0) #372078
	created = models.DateTimeField(auto_now_add=True)

class StoreInventory(models.Model):
	lcbo_id = models.IntegerField(default=0)
	store_no = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)
	updated_on = models.CharField(max_length=200)
	updated_at = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
