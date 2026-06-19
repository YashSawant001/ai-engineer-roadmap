Num = int(input("Enter a number of Students: "))
marks = []
for i in range(Num):
    mark = int(input(f"Number of Marks per student {i+1}: "))
    marks.append(mark)

print(max(marks))
print(min(marks))
print(sum(marks) / len(marks))