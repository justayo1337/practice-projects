import xml.etree.ElementTree as ET 

#using .parse()
myTree= ET.parse('test.xml')
myroot = myTree.getroot()
#$print(myroot.tag)

# using .fromstring()
data = ''' 
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
</note>
'''
myroot2= ET.fromstring(data)
#print(myroot2.tag)

#print tag of first child of element
'''print(myroot[0].tag)
# get attribute(s)
print(myroot[0].attrib)
for x in myroot:
  print(x.tag,x.text)'''

# find all element within tag
foods=myroot.findall('food')
for (i,x) in enumerate(foods,1) :
    name = x.find('name').text
    price= x.find('price').text

    print(i,name,price)

#adding attributes 
for x in myroot.iter('description') :
    a= str(x.text) + 'Description has been added'
    x.text = a 
    x.set('updated','yes')
myTree.write('new.xml')

# adding elements 
ET.SubElement(myroot[0],'speciality')
for i in myroot.iter('speciality'):
    b='South Nigerian Fishes'
    x.text=str(b)
myTree.write('new2.xml')

#remove attributes 
try:
    myroot[0][3].attrib.pop("What ever attribute you want")
    myTree.write('new3.xml')
except:
    pass

#remove tags 
myroot[0].remove(myroot[0][3])
myTree.write('new4.xml')
#OR 
myroot[0].clear()
myTree.write('new5.xml')