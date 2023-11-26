import pandas as pd
data = pd.read_excel(r'F:\juchao_link\股东大会公告链接_2018.xlsx')
a = list(data['年报链接'])
print(len(a))
# 更新原始DataFrame
data2 = data.drop_duplicates()
a2 = list(data2['年报链接'])
print(len(a2))

data2.to_excel(r'F:\juchao_link\股东大会公告链接_2018_去重.xlsx', index=False)  # 将DataFrame保存为Excel文件，不包含行索引




