arr = []
print("Enter 5 numbers:")
for _ in range(5):
    num = int(input("Enter a number: "))
    arr.append(num)
ascending = sorted(arr)
descending = sorted(arr, reverse=True)
print("\nSorted Lists:")
print("Ascending:", ascending)
print("Descending:", descending)

n = int(input("\nEnter a number to generate multiplication table: "))
table = []
for i in range(1, n + 1):
    row = [i * j for j in range(1, n + 1)]
    table.append(row)
print("\nMultiplication Table:")
print(table)
