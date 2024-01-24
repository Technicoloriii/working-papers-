# import pandas as pd
# # df = pd.read_csv(r"D:\PhD PSU\My intented papers\paper3-thesis\state files\ULTRAPLUSfinal888.csv")
# #
# # # 删除包含相同'geoname'和'year'的重复行，保留第一个出现的行
# # df_no_duplicates = df.drop_duplicates(subset=['geoname', 'year'])
# #
# # # 保存处理后的DataFrame到新的CSV文件
# # df_no_duplicates.to_csv(r"D:\PhD PSU\My intented papers\paper3-thesis\state files\ULTRAPLUSfinal999.csv", index=False)
# # from statsmodels.tsa.stattools import adfuller
# # #
# # 读取CSV文件，假设有一个'geoname'列和多个变量列
# df = pd.read_csv(r"D:\PhD PSU\My intented papers\paper3-thesis\state files\ULTRAPLUSfinal999.csv")
# numeric_cols = ['AGRm', 'MINm', 'MANm', 'TandWm', 'INFm', 'FandIm', 'Rem', 'HSm', 'PIEPCm', 'TRADEm', 'PSTEm', 'MEHIm', 'unemployrate']
# df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
#
# df = df.dropna(subset=['AGRm', 'MINm', 'MANm', 'TandWm', 'INFm', 'FandIm', 'Rem', 'HSm', 'PIEPCm', 'TRADEm', 'PSTEm', 'MEHIm', 'unemployrate'])

# 定义DF检验的函数
# def perform_adfuller(x):
#     result = adfuller(x, autolag='AIC', regression='ct')
#     return pd.Series({'ADF Statistic': result[0], 'P-value': result[1]})
#
# # 按照'geoname'列分组，对每个变量列执行DF检验
# results = df.groupby('geoname').apply(lambda x: x[['AGRm', 'MINm', 'MANm', 'TandWm', 'INFm', 'FandIm', 'Rem', 'HSm', 'PIEPCm', 'TRADEm', 'PSTEm', 'MEHIm', 'unemployrate']].apply(perform_adfuller))
#
# # 重置索引以获得平坦的结果DataFrame
# results = results.reset_index()
#
# # 保存结果到CSV文件
# results.to_csv(r"D:\PhD PSU\My intented papers\paper3-thesis\state files\DF1result.csv", index=False)
#
# print("结果已保存")

######目前已经得到了DK test的结果，但是明显存在大量的unit root，所以对需要的数据进行一阶差分#####
# df_diff = df.groupby('geoname')[numeric_cols].diff()
# df_diff[['geoname', 'year','region',"taxrevenueratio"]] = df[['geoname', 'year','region',"taxrevenueratio"]]
# df_diff= df_diff.replace(0, pd.NA).dropna()
# df_diff.to_csv("D:\PhD PSU\My intented papers\paper3-thesis\state files\diffresult(withtaxratio).csv", index=False)
#
# print("diff值已经去除0和空值")
# from statsmodels.tsa.stattools import adfuller
# def perform_adfuller(x):
#     result = adfuller(x, autolag='AIC', regression='ct')
#     return pd.Series({'ADF Statistic': result[0], 'P-value': result[1]})
#
# # 按照'geoname'列分组，对每个变量列执行DF检验
# results = df_diff.groupby('geoname').apply(lambda x: x[['AGRm', 'MINm', 'MANm', 'TandWm', 'INFm', 'FandIm', 'Rem', 'HSm', 'PIEPCm', 'TRADEm', 'PSTEm', 'MEHIm', 'unemployrate']].apply(perform_adfuller))
#
# # 重置索引以获得平坦的结果DataFrame
# results = results.reset_index()
#
# # 保存结果到CSV文件
# results.to_csv(r"D:\PhD PSU\My intented papers\paper3-thesis\state files\diffDFresult-temp.csv", index=False)
#
# print("diff DF test已保存")

##############################################进行df test然后对结果进行筛选且针对结果进行数据处理###############################
import pandas as pd
from statsmodels.tsa.stattools import adfuller

df = pd.read_csv(r"D:\PhD PSU\My intented papers\paper3-thesis\state files\ULTRAPLUSfinal999.csv")
numeric_cols = ['AGRm', 'MINm', 'MANm', 'TandWm', 'INFm', 'FandIm', 'Rem', 'HSm', 'PIEPCm', 'TRADEm', 'PSTEm', 'MEHIm', 'unemployrate']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

df = df.dropna(subset=['AGRm', 'MINm', 'MANm', 'TandWm', 'INFm', 'FandIm', 'Rem', 'HSm', 'PIEPCm', 'TRADEm', 'PSTEm', 'MEHIm', 'unemployrate'])

# 定义DF检验的函数
def perform_adfuller(x):
    results = []
    for col in numeric_cols:
        result = adfuller(x[col], autolag='AIC', regression='ct')
        results.append({'Variable': col, 'ADF Statistic': result[0], 'P-value': result[1]})
    return pd.DataFrame(results)

# 按照'geoname'列分组，对每个变量列执行DF检验
results = df.groupby('geoname').apply(perform_adfuller)
print(results.head(6))
results.to_csv(r"D:\PhD PSU\My intented papers\paper3-thesis\state files\dftestcomprehensive.csv", index=False)
# 根据p值阈值进行判断，小于0.05保留，大于等于0.05进行一阶差分
threshold = 0.1
for geoname, result in results.groupby('geoname'):
    for idx, row in result.iterrows():
        p_value = row['P-value']
        if p_value < threshold:
            # 保留数据
            print(f"Keep data for geoname {geoname}, variable {row['Variable']}")
        else:
            # 进行一阶差分
            print(f"Apply first-order differencing for geoname {geoname}, variable {row['Variable']}")
            df.loc[df['geoname'] == geoname, row['Variable']] = df.loc[df['geoname'] == geoname, row['Variable']].diff()

print(df.head(6))
# 保存处理后的DataFrame到新的CSV文件
df.to_csv(r'D:\PhD PSU\My intented papers\paper3-thesis\state files\processeddata.csv', index=False)

#########################################用处理好的数据进行df test##################################################


df = pd.read_csv(r"D:\PhD PSU\My intented papers\paper3-thesis\state files\processeddata.csv")
numeric_cols = ['AGRm', 'MINm', 'MANm', 'TandWm', 'INFm', 'FandIm', 'Rem', 'HSm', 'PIEPCm', 'TRADEm', 'PSTEm', 'MEHIm', 'unemployrate']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

df = df.dropna(subset=['AGRm', 'MINm', 'MANm', 'TandWm', 'INFm', 'FandIm', 'Rem', 'HSm', 'PIEPCm', 'TRADEm', 'PSTEm', 'MEHIm', 'unemployrate'])

# 定义DF检验的函数
def perform_adfuller(x):
    result = adfuller(x, autolag='AIC', regression='ct')
    return pd.Series({'ADF Statistic': result[0], 'P-value': result[1]})

# 按照'geoname'列分组，对每个变量列执行DF检验
results = df.groupby('geoname').apply(lambda x: x[['AGRm', 'MINm', 'MANm', 'TandWm', 'INFm', 'FandIm', 'Rem', 'HSm', 'PIEPCm', 'TRADEm', 'PSTEm', 'MEHIm', 'unemployrate']].apply(perform_adfuller))

# 重置索引以获得平坦的结果DataFrame
results = results.reset_index()

# 保存结果到CSV文件
results.to_csv(r"D:\PhD PSU\My intented papers\paper3-thesis\state files\processedDFTEST.csv", index=False)

print("结果已保存")
