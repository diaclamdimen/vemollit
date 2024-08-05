import pandas as pd
from sqlalchemy import create_engine

# Create a dataframe
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# Create a sqlalchemy engine
engine = create_engine('sqlite:///example.db')

# Convert the dataframe to a SQL table
df.to_sql('people', con=engine, if_exists='replace', index=False)
