rows = int(input("Enter the number of pyramid rows: "))
pyramid = []

for i in range(1, rows + 1):
    pyramid.append("*" * i)

for line in pyramid:
    print(line)