 import urllib3.request as u

website_name = input('Enter your site name:')
source= u.urlopen(website_name)
source_read = source.read()
print(source_read)
