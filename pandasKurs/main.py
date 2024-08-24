import pandas as pd

""" 
Pandas: simple demo
Author: SLOG
Creation Date: 2024/08/02
"""


# Series (1d)
temp = [28, 30, 34, 29]
ser = pd.Series(temp, index=["a", "b", "c", "d"])
print(ser)

# DataFrame (2d)
sensordata = {
    "sensor": ["", "B", "C", "D"],
    "temp": [28, 30, 34, 29],
}
df = pd.DataFrame(sensordata)
print(df)
print(df.describe())

# plt.plot(ser)
# plt.show()