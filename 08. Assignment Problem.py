#Assignment problem

from scipy.optimize import linear_sum_assignment

def assignment(cost_matrix):
  row, col = linear_sum_assignment(cost_matrix)

  total_cost = cost_matrix[row, col].sum()

  return row, col, total_cost

cost_matrix = np.array([[9, 11, 14, 11, 7],
               [6, 15, 13, 13, 10],
               [12, 13, 6, 8, 8],
               [11, 9, 10 ,12, 9],
               [7, 12, 14, 10, 14]])

row, col, total_cost = assignment(cost_matrix)

print("Optimal assignments:", row, col)
print("Total cost:", total_cost)
