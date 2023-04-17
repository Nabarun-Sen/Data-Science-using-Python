f=open("D:/Note/Json.txt","r")
s=f.read()
#print(s)
import json
dic=json.loads(s)
print(dic)
print(type(dic))
print(dic['car']['Ind'])
for i in dic:
    print(dic[i])