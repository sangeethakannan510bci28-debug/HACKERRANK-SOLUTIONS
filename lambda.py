cube = lambda x:  (x*x*x) 
# complete the lambda function 

def fibonacci(n):
    # return
    ls=[]
    for i in range(n):
        if i==0:
            ls.append(0)
        elif i==1:
            ls.append(1)
        elif i>1:
            res = ls[i-2]+ls[i-1]
            ls.append(res)

    return ls

