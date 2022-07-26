import os
import pandas as pd
import re
import string

boostan_data = list()
for chapter_name in os.listdir('../resources/boostan'):
    for file_name in os.listdir(f'../resources/boostan/{chapter_name}'):
        file = open(f'../resources/boostan/{chapter_name}/{file_name}', encoding='utf-8')
        poem = file.read()
        for hem in [x.strip() for x in poem.split('\n\n')]:
            if hem:
                boostan_data.append(
                    [hem, int(chapter_name.split('bab')[1]), int(file_name.split('sh')[1].split('.')[0])])

boostan_data = pd.DataFrame(boostan_data)
boostan_data.columns = ['poem', 'chapter', 'section']
boostan_data.sort_values(by=['chapter', 'section'], ignore_index=True, inplace=True)
boostan_data['book'] = 'B'

golestan_data = list()
for chapter_name in os.listdir('../resources/golestan'):
    for file_name in os.listdir(f'../resources/golestan/{chapter_name}'):
        file = open(f'../resources/golestan/{chapter_name}/{file_name}', encoding='utf-8')
        for hem in [x.strip() for x in re.split('\n\n|\.|\?|!', file.read())]:
            if len(hem.split()) < 3:
                continue
            if hem:
                if file_name.startswith('d'):
                    golestan_data.append([hem, 0, 1])
                else:
                    golestan_data.append(
                        [hem, int(chapter_name.split('bab')[1]), int(file_name.split('sh')[1].split('.')[0])])

golestan_data = pd.DataFrame(golestan_data)
golestan_data.columns = ['poem', 'chapter', 'section']
golestan_data.sort_values(by=['chapter', 'section'], ignore_index=True, inplace=True)
golestan_data['book'] = 'G'

all_data = pd.concat([boostan_data, golestan_data], ignore_index=True)['poem']

stopwords = ['زن']
replace_dict = {}
punctuations = '\.:!،؛؟»\]\)\}«\[\(\{' + string.punctuation

with open('../resources/stopwords.txt', encoding='utf-8') as f:
    var = f.readline()
    while var:
        stopwords.append(var.strip())
        var = f.readline()

with open('../resources/replace.txt', encoding='utf-8') as f:
    line = f.readline()
    while line:
        key, value = line.split('-')
        key, value = key.strip(), value.strip()
        replace_dict[f'{key}'] = f'{value}'
        line = f.readline()

poem_based_boostan = boostan_data.groupby(['book', 'chapter', 'section']).apply(
    lambda f: '\n'.join(f['poem'].tolist())).reset_index()

poem_based_golestan = golestan_data.groupby(['book', 'chapter', 'section']).apply(
    lambda f: '\n'.join(f['poem'].tolist())).reset_index()

poem_based_all = pd.concat([poem_based_boostan, poem_based_golestan], ignore_index=True)

beit_based_all = pd.concat([boostan_data, golestan_data], ignore_index=True)
