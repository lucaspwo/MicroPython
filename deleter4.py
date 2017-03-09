import os, json

os.remove('ledsConfig.txt')

config = {
    'r': 255,
    'g': 0,
    'b': 0,
    'p': 1,
    't': 15
}

data = json.dumps(config)
with open('ledsConfig.txt', 'w') as f: f.write(data)
f.close()
