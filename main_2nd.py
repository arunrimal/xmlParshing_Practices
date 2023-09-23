import xml.etree.ElementTree as ET
from urllib import response
import pandas as pd
import re
import requests
import xml
import gzip
import shutil
import csv
import time

response = requests.get("https://www.hospitalcareers.com/feeds/standard.xml?Limit=400&job_type=77")
print(response.status_code)
xml=response.content
print(type(xml))

def read_string(xml):
    tree = ET.fromstring(xml)
    return tree




start_time = time.time()

df_xml = pd.DataFrame(columns=['Title','Date','ExpirationDate','ReferenceNumber','Url','City','State','Country','PostalCode',
                        'Location','Remote','Description','ApplyUrl', 'JobType', 'Category', 'Company', 'CompanyDescription', 
                        'CompanyWebsite', 'CompanyLogo', 'Qualifications', 'Schedule', 'EmploymentTypeFeedOnly'])

#print(df_xml.head(0))
# def read_file(file):
    
#     tree = ET.parse(gzip.open(file, 'r'))
#     return tree


def xml_parser(tree):
    global df_xml
    jobs = tree. findall('job')
    for job in jobs:

        title = job.find('title').text
        title_text= title.strip() if title else 'Null'
        #print(title_text)

        date = job.find('date').text
        date_text=date.strip() if date else 'Null'
        #print(date_text)

        expirationdate = job.find('expirationdate').text
        expirationdate_text = expirationdate.strip() if expirationdate else 'Null'
        #print(expirationdate_text)

        referencenumber = job.find('referencenumber').text
        referencenumber_text=referencenumber.strip() if referencenumber else 'Null'
        #print(referencenumber_text)

        url = job.find('url').text
        url_text = url.strip() if url else 'Null' 
        #print(url_text)

        city = job.find('city').text
        city_text = city.strip() if city else 'Null'
        #print(city_text)

        state = job.find('state').text
        state_text = state.strip() if state else 'Null'
        #print(state_text)

        country = job.find('country').text
        country_text=country.strip() if country else 'Null'
        #print(country_text)

        postalcode = job.find('postalcode').text
        postalcode_text=postalcode.strip() if postalcode else 'Null'
        #print(postalcode_text)

        location = job.find('location').text
        location_text=location.strip() if location else 'Null'
        #print(location_text)

        remote = job.find('remote').text
        remote_text = remote.strip() if remote else 'Null'
        #print(remote_text)

        description= job.find('description').text
        desc_re = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        description_text = desc_re.sub('',description).strip() if description else 'Null'
        #print(description_text)

        applyurl = job.find('applyurl').text
        applyurl_text=applyurl.strip() if applyurl else 'Null'
        #print(applyurl_text)

        jobtype = job.find('jobtype').text
        jobtype_text=jobtype.strip() if jobtype else 'Null'
        #print(jobtype_text)

        category = job.find('category').text
        category_text=category.strip() if category else 'Null'
        #print(category_text)

        company = job.find('company').text
        company_text=company.strip() if category else 'Null'
        #print(company_text)

        companydescription= job.find('companydescription').text
        com_desc_re = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        companydescription_text = com_desc_re.sub('',companydescription).strip() if companydescription else 'Null'
        #print(companydescription_text)


        companywebsite = job.find('companywebsite').text
        companywebsite_text = companywebsite.strip() if companywebsite else 'Null'
        #print(companywebsite_text)

        companylogo = job.find('companylogo')
        companylogo_text = companylogo.text.strip() if companylogo else 'Null'
        #print(companylogo.text)

        qualifications = job.find('qualifications').text
        qualifications_text=qualifications.strip() if qualifications else 'Null'
        #print(qualifications_text)

        schedule = job.find('schedule').text
        schedule_text = schedule.strip() if schedule else 'Null'
        #print(schedule_text)

        employmenttypefeedonly = job.find('employmenttypefeedonly').text
        employmenttypefeedonly_text = employmenttypefeedonly.strip() if employmenttypefeedonly else 'Null'
        #print(employmenttypefeedonly_text)

        df_xml = df_xml.append({
            'Title'                 : title_text,
            'Date'                  : date_text,
            'ExpirationDate'        : expirationdate_text ,
            'ReferenceNumber'       : referencenumber_text,
            'Url'                   : url_text,
            'City'                  : city_text,
            'State'                 : state_text,
            'Country'               : country_text,
            'PostalCode'            : postalcode_text,
            'Location'              : location_text,
            'Remote'                : remote_text,
            'Description'           : description_text,
            'ApplyUrl'              : applyurl_text, 
            'JobType'               : jobtype_text, 
            'Category'              : category_text, 
            'Company'               : company_text, 
            'CompanyDescription'    : companydescription_text,
            'CompanyWebsite'        : companywebsite_text, 
            'CompanyLogo'           : companylogo_text, 
            'Qualifications'        : qualifications_text, 
            'Schedule'              : schedule_text, 
            'EmploymentTypeFeedOnly': employmenttypefeedonly_text
        },ignore_index=True)

        #print(df_xml)
    df_xml.to_csv('myxml_fromString_3.csv',mode='a',quoting=csv.QUOTE_ALL,encoding='utf-8', index=False, header=True)




if __name__ == "__main__":

    #file = 'myxml_2.xml.gz'
    #tree_dom = read_file(file)
    tree_dom = read_string(xml)
    xml_parser(tree_dom)
    end_time = time.time()
    time_taken = end_time-start_time
    print('total time taken: ', time_taken)
     
