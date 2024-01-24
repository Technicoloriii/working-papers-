
import pandas as pd
import os
#######wenjianhebing#######
# # 指定包含所有CSV文件的文件夹路
# folder_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/2017-2022'
#
# # 获取文件夹中所有CSV文件的文件名
# csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
#
# # 创建一个空的DataFrame来存储所有数据
# all_data = pd.DataFrame()
#
# # 逐个读取每个CSV文件的前93行，并将数据添加到all_data中
# for file in csv_files:
#     file_path = os.path.join(folder_path, file)
#     df = pd.read_csv(file_path, nrows=93)
#     all_data = pd.concat([all_data, df], ignore_index=True)
#
# # 将合并后的数据写入新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/2017-2022.csv'
# all_data.to_csv(output_file_path, index=False)
#
# print(f'合并完成，结果保存在 {output_file_path}')
#
# import pandas as pd
#
# # 读取原始CSV文件
# input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/gsp_naics_all_98-14.csv'
# df = pd.read_csv(input_file_path)
#
# # 定义条件，保留满足条件的行
# conditions = df['IndustryClassification'].isin(["11", "21", '31-33', "42", '44-45', '48-49', "51", "52", "53", "54", "61","62"])
# filtered_df = df[conditions]
#
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries\washed file/02-15filtered_file.csv'
# filtered_df.to_csv(output_file_path, index=False)
#
# print(f'筛选完成，结果保存在 {output_file_path}')
#
# input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/2017-2022.csv'
# df = pd.read_csv(input_file_path)
#
# # 定义条件，保留满足条件的行
# conditions = df['IndustryClassification'].isin(["11", "21", '31-33', "42", '44-45', '48-49', "51", "52", "53", "54", "61","62"])
# filtered_df = df[conditions]
#
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries\washed file/17-22filtered_file.csv'
# filtered_df.to_csv(output_file_path, index=False)
#
# print(f'筛选完成，结果保存在 {output_file_path}')


#############16-22wenjianhebing #################


# 读取原始CSV文件
# input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/2017-2022.csv'
# df = pd.read_csv(input_file_path)
#
# # 第一步：保留IndustryClassification满足条件的行
# conditions_step1 = df['IndustryClassification'].isin(["11", "21", '31-33', "42", '44-45', '48-49', "51", "52", "53", "54", "61", "62"])
# df_step1 = df[conditions_step1]
#
# # 第二步：在第一步的基础上，选择包含 "61" 或 "62" 的行，并对 "2017" 到 "2022" 列的数值进行相加
# conditions_step2 = df_step1['IndustryClassification'].isin(['61', '62'])
# df_step1['61,62'] = df_step1.loc[conditions_step2, ['2017', '2018', '2019', '2020', '2021', '2022']].sum(axis=1)
#
# # 在 "61,62" 行的 "Description" 列添加新的内容
# df_step1.loc[conditions_step2, 'Description'] = 'Educational services, health care, and social assistance'
#
# # 第三步：删除原来的 "61" 和 "62" 行
# df_step1 = df_step1[~conditions_step2]
#
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries\washed file/16-22filtered_file.csv'
# df_step1.to_csv(output_file_path, index=False)
#
# print(f'操作完成，结果保存在 {output_file_path}')


##################shujuronghe#######Data Merge##########

# 读取两个CSV文件
# file1_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries\washed file/02-15filtered_file.csv'
# file2_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries\washed file/17-22filtered_file.csv'
# df1 = pd.read_csv(file1_path)
# df2 = pd.read_csv(file2_path)
#
# # 合并两个数据框，按照 "GeoName" 和 "IndustryClassification" 列进行合并
# merged_df = pd.merge(df1, df2, on=['GeoName', 'IndustryClassification'], how='inner', suffixes=('_file1', '_file2'))
#
# # 选择需要的列
# selected_columns = ['GeoName', 'IndustryClassification', '2017_file2', '2018_file2', '2019_file2', '2020_file2', '2021_file2', '2022_file2']
#
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries\washed file/merged_file.csv'
# merged_df[selected_columns].to_csv(output_file_path, index=False)
#
# print(f'合并完成，结果保存在 {output_file_path}')

