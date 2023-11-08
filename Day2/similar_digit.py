# You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, and return the result in %.

# Example:

# compare(13,14)=50%;
# compare(23,22)=50%;
# compare(15,51)=100%;
# compare(12,34)=0%.

def compare(a, b):
    a,b=str(a),str(b)
    if sorted(a)==sorted(b):
        return '100%'
    else:
        for digit in a:
            if digit in b:
                return '50%'
    return '0%'
            