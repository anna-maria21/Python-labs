import glob
import os
import sys
from datetime import datetime
from functools import reduce
from concurrent.futures import ThreadPoolExecutor


def word_counter(data):
    temp_dict = {}
    for i in data:
        if i in temp_dict.keys():
            temp_dict.update({i: temp_dict[i] + 1})
        else:
            temp_dict.update({i: 1})
    return temp_dict


def merge_counters(data1, data2):
    for i in data2.keys():
        if i in data1.keys():
            data1.update({i: data1[i] + data2[i]})
        else:
            data1.update({i: data2[i]})
    return data1


start_time = datetime.now()
path = sys.argv[1]
mas_content = []
# os.chdir(r'C:\Users\User\PycharmProjects\ППРС\word_count_LR1\\'+path)
# my_files = glob.glob('*.txt')
# for item in my_files:
#     file = open(item)
#     content = [i for i in file.read().split('\n')]
#     mas_content.append(content)
for filename in glob.glob(os.path.join(path, '*.txt')):
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        content = [i for i in file.read().split('\n')]
        file.close()
    mas_content.append(content)
with ThreadPoolExecutor(max_workers=10) as executor:
    result = executor.map(word_counter, mas_content)

full_res = reduce(merge_counters, result)

print(full_res)
print('Time elapsed: ', datetime.now() - start_time)