############################2016data selection###############

# input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/SAGDP2N__ALL_AREAS_1997_2018.csv'
# df = pd.read_csv(input_file_path)
#
# # 定义条件，保留满足条件的行
# conditions = df['IndustryClassification'].isin(["11", "21", '31-33', "42", '44-45', '48-49', "51", "52", "53", "54", "61","62"])
# filtered_df = df[conditions]
#
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries\washed file/allfiltered_file.csv'
# filtered_df.to_csv(output_file_path, index=False)
#
# print(f'筛选完成，结果保存在 {output_file_path}')


# 读取panel data文件
# panel_data_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/02-22GDPby industry filtered_file-panel.csv'
# panel_data = pd.read_csv(panel_data_path)
#
# # 读取state tax revenue文件
# state_tax_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/state tax annully00--22.csv'
# state_tax = pd.read_csv(state_tax_path)
#
# # 合并两个文件，按照'id'和'时间变量'进行合并
# merged_data = pd.merge(panel_data, state_tax, left_on=['id', '时间变量'], right_on=['id', 'year'], how='left')
#
# # 将合并后的新列命名为'state tax revenue'
# merged_data = merged_data.rename(columns={'state_tax_revenue': 'state tax revenue'})
#
# # 保存结果为新的CSV文件
# output_path = '/path/to/merged_data.csv'
# merged_data.to_csv(output_path, index=False)
#
# print(f'合并完成，结果保存在 {output_path}')




##############zhuanbianwei panel Data###################
#
# import pandas as pd
#
# # 读取包含各个年份的CSV文件
# input_file_path = '/path/to/your/input/file.csv'
# df = pd.read_csv(input_file_path)
#
# # 将数据转换为面板数据格式
# panel_data = df.melt(id_vars=['YourIdentifierColumn'], var_name='Year', value_name='Value')
#
# # 将 "Year" 列转换为整数类型
# panel_data['Year'] = panel_data['Year'].astype(int)
#
# # 可选：将 "YourIdentifierColumn" 列的名称替换为更具体的标识符名称
# panel_data = panel_data.rename(columns={'YourIdentifierColumn': 'Entity'})
#
# # 将结果保存为新的CSV文件
# output_file_path = '/path/to/your/output/panel_data.csv'
# panel_data.to_csv(output_file_path, index=False)
#
# print(f'转换完成，结果保存在 {output_file_path}')


##########面板数据转换###########

# import pandas as pd
#
# # 读取包含各个年份的CSV文件
# input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/02-22GDPby industry filtered_file - Copy.csv'
# df = pd.read_csv(input_file_path)
#
# # 使用melt函数将数据转换为面板数据格式
# panel_data = pd.melt(df, id_vars='GeoName')
#
# # # 将 "year" 列的内容转换为整数类型
# # panel_data['year'] = panel_data['year'].astype(int)
#
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/panel_data.csv'
# panel_data.to_csv(output_file_path, index=False)
#
# print(f'转换完成，结果保存在 {output_file_path}')

# 读取CSV文件为DataFrame
# input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/02-22GDPby industry filtered_file - Copy.csv'
# df = pd.read_csv(input_file_path)  # 如果文件没有标题行，可以省略header=None
#
# # 删除DataFrame的前两列和第一行
# df = df.iloc[0:, 2:]
#
# # 将DataFrame每12行分为一个新的DataFrame，并转置
# dfs = [df.iloc[i:i+12, :].T.reset_index(drop=True) for i in range(0, len(df), 12)]
#
# print(dfs[0])
#
# print(dfs[1])
#
# print(dfs[50])
# # 将分DataFrame按照原本的顺序自上而下拼接
# result_df = pd.concat(dfs, axis=0, ignore_index=True)
#
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/new_file.csv'
# result_df.to_csv(output_file_path, index=False)
#
# print(f'处理完成，结果保存在 {output_file_path}')


