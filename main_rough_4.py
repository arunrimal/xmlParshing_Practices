
import xml.etree.ElementTree as ET


# parser = ET.XMLPullParser(['start', 'end'])
# parser.feed('<mytag>sometext')
# list(parser.read_events())
# [('start', <Element 'mytag' at 0x7fa66db2be58>)]
# parser.feed(' more text</mytag>')
# for event, elem in parser.read_events():
# print(event)
# print(elem.tag, 'text=', elem.text)

xml_iter = ET.iterparse('eg.xml',events=('start','end'))
for event, elem in xml_iter:
    if event=='start':
        #print('<%s>' % elem.tag, end='' '\n')
        text=str(elem.text).strip()
        if text !='':
            print(text, end='' '\n')
        # elif event=='end':
        #     print('<%s>' % elem.tag)




