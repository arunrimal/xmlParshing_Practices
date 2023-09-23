
import xml.etree.ElementTree as ET


# tree = ET.parse('myxml_2.xml')
# #print(tree.find('job')[11].text)
# root = tree.getroot()
# print(root[3][11])

# for children in root:
#     for child in children:



file = 'myxml_2.xml'
tree = ET.parse(file)

job = tree. find('job')
title = job.findtext('title')
print(title)
print(type(title))
description = job.find('description')
print(description)