#####保留expenditure per capita###########
# input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/person income expenditure per capita1997_2022.csv'
# df = pd.read_csv(input_file_path)
#
# # 定义条件，保留满足条件的行
# conditions = df['Description'].isin(["Per capita personal consumption expenditures"])
# filtered_df = df[conditions]
#
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries\washed file/filtered personal income.csv'
# filtered_df.to_csv(output_file_path, index=False)
#
# print(f'筛选完成，结果保存在 {output_file_path}')


#########panel data merge##########


# 读取第一个panel data文件
# panel1_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/merged_panel.csv'
# panel1 = pd.read_csv(panel1_path)
#
# # 读取第二个panel data文件
# panel2_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/longdatagdp.csv'
# panel2 = pd.read_csv(panel2_path)
#
# # 合并两个panel data，按照'id'和'year'进行合并
# merged_panel = pd.merge(panel1, panel2, on=['GeoName', 'year'], how='outer')
#
# # 保存结果为新的CSV文件
# output_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/Ultramerged_panel-2.csv'
# merged_panel.to_csv(output_path, index=False)
#
# print(f'合并完成，结果保存在 {output_path}')

##########数据帅选GDP###########

# # input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/SAGDP2N__ALL_AREAS_1997_2018.csv'
# # df = pd.read_csv(input_file_path)
# input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/2017-2022.csv'
# df = pd.read_csv(input_file_path)
#
#
# # 仅保留IndustryId的内容为“1”的行
# filtered_df = df[df['LineCode'] == 1]
#
# # 将筛选后的内容保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/gdp filtered2.csv'
# filtered_df.to_csv(output_file_path, index=False)
#
# print(f'筛选完成，结果保存在 {output_file_path}')

########################data merge of gdps########
# 读取第一个panel data文件
# panel1_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/gdp filtered.csv'
# panel1 = pd.read_csv(panel1_path)
#
# # 读取第二个panel data文件
# panel2_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\GDP by industries/gdp filtered2.csv'
# panel2 = pd.read_csv(panel2_path)
#
# # 合并两个panel data，按照'id"合并
# merged_panel = pd.merge(panel1, panel2, on=['GeoName'], how='outer')
#
# # 保存结果为新的CSV文件
# output_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/GDP by industries/mergedgdp.csv'
# merged_panel.to_csv(output_path, index=False)

########将gdp的宽数据变为长数据############
# import pandas as pd
#
# 读取宽数据CSV文件
# wide_data_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\gdp and personal income/personal income by state.csv'
# wide_data = pd.read_csv(wide_data_path)
#
# # 使用melt方法将宽数据转换为长数据
# long_data = pd.melt(wide_data, id_vars='GeoName', var_name='variable_name', value_name='value')
#
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/gdp and personal income/longdatapersonalincome.csv'
# long_data.to_csv(output_file_path, index=False)
#
# print(f'转换完成，结果保存在 {output_file_path}')

########################data merge of ultrararara########
# # 读取第一个panel data文件
# panel1_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/Ultramerged_panel-2.csv'
# panel1 = pd.read_csv(panel1_path)
#
# # 读取第二个panel data文件
# panel2_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/longdatapersonalincome.csv'
# panel2 = pd.read_csv(panel2_path)
# # 将 'year' 列转换为整数类型
# # panel1['GeoName'] = panel1['GeoName'].astype(str)
# # panel2['GeoName'] = panel2['GeoName'].astype(str)
# # panel1['year'] = panel1['year'].astype(int)
# # panel2['year'] = panel2['year'].astype(int)
# # print(panel1.head())
# # print(panel2.head())
# # 合并两个panel data，按照'id"合并
# merged_panel = pd.merge(panel1, panel2, on=['GeoName',"year"], how='outer')
#
# # 保存结果为新的CSV文件
# output_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/ULTRARARARARA.csv'
# merged_panel.to_csv(output_path, index=False)
# print(f'合并完成，结果保存在 {output_path}')

