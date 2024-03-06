import pandas as pd

#creditd = pd.D('credit_card_clients.csv')
df = pd.DataFrame({
    "nome": ["paulo"],
    "idade": [28],
    "sexo": ["masculino"]
})

# import data
credit = pd.read_csv("./credit_card_clients.csv")
"""        ID  LIMIT_BAL  SEX  ...  PAY_AMT5  PAY_AMT6  default payment next month
0          1      20000    2  ...         0         0                           1
1          2     120000    2  ...         0      2000                           1
2          3      90000    2  ...      1000      5000                           0
3          4      50000    2  ...      1069      1000                           0
4          5      50000    1  ...       689       679                           0
     ...        ...  ...  ...       ...       ...                         ...
29995  29996     220000    1  ...      5000      1000                           0
29996  29997     150000    1  ...         0         0                           0
29997  29998      30000    1  ...      2000      3100                           1
29998  29999      80000    1  ...     52964      1804                           1
29999  30000      50000    1  ...      1000      1000                           1"""

#credit.info()
""" 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30000 entries, 0 to 29999
Data columns (total 25 columns):
 #   Column                      Non-Null Count  Dtype
---  ------                      --------------  -----
 0   ID                          30000 non-null  int64
 1   LIMIT_BAL                   30000 non-null  int64
 2   SEX                         30000 non-null  int64
 3   EDUCATION                   30000 non-null  int64
 4   MARRIAGE                    30000 non-null  int64
 5   AGE                         30000 non-null  int64
 6   PAY_0                       30000 non-null  int64
 7   PAY_2                       30000 non-null  int64
 8   PAY_3                       30000 non-null  int64
 9   PAY_4                       30000 non-null  int64
 10  PAY_5                       30000 non-null  int64
 11  PAY_6                       30000 non-null  int64
 12  BILL_AMT1                   30000 non-null  int64
 13  BILL_AMT2                   30000 non-null  int64
 14  BILL_AMT3                   30000 non-null  int64
 15  BILL_AMT4                   30000 non-null  int64
 16  BILL_AMT5                   30000 non-null  int64
 17  BILL_AMT6                   30000 non-null  int64
 18  PAY_AMT1                    30000 non-null  int64
 19  PAY_AMT2                    30000 non-null  int64
 20  PAY_AMT3                    30000 non-null  int64
 21  PAY_AMT4                    30000 non-null  int64
 22  PAY_AMT5                    30000 non-null  int64
 23  PAY_AMT6                    30000 non-null  int64
 24  default payment next month  30000 non-null  int64
 dtypes: int64(25)
 memory usage: 5.7 MB
"""

credit.head()
"""ID  LIMIT_BAL  SEX  ...  PAY_AMT5  PAY_AMT6  default payment next month
0   1      20000    2  ...         0         0                           1
1   2     120000    2  ...         0      2000                           1
2   3      90000    2  ...      1000      5000                           0
3   4      50000    2  ...      1069      1000                           0
4   5      50000    1  ...       689       679                           0"""

credit.tail()
"""          ID  LIMIT_BAL  SEX  ...  PAY_AMT5  PAY_AMT6  default payment next month
29995  29996     220000    1  ...      5000      1000                           0
29996  29997     150000    1  ...         0         0                           0
29997  29998      30000    1  ...      2000      3100                           1
29998  29999      80000    1  ...     52964      1804                           1
29999  30000      50000    1  ...      1000      1000                           1"""

#credit.shape
#(30000, 25)

#rename columns
credit_renamed = credit.rename(columns = {
    "LIMIT_BAL":"credit_value"
    })


#drop column
credit_renamed.drop(["default payment next month"], axis=1, inplace=True)

#export to excel
#credit_renamed.to_excel("credit_renamed.xlsx")

# access index
credit.index
#RangeIndex(start=0, stop=30000, step=1)

#access columns
credit.columns
"""
Index(['ID', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0',
       'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
       'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
       'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6',
       'default payment next month'],
      dtype='object')
"""

