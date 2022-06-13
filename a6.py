# Jezy Mirson 314470287 Idan Tabachnik 206230104
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas as pd

import re
data = pd.read_csv("export_CSV.csv")
data['num_of_words'] = 'v'
description = data.loc[:, 'description']
for i in range(len(description)):
    data['num_of_words'][i] = len(description[i].split(' '))
data["No_punct_description"] = data['description']


def remove_characters(characters):
    des = re.split('[\n , : ; . - _ ]', characters)
    while '' in des:
        des.remove('')
    des = ' '.join(str(e) for e in des)
    return str(des)


data['No_punct_description'] = data['No_punct_description'].apply(
    remove_characters)
data.loc[:, ['description', 'No_punct_description']].head(20)
data['has_restaurants'] = 'v'
data['has_museums'] = 'v'


def count_val(n):
    counter = 0
    des = n.split(' ')
    for x in des:
        if looking_for == x:
            counter += 1
    return (counter)


looking_for = 'restaurants'
data['has_restaurants'] = data['No_punct_description'].apply(count_val)
looking_for = 'museum'
data['has_museums'] = data['No_punct_description'].apply(count_val)


def count_val(n):
    counter = 0
    des = n.split(' ')
    for x in des:
        if 'beach' == x or 'ocean' == x or 'sea' == x:
            counter += 1
    return (counter)


data['has_beaches'] = data['No_punct_description'].apply(count_val)
print('The average number of words in the description column data is {k}'.format(
    k=data.loc[:, 'num_of_words'].mean()))
print('the city with the longest description column {k}'.format(
    k=data.loc[:, 'num_of_words'].max()))
x = data.loc[:, 'num_of_words']

plt.figure(figsize=(10, 5))
plt.hist(x, bins=20, color='skyblue', ec="red")
plt.xlabel("num_of_words")
plt.ylabel("number of countries of this number of words")
plt.title("different levels of num_of_words")
plt.show()
x = data.loc[:, 'has_beaches']
y = data.loc[:, 'has_restaurants']

plt.figure(figsize=(10, 5))
plt.scatter(x, y, c='red', alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.xlabel("has_beaches")
plt.ylabel("has_restaurants")
plt.title("relationship between number of beaches and number of restaurants")
plt.show()
x = data.loc[:, 'has_beaches']
y = data.loc[:, 'has_museums']

plt.figure(figsize=(10, 5))
plt.scatter(x, y, c='red', alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.xlabel("has_beaches")
plt.ylabel("has_museums")
plt.title("relationship between number of beaches and number of museums")
plt.show()
