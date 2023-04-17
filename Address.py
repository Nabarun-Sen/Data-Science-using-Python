dic={}
dic['car'] = {'Aus': 'Tiago', 'Eng': 'Hundai', 'Ind': 'Maruti'}
dic['bike'] = {'Aus': 'Kawasaki', 'Eng': 'Honda', 'Ind': 'Pulsar'}
import json
j=json.dumps(dic)
print(j)
with open ("D:/Note/Json.txt","w") as file:
    file.write(j)