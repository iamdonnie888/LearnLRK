import pandas as pd


FILE_PATH = r'./读取 Excel：read_excel().xlsx'

# 1.读取 sheet，默认第一个
sheet = pd.read_excel(FILE_PATH)

# 2.输出 sheet
print(sheet)

