import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.family"] = "SimHei"  # 支持中文
import pandas as pd
df = pd.read_csv("movies.csv")
# 评分分布
plt.figure(figsize=(10, 5))
plt.hist(df["rating"], bins=20, color="steelblue", edgecolor="white")
plt.title("豆瓣 Top250 评分分布")
plt.xlabel("评分")
plt.ylabel("电影数量")
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

# 年代分布（Top 15）
year_counts = df["year"].value_counts().head(15).sort_index()
plt.figure(figsize=(12, 5))
year_counts.plot(kind="bar", color="coral")
plt.title("各年代上榜电影数量")
plt.xlabel("年份")
plt.ylabel("数量")
plt.tight_layout()
plt.savefig("year_distribution.png")
plt.show()

