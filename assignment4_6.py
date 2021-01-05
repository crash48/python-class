
def computepay(hrs, rph) :
    if hrs < 40 :
        gpay = (fw * 40 * rph)
    gpay = (fw * 40 * rph) + (overtime * rph * 1.5)
    return gpay
hrs = input("Enter Hours:")
hrs = int(hrs)
rph1 = input("Enter rate per Hour:")
rph=float(rph1)
h = float(hrs)
fw = hrs // 40
overtime  = hrs % 40

computepay(hrs,rph)
print(computepay(hrs,rph))


