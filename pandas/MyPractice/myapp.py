import pandas as pd

# 创建一个包含示例数据的字典
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Lawyer'],  # 新增列
    'Salary': [70000, 120000, 50000, 90000]  # 新增列
}

# 使用字典创建 DataFrame
df = pd.DataFrame(data)

# 打印 DataFrame
print(df)