##########数据筛选per capita expenditure###########
# df = pd.read_csv(input_file_path)
# input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\gdp and personal income\income/person income expenditure per capita1997_2022.csv'
# df = pd.read_csv(input_file_path)
#
#
# # 仅保留IndustryId的内容为“1”的行
# filtered_df = df[df['LineCode'] == 1]
#
# # 将筛选后的内容保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/all washed/personal expenditure filtered2.csv'
# filtered_df.to_csv(output_file_path, index=False)
#
# print(f'筛选完成，结果保存在 {output_file_path}')
##########totaloutlay wide to long###############

#  读取宽数据CSV文件
# wide_data_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/trustfunds.csv'
# wide_data = pd.read_csv(wide_data_path)
#
# # 使用melt方法将宽数据转换为长数据
# long_data = pd.melt(wide_data, id_vars='GeoName')
# # var_name='variable_name', value_name='value'
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data/trustfundslong.csv'
# long_data.to_csv(output_file_path, index=False)


# ##########constraint wide to long###############
#
#  读取宽数据CSV文件
# wide_data_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\medianhouseholdincome.csv'
# wide_data = pd.read_csv(wide_data_path)
#
# # 使用melt方法将宽数据转换为长数据
# long_data = pd.melt(wide_data, id_vars='year')
# # var_name='variable_name', value_name='value'
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\medianhouseholdincomelong.csv'
# long_data.to_csv(output_file_path, index=False)

##########federalfunds wide to long###############

#读取宽数据CSV文件
# wide_data_path = r'D:\PhD PSU\My intented papers\paper3-thesis\state files\population_xls\population.csv'
# wide_data = pd.read_csv(wide_data_path)
#
# # 使用melt方法将宽数据转换为长数据
# long_data = pd.melt(wide_data, id_vars='year')
# # var_name='variable_name', value_name='value'
# # 将结果保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\populationlong.csv'
# long_data.to_csv(output_file_path, index=False)
# print(f'转换完成，结果保存在 {output_file_path}')

#######data merge on income expenditure per capita###############
#读取第一个panel data文件
panel1_path = r'D:\PhD PSU\My intented papers\paper3-thesis\state files\ULTRAPLUSfinal999.csv'
panel1 = pd.read_csv(panel1_path)

# 读取第二个panel data文件
panel2_path = r'D:\PhD PSU\My intented papers\paper3-thesis\Data/populationlong.csv'
panel2 = pd.read_csv(panel2_path)
# 将 'year' 列转换为整数类型
# panel1['GeoName'] = panel1['GeoName'].astype(str)
# panel2['GeoName'] = panel2['GeoName'].astype(str)
# panel1['year'] = panel1['year'].astype(int)
# panel2['year'] = panel2['year'].astype(int)
# print(panel1.head())
# print(panel2.head())
# 合并两个panel data，按照'id"合并
merged_panel = pd.merge(panel1, panel2, on=['geoname',"year"], how='outer')

# 保存结果为新的CSV文件
output_path = r'D:\PhD PSU\My intented papers\paper3-thesis\state files/ULTRAPLUSFINALmate.csv'
merged_panel.to_csv(output_path, index=False)
print(f'合并完成，结果保存在 {output_path}')


