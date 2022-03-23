import glob
import os
import sys
from datetime import datetime

d = {}


def word_counter(data):
    for i in data:
        if i in d.keys():
            d.update({i: d[i] + 1})
        else:
            d.update({i: 1})
    return d


start_time = datetime.now()
path = sys.argv[1]

for filename in glob.glob(os.path.join(path, '*.txt')):
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        content = [i for i in file.read().split('\n')]
        file.close()
    word_counter(content)

print(d)
print('Time elapsed: ', datetime.now() - start_time)
