largest = None
smallest = None
while True:
    number = input("Enter a number: ")
    
    if number == "done":
        break
    print(number)
    try:
        num = int(number)
    except:
        print("Invalid Input")
        continue
    if smallest  is None:
        smallest = num
    if largest is None:
        largest = num
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num 

print("Maximum is", largest)
print("Minimum is", smallest)


    
