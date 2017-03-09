import os

os.remove('ledsConfig.txt')

with open('meApague.txt', 'w') as f: f.write('data')
