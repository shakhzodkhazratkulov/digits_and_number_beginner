#Find the sum of digits in an integer
def get_sum_digits(num):
    x=0
    x1=num%10
    num//=10
    x2=num%10
    num//=10
    x3=num%10
    num//=10
    x4=num%10
    num//=10
    x5=num%10
    num//=10

    x = x1+x2+x3+x4+x5
    return x

print(get_sum_digits(1234))