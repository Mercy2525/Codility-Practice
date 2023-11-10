def tribonacci(signature, n):
    if len(signature)>n:
        return signature[:n]
    

    while len(signature)<n:
        next_num=sum(signature[-3:])
        signature.append(next_num)
    return signature

print(tribonacci([1, 1, 1],8))

def fibonacci(signature, n):
    #signature = [1,1,1]

    while len(signature)<n:
        next_num=sum(signature[-2:])
        signature.append(next_num)
    return signature


