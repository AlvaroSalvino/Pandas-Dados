import pandas as pd

df = pd.DataFrame(
     {
         "Name": [
             "Braund, Mr. Owen Harris",
             "Allen, Mr. William Henry",
             "Bonnell, Miss. Elizabeth",
         ],
         "Age": [22, 35, 58],
         "Sex": ["male", "male", "female"],
     }
 )

df.to_csv()

print(df.head())

df = df.rename(columns={'Name':"Nome", 'Age': "Ano", 'Sex': "Sexo"})

print(df.head())