##############合并########
# 读取第一个panel data文件
# panel1_path = r'D:\PhD PSU\My intented papers\paper3-thesis\state files/ULTRAPLUSfinal666.csv'
# panel1 = pd.read_csv(panel1_path)
#
# # 读取第二个panel data文件
# panel2_path = r'D:\PhD PSU\My intented papers\paper3-thesis\state files\predictionn.csv'
# panel2 = pd.read_csv(panel2_path)
#
# # 合并两个panel data，按照'id"合并
# merged_panel = pd.merge(panel1, panel2, on=['geoname',"year"], how='outer')
#
# # 保存结果为新的CSV文件
# output_path = r'D:\PhD PSU\My intented papers\paper3-thesis\state files/ULTRAPLUSfinal888.csv'
# merged_panel.to_csv(output_path, index=False)
# print(f'合并完成，结果保存在 {output_path}')
# #########替换非数值类型和缺失值###############

# # 读取CSV文件为DataFrame
# input_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\intergovernmental transfer/igt structure.csv'
# df = pd.read_csv(input_file_path)
#
# # 选择你想要处理的变量名列表
# selected_variables = ['1997', '1998', '1999', '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022',]  # 替换为你实际的变量名列表
#
# # 循环处理每个变量
# for variable in selected_variables:
#     # 替换非数值类型或空值为0
#     df[variable] = pd.to_numeric(df[variable], errors='coerce').fillna(0)
#
# # 将处理后的内容保存为新的CSV文件
# output_file_path = 'D:\PhD PSU\My intented papers\paper3-thesis\Data\intergovernmental transfer/igt structure-filtered.csv'
# df.to_csv(output_file_path, index=False)
#
# print(f'处理完成，结果保存在 {output_file_path}')


######################月度转年度数据#########################

# # 读取CSV文件为DataFrame
# input_file_path = 'D:/PhD PSU/My intented papers/paper3-thesis/Data/unemploymentrate_xls/unemployment.csv'
#
# df = pd.read_csv(input_file_path)
#
# # 将时间列转换为日期类型
# df['DATE'] = pd.to_datetime(df['DATE'])
#
# # 提取年份和月份
# df['Year'] = df['DATE'].dt.year
# df['Month'] = df['DATE'].dt.month
#
# # 按年和月对数据进行分组，并计算每组的平均值
# annual_data = df.groupby('Year').mean().reset_index()
#
# # 将处理后的内容保存为新的CSV文件
# output_file_path = 'D:/PhD PSU/My intented papers/paper3-thesis/Data/unemploymentrate_xls/unemploymentLONG.csv'
#
# annual_data.to_csv(output_file_path, index=False)
#
# print(f'处理完成，结果保存在 {output_file_path}')


##########unemployment rate wide to long###############

#  读取宽数据CSV文件
# wide_data_path = 'D:/PhD PSU/My intented papers/paper3-thesis/Data/unemploymentrate_xls/unemploymentLONG.csv'
#
# wide_data = pd.read_csv(wide_data_path)
#
# # 使用melt方法将宽数据转换为长数据
# long_data = pd.melt(wide_data, id_vars='year')
# # var_name='variable_name', value_name='value'
# # 将结果保存为新的CSV文件
# output_file_path = 'D:/PhD PSU/My intented papers/paper3-thesis/Data/unemploymentLONG.csv'
# long_data.to_csv(output_file_path, index=False)
#
# print(f'转换完成，结果保存在 {output_file_path}')

##################政党数据筛选####################
# 读取CSV文件为DataFrame
# wide_data_path = r'D:\PhD PSU\My intented papers\paper3-thesis\Data\Political/united_states_governors2020.csv'
# df = pd.read_csv(wide_data_path)
#
# # 筛选数据，只保留year大于1997的行
# df_filtered = df[df['year'] > 1996]
#
# # 将处理后的内容保存为新的CSV文件
# output_file_path = 'D:/PhD PSU/My intented papers/paper3-thesis/Data/Political/state governor.csv'
# df_filtered.to_csv(output_file_path, index=False)
#
# print(f'处理完成，结果保存在 {output_file_path}')

