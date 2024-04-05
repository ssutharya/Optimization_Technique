# Transportation problem - northwest corner cell method using user inpuut

import numpy as np

def northwest_corner_cell(supply, demand):
  solution = np.zeros((len(supply), len(demand)))

  current_supply = supply.copy()
  current_demand = demand.copy()

  for i in range(len(supply)):
    for j in range(len(demand)):
      allocation = min(current_supply[i], current_demand[j])

      solution[i][j] = allocation
      current_supply[i] -= allocation
      current_demand[j] -= allocation

      if current_demand[j] == 0:
        break

  return solution

supply = list(map(int, input("Enter the supply for each source (separated by spaces): ").split()))
demand = list(map(int, input("Enter the demand for each destination (separated by spaces): ").split()))

solution = northwest_corner_cell(supply, demand)

print("\nInitial Solution:")
print(solution)
