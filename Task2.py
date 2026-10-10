Units = int(input("Enter the total units : "))

if(Units >= 1 and Units <= 100):

    print("Basic Rate")

elif(Units > 100 and Units <= 300):

    print("Standard Rate")

elif(Units > 300):

    print("High Usage Rate")

else:
    
    print("invalid units0")