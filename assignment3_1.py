gpay = float
fw = float
overtime = float
rph = float
hrs = input("Enter Hours:")
hrs = int(hrs)
h = float(hrs)
rph = input("Enter rate per Hour:")

fw = hrs // 40
overtime  = hrs % 40

#print(fw)
#print(overtime)
if hrs < 40 :
    gpay = (fw * 40 * float(rph))
gpay = (fw * 40 * float(rph)) + (overtime * (float(rph) * 1.5))

print (gpay)
