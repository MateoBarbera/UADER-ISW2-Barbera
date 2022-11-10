# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55

import json, sys
version='1.0'

if len(sys.argv)==1:
    print('no se puede ejecutar')
    sys.exit()

if len(sys.argv)==2:
    if (sys.argv[1] == '-h'):
        with open('README.md', 'r') as (helpfile):
            text = helpfile.read()
            print(text)
            sys.exit()
    else:
        jsonkey ='token1'
else:
   
    jsonkey=sys.argv[2]

jsonfile = sys.argv[1]

with open(jsonfile, 'r') as (myfile):
    data = myfile.read()
obj = json.loads(data)
try:
    print ('{'+version+'}'+str(obj[jsonkey]))
except:
    print('TOKEN NO RECONOCIDO')
# okay decompiling getJason.pyc
