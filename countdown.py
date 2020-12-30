
nstr=input("How many seconds would you like to count down?")
n = int(nstr)
import time
ans = "x"
while ans != "y" :
    ans=input("Do you want to start? <Y/N>")
    ans=str.lower(ans)
    if ans=="y" :
        while n > 0 :
            print(n)
            n=n-1
            time.sleep(1)
        print("Blastoff!")
    elif ans=="n" :
        print("Launch sequence abborted!")
        print("Exiting in 3...")
        time.sleep(1)
        print("2..")
        time.sleep(1)
        print("1.")
        time.sleep(1)
        print("Good bye!")
        quit()
    else :
        print("Wrong input, try again.")

# this is a comment
# TODO: Fix this piece of code
