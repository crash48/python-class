score = input("Enter score between 0.1 and 1.0:")


if float(score) > 1.0 or float(score) < 0.0 :
    print("Score out of range!")
if float(score) >= 0.9 :
    print("A")
elif float(score) >= 0.8 : 
    print("B")
elif float(score) >= 0.7 :
    print("C")
elif float(score) >= 0.6 :
    print("D")
elif float(score) < 0.6 :
    print("F)")