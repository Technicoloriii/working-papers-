from pandas import DataFrame
import pandas as pd
import numpy as np
import glob


# 读取Excel文件
file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/total_tax_rows_combined_processed2.xlsx'
df = pd.read_excel(file_path)

# 创建一个新的DataFrame，存储每一列每四行的求和结果
result_df = pd.DataFrame()

# 遍历每一列，每四行求和，并添加到新的DataFrame中
for column in df.columns:
    if df[column].dtype == 'float64' or df[column].dtype == 'int64':
        # 如果是数字列，执行每四行求和的操作，指定min_periods为4
        result_df[column] = df[column].rolling(window=4, min_periods=4).sum()

# 将结果保存到新的Excel文件
output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/output_excel_file.xlsx'  # 替换成你想保存的Excel文件路径
result_df.to_excel(output_file_path, index=False)



# # 读取Excel文件
# file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/total_tax_rows_combined_processed2.xlsx'
# df = pd.read_excel(file_path)
#
# # 创建一个新的DataFrame，存储每一列每四行的求和结果
# result_df = pd.DataFrame()
#
# # 遍历每一列，每四行求和，并添加到新的DataFrame中
# for column in df.columns:
#     if df[column].dtype == 'float64' or df[column].dtype == 'int64':
#         # 如果是数字列，执行每四行求和的操作，添加偏移量
#         result_df[column] = df[column].shift(-3).rolling(window=4, min_periods=1).sum()
#
# # 将结果保存到新的Excel文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/output_excel_file.xlsx'  # 替换成你想保存的Excel文件路径
# result_df.to_excel(output_file_path, index=False)

# # 读取Excel文件
# file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/total_tax_rows_combined_processed2.xlsx'
# df = pd.read_excel(file_path)
#
# # 创建一个新的DataFrame，存储每一列每四行的求和结果
# result_df = pd.DataFrame()
#
# # 遍历每一列，每四行求和，并添加到新的DataFrame中
# for column in df.columns:
#     if df[column].dtype == 'float64' or df[column].dtype == 'int64':
#         # 如果是数字列，执行每四行求和的操作
#         result_df[column] = df[column].rolling(window=4, min_periods=1).sum()
#
# # 将结果保存到新的Excel文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/output_excel_file.xlsx'  # 替换成你想保存的Excel文件路径
# result_df.to_excel(output_file_path, index=False)

# # 读取Excel文件
# file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/total_tax_rows_combined_processed2.xlsx'
# df = pd.read_excel(file_path)
#
# # 遍历每一列，每四行求和
# for column in df.columns:
#     if df[column].dtype == 'float64' or df[column].dtype == 'int64':
#         # 如果是数字列，执行每四行求和的操作
#         df[column] = df[column].rolling(window=4, min_periods=1).sum()
#
# # 将结果保存到新的Excel文件
# new_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/yearly_data.xlsx'
# df.to_excel(new_file_path, index=False)


