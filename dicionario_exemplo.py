import json

dic = {'rede1':
            {'id':'bla',
            'key':'123'},
        'rede2':
            {'id':'ble',
            'key':'456'},
        'rede3':
            {'id':'bli',
            'key':'789'}
        }

print(dic)

for i in dic.keys():
    if i == 'rede2':
        for n in dic[i].keys():
            if n == 'id':
                print(dic[i][n])

dic2 ={'rede2': dic.pop('rede2')}

print(dic)
print(dic2)

dic.update(dic2)

print(dic)


f = open('teste.json', 'w')
f.write(json.dumps(dic))
f.close()

f = open('teste.json').read()
dic3 = json.loads(f)
print(dic3)
print(dic3['rede2'])