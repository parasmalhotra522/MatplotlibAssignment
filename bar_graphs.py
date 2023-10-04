import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("Data.xlsx")
# view dataset

df2 = pd.DataFrame(
    {"Name" : "Total",
"Less Than 4 hrs":sum(df["Less Than 4 hrs"])/len(df["Less Than 4 hrs"]),
"4 hr to less than 5 hrs": sum(df["4 hr to less than 5 hrs"])/ len(df["4 hr to less than 5 hrs"]),
"5 hr to less than 6 hrs": sum(df["5 hr to less than 6 hrs"])/len(df["5 hr to less than 6 hrs"]),
"6 hrs to less than 7 hr": sum(df["6 hrs to less than 7 hr"])/len(df["6 hrs to less than 7 hr"])
     }, index=[0] )
# print(df2)
df = (pd.concat([df, df2], ignore_index=True))


print(df)
df_total = (df["Less Than 4 hrs"] + df["4 hr to less than 5 hrs"] + df["5 hr to less than 6 hrs"] + df["6 hrs to less than 7 hr"] )

df.plot(
    x='Name',
    kind='barh',
    stacked=True,
    title='Hours of School Night Sleep',
    mark_right=True,

).invert_yaxis()
df_rel = df[df.columns[1:]].div(df_total, 0) * 100

for n in df_rel:
    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n],
                                         df[n], df_rel[n])):
        plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%',
                 va='center', ha='center')

# plt.legend(loc="upper right")
plt.xticks(visible=False)
plt.show()
