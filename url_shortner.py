from pyshorteners import Shortener
ACCESS_TOKEN = '641d4b444eaa6ad86dff0901631fe82014b25fea'

# Shorten long URL
long_url = input("Enter Your Long Link: ")
url_shortener = Shortener( bitly_token = ACCESS_TOKEN)
print ("Short URL is {}".format(url_shortener.short(long_url)))

#Expand short URL
short_url = input("Enter Your Short Link: ")
url_expander = Shortener( bitly_token = ACCESS_TOKEN)
print ("Long URL is {}".format(url_expander.expand(short_url)))