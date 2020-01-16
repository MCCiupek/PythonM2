import numpy as np
import pandas as pandas
import pandas_datareader as data
import pickle
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Data variables
start_date = "2018.01.01"       # Date format to respect : "YYYY.MM.DD"
end_date = "2019.01.01"
stock_name = "GOOG"             # using several tickers : tickers = ["TICK1", "TICK2", ...]

# Fetch data
google_data = data.DataReader(stock_name, 'yahoo', start=start_date, end=end_date)

# Get adjusted Close
closed_data = google_data['Close']
print(closed_data.describe())   # Stats descriptives

# Compute he 20 days moving average
goog = closed_data.loc[:]
short_rolling_goog_20 = goog.rolling(window=20).mean()
short_rolling_goog_100 = goog.rolling(window=100).mean()
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(short_rolling_goog_20.index, short_rolling_goog_20, label='GOOG 20-days moving avg')
ax.plot(short_rolling_goog_100.index, short_rolling_goog_100, label='GOOG 100-days moving avg')

ax.set_xlabel('Date')
ax.set_ylabel('Closing Price ($)')
ax.legend()
plt.savefig("mygraph.png")
# ou plt.show()

# Print statistics
print(google_data.tail())
print('Lines:{0}; Columns {1}'.format(google_data.shape[0], google_data.shape[1]))

# filename (reused)
dump_file_name = "{0}_stock_{1}-{2}.csv".format(stock_name, start_date, end_date)

# Dump data into file
# np.savetxt(dump_file_name, google_data, delimiter=",")
pickle.dump(google_data, open(dump_file_name, 'wb'))

# Read the file from dump file
# google_data_loaded = pandas.read_csv(dump_file_name, delimiter=',')
google_data_loaded = pickle.load(open(dump_file_name, 'rb'))

print('-> LOADED')
print(google_data_loaded.tail())
print('Lines:{0}; Columns {1}'.format(google_data.shape[0], google_data.shape[1]))

# Pour sauvegarder l'objet : pickle.dump(object, file)
# Pour charger l'objet : pickle.load(file)
# Charger le fichier :  open(dump_file_name, 'wb') [pour l'ecriture]
#                       open(dump_file_name, 'rb') [pour la lecture]
# picke permet un pas à pas détaillé pdt l'execution ?