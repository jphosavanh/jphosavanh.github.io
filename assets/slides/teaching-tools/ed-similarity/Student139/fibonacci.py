fibonaci_seq=[]
num = int(input("Which term? "))
i = 0 
while i < num:
    if i == 0 or i == 1:
        fibonaci_seq.append(1)
    else:
        sum_n = fibonaci_seq[i - 1]  + fibonaci_seq [i - 2]
        fibonaci_seq.append(sum_n)
    i+=1 
print(fibonaci_seq[-1])


