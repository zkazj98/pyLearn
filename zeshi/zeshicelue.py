import pandas as pd

# 设置不换行
pd.set_option('expand_frame_repr', False)
# 设置列宽
pd.set_option('max_colwidth', 80)

df = pd.read_csv("sz300001.csv", encoding="gbk")
# df.columns = [i.encode('utf-8') for i in df.columns]
# print(df.columns)
df = df[['交易日期', '股票代码', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅']]
df.sort_values(by=['交易日期'], inplace=True)
# df['涨跌幅2'] = df['收盘价'].pct_change()
# # 判断给出的涨跌幅是否是复权涨跌幅
# print(df[abs(df['涨跌幅2'] - df['涨跌幅']) > 0.00001])
df['复权因子'] = (df['涨跌幅'] + 1).cumprod()
init_price = df.iloc[0]['收盘价'] / (1 + df.iloc[0]['涨跌幅'])
df['收盘价_后复权'] = init_price * df['复权因子']
df['开盘价_后复权'] = df['开盘价'] / df['收盘价'] * df['收盘价_后复权']
df['最高价_后复权'] = df['最高价'] / df['收盘价'] * df['收盘价_后复权']
df['最低价_后复权'] = df['最低价'] / df['收盘价'] * df['收盘价_后复权']

df.to_csv("outpu_sz300001.csv", index=False, mode='w', float_format='%.15f', encoding='gbk')
