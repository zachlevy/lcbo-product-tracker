from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
import string
import urllib2
import json
from producttracker.models import TrackProduct, Product, StoreInventory

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def product(request, product_id):
	product = Product.objects.get(lcbo_id=product_id)
	inventory = StoreInventory.objects.filter(lcbo_id=product_id)
	for store in inventory:
		print store.id
	return HttpResponse("Product updated: " + str(product.updated_at))

def update_inventory(request, product_id):
	json_string = urllib2.urlopen('http://lcboapi.com/products/' + product_id + "/inventories?per_page=100")
	data = json.load(json_string)
	#print data['result']['product_id']
	'''
	for key in data['result']:
		print key
		print data['result'][key]
	'''
	save_errors = {}
	for store in data['result']:
		si = StoreInventory(
			lcbo_id = store['product_id'],
			store_no = store['store_id'],
			quantity = store['quantity'] if store['quantity'] else 0,
			updated_on = store['updated_on'] if store['updated_on'] else "",
			updated_at = store['updated_at'] if store['updated_at'] else "",
		)
		try:
			si.save() # Could throw exception
		except:
			print "store" + si.store_no + "errored"
	return HttpResponse("updated inventory: ")

def update_product(request, product_id):
	last = Product.objects.filter(lcbo_id=product_id).order_by('-id')[0]
	json_string = urllib2.urlopen('http://lcboapi.com/products/' + product_id)
	data = json.load(json_string)
	#data['result'] = data['result']
	#data = json.loads(json_string)
	for key in data['result']:
		print key
		print data['result'][key]
	if (data['result']['limited_time_offer_ends_on'] is None):
		data['result']['limited_time_offer_ends_on'] = ""
	if (data['result']['bonus_reward_miles'] is None):
		data['result']['bonus_reward_miles'] = 0
	if (data['result']['bonus_reward_miles_ends_on'] is None):
		data['result']['bonus_reward_miles_ends_on'] = ""
	if (data['result']['sugar_content'] is None):
		data['result']['sugar_content'] = ""
	if (data['result']['released_on'] is None):
		data['result']['released_on'] = ""
	if (data['result']['value_added_promotion_description'] is None):
		data['result']['value_added_promotion_description'] = ""
	if (data['result']['description'] is None):
		data['result']['description'] = ""
	if (data['result']['serving_suggestion'] is None):
		data['result']['serving_suggestion'] = ""
	if (data['result']['tasting_note'] is None):
		data['result']['tasting_note'] = ""
	if (data['result']['image_thumb_url'] is None):
		data['result']['image_thumb_url'] = ""
	if (data['result']['image_url'] is None):
		data['result']['image_url'] = ""
	if (data['result']['style'] is None):
		data['result']['style'] = ""
	if (data['result']['sugar_in_grams_per_liter'] is None):
		data['result']['sugar_in_grams_per_liter'] = ""

	#check if the query is new
	if (data['result']['updated_at'] == last.updated_at):
		return HttpResponse("already recent as of " + data['result']['updated_at'])

	p = Product(
		lcbo_id = data['result']['id'],
		name = data['result']['name'],
		tags = data['result']['tags'],
		is_dead = data['result']['is_dead'],
		is_discontinued = data['result']['is_discontinued'],
		price_in_cents = data['result']['price_in_cents'],
		regular_price_in_cents = data['result']['regular_price_in_cents'],
		limited_time_offer_savings_in_cents = data['result']['limited_time_offer_savings_in_cents'],
		limited_time_offer_ends_on = data['result']['limited_time_offer_ends_on'],
		bonus_reward_miles = data['result']['bonus_reward_miles'],
		bonus_reward_miles_ends_on = data['result']['bonus_reward_miles_ends_on'],
		stock_type = data['result']['stock_type'],
		primary_category = data['result']['primary_category'],
		secondary_category = data['result']['secondary_category'],
		origin = data['result']['origin'],
		package = data['result']['package'],
		package_unit_type = data['result']['package_unit_type'],
		package_unit_volume_in_milliliters = data['result']['package_unit_volume_in_milliliters'],
		total_package_units = data['result']['total_package_units'],
		volume_in_milliliters = data['result']['volume_in_milliliters'],
		alcohol_content = data['result']['alcohol_content'],
		price_per_liter_of_alcohol_in_cents = data['result']['price_per_liter_of_alcohol_in_cents'],
		price_per_liter_in_cents = data['result']['price_per_liter_in_cents'],
		inventory_count = data['result']['inventory_count'],
		inventory_volume_in_milliliters = data['result']['inventory_volume_in_milliliters'],
		inventory_price_in_cents = data['result']['inventory_price_in_cents'],
		sugar_content = data['result']['sugar_content'],
		producer_name = data['result']['producer_name'],
		released_on = data['result']['released_on'],
		has_value_added_promotion = data['result']['has_value_added_promotion'],
		has_limited_time_offer = data['result']['has_limited_time_offer'],
		has_bonus_reward_miles = data['result']['has_bonus_reward_miles'],
		is_seasonal = data['result']['is_seasonal'],
		is_vqa = data['result']['is_vqa'],
		is_kosher = data['result']['is_kosher'],
		value_added_promotion_description = data['result']['value_added_promotion_description'],
		description = data['result']['description'],
		serving_suggestion = data['result']['serving_suggestion'],
		tasting_note = data['result']['tasting_note'],
		updated_at = data['result']['updated_at'],
		image_thumb_url = data['result']['image_thumb_url'],
		image_url = data['result']['image_url'],
		varietal = data['result']['varietal'],
		style = data['result']['style'],
		tertiary_category = data['result']['tertiary_category'],
		sugar_in_grams_per_liter = data['result']['sugar_in_grams_per_liter'],
		clearance_sale_savings_in_cents = data['result']['clearance_sale_savings_in_cents'],
		has_clearance_sale = data['result']['has_clearance_sale'],
		product_no = data['result']['product_no'],
	)
	p.save()
	return HttpResponse(data['result']['id'])


