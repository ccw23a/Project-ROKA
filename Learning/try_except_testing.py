ta1 = {'name':'Thomas', 'age':30, 'grade':[2, 5, 6, 3]}

try:
    print(ta1['agr'])

except:
    print(ta1['name'])

finally:
    print(ta1)