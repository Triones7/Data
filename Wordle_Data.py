import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 读取 Excel 文件，假设文件名为 'data.xlsx'
file_path = 'data.xlsx'

# 读取 Excel 中的第一个 sheet
df = pd.read_excel(file_path)

# 假设日期列为 'Date'，人数列为 'People'
# 如果列名不同，请根据实际情况修改列名
expected_columns = ['Date', 'Number of reported results']
if not all(col in df.columns for col in expected_columns):
    raise ValueError(f"Excel 文件中缺少必要的列。预期列：{expected_columns}，实际列：{df.columns}")

# 指定日期格式为 'YYYY/MM/DD'
date_format = '%Y/%m/%d'
df['Date'] = pd.to_datetime(df['Date'], format=date_format)  # 转换为日期类型
df.set_index('Date', inplace=True)  # 设置日期列为索引

# 检查数据是否有缺失值
if df.isnull().values.any():
    print("警告：数据中存在缺失值。")
    # 可以选择填充缺失值或删除包含缺失值的行
    # df.fillna(method='ffill', inplace=True)  # 前向填充缺失值
    # df.dropna(inplace=True)  # 删除包含缺失值的行

# 设置中文字体
# 首先，找到系统中可用的中文字体
# 这里我们假设 'SimHei' 字体可用，你可以根据实际情况替换为其他中文字体
font_path = fm.findfont(fm.FontProperties(family='SimHei'))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Number of reported results'], marker='o', linestyle='-', color='b')
plt.title('日期与人数折线图')
plt.xlabel('日期')
plt.ylabel('人数')
plt.grid(True)
plt.xticks(rotation=45)  # 如果日期显示不清晰，可以旋转 x 轴标签
plt.tight_layout()  # 调整布局，避免标签重叠
plt.show()
