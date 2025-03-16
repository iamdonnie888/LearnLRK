import pandas as pd

# 测试数据
data = {'Name': ['河北彩伽', '三上悠亜', '吉高寧々'],
        'Number': ['SONE-001', 'SONE-002', 'FSDSS-001'],
        'Content': ['SONE-308 美脚下半身が大絶頂するまで[媚薬?巨根]ピストンを欲しがるデカチンキメセク大好き脚長スケベお姉さん 楓ふうあ', '姉がメンズエステのバイトを始めたんだが、僕の体で際どいマッサージの練習をしてきてヤバい！ 黒島玲衣', 'AV制作アシスタントに密着 パワハラ上司やセクハラ男優の無茶振りにも健気に働く女性AD 吉高寧々']}

# 1.创建 DataFrame 对象
df = pd.DataFrame(data)

append_data = {'Name': '苍井空', 'Number': 'SONE-888', 'Content': '3'}
#append_data['Content'] = 'FSDSS-490 性欲の高鳴りは彼女のくびれ巨乳の所為。初めて迎えた夜が終わっても僕たちはヤリ続けた。 本郷愛'

append_df = pd.DataFrame([append_data])

df = pd.concat([df, append_df], ignore_index=True)

print(df)

# 2.写入 excel 至指定位置（若文件已存在，则覆盖）
FILE_PATH = r'./在Excel文件追加一行.xlsx'
df.to_excel(FILE_PATH)

