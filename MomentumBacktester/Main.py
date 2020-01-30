# Entry point for the backtester.
# Collects data and launches calculation process.

import pandas_datareader as data
import pickle
from Quote import Quote
from MomentumStrategy import MomentumStrategy

# Download data/load data section
# Data variables
start_date = '2009-01-01'
end_date = '2019-01-01'
stock_name = 'GOOG'

# Fetch data
# google_data = data.DataReader(stock_name, 'yahoo', start=start_date, end=end_date)

# Filename (reused)
dump_file_name = "{0}_stock_{1}-{2}-pkl.pkl".format(stock_name, start_date, end_date)

# Dump the data into a file
# pickle.dump(google_data, open(dump_file_name, 'wb'))

# Read the file from dump file
google_data_loaded = pickle.load(open(dump_file_name, 'rb'))


# Create an instance of MomentumStrategy class with arbitrary parameters
strategy = MomentumStrategy(150, 290, 1)

# FOR loop on quotes: create the Quote instance objects (one per quote line) and feed it (step()) to the strategy object
# google_data_loaded.index[quote_line] is the time assosciated with the quote at index quote_line
all_quotes = [None] * len(google_data_loaded)

for quote_line in range(0,len(google_data_loaded)):
    all_quotes[quote_line] = Quote(1, google_data_loaded['Adj Closed'][quote_line], google_data_loaded.index[quote_line])

for quote_line in range(0,len(google_data_loaded)):
    strategy.step(all_quotes[quote_line])

# Close remaining position to output trade statistics
strategy.close_pending_position(all_quotes[len(google_data_loaded)])
print("Total {0} positions opened.".format(len(strategy.all_positions())))

# Calculate pnl
total_pnl = 0

for position in strategy.all_positions():
    total_pnl += position.return_current_pnl()
    print("Position {0}: profit {1:2.2f}, draw down {2:2.2f}".format(position.trade_situation_id(),
                                                                     position.return_current_pnl(),
                                                                     position.return_current_draw_down()))

print("Total profit (loss) is: {0:2.2f}.".format(total_pnl))