##############合并########
# # 读取第一个panel data文件
# panel1_path = r'D:\PhD PSU\My intented papers\paper3-thesis\Data\Final version/ULTRAPLUSfinal333.csv'
# panel1 = pd.read_csv(panel1_path)
#
# # 读取第二个panel data文件
# panel2_path = r'D:\PhD PSU\My intented papers\paper3-thesis\Data\Political/state governor.csv'
# panel2 = pd.read_csv(panel2_path)
#
# # 合并两个panel data，按照'id"合并
# merged_panel = pd.merge(panel1, panel2, on=['GeoName',"year"], how='outer')
#
# # 保存结果为新的CSV文件
# output_path = r'D:\PhD PSU\My intented papers\paper3-thesis\Data/Final version/ULTRAPLUSfinal444.csv'
# merged_panel.to_csv(output_path, index=False)
# print(f'合并完成，结果保存在 {output_path}')

#######计算prediction 的tax revenue#############

# 读取CSV文件为DataFrame
panel_data_path = r'D:\PhD PSU\My intented papers\paper3-thesis\state files\ULTRAPLUSfinal666.csv'
df = pd.read_csv(panel_data_path)


# # 示例：假设不同的分组需要不同的计算公式
# def calculate_prediction(region):
#     if GeoName['region'].iloc[0] == 'Far West':
#         # 对于分组 A，假设计算方式是 var1 + var2
#         GeoName['prediction'] = region['TandWr']*-0.5484 + region['FandIr']*-1.70604 + region['INFr']*-0.572237 + region['PSTEr']*0.2919 + region['unemployrate']*-0.0025677 + 0.2180679
#     elif region['region'].iloc[0] == 'Great Lakes':
#         # 对于分组 B，假设计算方式是 var1 * var2
#         region['prediction'] = region['AGRr']*0.4495893 + region['MINr']*-1.006615 + region['MANr']*-0.0594577 + region['TandWr']*-0.322338 + region['FandIr']*-0.2267668 + region['unemployrate']*0.0015273 + 0.0780404
#     elif region['region'].iloc[0] == 'Mideast':
#         # 对于分组 C，假设计算方式是 var1 - var2
#         region['prediction'] = region['MINr']*-0.156207 + region['MANr']*-0.0396119 + region['TandWr']*0.4429027 + region['FandIr']*0.0347388 + region['HSr']*-0.2321409 + region['unemployrate']*-0.0008518 + 0.0222942
#     elif region['region'].iloc[0] == 'New England':
#         # 对于分组 D，假设计算方式是 var1 - var2
#         region['prediction'] = region['MINr']*7.210451 + region['FandIr']*0.3635953 + region['HSr']*0.6137935 + region['PSTEr']*-0.8714954
#     elif region['region'].iloc[0] == 'Plains':
#         # 对于分组 E，假设计算方式是 var1 - var2
#         region['prediction'] = region['AGRr']*-0.2425323 + region['MINr']*0.3439634 + region['MANr']*0.0733198 + region["TandWr"]*0.0849959+ region['INFr']* -0.146418 + region['FandIr']*-0.1470049 +region["PSTEr"]*-0.5388382 + region['HSr']*0.3196291 + region["PIEPCm"]*0.0212268 + region['MEHIm']*0.0085626-0.0587206
#     elif region['region'].iloc[0] == 'Rocky Mountain':
#         # 对于分组 F，假设计算方式是 var1 - var2
#         region['prediction'] = region['MANr']*-0.125827 +region["TandWr"]*-0.2473223 + region['INFr']*-0.3116889+region["PSTEr"]*-0.1867746-0.0978338
#     elif region['region'].iloc[0] == 'Southeast':
#         # 对于分组 G，假设计算方式是 var1 - var2
#         region['prediction'] = region['AGRr']*0.4647685 + region['MANr']*-0.1953741 + region["TandWr"]*0.2304958 + region['FandIr']*-0.6692+region["PIEPCm"]*-0.0299612+region['MEHIm']*0.0008565+0.1804981
#     else:
#         # 对于其他分组，可以定义默认的计算方式
#         region['prediction'] = region['AGRr']*1.367147 + region['MANr']*-0.1176086  + region['HSr']*0.2579161 + 0.0614231

