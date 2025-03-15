import pandas as pd

data1 = {'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35]}
df1 = pd.DataFrame(data1)

data2 = {'Subject': ['Math', 'English', 'Science'],
         'Score': [80, 90, 85]}
df2 = pd.DataFrame(data2)

FILE_PATH = r'./创建多个工作表的 Excel 文件.xlsx'
with pd.ExcelWriter(FILE_PATH) as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
    # index = False 表示不显示行索引
