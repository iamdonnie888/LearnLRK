import pandas as pd
import numpy as np
import mysql.connector

# 连接到 MySQL 数据库
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="benben",
    database="av_numbers_db"
)

start_page = int(input('请输入起始文件号码：'))
end_page = int(input('请输入终止文件号码：'))

csv_base_path = r'./AVNB/csv/AVLIST_'
csv_tail_path = '.csv'

# 创建游标
mycursor = mydb.cursor()

# 自动创建表（如果不存在）
create_table_sql = """
CREATE TABLE IF NOT EXISTS av_number (
    Id INT AUTO_INCREMENT PRIMARY KEY,  -- 自增主键（隐式非空）
    Number VARCHAR(255),
    Name VARCHAR(255) CHARACTER SET utf8mb4,
    Content VARCHAR(1023) CHARACTER SET utf8mb4
)
"""
mycursor.execute(create_table_sql)

for page in range(start_page, end_page + 1):
    page = str(page)
    csv_path = csv_base_path + page + csv_tail_path
    # 读取 CSV 文件
    df = pd.read_csv(csv_path).replace({np.nan: None})

    # 插入数据
    for index, row in df.iterrows():
        sql = "INSERT INTO av_number (Number, Name, Content) VALUES (%s, %s, %s)"
        val = (row['Number'], row['Name'], row['Content'])
        mycursor.execute(sql, val)

# 提交更改
mydb.commit()

# 关闭连接
mycursor.close()
mydb.close()
