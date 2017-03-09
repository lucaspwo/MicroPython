import os, json

os.remove('ledsConfig.txt')

config = {
    'lRED': 255,
    'lGREEN': 0,
    'lBLUE': 0,
    'lPULSE': 1,
    'lPULSETIME': 15
}

data = json.dumps(config)
with open('ledsConfig.txt', 'w') as f: f.write(data)
f.close()
