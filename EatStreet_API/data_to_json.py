# -*- coding: utf8 -*-
import json
import requests
import sys
sys.stdout.flush()

print('start!', flush = True)
headers = {
	'X-Access-Token': '__API_EXPLORER_AUTH_KEY__',
}

city_list = ['New York','Los Angeles','Chicago','Houston','Phoenix','Philadelphia','San Antonio',
'San Diego','Dallas','San Jose','Austin','Jacksonville','San Francisco','Columbus','Indianapolis',
'Fort Worth','Charlotte','Seattle','Denver','El Paso','Washington','Boston','Detroit','Nashville',
'Memphis','Portland','Oklahoma City','Las Vegas','Louisville','Baltimore','Milwaukee','Albuquerque',
'Tucson','  Fresno', 'Sacramento','Mesa', 'Kansas City', 'Atlanta', 'Long Beach', 'Colorado Springs',
'Raleigh', 'Miami','Virginia Beach' ,'Omaha' , 'Oakland','Minneapolis','Tulsa','Arlington','New Orleans',
'Wichita','Cleveland','Tampa','Bakersfield','Aurora','Honolulu','Anaheim', 'Santa Ana','Corpus Christi',
'Riverside', 'Lexington', 'St. Louis', 'Stockton', 'Pittsburgh', 'Saint Paul','Cincinnati','Anchorage',
'Henderson','Greensboro', 'Plano','Newark', 'Lincoln','Toledo','Orlando','Chula Vista','Irvine','Fort Wayne',
'Jersey City','Durham', 'St. Petersburg','Laredo','Buffalo','Madison','Lubbock','Chandler','Scottsdale',
'Glendale','Reno','Norfolk','Winston–Salem','North Las Vegas','Irving','Chesapeake','Gilbert','Hialeah',
'Garland','Fremont','Baton Rouge','Richmond','Boise','San Bernardino','Spokane','Des Moines','Modesto',
'Birmingham','Tacoma','Fontana','Rochester','Oxnard','Moreno Valley','Fayetteville','Aurora','Glendale',
'Yonkers','Huntington Beach','Montgomery','Amarillo','Little Rock','Akron','Columbus','Augusta',
'Grand Rapids','Shreveport','Salt Lake City','Huntsville','Mobile','Tallahassee','Grand Prairie',
'Overland Park','Knoxville','Port St. Lucie','Worcester','Brownsville','Tempe','Santa Clarita',
'Newport News','Cape Coral','Providence','Fort Lauderdale','Chattanooga','Rancho Cucamonga','Oceanside',
'Santa Rosa','Garden Grove','Vancouver','Sioux Falls','Ontario','McKinney','Elk Grove','Jackson',
'Pembroke Pines','Salem','Springfield','Corona','Eugene','Fort Collins','Peoria','Frisco','Cary',
'Lancaster','Hayward','Palmdale','Salinas','Alexandria','Lakewood','Springfield','Pasadena','Sunnyvale',
'Macon','Pomona','Hollywood','Kansas City','Escondido','Clarksville','Joliet','Rockford','Torrance',
'Naperville','Paterson','Savannah','Bridgeport','Mesquite','Killeen','Syracuse','McAllen','Pasadena',
'Bellevue','Fullerton','Orange','Dayton','Miramar','Thornton','West Valley City','Olathe','Hampton',
'Warren','Midland','Waco','Charleston','Columbia','Denton','Carrollton','Surprise','Roseville',
'Sterling Heights','Murfreesboro','Gainesville','Cedar Rapids','Visalia','Coral Springs','New Haven',
'Stamford','Thousand Oaks','Concord','Elizabeth','Lafayette','Kent','Topeka','Simi Valley','Santa Clara',
'Athens','Hartford','Victorville','Abilene','Norman','Vallejo','Berkeley','Round Rock','Ann Arbor',
'Fargo','Columbia','Allentown','Evansville','Beaumont','Odessa','Wilmington','Arvada','Independence',
'Provo','Lansing','El Monte','Springfield','Fairfield','Clearwater','Peoria','Rochester','Carlsbad',
'Westminster','West Jordan','Pearland','Richardson','Downey','Miami Gardens','Temecula','Costa Mesa',
'College Station','Elgin','Murrieta','Gresham','High Point','Antioch','Inglewood','Cambridge','Lowell',
'Manchester','Billings','Pueblo','Palm Bay','Centennial','Richmond','Ventura','Pompano Beach',
'North Charleston','Everett','Waterbury','West Palm Beach','Boulder','West Covina','Broken Arrow',
'Clovis','Daly City','Lakeland','Santa Maria','Norwalk','Sandy Springs','Hillsboro','Green Bay',
'Tyler','Wichita Falls','Lewisville','Burbank','Greeley','San Mateo','El Cajon','Jurupa Valley',
'Rialto','Davenport','League City','Edison','Davie','Las Cruces','South Bend','Vista','Woodbridge',
'Renton','Lakewood','San Angelo','Clinton']

