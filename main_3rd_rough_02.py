from lxml import etree as et
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor


# response = requests.get("https://www.hospitalcareers.com/feeds/standard.xml?Limit=400&job_type=77")
# #print(response.status_code)
# content_xml=response.content

start_time = time.time()

def open_file(file_name):
        
        parser = list(et.iterparse(file_name, tag='job'))
        #print(parser)
        return parser

def find_tag(parser):
        list_tag = []
        for tup in parser:
                list_tag.append(tup[-1])
                #print(tup[-1])
        #print(list_tag)
        return list_tag


def find_Children(list_tag):
        child_list_all = []
        for ele in list_tag:                
                #print(ele.tag , '  this is arun!!  ', ele.text)
                child_list=[]
                for child in ele:             
                        
                        #print(child.tag , ': ', child.text)
                        
                        child_list.append((child.tag,child.text))       
                
                #print('this is child_list: ',child_list)        
                child_list_all.append(child_list)
        #print('this is child_list_all: ',child_list_all)
        
        with ThreadPoolExecutor(20) as executor:
                executor.map(find_Children, list_tag)
        
        return child_list_all
      
def catch_children(list):
        col_list= []        
        data_list_all = []

        #print(list[0])
        for ele in list:
        #print(ele)
                for i in ele:
                        #print(i)
                        elem = (i[0])
                        #sub_list.append(i[0])
                        if elem not in col_list:

                                col_list.append(str(elem))
        #print(col_list)
        
        for ele in list:
                #print(ele)
                data_list=[]
                for i in ele:
                        elem=i[1]
                        #print(elem)
                        data_list.append(i[1]) 
                #print(data_list)
                data_list_all.append(data_list)
        #print(data_list_all)

        with ThreadPoolExecutor(20) as executor:
                executor.map(catch_children, list)

        return col_list, data_list_all

def save_to_csv(data, columns):
        df = pd.DataFrame(data= data, columns=columns)
        #print(df)
        df.to_csv('jpt_05.csv', mode='w', encoding='utf-8',index=False ,header=True)
        



               
if __name__=="__main__":

        file_name = 'myxml_2.xml'
                
        content = open_file(file_name)
        tag_list = find_tag(content)
        #print(tag_list)
        #print(children)
        children = find_Children(tag_list)
        columns, data=catch_children(children)
        save_to_csv(data, columns)
        end_time = time.time()
        print(time.time()-start_time)





        









