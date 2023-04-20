largest = None
smallest = None
while True:
    number = input("Enter a number: ")
    
    if number == "done":
        print("All done")
        break
    print(number)
    try:
        num = float(number)
    except:
        print("Invalid Input")
        continue
    if smallest  is None:
        smallest = num
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num 
def done(largest,smallest):
    print("Maximum is", largest)
    print("Minimum is", smallest)
done(largest,smallest)
    
