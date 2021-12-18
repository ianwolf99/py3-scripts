import requests
import urllib
import urllib2
ID_USERNAME = 'signup-user-name'
ID_EMAIL = 'signup-user-email'
ID_PASSWORD = 'signup-user-password'
USERNAME = 'username'
EMAIL = 'you@email.com'
PASSWORD = 'yourpassword'
SIGNUP_URL = 'https://twitter.com/account/create'
def submit_form():
"""Submit a form"""
	payload = {ID_USERNAME : USERNAME,
				ID_EMAIL : EMAIL,
				ID_PASSWORD : PASSWORD,}

	resp = requests.get(SIGNUP_URL)
	print ("Response to GET request: %s" %resp.content)
	# send POST request
	resp = requests.post(SIGNUP_URL, payload)
	print ("Headers from a POST request response: %s" %resp.headers)
#print "HTML Response: %s" %resp.read()
if __name__ == '__main__':
	submit_form()			