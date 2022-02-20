import numpy as np
import pandas as pd
import warnings

def get_price_data(chosen_coin, chosen_dataset):
    """
    Acquire price data for coins.
    :param: string name of excel worksheet containing coin data.
    """
    warnings.filterwarnings('ignore')

    # Choose sample of tickers to pull from
    path = f'coin_data/{chosen_coin}/{chosen_dataset}.csv'

    # Retrieve price data
    data = pd.read_csv(path, names=["Open","High","Low","Close","Volume","Trades"])
    prices = data.loc[:, "Open"].tolist()

    return prices
    # Save data to csv
    #path = f'strategy/prices/{chosen_dataset}.csv'
    #data.to_csv(path)

    