#access only values
credit.values
"""
[[     1  20000      2 ...      0      0      1]
 [     2 120000      2 ...      0   2000      1]
 [     3  90000      2 ...   1000   5000      0]
 ...
 [ 29998  30000      1 ...   2000   3100      1]
 [ 29999  80000      1 ...  52964   1804      1]
 [ 30000  50000      1 ...   1000   1000      1]]
"""

#dataframe iterator
#for index,row in credit.iterrows():
    #print(index)
    #print(row)
    
#access column value
credit['LIMIT_BAL']
credit.LIMIT_BAL
"""
0         20000
1        120000
2         90000
3         50000
4         50000
 
29995    220000
29996    150000
29997     30000
29998     80000
29999     50000
Name: LIMIT_BAL, Length: 30000, dtype: int64
"""

#access multiple columns value
credit[['ID', 'LIMIT_BAL']]
"""
          ID  LIMIT_BAL
0          1      20000
1          2     120000
2          3      90000
3          4      50000
4          5      50000
     ...        ...
29995  29996     220000
29996  29997     150000
29997  29998      30000
29998  29999      80000
29999  30000      50000

[30000 rows x 2 columns]
"""
credit.filter(like='PAY')
"""
       PAY_0  PAY_2  PAY_3  PAY_4  ...  PAY_AMT3  PAY_AMT4  PAY_AMT5  PAY_AMT6
0          2      2     -1     -1  ...         0         0         0         0
1         -1      2      0      0  ...      1000      1000         0      2000
2          0      0      0      0  ...      1000      1000      1000      5000
3          0      0      0      0  ...      1200      1100      1069      1000
4         -1      0     -1      0  ...     10000      9000       689       679
     ...    ...    ...    ...  ...       ...       ...       ...       ...
29995      0      0      0      0  ...      5003      3047      5000      1000
29996     -1     -1     -1     -1  ...      8998       129         0         0
29997      4      3      2     -1  ...     22000      4200      2000      3100
29998      1     -1      0      0  ...      1178      1926     52964      1804
29999      0      0      0      0  ...      1430      1000      1000      1000

[30000 rows x 12 columns]
"""

#access line from df
credit.loc[0]
"""
ID                                1
LIMIT_BAL                     20000
SEX                               2
EDUCATION                         2
MARRIAGE                          1
AGE                              24
PAY_0                             2
PAY_2                             2
PAY_3                            -1
PAY_4                            -1
PAY_5                            -2
PAY_6                            -2
BILL_AMT1                      3913
BILL_AMT2                      3102
BILL_AMT3                       689
BILL_AMT4                         0
BILL_AMT5                         0
BILL_AMT6                         0
PAY_AMT1                          0
PAY_AMT2                        689
PAY_AMT3                          0
PAY_AMT4                          0
PAY_AMT5                          0
PAY_AMT6                          0
default payment next month        1
Name: 0, dtype: int64
"""

#access multiple lines from df
credit.loc[0:2]
"""
   ID  LIMIT_BAL  SEX  ...  PAY_AMT5  PAY_AMT6  default payment next month
0   1      20000    2  ...         0         0                           1
1   2     120000    2  ...         0      2000                           1
2   3      90000    2  ...      1000      5000                           0

[3 rows x 25 columns]
"""

#access lines and columns
credit.loc[0:2, ['ID', 'LIMIT_BAL']]
"""
   ID  LIMIT_BAL
0   1      20000
1   2     120000
2   3      90000
"""

#filter by bool value
credit[credit["SEX"] == 2]
"""        ID  LIMIT_BAL  SEX  ...  PAY_AMT5  PAY_AMT6  default payment next month
0          1      20000    2  ...         0         0                           1
1          2     120000    2  ...         0      2000                           1
2          3      90000    2  ...      1000      5000                           0
3          4      50000    2  ...      1069      1000                           0
7          8     100000    2  ...      1687      1542                           0
     ...        ...  ...  ...       ...       ...                         ...
29180  29181     140000    2  ...      4500      4600                           1
29181  29182     170000    2  ...      5000      5100                           0
29182  29183     280000    2  ...      3936      3845                           0
29185  29186      50000    2  ...       758       700                           0
29282  29283      80000    2  ...         0         0                           0

[18112 rows x 25 columns]
"""



    
