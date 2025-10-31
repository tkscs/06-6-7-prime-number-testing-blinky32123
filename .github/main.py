p=67
n=1
d=p%2 
a=p%3
b=p%5
c=p%7 
for x in range(1):
    if d>0:
        print("prime")
        break
    # if a>0:
    #     print("prime")
    #     break
    # if b>0:
    #     print("prime")
    #     break
    # if c>0:
    #     print("prime")
    #     break
    else:
        print("no prime")