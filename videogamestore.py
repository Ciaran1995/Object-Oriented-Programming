#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:03:31 2021

@author: ciaranmcdonnell
"""
from store import Store

class VideoGameStore(Store):
    """Class representing a videogame store inheriting from general store class.
    
    Attributes:
        name: string containing store name.
        address: string containing address of store.
        revenue: float of the revenue intake of the store.
        console_list: list of strings containing the consoles the store deals in .
        game_inventory: dictionary with game name as key, and then a list containing
            [consoles game is played on (str), number of copies left in stock (int),
             price of game (float)].
              
    Methods:
        calculate_profit: inherited from parent class, input the total outflow 
                of money as int or string, calculates profit made by store.
        add_game: input the quantities listed in game_inventory attribute, 
                adds the game and its details to the store inventory.
        sell_game: input the name of the game (str), choose how many copies 
                to sell (int) and the total price will be calcuated and games
                removed from inventory.     
    """
    
    def __init__(self, name, address, revenue, console_list):
        """Initialise instance of videogamestore class.
        

        Parameters
        ----------
        name : string
            string containing store name.
        address : string
            string containing address of store.
        revenue : float
            float of the revenue intake of the store.
        console_list : dictionary
           dictionary with game name as key, and then a list containing
            [consoles game is played on (str), number of copies left in stock (int),
             price of game (float)].

        Returns
        -------
        None.

        """
        super().__init__(name, address, revenue)
        self.console_list = console_list
        self._game_inventory = {}
        
    @property 
    def game_inventory(self):
        """get game_inventory attribute
        

        Returns
        -------
        dictionary
            game_inventory is a dictionary with game name as key, and then a list containing
            [consoles game is played on (str), number of copies left in stock (int),
             price of game (float)]..

        """
        return self._game_inventory
    
    def calculate_profit(self, outflow):
        """Print the profit made by store.
        
        Use parent class method. Use the total money outflow subtracted from the revenue of store to 
        calculate and print the store name and corresponding profit. Does not 
        return the profit at the moment, just prints it.
        

        Parameters
        ----------
        outflow : float
            Total amount of money in store outflow, costs, expenses, wages etc.

        Returns
        -------
        None. 

        """
        print("====", self.name, "Profit Calculator ====" )
        Store.calculate_profit(self, outflow)
        
    def add_game(self, game_name, console, number_copies, price):
        """Add game to inventory.
        
        Add a games name, what console it can be played on, number of copies
        available and the price of the game to a dictionary entry with the 
        name as the key, and the other characteristics as a list in the above
        order. This will not aoutomatically add to already existing dictionary
        entries, this should be done by just updating the number of copies.
        

        Parameters
        ----------
        game_name : string
            Name of the game to be added to inventory.
        console : list, string
            List of the console names the game can be played on.
        number_copies : int
            Number of copies of a given game in stock. Will not throw error 
            for negative int.
        price : float
            Price of the game being added to the inventory.

        Returns
        -------
        None.

        """
        self._game_inventory[game_name]= [console, number_copies, price]
        
        # Possibly add an alphabetical sorting method in here?
        
    def sell_game(self, game_name):
        """Sell game from the store.
        
        Choose name of the game to sell, choose how many copies to sell and 
        then calculate and print the price of the transaction. Sale will not
        be completed until confirmation given as [y]/[n] input. Can't currently
        sell multiple games at once. Does account for game not in stock, or 
        requesting more copies of a game than are in stock.
        

        Parameters
        ----------
        game_name : str
            Name of the game to be sold. Must match the inventory name exactly.

        Returns
        -------
        None.

        """
    
        print("==== Welcome to ", self.name, "====")
        sell = True
        while sell == True:
        
            if self._game_inventory[game_name][1] < 1:
                print("\n We don't have ", self._game_inventory[game_name], "in stock.")
            else:
                print("We have", self._game_inventory[game_name][1], "copies of", game_name, "in stock.")
                quantity = input("How many copies would you like to purchase?\n")
                
                if self._game_inventory[game_name][1]-int(quantity)<0:
                    print("Not enough copies in stock")
                    
                else:    
                    print("That will cost £"+ str(int(quantity)*self._game_inventory[game_name][2]))
                
                    sale = input("Continue with purchase? [y]/[n] \n")
                
                    if sale == "y":
                        print("Thank you for your purchase. Have a nice day!")
                        
                        self._game_inventory[game_name][1] -= int(quantity)
                        self.revenue += int(quantity)*self._game_inventory[game_name][2]
                        
                        sell = False
                
                    
                    
                    