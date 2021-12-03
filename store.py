# -*- coding: utf-8 -*-
"""
Spyder Editor
Final additional project
Ciaran McDonnell

"""
class Store:
    """Most general store class.
      
      Create a parent class with the general store attributes that can be
      inherited for more specific store classes.
      
      Attributes:
          name: string
              string containing store name.
          address: string
              string containing address of store.
          revenue: float
              float of the revenue intake of the store.   
          employees: list, string
              initially empty list. List of employee names.
              
      Methods:
          calculate_profit: input the total outflow of money as int or string,
                calculates profit made by store.              
          add_employee: input employee name (str) and add to the end of the list
                of current employees.             
          remove_employee: input existing emplyee name (str) and remove from the
                current employee list. Must match list entry exactly.               
          print_employees: prints the list of current employees vertically.    
      
    """
      
    def __init__(self, name, address, revenue):
        """Initialise instance of Store class.

        Parameters
        ----------
        name : string
            string containing store name.
        address : string
i            string containing address of store.
        revenue : float
            float of the revenue intake of the store.

        Returns
        -------
        None.

        """
        self._name = name
        self._address = address
        self._revenue = revenue
        self.employees = []
        
    @property
    def name(self):
        """Get the name of the store
        

        Returns
        -------
        str
            Name of the store.

        """
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        
    @property
    def address(self):
        """Get the address of the store
        

        Returns
        -------
        str
            Address of the store.

        """
        return self._address
    
    @address.setter
    def address(self, new_address):
        self._addres = new_address
        
    @property
    def revenue(self):
        """Get the revenue of the store.
        

        Returns
        -------
        float
            Revenue of the store.

        """
        return self._revenue
    
    @revenue.setter
    def revenue(self, new_revenue):
        self._revenue = new_revenue
    
    def calculate_profit(self, outflow):
        """Print the profit made by store.
        
        Use the total money outflow subtracted from the revenue of store to 
        calculate and print the store name and corresponding profit. Does not 
        return the profit at the moment, just prints it. Accounts for negative 
        profits, i.e. losses.
        

        Parameters
        ----------
        outflow : float
            Total amount of money in store outflow, costs, expenses, wages etc.

        Returns
        -------
        None. 
        
        """
        profit = self.revenue - outflow
        if (profit)<0:
            print("Loss of £"+ str(abs(profit)))
        else:
            print("We made £" + str(profit))
            
    def add_employee(self, employee_name):
        """Add employee name to list.
        
        Take in new employee name as a string and add it to the end of the
        current employee list. List currently not ordered.

        Parameters
        ----------
        employee_name : str
            Name of the employee to add to the store.

        Returns
        -------
        None.

        """
        self.employees.append(employee_name)     
        
    def remove_employee(self, employee_name):
        """Remove employee from current employee list.
        
        Use input name (str) to match and remove from current employee list.
        Does not currently account for multiple employees with same name. 
        Name must match exactly to the current employee list entry.
        

        Parameters
        ----------
        employee_name : str
            Name of employee to remove from employee list.

        Returns
        -------
        None.

        """
        if employee_name in self.employees:
            self.employees.remove(employee_name)
        else:
            print("Oops! We don't have an employee named", employee_name + "!")
            
    def print_employees(self):
        """Print the list of current employees.
        
        Print the list of current employees vertically on separate lines with 
        a heading. Does not return the list at the moment, only prints the
        entries.
        

        Returns
        -------
        None.

        """
        print("=== Current Employee List ===")
        for i in self.employees:
            print(i)
        
            
            
            
            
            
            
        