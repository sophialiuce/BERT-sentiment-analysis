"""
Author: Hongfa Xue
"""

import pandas as pd
import numpy as np
import sys

#Read raw train file from command line
train_file = sys.argv[1]


train=pd.DataFrame()
train = pd.read_csv(train_file,encoding = 'utf-8')
verbatim = train['verbatim'].apply(lambda x: np.str_(x)).values.tolist()

topics = train['topic']
topic_list = list(set (topics))

print ('Total number of topics is:',len(topic_list))


print (topic_list)

import csv

headline = ['id','verbatim']

for i in topic_list:
    headline.append(i)

#Output train.csv file with BERT multilabel-classification trainning format
with open('train.csv', 'w', newline='',encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(headline)

    dic=[]
    for v in verbatim:
        if v in dic:
            continue
        b = np.zeros(len(topic_list), dtype=int)
        indices = [i for i, x in enumerate(verbatim) if x == v]
        id = indices[0]
        index = topic_list.index(topics[id])
        b[index] = 1
        if len(indices)> 1:

            for j in indices[1:]:
                if topics[j]!=topics[id]:
                    index = topic_list.index(topics[j])
                    b[index]=1


        row = [id,v]
        dic.append(v)
        for i in b:
            row.append(i)
        print (row)
        writer.writerow(row)






