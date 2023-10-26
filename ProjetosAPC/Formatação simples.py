def trunc (x,p):
    q=10**p
    r = int(x * q)
    y=float(r / q)
    return y

a=float(input())
b=float(input())
p=int(input())
c=trunc((a/b), p)
ina=int(a)
inb=int(b)
abp=(f"{c :.{p}f}")
print('O resultado de ', ina, ' por ', inb, ' é ',abp, '.', sep="")

