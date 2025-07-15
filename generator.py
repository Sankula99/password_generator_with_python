import random

def random_password():
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = [c.upper() for c in lower]
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', '?', '/', '|']
    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(symbols) + ''.join(random.choices(lower + upper + digits + symbols, k=8))
    password = ''.join(random.sample(password, len(password)))  
    print(password)

def main():
    random_password()

if __name__ == "__main__":
    main()
