def is_leap(year):

    
    # Write your logic here
    #constraints

    if year%100==0 and year%400==0:
        return True
    elif year%100 ==0 and year%400 !=0:
        return False
    elif year%100!=0 and year%4 ==0:
        return True
    elif year%4 !=0:
        return False
while True:
    
    year = int(input("put the year : "))
    print(f"is {year} is leap year =  ",is_leap(year))
