import requests
import json
import os
from selenium import webdriver
from datetime import *
from urllib2 import urlopen

# Set up the driver to open up da browser
driverPath = os.path.expanduser('PUT PATH TO CHROME DRIVER HERE')
driver = webdriver.Chrome(driverPath)

# Base URL. Using Exclucity but you can replace it with any
# shopify site.
base_url = 'https://shop.exclucitylife.com/products.json?'

# Base backdoor url.
base_backdoor_url = 'https://shop.exclucitylife.com/cart/'

# Products within the past 3 days - hardcoded lol sry
min_date = 'created_at_min=2016-11-19T00:00:00-04:00'

# Get the data based on the min_date
def get_data_with_min_date(url):
    page_id = 1
    products_page = ['start..']
    products_list = []

    response = urlopen(url)
    products_data = json.loads(str(response.read()))
    products_list.extend(products_data['products'])

    return products_list


# Generates backdoor link
def generate_backdoor_link(products_list, size, name):
    print 'Running backdoor link generator...'

    for i in range(0, len(products_list)):

        product = products_list[i]
        product_title = product['title']

        if name in product_title:

            print ' Keyword found!'
            print ' Searching variants for size...'
            product_variant = product['variants']

            for i in range(0, len(product_variant)):
                if float(product_variant[i]['option2']) == size:
                    if product_variant[i]['available'] == True:
                        print ' Selected size: ' + str(size) + ' is available'
                        print ' ID: ' + str(product['id']) + ' | ' + product['title'] + ' | ' + product['vendor'] + ' | ' + product['product_type']
                        print ' Creating backdoor link keyword: ' + name
                        backdoor_link = base_backdoor_url + str(product_variant[i]['id']) + ':1\n'
                        print ' Opening backdoor link...'
                        driver.get(backdoor_link)
                        ##driver.switch_to_default_content()
                    else:
                        print ' Not available'

# Ok so this took me like 15 mins to make so.. ya
products = get_data_with_min_date(base_url + min_date)
generate_backdoor_link(products, 8, "AIR JORDAN")
