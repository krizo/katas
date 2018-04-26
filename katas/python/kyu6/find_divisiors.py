def divisors(integer):
    divs = [ divider for divider in range(1, integer) if integer % divider == 0 and divider != 1 ]
    return "{} is prime".format(integer) if len(divs) == 0 else divs

