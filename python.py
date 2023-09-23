import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

print('\nthese are the classes in ET:\n')
# Display the class in ET module
for (name, memberr) in getmembers(ET, isclass):
    if not name.startswith("_"):
        print(name)

print('\nthese are the functions used in ET:\n')

# Display the function in ET module
for (name, memberr) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(name)