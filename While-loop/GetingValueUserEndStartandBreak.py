print("Taking input from user start and end values and printing values in between while loop")
start = int(input("Enter start value: "))
end = int(input("Enter end value: "))
i = start
break_point =int(input("Enter a break point value: "))
while i <= end:
    print(i)
    if i == break_point:
        print("Breaking the loop as i reached 15")
        break
    i += 1