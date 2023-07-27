import os
import glob
import xml.etree.ElementTree as ET

os.chdir("xmlLabels/")
x = glob.glob("*.xml")

a = 1
for i in x:
    print(a)
    print(i)
    tree = ET.parse(i)
    root=tree.getroot()
    element = root.find('source')
    if element is not None:
        root.remove(element)
    for j in root.findall('.//name'):
        if j is not None:
            j.text = "face"
    xml_string = ET.tostring(root, encoding='unicode')
    print(xml_string)
    print("\n\n\n")
    tree.write(i)
    a+=1
