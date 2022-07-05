# Challenge 1:
# Get the nth number in the fibonacci sequence given n
# Alternatively given a number F, print out whether it's a fibonacci number and what the closest index n in the
# fibonacci sequence is.

def fibonacci(n,f):
    prev = 0
    curr = 1
    list_fibanocci = [0,1]
    if n == 1:
        print(prev)
    elif n == 2:
        print(list_fibanocci)
    elif n > 2:
        for i in range(n-2):
            total = prev + curr
            list_fibanocci.append(total)
            prev = curr
            curr = total
        print("The "+str(n)+"th number in fibonacci series is: "+str(total))
    if f in list_fibanocci:
        print(str(f)+" "+"is a fibonacci number")
    else:
        diff = list_fibanocci[-1]
        ind = n-1
        for i in range(len(list_fibanocci)):
            x = abs(f-list_fibanocci[i])
            if x < diff:
                diff = x
                ind = i
        print("The closest index in the fibanocci series in the range of "+str(n)+ " for "+str(f)+" is: "+str(ind))
            

fibonacci(6,4)
