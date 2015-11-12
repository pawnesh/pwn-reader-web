#!/user/bin/python
import os
import json
import re
from os import listdir


    
rootDir = 'manga'
output = 'var mangas = {\n'
pages = []
chapters = []

print "Starting traversing"
thisDir = 'nothing'

def natural_key(string_):
    """See http://www.codinghorror.com/blog/archives/001018.html"""
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

def trace(path):
    text = ''
    counter = 0
    length  =  len(os.listdir(path))
    files = os.listdir(path)
    files = sorted(files,key=natural_key)
    for f in files:
        if(os.path.isfile(path+'/'+f)):
            text = text + '\t\t"'+str(counter)+'" : "'+path+'/'+f+'",\n'
            counter += 1
        else:
            if(counter == (length-1)):
                text = text + '\t"'+f+'" : {\n'+trace(path+'/'+f)+'}\n'
            else:
                text = text + '\t"'+f+'" : {\n'+trace(path+'/'+f)+'},\n'
            #counter += 1
    return text

output = output + trace(rootDir)
output = output + '}'
print "Opening lib.js"
fo = open("lib.js", "w+")
fo.write(output)
fo.close()
print "written to lib.js"
