import urllib, urllib2
import re

categoriesPage = urllib2.urlopen('https://cityonline.calgary.ca//Pages/Category.aspx?cat=CITYonlineDefault&amp;category=PDCTransportation&amp')
dataLinkPattern = re.compile('/Pages/Category.aspx?cat=CITYonlineDefault&amp;category=\S+&amp;publicdata')

dataLinks = [dataLinkPattern.search(line).group(0) for line in categoriesPage.readlines() if '/Pages/Category.aspx?cat=CITYonlineDefault&amp' in line]

for link in dataLinks:
    print link