test_city_list = ['New York', 'Error city', 'Los Angeles','Chicago']

#get menu function
def return_menu(api_key):
	menu_url1 = 'https://api.eatstreet.com/publicapi/v1/restaurant/'
	menu_url2 = str(api_key)
	menu_url3 = '/menu?includeCustomizations=false'
	menu_url = menu_url1 + menu_url2 + menu_url3
	
	menu_response = requests.get(menu_url, headers = headers)
	menu_response_data = menu_response.json()
	menu_final_list = []
	try:
		error_true = menu_response_data['error']
		return [{'No Menu'}]
	
	except:
		dic = {}
		for i in menu_response_data:
			menu_out_list = []
			menu_cate = i['name']
			for j in i['items']:
				#menu_out_list = []
				dic2 = {}
				dic2['menu_cate'] = menu_cate
				dic2['menu_name'] = j['name']
				try:
					dic2['menu_desc'] = j['description']
				except:
					dic2['menu_desc'] = 'No_desc'
				try:
					dic2['menu_price'] = j['basePrice']
				except:
					dic2['menu_price'] = 0
				
				menu_out_list.append(dic2)
			menu_final_list.append(menu_out_list)
			#dic[i['name']] = menu_out_list
				#dic_list = list(dic)
		return menu_final_list


#search restaurant (output = res_out_list)
print('search restaurant!', flush = True)
res_out_list = []
for i in test_city_list:
	print('city : ', i, flush = True)
	res_url1 = 'https://api.eatstreet.com/publicapi/v1/restaurant/search?method=both&street-address='
	res_url2 = i
	res_url = res_url1 + res_url2
	res_response = requests.get(res_url, headers = headers)
	
	try:
		res_response_data = res_response.json()
		for j in res_response_data['restaurants']:
			dic = {}
			dic['city'] = i
			dic['name'] = j['name']
			dic['apiKey'] = j['apiKey']
			dic['logoUrl'] = j['logoUrl']
			dic['street_address'] = j['streetAddress']
			dic['foodTypes'] = j['foodTypes']
			dic['menu'] = return_menu(str(j['apiKey']))
			dic['deliveryMin'] = j['deliveryMin']
			dic['deliveryPrice'] = j['deliveryPrice']
			dic['state'] = j['state']
			dic['zip'] = j['zip']
			dic['foodTypes'] = j['foodTypes']
			dic['phone'] = j['phone']
			dic['latitude'] = j['latitude']
			dic['minFreeDelivery'] = j['latitude']
			dic['hours_Mon'] = j['hours']['Monday']
			dic['hours_Sun'] = j['hours']['Sunday']
			dic['hours_Sat'] = j['hours']['Saturday']
			dic['timezone'] = j['timezone']
			res_out_list.append(dic)
			#res_out_list.append()

	except KeyError:
		continue



#output save('res_out_list')
print('save output!', flush = True)
output_json = json.dumps(res_out_list)

f = open('./res_infor_US.json', 'w')
f.write(output_json)
f.close()