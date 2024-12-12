def pro(*b):
    res=b[0]
    if len(b)>1:
        i=1
        while i<len(b):
            res*=b[i]
            i+=1
    return res

def add(*b):
    res=b[0]
    if len(b)>1:
        i=1
        while i<len(b):
            res+=b[i]
            i+=1
    return res

def sub(*b):
    res=b[0]
    if len(b)>1:
        i=1
        while i<len(b):
            res-=b[i]
            i+=1
    return res

def div(*b):
    res=b[0]
    if len(b)>1:
        i=1
        while i<len(b):
            if b[i]!=0:
                res/=b[i]
            i+=1
    return res

if __name__ == "__main__":
    print("Frm Arithmetic :",globals())