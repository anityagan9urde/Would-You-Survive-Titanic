import json, requests
import pandas as pd
d = {'Age': '24', 'Sex': 'female', 'Embarked': 'C'}
#json_d = json.dumps(d)
#print(json_d)
whole_table = pd.DataFrame([d])
print(whole_table)
object_table = whole_table[whole_table.columns.drop('Age')]
print(object_table)
ohe = pd.get_dummies(object_table)
print(ohe)
query = whole_table[whole_table.columns.drop('Sex', 'Embarked')].append(ohe).fillna(0)
print(query)

