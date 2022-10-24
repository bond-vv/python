# -*- coding: utf-8 -*-
"""Lesson_3_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fwbUpuJrClbNUsh7Bcmw8fvAaUuH4RLo
"""

import pandas as pd

import numpy as np

import pickle

data1 = {'author_id': [1, 2, 3], 'author_name':['Тургенев', 'Чехов', 'Островский']}

authors = pd.DataFrame(data1)

authors

data2 = {'author_id': [1, 1, 1, 2, 2, 3, 3], 'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 'price':[450, 300, 350, 500, 450, 370, 290]}

book = pd.DataFrame(data2)

book

authors_price = pd.merge(authors, book, on='author_id', how='inner')

authors_price

#authors_price.sort_values(by="price", inplace = True)

top5 = authors_price.sort_values(by="price").tail(5)

top5

authors_price

authors_stat = authors_price.groupby("author_name").price.agg( min_price = "min", max_price = "max", mean_price = "mean").reset_index()

"""daily_sales = sales.groupby([pd.Grouper(key='date', freq='D')
                            ]).agg(daily_sales=('ext price',
                                                'sum')).reset_index()
daily_sales['quarter_sales'] = daily_sales.groupby(
    pd.Grouper(key='date', freq='Q')).agg({'daily_sales': 'cumsum'})
"""

authors_stat

authors_stat.shape

authors_price["cover"] =['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']

authors_price

authors_price['cover'] = authors_price['cover'].astype("category")

authors_price['cover'].cat.set_categories(["твердая", "мягкая"], inplace=True)

authors_price.info()

book_info = pd.pivot_table(authors_price, index=["author_name"], columns=["cover"], values = ["price"], aggfunc=np.sum, fill_value=0, margins=True)

book_info

with open('book_info.pkl', 'wb') as f:
	pickle.dump(book_info, f)

with open('book_info.pkl', 'rb') as f:
	book_info2 = pickle.load(f)

book_info2