import numpy as np
import pandas as pd

url = 'https://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv'
df = pd.read_csv(url)
include = ['Age', 'Sex', 'Embarked', 'Survived']
df = df[include]

categoricals = []
for col, col_type in df.dtypes.iteritems():
    if col_type == 'O':
        categoricals.append(col)
    else:
        df[col].fillna(0, inplace=True)

df_ohe = pd.get_dummies(df, columns=categoricals, dummy_na=True)

from sklearn.linear_model import LogisticRegression
dependent_variable = 'Survived'
X = df_ohe[df_ohe.columns.difference([dependent_variable])]
y = df_ohe[dependent_variable]
regressor = LogisticRegression()
regressor.fit(X, y)

# Saving model to disk
import joblib
joblib.dump(regressor, 'model.pkl')

# Loading model to compare the results
regressor = joblib.load('model.pkl')
model_columns = list(X.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print(X.columns)#['Age', 'Embarked_C', 'Embarked_Q', 'Embarked_S', 'Embarked_nan', 'Sex_female', 'Sex_male', 'Sex_nan']
