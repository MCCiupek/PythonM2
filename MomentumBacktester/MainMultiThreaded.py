# Entry point for the multithreaded backtester.
# Collects data and launches calculation process.

import pandas_datareader as data
import pickle
from MomentumBacktester.Quote import Quote
from MomentumBacktester.MomentumStrategy import MomentumStrategy
import concurrent.futures

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


# Function launched in parallel
def backtest_strategy(strategy_arg: tuple, quotes_arg: list) -> MomentumStrategy:
    """
    Creates the MomentumStrategy instance with received in argument strategy_arg. Initializes the trading on quotes list
    :param strategy_arg: tuple with 3 parameters of the strategy (slow MA, fast MA and take profit)
    :param quotes_arg: list of Quote objects (common to all the backtesters and created once)
    :return: backtested strategy
    """

    # Close the position (if hanging) with the last available quote

    return None



# Convert all the data in Quote objects reusable later in classes. Easier to maintain and reuse between backtests

# start parameters
ma_start = 5
ma_end = 150
ma_step = 20
target_profit_start = 1
target_profit_end = 10
target_profit_step = 3
# Map of constructed arguments

# Loop on target profit

    # Loop on MA parameters


            # Double check that the ma_slow > ma_fast! Required not to have the problem with our backtester. Also saves
            # memory

                # Create and append tuple (ma_slow, ma_fast, target_profit) with 3 parameters to the all_strategy
                # arguments list


# Start working with ThreadPoolExecutor

    # Create an empty list of Futures

    #print("Adding threads\nMA slow\tMA fast\tTarget Profit")
    # For all the values of all_strategy_arguments submit the backtest_strategy to the executor

    #    print("{0}\t{1}\t{2}".format(i, all_strategy_arguments[i][0], all_strategy_arguments[i][1],
    #                                 all_strategy_arguments[i][2]))

    #print("MA slow\tMA fast\tTarget Profit\tPositions opened\tPnL")
    # Wait on all executions to end

    # Output execution details (ordered)

        # Calculate the pnl

        # output the strategy backtest result
        #print("{0}\t{1}\t{2}\t{3}\t{4:1.2f}\t\t{5}".format(strategy_result.get_ma_slow(), strategy_result.get_ma_fast(),
        #                                                   strategy_result.get_target_profit(),
        #                                                   len(strategy_result.all_positions()), total_pnl,
        #                                                   strategy_result.get_strategy_id()))
