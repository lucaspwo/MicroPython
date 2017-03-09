import os, json

os.remove('meApague.txt')

dicio = {}

dicio["config"] = {
    'lRED': 255,
    'lGREEN': 0,
    'lBLUE': 0,
    'lPULSE': 1,
    'lPULSETIME': 15
}

data = json.dumps(dicio)
with open('ledsConfig.txt', 'w') as f: f.write(data)
f.close()
