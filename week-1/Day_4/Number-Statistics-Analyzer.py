ip = int(input("how many numbers you want to enter: "))

num_list = []

for i in range(ip):
    num = int(input("enter a number: "))
    num_list.append(num)

for num in num_list:
    if num > 0:
        print(f"{num} is a positive number")
    elif num < 0:
        print(f"{num} is a negative number")
    else:
        print(f"{num} is zero")

for i in range(len(num_list)):
    if i == 0:
        largest = num_list[i]
        smallest = num_list[i]
    else:
        if num_list[i] > largest:
            largest = num_list[i]
        if num_list[i] < smallest:
            smallest = num_list[i]

print(f"{largest} is the largest number")
print(f"{smallest} is the smallest number")
