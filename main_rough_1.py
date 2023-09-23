from distutils.filelist import findall
import xml.etree.ElementTree as ET
from urllib import response
import requests
import xml
from pathlib import Path
import zipfile
import zip
import gzip

# response = requests.get("https://www.hospitalcareers.com/feeds/standard.xml?Limit=400&job_type=77")
# print(response.status_code)
# content_xml=response.content
# print(type(content_xml))
# f = open('myxml_2.xml','wb')
# f.write(content_xml)
# f.close()

# f = zipfile.ZipFile("XML.zip", 'w')
# f.write("myxml_2.xml")
# f.close()

# f = open('test.txt','r')
# print(f.read())

# gzipper = gzip.GzipFile('myxml_2.xml')


# tree = ET.parse('eg.xml')
# print(tree.find('country')[0].text)

        # this is wrong
        # xml_zip_content = zip.open('XML.zip', 'r')
        # tree= ET.parse(xml_zip_content)
        # print(tree.find('job')[0].text)

# with zipfile.ZipFile('XML.zip','r')as zip:
#     zip.extract('myxml_2.xml')
#     tree = ET.parse('myxml_2.xml')
#     # print(tree.find('job')[0].text)
#     # print(tree.find('job')[1].text)
#     # print(tree.find('job')[2].text)
#     # print(tree.find('job')[3].text)
#     # print(tree.find('job')[4].text)
#     # print(tree.find('job')[5].text)
#     # print(tree.find('job')[6].text)
#     # print(tree.find('job')[7].text)
#     # print(tree.find('job')[8].text)
#     # print(tree.find('job')[9].text)
#     # print(tree.find('job')[10].text)
#     # print(tree.find('job')[11].text)

#     print(tree.find('job')[12].text)
#     inside_content =tree.find('job')[12]
#     print(inside_content)

    # print(tree.find('job')[13].text)
    # print(tree.find('job')[14].text)
    # print(tree.find('job')[15].text)
    # print(tree.find('job')[16].text)


tree = ET.parse('myxml_2.xml')
#print(tree.find('job')[11].text)
root = tree.getroot()
print(root.tag)
print(root.attrib)

job = tree.find('job')
description = job[11].text
#print(description)
# abc = ET.parse(description)
# abc.find('h2').text

for ele in root.find("./job"):
    
    #print(type(ele))
    print(ele.find('title'))



