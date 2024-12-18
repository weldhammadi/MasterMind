import random

def generate_secret_code():
    return [random.randint(1, 6) for _ in range(4)]
