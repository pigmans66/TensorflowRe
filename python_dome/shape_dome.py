import numpy as np
tans_case=[]
for i in range(33):
    if i==0:
        shape_date=" "*20+"*"*(150)
        tans_case.append(shape_date)
    elif i==32:
        shape_date=" "*20+"*"*(150)
        tans_case[-1]=shape_date
    else:
        shape_date=' '*20+"*"+" "*148+"*"
        tans_case.append(shape_date)
for i in range(33):
    print(tans_case[i])
def tans_case():
    print(tans_case)