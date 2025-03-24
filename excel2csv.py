import pandas as pd


def excel_to_csv(excel_file_path, csv_file_path):
    try:
        # 读取 Excel 文件
        df = pd.read_excel(excel_file_path)
        # 将数据保存为 CSV 文件
        df.to_csv(csv_file_path, index=False)
        print(f"成功将 {excel_file_path} 转换为 {csv_file_path}")
    except FileNotFoundError:
        print(f"错误: 文件 {excel_file_path} 未找到。")
    except Exception as e:
        print(f"发生未知错误: {e}")


if __name__ == "__main__":
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入终止页码：'))

    excel_base_path = r'./AVNB/excel/AVLIST_'
    excel_tail_path = '.xlsx'

    csv_base_path = r'./AVNB/csv/AVLIST_'
    csv_tail_path = '.csv'

    for page in range(start_page, end_page + 1):
        page = str(page)
        #EXCEL_PATH = base_path + page + tail_path
        #EXCEL_PATH = base_path + page + tail_path
        # 请替换为你的 Excel 文件路径
        excel_file = excel_base_path + page + excel_tail_path
        # 请替换为你想要保存的 CSV 文件路径
        csv_file = csv_base_path + page + csv_tail_path
        excel_to_csv(excel_file, csv_file)

