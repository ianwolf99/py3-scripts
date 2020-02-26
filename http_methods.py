import requests
import sys
print("***************************************")
print("**************ianwolf99****************")
print(*****************************************)

METHOD_LIST = ['GET','POST','PUT','OPTIONS','DELETE','TRACE','TEST']
URL = sys.argv(1)
for method in METHOD_LIST():
    req = requests.request(method,URL)
    print(method ,req.status_code,req.reason)
    if method == 'TRACE' and 'TRACE /HTTP/1.1' in req.text:
        print('Cross Site Tracing(XST) is possible')