#     # 返回计算后的 DataFrame
#     return region
#
# df_with_prediction = df.apply(calculate_prediction, axis=1)
# # output_file_path = r'D:\PhD PSU\My intented papers\paper3-thesis\stata files\ULTRAPLUSfinal777.csv'
# # df.to_csv(output_file_path, index=False)
# print("finished")

# 示例：假设不同的分组需要不同的计算公式
# def calculate_prediction(region):
#     if row['region'] == 'Far West':
#         # 对于分组 A，假设计算方式是 var1 + var2
#         row['prediction'] = row['TandWr']*-0.5484 + row['FandIr']*-1.70604 + row['INFr']*-0.572237 + row['PSTEr']*0.2919 + row['unemployrate']*-0.0025677 + 0.2180679
#     elif row['region'] == 'Great Lakes':
#         # 对于分组 B，假设计算方式是 var1 * var2
#         row['prediction'] = row['AGRr']*0.4495893 + row['MINr']*-1.006615 + row['MANr']*-0.0594577 + row['TandWr']*-0.322338 + row['FandIr']*-0.2267668 + row['unemployrate']*0.0015273 + 0.0780404
#     elif row['region']  == 'Mideast':
#         # 对于分组 C，假设计算方式是 var1 - var2
#         row['prediction'] = row['MINr']*-0.156207 + row['MANr']*-0.0396119 + row['TandWr']*0.4429027 + row['FandIr']*0.0347388 + row['HSr']*-0.2321409 + row['unemployrate']*-0.0008518 + 0.0222942
#     elif row['region'] == 'New England':
#         # 对于分组 D，假设计算方式是 var1 - var2
#         row['prediction'] = row['MINr']*7.210451 + row['FandIr']*0.3635953 + row['HSr']*0.6137935 + row['PSTEr']*-0.8714954
#     elif row['region'] == 'Plains':
#         # 对于分组 E，假设计算方式是 var1 - var2
#         row['prediction'] = row['AGRr']*-0.2425323 + row['MINr']*0.3439634 + row['MANr']*0.0733198 + row["TandWr"]*0.0849959+ row['INFr']* -0.146418 + row['FandIr']*-0.1470049 +row["PSTEr"]*-0.5388382 + row['HSr']*0.3196291 + row["PIEPCm"]*0.0212268 + row['MEHIm']*0.0085626-0.0587206
#     elif row['region'] == 'Rocky Mountain':
#         # 对于分组 F，假设计算方式是 var1 - var2
#         row['prediction'] = row['MANr']*-0.125827 +row["TandWr"]*-0.2473223 + row['INFr']*-0.3116889+row["PSTEr"]*-0.1867746-0.0978338
#     elif row['region'] == 'Southeast':
#         # 对于分组 G，假设计算方式是 var1 - var2
#         row['prediction'] = row['AGRr']*0.4647685 + row['MANr']*-0.1953741 + row["TandWr"]*0.2304958 + row['FandIr']*-0.6692+row["PIEPCm"]*-0.0299612+row['MEHIm']*0.0008565+0.1804981
#     else:
#         # 对于其他分组，可以定义默认的计算方式
#         row['prediction'] = row['AGRr']*1.367147 + row['MANr']*-0.1176086 + row['HSr']*0.2579161 + 0.0614231
#
#     # 返回计算后的 DataFrame
#     return row
# df_with_prediction = df.apply(calculate_prediction, axis=1)
# output_file_path = r'D:\PhD PSU\My intented papers\paper3-thesis\stata files\ULTRAPLUSfinal777.csv'
# df.to_csv(output_file_path, index=False)