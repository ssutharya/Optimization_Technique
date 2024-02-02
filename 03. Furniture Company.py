''' A furniture company produces chairs and tables from two resources, wood and metal.
   The company has 125 units of wood and 80 units of metal available.
   Each chair requires 1 unit of wood and 3 units of metal, while each table requires 5 units of wood and 1 unit of metal.
   The profit from selling a chair is 20 dollars, and the profit from selling a table is 30 dollars.
   How many chairs and tables should the company produce to maximize its profit?
   What is the maximum profit? Implement using linear programming package'''

from scipy.optimize import linprog

coeff = [-20, -30]                                      
#constraints:
A = [[1, 5], [3, 1]]                                            

b = [125, 80]                     
                   
# x, y >= 0                    
x_bounds = (0, None)                                        
y_bounds = (0, None)                                                        
result = linprog(coeff, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

num_chairs, num_tables = result.x
max_profit = -result.fun                         
print(f"Number of chairs to produce: {int(num_chairs)}")
print(f"Number of tables to produce: {int(num_tables)}")
print(f"Maximum profit: ${max_profit:.2f}")
