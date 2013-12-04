def digit_sum(num):
    return sum(int(x) for x in str(num))

def digit_sum_alt(num):
    def digits(number):
        while number:
            yield number % 10
            number /= 10
    
    return sum(digits(num))
