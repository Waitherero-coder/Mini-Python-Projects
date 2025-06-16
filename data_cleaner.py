import pandas as pd
# Placeholder for cleaning data
df = pd.DataFrame({'Name': ['Liza', '  John ', 'Mary'], 'Age': [23, 25, None]})
df['Name'] = df['Name'].str.strip()
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)