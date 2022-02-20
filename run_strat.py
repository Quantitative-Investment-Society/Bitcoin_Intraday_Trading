import sys
import get_data as Data
import strat_exec as Strat
import matplotlib.pyplot as plt





def run_strat():
    """
    Runs Strategy.
    :requires: name of excel file with ticker data
    """
    if len(sys.argv) != 3:
        print('Usage: python3 driver.py <coin_filename>') 
        sys.exit(1)
    # retrive price/time and all other data for coin dataset
    coin_file = sys.argv[1]
    prices = Data.get_price_data(coin_file)

    # run strat
    cash = 1000
    asset_quantity = 0
    jump_cutoff = 0
    trading_frequency = 720 * 60
    Strat_obj = Strat.Crypto_simple_negative_correlation_trading(cash, asset_quantity, jump_cutoff, trading_frequency)

    # backtest portfolio
    Strat_obj.strat_exec(prices)

    #performance
    Strat_obj.model_stats_for_graph()
    return	


run_strat()