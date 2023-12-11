import pandas as pd
data=pd.read_csv('StudentsPerformance.csv')
lunch_1=data.loc[data.lunch=='free/reduced']
mean_1_1=lunch_1['math score'].mean()
mean_2_1=lunch_1['reading score'].mean()
mean_3_1=lunch_1['writing score'].mean()
lunch_2=data.loc[data.lunch=='standard']
mean_1_2=lunch_2['math score'].mean()
mean_2_2=lunch_2['reading score'].mean()
mean_3_2=lunch_2['writing score'].mean()


print(mean_1_1, mean_2_1, mean_3_1)
print(mean_1_2, mean_2_2, mean_3_2)
d1=0
for i in lunch_1['math score']:
    d=(i-mean_1_1)*(i-mean_1_1)
    d1+=d
d2=d1/len(lunch_1['math score'])
print(d2)
d2=0
d1=0
for i in lunch_1['reading score']:
    d=(i-mean_2_1)*(i-mean_2_1)
    d1+=d
d2=d1/len(lunch_1['reading score'])
print(d2)
d2=0
d1=0
for i in lunch_1['writing score']:
    d=(i-mean_3_1)*(i-mean_3_1)
    d1+=d
d2=d1/len(lunch_1['writing score'])
print(d2)
d1=0
d2=0
#==========================
for i in lunch_2['math score']:
    d=(i-mean_1_2)*(i-mean_1_2)
    d1+=d
d2=d1/len(lunch_2['math score'])
print(d2)
d2=0
d1=0
for i in lunch_2['reading score']:
    d=(i-mean_2_2)*(i-mean_2_2)
    d1+=d
d2=d1/len(lunch_2['reading score'])
print(d2)
d2=0
d1=0
for i in lunch_2['writing score']:
    d=(i-mean_3_2)*(i-mean_3_2)
    d1+=d
d2=d1/len(lunch_2['writing score'])
print(d2)
