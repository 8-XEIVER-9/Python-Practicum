def is_prime(num):
    for dels in range(2, int(num**0.5) + 1):
        if num % dels == 0 and num != dels:
            return False
    return True