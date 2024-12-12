import os 
from math import ceil
file_size = os.path.getsize(input())
scale = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
weight = 0
while file_size > 1024 and weight < 5:
    file_size = ceil(file_size / 1024)
    weight += 1
print(f"{file_size}{scale[weight]}")
