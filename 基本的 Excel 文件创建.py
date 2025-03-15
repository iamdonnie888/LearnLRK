import pandas as pd

# 测试数据
data = {'ID': [1, 2, 3, 4],
        'Name': ['张三', '李四', '王五', '赵六'],
        'Age': [18, 20, 21, 19],
        'Grade': [90, 70, 80, 90]}

# 1.创建 DataFrame 对象
df = pd.DataFrame(data)

# 可选操作。
# 将 ID 设为索引，若不设置，会使用默认索引 narray(n)，如下图所示
df = df.set_index('ID')

# 2.写入 excel 至指定位置（若文件已存在，则覆盖）
FILE_PATH = r'./基本的 Excel 文件创建.xlsx'
df.to_excel(FILE_PATH)
