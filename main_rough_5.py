
import xml.etree.ElementTree as ET
import re



file = 'eg.xml'
# tree = ET.parse(file)

# job = tree. find('job')
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
# companydescription= job.find('companydescription')
# print(companydescription)
xml_iter = ET.iterparse(file ,events=('start','end'))
for event, elem in xml_iter:
    if event=='start':
        #print('%s' % elem.tag, end=': ')
        
        text=str(elem.text).strip()
        if text !='':
            #print(''.join(ET.fromstring(text).itertext()),end='' '\n')
            regex = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
            f_text = regex.sub('',text)
            print(f_text, end='' '\n')
            #print(text, end='' '\n')
        # elif event=='end':
        #     print('<%s>' % elem.tag)


# companywebsite
# companylogo
# qualifications
# schedule
# employmenttypefeedonly





