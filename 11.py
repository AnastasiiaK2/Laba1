a,b,c=map(int,input().split())
d=b*b-4*a*c
if d>0:
    x1=(-b+d**0.5)/(a*a)
    x2=(-b-d**0.5)/(a*a)
    print("Корни:","{:.3f}".format(x1)," ","{:.3f}".format(x2))
else:
    if d==0:
        x1=(-b)/(a*a)
        print("Корень:","{:.3f}".format(x1))
    else:
        print("Нет корней")
