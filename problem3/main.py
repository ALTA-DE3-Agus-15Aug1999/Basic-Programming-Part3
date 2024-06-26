def prime_number(num):
    if num < 2 :
        return "Not Prime"
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime" 
    return "Prime"
    

def main():
    num = int
    if num <= 0:
        return "error response"
    elif prime_number(num):
        return "Prime"
    else:
        return "Not Prime"

if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"