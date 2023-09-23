import xml.etree.ElementTree as ET
import requests
import pandas as pd


# df_xml = pd.DataFrame(columns=['Job' ,'Title','Date','ExpirationDate','ReferenceNumber','Url','City','State','Country','PostalCode',
#                         'Location','Remote','Description','ApplyUrl', 'JobType', 'Category', 'Company', 'CompanyDescription', 
#                         'CompanyWebsite', 'CompanyLogo', 'Qualifications', 'Schedule', 'EmploymentTypeFeedOnly'])

response = requests.get("https://www.hospitalcareers.com/feeds/standard.xml?Limit=400&job_type=77")
#print(response.status_code)
content_xml=response.content

parser = ET.XMLPullParser(['start'])

parser.feed(content_xml)

list_event_all = list(parser.read_events())

print(list_event_all[4[1,]])
print(list_event_all[31[1,]])

# def event_surfing(list_event):
#     for event, elem in list_event:

#         # if ( elem.tag == 'job'):
    
#         print("%s" %elem.tag, ': ', elem.text)  
        
#         #print(abc.tag,':', abc.text)
        
        
        # df_xml = df_xml.append({
        #     'Title'                 : title_text,
        #     'Date'                  : date_text,
        #     'ExpirationDate'        : expirationdate_text ,
        #     'ReferenceNumber'       : referencenumber_text,
        #     'Url'                   : url_text,
        #     'City'                  : city_text,
        #     'State'                 : state_text,
        #     'Country'               : country_text,
        #     'PostalCode'            : postalcode_text,
        #     'Location'              : location_text,
        #     'Remote'                : remote_text,
        #     'Description'           : description_text,
        #     'ApplyUrl'              : applyurl_text, 
        #     'JobType'               : jobtype_text, 
        #     'Category'              : category_text, 
        #     'Company'               : company_text, 
        #     'CompanyDescription'    : companydescription_text,
        #     'CompanyWebsite'        : companywebsite_text, 
        #     'CompanyLogo'           : companylogo_text, 
        #     'Qualifications'        : qualifications_text, 
        #     'Schedule'              : schedule_text, 
        #     'EmploymentTypeFeedOnly': employmenttypefeedonly_text
        #},ignore_index=True)




# event_surfing(list_event)








