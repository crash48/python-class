hrs = input("Enter Hours:")
hrs = int(hrs)
h = float(hrs)
rph1 = input("Enter rate per Hour:")
rph=float(rph1)

fw = hrs // 40
overtime  = hrs % 40

#print(fw)
#print(overtime)
if hrs < 40 :
    gpay = (fw * 40 * rph)
gpay = (fw * 40 * rph) + (overtime * rph * 1.5)

print (gpay)
