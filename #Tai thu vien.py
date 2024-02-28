#Tai thu vien
import pandas as pd
import matplotlib.pyplot as plt
import os

os. chdir("C:/Users/Admin/Documents/HK6/Apache Spark/Thuchanh\Lab 2.1")

#Buoc1: Tai du lieu
df = pd.read_csv("sales_data.csv")

#Buoc2: Khai pha du lieu
#xem mot so dong
print(df.head())
#kiem tra du lieu loi
print(df.isnull().sum())

#xem thong ke du lieu
print(df.describe());

#loc du lieu theo mot so san pham cu the
product_a_data = df[df["Product"] == "Product A"]

#Buoc3: Truc quan du lieu co ban
#Tao bieu do cho truong du lieu product
product_sales = df.groupby("Product")["Amount"].sum()
plt.xlabel("San pham")
plt.ylabel("So luong ban")
plt.show()