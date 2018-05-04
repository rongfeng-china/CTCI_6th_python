class Object:
    def __init__(self,element,attribute,value='',children = None):
        self.element = element
        self.attribute = attribute
        self.value = value
        self.children = children

def xml_encoding(xml,dict):
    result = ''
    while xml != None:
        element = xml.element
        if element in dict:
            result += (' '+str(dict[element]))
        attribute = xml.attribute
        for item in attribute:
            if item in dict:
                result += (' '+str(dict[item]))
            result += (' '+str(attribute[item]))
        result += ' 0'
        if xml.value != '':
            result += (' '+xml.value+' 0')
        if xml.children != None:
            xml = xml.children
        else:
            break
    return result+' 0'
        

dict = {'family':1, 'person':2,'firstName':3,'lastName':4,'state':5}
xml = Object('family',{'lastName':'McDowell','state':'CA'},'',Object('person',{'firstName':'Gayle'},'Some Message',None))
result = xml_encoding(xml,dict)
print result



