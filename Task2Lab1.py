string = input("Enter a string: ")
print("Positions of 'i':")
for i in range(len(string)):
    if string[i] == "i":
        print(i)
        