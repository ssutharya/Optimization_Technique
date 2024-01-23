#dynamic programming

def knapsack(cap, w, val, n):                            #cap - capacity, w - weight, val - value, n - number of items
    F = [[0] * (cap + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(cap + 1):
            if w[i - 1] <= j:
                F[i][j] = max(val[i - 1] + F[i - 1][j - w[i - 1]], F[i - 1][j])
            else:
                F[i][j] = F[i - 1][j]

    print("\nThe Matrix is:")
    for i in range(n + 1):
        for j in range(cap + 1):
            print(F[i][j], end="\t")
        print()

    i, j = n, cap
    print("Selected items:")
    while i > 0 and j > 0:
        if F[i][j] != F[i - 1][j]:
            print(f"Item: {i} (Weight: {w[i - 1]} & Value: {val[i - 1]})")
            j -= w[i - 1]
        i -= 1


n = int(input("Enter the number of items: "))
cap = int(input("Enter the maximum capacity: "))

w = []
val = []

print("Enter the weight and its corresponding value:")
for i in range(n):
    weight = int(input(f"Weight {i + 1}: "))
    value = int(input(f"Value {i + 1}: "))
    w.append(weight)
    val.append(value)

knapsack(cap, w, val, n)
