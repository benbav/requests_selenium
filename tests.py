from requests_selenium import requests_selenium
import requests
url = 'https://www.psychologytoday.com/'

r = requests.get(url)
print(r.text)

'''
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
</body></html>
'''
r = requests_selenium.get(url)
print(r.text)


driver = requests_selenium.get_driver()

print(driver)



