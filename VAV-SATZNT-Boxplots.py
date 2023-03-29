import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, AutoDateLocator, AutoDateFormatter
import matplotlib.dates as mdates

path = "G:/Shared drives/Developing Novel SOO to Operate Shades at Willis Tower/03 - Analysis & Report/06 - Paper (ENB)/Data/Plots/VAV-SATZNT.csv"

df = pd.read_csv(path, usecols=['Date', 'SA-T', 'ZN-T'])
df['Date'] = pd.to_datetime(df['Date'])
DateTime = df['Date']
SupplyTemp = df['SA-T']
ZoneTemp = df['ZN-T']

dt11 = datetime.datetime(2021, 5, 3, 0, 0)
dt12 = datetime.datetime(2022, 2, 21, 0, 0)
dt21 = datetime.datetime(2022, 2, 14, 0, 0)
dt22 = datetime.datetime(2022, 3, 7, 0, 0)
step1 = datetime.timedelta(weeks=2)
step2 = datetime.timedelta(weeks=1)

dateticklabels = pd.date_range(start=dt11, end=dt12, freq=step1).strftime('%Y-%m-%d-%H:%M').tolist()
dateticklabels += pd.date_range(start=dt21, end=dt22, freq=step2).strftime('%Y-%m-%d-%H:%M').tolist()

plt.style.use('classic')
df = pd.DataFrame(list(zip(SupplyTemp, ZoneTemp)), columns = ['SA-T', 'ZN-T'])
df.boxplot(column = ['SA-T', 'ZN-T'], whis=(0,100), widths=(0.2, 0.2), whiskerprops = {'color' : 'k'},
    medianprops = {'color' : 'k'}, boxprops = {'color' : 'k', 'linewidth' : 2})
locs, labels = plt.xticks()
ax = plt.gca()

plt.ylabel("Temperature (°C)", fontsize=15)
plt.xticks(ticks=locs, labels=['SA-T', 'ZN-T'],fontsize=15)
plt.ylim([10, 30])

plt.tight_layout()
plt.show()