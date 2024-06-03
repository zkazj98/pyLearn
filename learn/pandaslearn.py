import pandas as pd

# 设置不换行
pd.set_option('expand_frame_repr', False)
# 设置列宽
pd.set_option('max_colwidth', 80)
df = pd.read_csv(
    # 文件路径
    filepath_or_buffer='../index_data/sz000002.csv',
    # 分隔符
    sep=',',
    # 跳过前几行
    skiprows=1,
    # 读取前几行
    nrows=15,
    # 使用哪一列设置为索引列
    index_col='交易日期',
    # 读取那些列
    usecols=['交易日期', '股票代码', '股票名称', '新浪概念', '收盘价', '涨跌幅', '成交量', 'MACD_金叉死叉'],
    # 空值设置成什么
    na_values='NULL'
)
# print(df.shape[1])  # 获取行数
# print(df.index)  # 获取所有行索引
# print(df.columns)  # 获取所有列数据
# print(df.dtypes)  # 获取列数据类型
# print(df.head(3))  # 获取前三行数据
# print(df.tail(3))  # 获取后三行数据
# print(df.sample(frac=0.5))  # n随机获取三行数据，frac设置收取比例
# print(df.describe())  # 获取列详细描述
#
# print(df[['股票代码', '股票名称']])  # 获取固定列数据
# print(df.loc['14/12/2016'])# 获取固定行数据
# print(df.loc['13/12/2016':'06/12/2016'])  # 获取范围行数据，前面是开始，后面是结束
# print(df.loc[:,'股票名称':'收盘价'])  # 逗号前是行范围，后面是列范围
# print(df.loc[:,:])  # 全部数据
# print(df.at["13/12/2016", "收盘价"])  # 获取指定单个元素数据
# print(df.loc["13/12/2016", "收盘价"])  # 获取指定单个元素数据


# print(df['收盘价']*100) # 所有数据乘100
# df['收盘价*100']=df['收盘价']*100 # 新增一列
# print(df)

# print(df[['收盘价', '成交量']].mean(axis=1))  # 收盘价平均值计算 axis=1代表对列数据均值 0代表操作行


# df['昨天收盘价'] = df['收盘价'].shift(-1)  # 补充列获取上一行数据，负数就代表取下一行数据
# del df['昨天收盘价']  # 删除列
# df['涨跌'] = df['收盘价'].diff(-1)  # 获取和下一行的差值
# df.drop(['涨跌'], axis=1, inplace=True)  # 删除这一列 inplace代表真正移除掉
# df['涨跌幅'] = df['收盘价'].pct_change(-1)  # 获取和下一行的差值比例，分母是当前行，分子是差值
# df['成交量_sum'] = df['成交量'].cumsum()  # 累加
# df['涨跌幅累乘'] = (df['涨跌幅'] + 1).cumprod()  # 累乘，通常用于资金曲线
# df['收盘价排名'] = df['收盘价'].rank(ascending=True,pct=False)  # 排序ascending=True从小到大 ,pct=True输出排名百分比
# df['股票代码'].value_counts()  # 获取每个元素出现次数


# df['股票代码']=='sh000002' #获取每一行针对这个条件的判断结果
# print(df[df['股票代码'] == 'sz000002'])  # 输出符合条件的数据
# print(df[df['股票代码'].isin(['sz000002'])])  # 输出在列表中的数据
# print(df[(df['收盘价'] >= 24) | (df['收盘价'] <= 27)])  # 输出多条件判断


# print(df.dropna(subset=['MACD_金叉死叉'], how='any'))  # 这一行有任意一列是null就把整行删掉，all的话全是null才会删掉,subset标识在哪几列判断
# print(df.fillna(value='没有'))  # 补充空值
# df['MACD_金叉死叉']=df['MACD_金叉死叉'].fillna(value=df['收盘价'])
# df['空值'] = None
# df = df.assign(MACD_金叉死叉=df['MACD_金叉死叉'].fillna(value=df['收盘价']),
#                空值=df['空值'].fillna(value=df['收盘价']))  # 多列填充数据进去

# print(df.fillna(method='ffill'))  # 向上找一个不为空的值并赋值
# print(df.fillna(method='bfill'))  # 向下找一个不为空的值并赋值
#
# print(df.notnull())  # 获取每个值是不是非空
# print(df.isnull())  # 获取每个值是不是空
# print(df[df['MACD_金叉死叉'].notnull()])  # 判断固定列值是不是为空

df.reset_index(inplace=True)  # 将设置的index恢复
# print(df.sort_values(by=['交易日期', '收盘价'], ascending=[True, False]))  # ascending的True是正序，false是倒序
# df1 = df.iloc[0:10][['股票代码', '收盘价']]
# df2 = df.iloc[5:15][['股票代码', '收盘价']]
# mergedf = pd.concat([df1, df2], axis=0, ignore_index=True)  # axis=0垂直拼接 1为水平拼接 ignore_index去掉原来的index，避免重复
# mergedf.drop_duplicates(subset=['股票代码'], keep='last',
#                         inplace=True)  # 去重，subset设置针对什么字段去重，keep设置重复保留的数据，last表示保留最后一条，first最先一条，False都不保留
# print(mergedf)


# print(df.rename(columns={"MACD_金叉死叉": "金叉死叉"}))  # 修改列名
# print(df.empty)  # 判断dataframe是否为空
# print(df.T)  # 转置，行变列，列变行
# print(df['股票代码'].str[:2])  # 去除整列数据前两位
# print(df['股票代码'].str.upper())  # 全部大写
# print(df['股票代码'].str.len())  # 字符长度
# print(df['股票代码'].str.contains('sz'))  # 判断字符串长度是否存在

# print(df['新浪概念'].str.split('；').apply(pd.Series))  # 获取分割后数据，为什么要使用str，pands规定的,split之后apply(
# pd.Series)可以平铺展开，explode()可以垂直展开
# print(df.dtypes)
df['交易日期'] = pd.to_datetime(df['交易日期'], dayfirst=True)  # 修改成时间格式
print(df['交易日期'].dt.dayofweek)  # 获取年，还有很多像是year，month，dayofweek获取这是第几天
# df['交易日期'] + pd.Timedelta(days=1)  # 添加时间差
df['收盘价_3天均值'] = df['收盘价'].rolling(3).mean()  # 计算三天平均收盘价
df['收盘价_至今均值'] = df['收盘价'].expanding().mean()  # 计算至今平均收盘价
print(df[['收盘价', '收盘价_3天均值', '收盘价_至今均值']])
df.to_csv('../output.csv', encoding='GBK', index=False)  # 导出csv，设置编码格式，是否保留索引