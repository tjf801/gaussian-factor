from complex import complex
from math import sqrt, ceil

def sum_of_two_squares(n):
    if n % 4 == 3: return (n, 0)
    for i in range(ceil(sqrt(n))):
        if sqrt(n - (i*i)).is_integer():
            return (i, int(sqrt(n - (i*i))))

def prime_factors(n):
    factors = []
    i = 2
    while n != 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i += 1
    return factors

def gaussian_factors(z):
    if isinstance(z, int): n = z*z
    else: n = z.norm()

    n_factors = prime_factors(n)
    
    possible_factors = []
    for index in range(len(n_factors)):
        i = n_factors[index]
        f = (complex(sum_of_two_squares(i)), complex(sum_of_two_squares(i)).conjugate())
        #remove the extra copy of the factors in class 3 (mod 4)
        if not (index%2==1 and i%4==3): possible_factors.append(f)
    
    z_factors = []
    i = 0
    #find the correct one in each pair
    for conjugate_pair in possible_factors:
        if z % conjugate_pair[0] == 0:
            z_factors.append(conjugate_pair[0])
            z = z / conjugate_pair[0]
        else:
            z_factors.append(complex(0, 1)*conjugate_pair[1])
            z = z / conjugate_pair[1]
            z = z * complex(0, -1)
        i = i + 1
    
    #turn z into a gaussian integer and then add it to the factors list
    z_factors.insert(0, complex(round(z.real), round(z.imaginary)))

    print(z_factors)
    return z_factors
