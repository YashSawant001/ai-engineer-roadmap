ip = int(input("how many numbers you want to enter: "))

num_list = [0]

positive_count = 0
negative_count = 0
zero_count = 0

for i in range(ip):
    num = int(input("enter a number: "))
    num_list.append(num)

for num in num_list:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"positive count is {positive_count}")
print(f"negative count is {negative_count}")
print(f"zero count is {zero_count}")

largest = num_list[0]
smallest = num_list[0]

for num in num_list:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print(f"{largest} is the largest number")
print(f"{smallest} is the smallest number")


avg=sum(num_list)/len(num_list)
print(f"average is {avg}")
