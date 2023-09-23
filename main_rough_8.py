from lxml import etree as et
from numpy import empty
import requests
import pandas as pd


# df_xml = pd.DataFrame(columns=['Title','Date','ExpirationDate','ReferenceNumber','Url','City','State','Country','PostalCode',
#                         'Location','Remote','Description','ApplyUrl', 'JobType', 'Category', 'Company', 'CompanyDescription', 
#                         'CompanyWebsite', 'CompanyLogo', 'Qualifications', 'Schedule', 'EmploymentTypeFeedOnly'])

df_xml = pd.DataFrame()

# response = requests.get("https://www.hospitalcareers.com/feeds/standard.xml?Limit=400&job_type=77")
# #print(response.status_code)
# content_xml=response.content
file_name = 'eg.xml'
parser = et.iterparse(file_name, tag='country')
#parser = list(et.iterparse(file_name,event=['start'], tag='country'))
print(parser)
List = []
for event, elem in parser:
        
        print('%s' %elem.tag, elem.text)
        list_1 = []
        for child in elem:
                                        
                #print(child.tag , ': ', child.text)
                #print('%s' %child.tag, child.text)
                
                list_1.append(child.text)
                #print(List)
                # df_xml = df_xml.append({
                #          '%s' %child.tag : child.text            
                #         },ignore_index=True)
               
          
                #df_xml.to_csv('jpt_01.csv', mode='a', encoding='utf-8', header=False)
        List.append(list_1)
print(List)     
# # print(df_xml)
                


        









