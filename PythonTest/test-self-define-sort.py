def mycmp(x,y,q='m'):

    if x.index(q) < y.index(q):
        return -1
    elif x.index(q) > y.index(q):
        return 1
    else:
        return 0

p=['abc@123.com', 'nee@123.com', 'm@123.com']
p.sort(mycmp)
# p=['m@123.com', 'abc@123.com', 'nee@123.com']