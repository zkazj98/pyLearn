import pandas as pd

df = pd.read_csv(
    # 文件路径
    filepath_or_buffer='../index_data/sz000002.csv',
    # 分隔符
    sep=',',
    # 跳过前几行
    skiprows=1,
    # 读取前几行
    nrows=10,
    # 使用哪一列设置为索引列
    index_col='交易日期',
    # 读取那些列
    usecols=['交易日期', '股票代码', '股票名称', '收盘价', '涨跌幅', '成交量', 'MACD_金叉死叉'],
    # 空值设置成什么
    na_values='NULL'
)
print(df)
