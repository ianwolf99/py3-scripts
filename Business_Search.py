from pygeocoder import Geocoder
import sys
def search_business(business_name):
	results = Geocoder.geocode(business_name)
	for result in results:
		print (result)
if __name__ == '__main__':
	business_name = sys.argv[1]
	print ("Searching %s" %business_name)
	search_business(business_name)