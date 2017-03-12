import os, json

os.remove('ledsConfig.txt')

config = {
    'all': [255,0,0,1,15]
}

data = json.dumps(config)
with open('ledsConfig.txt', 'w') as f: f.write(data)
f.close()
