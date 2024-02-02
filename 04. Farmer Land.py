''' A farmer has a field of 60 acres in which he plants two crops, wheat and barley.
   The farmer has to plant at least 20 acres of wheat and at least 10 acres of barley. 
   He has 1200 pounds of fertilizer and 600 pounds of insecticide available. 
   Each acre of wheat requires 20 pounds of fertilizer and 10 pounds of insecticide, while each acre of barley requires 10 pounds of fertilizer and 15 pounds of insecticide.
   The profit from an acre of wheat is 200 dollars, and the profit from an acre of barley is 150 dollars.
   How many acres of each crop should the farmer plant to maximize his profit? What is the maximum profit? Implement using linear programming package'''

from scipy.optimize import linprog

coeff = [-200, -150]                                                         

#constraints:
A = [[20, 10], [10, 15]]

b = [1200, 600]  

# x, y >= 0 
x_bounds = (20, None)
y_bounds = (10, None)

result = linprog(coeff, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

wheat, barley = result.x
max_profit = -result.fun                                             

print(f"Number of acres for wheat to plant: {wheat:.2f}")
print(f"Number of acres for barley to plant: {barley:.2f}")
print(f"Maximum profit: ${max_profit:.2f}")
