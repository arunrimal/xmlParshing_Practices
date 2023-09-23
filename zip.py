from zipfile import ZipFile
import os

#Extracting a zip file

# file_name = 'test.zip'

# #Opening the zip file in read mode
# with ZipFile(file_name, 'r') as zip:
#     #printing all the content of zip file 
#     print(zip.printdir())

#     #extracting all the files 
#     print('extracting all the files now...')
#     zip.extractall()
#     print('Done!')

#Writing to a zip file (this way writes only one file)

# with ZipFile('my_zip_write_01.zip','w')as zip:
#     zip.write('myxml_2.xml')

# with ZipFile('my_zip_write_01.zip','r')as zip:
#     zip.printdir()

##########################################################
## writing number of files to a zip file
## first state the directory or path the files are in
## secong make a list so that files can be stored in a list for write to zip file
## third write all the files in list to a zip file

# directory = './venv_xml'
# file_list = []

# for file in os.listdir('.'):
#     if file.endswith('.xml'):
#         print(file)
#         file_list.append(file)
# print('total file: ', file_list)

# with ZipFile('my_zip_write_files_02.zip','w') as zip:
#     for file in file_list:      
#         zip.write(file)
#         zip.printdir()


