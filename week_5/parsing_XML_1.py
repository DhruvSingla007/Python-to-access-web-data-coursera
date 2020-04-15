import xml.etree.cElementTree as ET

data = '''
<person>
  <name>Dhruv Singla</name>
  <phone type = "int">
     +91 8307134416
  </phone>
  <email hide = "yes"/>
</person>'''

# This code will only work if the XML is correct
tree = ET.fromstring(data)

# .text is used to get the content 
print("Name : ", tree.find('name').text)

# .get is used to get the attribute of the tag
print("Attribute : ", tree.find('email').get('hide'))