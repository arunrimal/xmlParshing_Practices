import pandas as pd
from main_rough_7 import child_list_all



# list = [[('rank', '4'), ('year', '2011'), ('gdppc', '59900')],
#     [('rank', '1'), ('year', '2008'), ('gdppc', '141100'), ('neighbor', None), ('neighbor1', None)],
#     [('rank', '4'), ('year', '2011'), ('gdppc', '59900'), ('neighbor', None)],
#     [('rank', '68'), ('year', '2011'), ('gdppc', '13600'), ('neighbor', None), ('neighbor', None)]]
list=child_list_all

col_list= []

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

data_list_all = []
for ele in list:
    data_list=[]
    for i in ele:
        elem=i[1]
        data_list.append(i[1]) 
    #print(data_list)
    data_list_all.append(data_list)
#print(data_list_all)

# mother_list = col_list+data_list_all
# print(mother_list)
# print(mother_list[0])
# print(mother_list[-1])

df = pd.DataFrame(data= data_list_all, columns=col_list)
#print(df)
df.to_csv('jpt_03.csv', mode='w', encoding='utf-8',index=False ,header=True)

#df = pd.DataFrame()
# for x in list:
#     print(x)
#     for xx in x:
#         #print(xx)
#         for xxx in xx:
#             print(xxx[0])

# for x in list:
#     print(x[0])
#     # print(x[0][0])
#     # print(x[0][1])
    
    
# ['rank', 'year', 'gdppc', 'neighbor', 'neighbor1', 
# ['4', '2011', '59900'], 
# ['1', '2008', '141100', None, None], 
# ['4', '2011', '59900', None], 
# ['68', '2011', '13600', None, None]]