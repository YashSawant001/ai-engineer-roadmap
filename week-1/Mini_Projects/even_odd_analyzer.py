num = int(input("number of no. you want to enter : "))
num_list = []

for i in range(num):
    numb = int(input(f"enter the number {i+1}: "))
    num_list.append(numb)

print(num_list)

even_count = 0
odd_count = 0

for i in num_list:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"no. of odd is {odd_count}")
print(f"no. of even is {even_count}")

largest = num_list[0]
smallest = num_list[0]

for numb in num_list:
    if largest < numb:
        largest = numb
    if smallest > numb:
        smallest = numb
print(largest)
print(smallest)
print(f"Average is {sum(num_list) / len(num_list)}")