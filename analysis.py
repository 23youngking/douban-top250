import pandas as pd

df = pd.read_csv("movies.csv")

print("平均评分：", df["rating"].mean())
print("评分最高：", df.nlargest(5, "rating")[["title", "rating"]])
print("各年代电影数量：\n", df["year"].value_counts().head(10))