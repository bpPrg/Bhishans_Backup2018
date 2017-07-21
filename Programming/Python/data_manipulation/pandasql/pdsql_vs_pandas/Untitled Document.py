#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 9, 2017
# Ref: http://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html

# Imports
import pandas as pd
import numpy as np
import wget
import pandasql as pdsql


def pysql(q):
    """Useful function."""
    return pdsql.sqldf(q, globals())

# download the data
# url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/' +\
# 'data/tips.csv'
# wget.download(url)

# pandas.DataFrame
tips = pd.read_csv('tips.csv')

# head 5 lines
q = """
SELECT *
From tips
LIMIT 5;
"""

df1 = pysql(q)
# print(tips.head())
# print(df1)

# choose only some columns
q = """
SELECT total_bill, tip, smoker, time
From tips
LIMIT 5;
"""

df1 = pysql(q)
print(tips[['total_bill', 'tip', 'smoker', 'time']].head(5))
print(df1)
