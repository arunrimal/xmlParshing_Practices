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
file_name = 'myxml_2.xml'
parser = list(et.iterparse(file_name, tag='job'))
#print(parser)
list_tag = []
for tup in parser:
        list_tag.append(tup[-1])
        #print(tup[-1])
#print(list_tag)
#print(type(parser))

#print(parser)
child_list_all = []
#def find_Children(list_tag):
for ele in list_tag:                
        #print(ele.tag , '  this is arun!!  ', ele.text)
        child_list=[]
        for child in ele:
                
                
                #print(child.tag , ': ', child.text)
                
                child_list.append((child.tag,child.text))       
                #df_xml['%s' %child.tag] = child.text
                #print(df_xml['%s' %child.tag])
                # df_xml=df_xml.append({
                #         str('%s' %child.tag).upper : child.text
                # },ignore_index=True)
                #print(df_xml[str('%s' %child.tag)])
                
                
        #print('this is child_list: ',child_list) 
        
        child_list_all.append(child_list)
#print('this is child_list_all: ',child_list_all)
#return child_list_all        #df_xml.to_csv('jpt_01.csv', mode='w', encoding='utf-8', header=False)
      

#print(df_xml)


# for event, elem in parser:
#         for child in elem:
#                 for i in range(0, 4):                        
#                 #print(child.tag , ': ', child.text)
#                 #print('%s' %child.tag, child.text)
                
#                         list.append(child.tag)
#                         print(list)
#                 # df_xml = df_xml.append({
#                 #          '%s' %child.tag : child.text            
#                 #         },ignore_index=True)
               
          
#                 #df_xml.to_csv('jpt_01.csv', mode='a', encoding='utf-8', header=False)
                
# # print(df_xml)

#tag = find_Children(list_tag)

        









