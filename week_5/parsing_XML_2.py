import xml.etree.cElementTree as ET

input = '''
<stuff>
   <users>
       <user x = "2">
           <id> 007 </id>
           <name> Dhruv Singla </name>
       </user>
       <user x = "9">
           <id> 022 </id>
           <name> Swati Singla </name>
       </user>
    </users>
</stuff>
'''

tree = ET.fromstring(input)

userList = tree.findall('users/user')
print("User count : ", len(userList))

for user in userList:
    print("Name : ", user.find('name').text)
    print("ID : ", user.find('id').text)
    print("Attribute : ", user.get('x'))