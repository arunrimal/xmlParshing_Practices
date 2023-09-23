from lxml import etree as et
import pandas as pd
import time



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
        return col_list, data_list_all

def save_to_csv(data, columns):
        df = pd.DataFrame(data= data, columns=columns)
        #print(df)
        df.to_csv('jpt_04.csv', mode='w', encoding='utf-8',index=False ,header=True)
        


               
if __name__=="__main__":

        file_name = 'myxml_2.xml'
                
        content = open_file(file_name)
        tag_list = find_tag(content)
        children = find_Children(tag_list)
        columns, data=catch_children(children)
        save_to_csv(data, columns)
        end_time = time.time()
        print(end_time-start_time)





        