#
# # 读取原始Excel文件
# file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/total_tax_rows_combined_processed2.xlsx'
# df = pd.read_excel(file_path, index_col=0)  # 假设第一列是州的名称
#
# # 删除最左侧一列和最上面一行
# df = df.iloc[1:, 1:]
#
# # 将每个州的数据每隔四个季度求和
# df_yearly = df.groupby((df.columns.astype(int) - 1) // 4 * 4 + 1, axis=1).sum()
#
# # 保存新的Excel文件
# new_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/yearly_data.xlsx'
# df_yearly.to_excel(new_file_path)
#
# print("每个州的数据已每隔四个季度求和，并保存为新的Excel文件。")
# #
# # # 读取原始Excel文件
# # file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/total_tax_rows_combined_processed2.xlsx'
# # df = pd.read_excel(file_path, index_col=0)  # 假设第一列是州的名称
# #
# # # 将每个州的数据每隔四个季度求和
# # df_yearly = df.groupby((df.columns.astype(int) - 1) // 4 * 4 + 1, axis=1).sum()
# #
# # # 保存新的Excel文件
# # new_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/yearly_data.xlsx'
# # df_yearly.to_excel(new_file_path)
# #
# print("每个州的数据已每隔四个季度求和，并保存为新的Excel文件。")
#
# # 读取原始Excel文件
# # file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/total_tax_rows_combined_processed2.xlsx'
# #
# # df = pd.read_excel(file_path, index_col=0)  # 假设第一列是州的名称
#
# # 将每个州的数据每隔四个季度求和
# df_yearly = df.groupby(np.floor_divide(df.columns.astype(int), 4) * 4, axis=1).sum()
#
# # 保存新的Excel文件
# new_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/yearly_data.xlsx'
# df_yearly.to_excel(new_file_path)
#
# print("每个州的数据已每隔四个季度求和，并保存为新的Excel文件。")
#
#
# #
# # 读取原始Excel文件
# file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/total_tax_rows_combined_processed2.xlsx'
# df = pd.read_excel(file_path, index_col=0)  # 假设第一列是州的名称
#
# # 将每个州的数据每隔四个季度求和
# df_yearly = df.groupby(df.columns // 4 * 4, axis=1).sum()
#
# # 保存新的Excel文件
# new_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/yearly_data.xlsx'
# df_yearly.to_excel(new_file_path)
#
# print("每个州的数据已每隔四个季度求和，并保存为新的Excel文件。")

######################################################################################
# # 指定Excel文件所在的文件夹路径
# excel_folder = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly'
#
# # 获取文件夹中所有的Excel文件（包括xlsx和xls）
# excel_files = glob.glob(excel_folder + '/*.xls*')  # 匹配xlsx和xls文件
#
# # 创建一个空的DataFrame，用于存储所有选取的行数据
# total_tax_data = pd.DataFrame()
#
# # 循环读取每个Excel文件并处理
# for file in excel_files:
#     # 读取Excel文件
#     excel_data = pd.read_excel(file, header=0)
#
#     # 检查第一列是否包含 "Total Tax" 或 "Total Taxes"，并且不是空白列
#     contains_total_tax = excel_data.iloc[:, 0].apply(
#         lambda cell: 'Total Tax' in str(cell) or 'Total Taxes' in str(cell) or 'Total' in str(cell) or 'TOTAL' in str(cell)if pd.notna(cell) else False)
#
#     # 选取符合条件的整行数据
#     total_tax_rows = excel_data[contains_total_tax]
#
#     # 遍历每个选中的行，处理非数字内容
#     for index, row in total_tax_rows.iterrows():
#         for col in range(1, len(row)):
#             cell_value = str(row[col])
#             # 删除非数字内容，将右侧的单元格左移
#             row[col - 1] = ''.join(filter(str.isdigit, cell_value))
#
#     # 添加一列标识来源文件的信息
#     total_tax_rows['Source File'] = file
#
#     # 将选取的行数据追加到total_tax_data中
#     total_tax_data = total_tax_data.append(total_tax_rows, ignore_index=True)
#
# # 将选取的行数据按文件自上而下的顺序保存为新的Excel文件
# total_tax_data.to_excel('D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/total_tax_rows_combined_processed2.xlsx', index=False)
###############################################################################
#
#
# import pandas as pd
#
# # 读取原始Excel文件
# file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\state tax revenue quarterly/total_tax_rows_combined_processed2.xlsx'
# df = pd.read_excel(file_path, index_col='Time')  # 假设"Time"是时间列的名称
#
# df["Time"].heade()
#


# 将时间列转换为日期格式
# df.index = pd.to_datetime(df.index, format='%Yq%q')
#
# # 按州进行分组，并按年度进行求和
# df_yearly = df.groupby(df.index.year).sum()
#
# # 保存新的Excel文件
# new_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\yearly_data.xlsx'
# df_yearly.to_excel(new_file_path)
#
# print("数据已按年度总结，并保存为新的Excel文件。")
