import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("PieData.xlsx")
# print(df)
colors = ["#05A9C7", "#154734", "#63666A", "#F6BE00", "#D76B00"]
fig = plt.figure(figsize=(10, 7))

patches, texts, start = plt.pie(
df["Percent"],
    colors=colors,
    startangle=120,
    autopct="%.1f%%",
    textprops={'color': 'white',
                   'size': 'large',
                   'fontweight': 'bold'},
)

plt.legend(patches, df["AgreeRatio"], loc="best")
plt.axis('equal')
# plt.setp(, color="white")
plt.show()
