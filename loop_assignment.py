## ==== Question No.1 ====
for x in range(1, 6):
    for i in range(1, x+1):
        print(i, end=" ") 
    print("\n")

## ==== Question No. 2 ====
_user_input = int(input("Enter a number value: "))
_total_sum = 0

for x in range(1, _user_input+1):
    _total_sum = _total_sum + x
print(_total_sum)

## ==== Question 3 ====
for x in range(5, 0, -1):
    print("* " * x)

for y in range(0, 6):
    print("* " * y)