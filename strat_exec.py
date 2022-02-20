import data
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

class Crypto_simple_negative_correlation_trading:
    def __init__(self, cash, asset_quantity, jump_cutoff, trading_frequency):
        self.cash = cash
        self.asset_quantity = asset_quantity
        self.jump_cutoff = jump_cutoff
        self.trading_frequency = trading_frequency  #7200second = 2 hours
        self.asset_quantity_data = []
        self.cash_data = []
    
    #def strat_exec(prices, times):
    #    start_time = datetime.strptime(times[0], "%Y-%m-%d %H:%M:%S")
    #    start_price = prices[0]
#
     #   for i in range(0, len(times)):
     #       current_time = datetime.strptime(times[i], "%Y-%m-%d %H:%M:%S")
     #       time_diff = current_time - start_time
     #       current_price = prices[i]
#
      #      if time_diff.total_seconds() >= self.trading_frequency: # can i assume a trade will happen evry 4 hours
      #          make_trade(start_price, current_price)
# 
#                #update
#                start_time = current_time
#                start_price = current_price
#        return
    def strat_exec(self, prices):
        plt.figure(1)
        plt.plot(prices, 'g')
        plt.show()
        start_price = prices[0]
        for i in range(1, len(prices)):
            current_price = prices[i]
            self.make_trade(start_price, current_price)
            
            start_price = current_price
        return
    
    def make_trade(self, start_price, current_price):
            #if jump is not significant
            price_diff = start_price-current_price
            if( abs(price_diff) < self.jump_cutoff ):
                return
            
            #go long
            if start_price > current_price:
                #- buy asset
                #- decrease cash
                if self.cash != 0:
                    self.cash = 0.9 * self.cash    # transaction cost
                    self.asset_quantity = self.cash / current_price
                    self.cash = 0
            
            #go short
            elif start_price < current_price: 
                #- sell asset
                #- increase cache
                if self.asset_quantity != 0:
                    self.cash = self.asset_quantity * current_price
                    self.cash = 0.9 * self.cash   # transaction cost
                    self.asset_quantity = 0
            
            self.model_stats()

            self.asset_quantity_data.append(self.asset_quantity)
            self.cash_data.append(self.cash)
            return

    def model_stats(self):
        print(self.cash, " ", self.asset_quantity)

    def model_stats_for_graph(self):
        plt.figure(2)
        plt.plot(self.cash_data, 'r')
        plt.plot(self.asset_quantity_data, 'k')
        plt.show()

#jump_cutoff (rolling lookback)
#time interval
