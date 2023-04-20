def computepay(h, r):
    if h <= 40:
        pay = h * r
    elif h > 40:
        pay = 40 * r + (h - 40.00) * (r * 1.5)
        return(pay)

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
r = float(rate)
h = float(hrs)
p = computepay(h, r)
print("Pay", p)


      
    

