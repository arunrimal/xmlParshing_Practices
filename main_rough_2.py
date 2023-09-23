
import xml.etree.ElementTree as ET
import re
import gzip
import shutil


# with open('myxml_2.xml', 'rb') as file_in, gzip.open('myxml_2.xml.gz', 'wb') as file_out:
#     shutil.copyfileobj(file_in, file_out)


file = 'myxml_2.xml.gz'

tree = ET.parse(gzip.open(file, 'r'))

job = tree. find('job')
#for job in jobs:
# title = job.find('title')
# print(title.text)
# # date
# expirationdate
# referencenumber
# url
# city
# state
# country
# postalcode
# location
# remote
# description= job.find('description')
# print(description.text)

# applyurl
# jobtype
# category
# company = job.find('company')
# print(company.text)
# companydescription
companydescription= job.find('companydescription').text
com_desc_re = re.compile(r'<[^>]+>')
f_text = com_desc_re.sub('',companydescription)
print(f_text)


# companywebsite
# companylogo
# qualifications
# schedule
# employmenttypefeedonly





