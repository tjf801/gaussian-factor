from math import floor, ceil, sqrt

class complex():
    def __init__(self, *args):
        if len(args)==1:
            try: float(args[0][:-1]); isimag=True
            except: isimag = False
            if isinstance(args[0], (int, float)): #if it is just a classic int or float
                self.real = args[0]
                self.imaginary = 0
            elif isinstance(args[0], tuple): #if it is (a, b) make a+bi
                self.real = args[0][0]
                self.imaginary = args[0][1]
            elif isimag and args[0][-1] in "ij": #if it is an int or float with an i (e.g. 4.2i)
                self.real = 0
                self.imaginary = float(args[0][:-1]) if not args[0][:-1].isdigit() else int(args[0][:-1])
            elif isinstance(args[0], str): #if it is a string
                real, imaginary = args[0][0], ""
                I = False
                for i in range(1, len(args[0])):
                    char = args[0][i]
                    if char in "01234567890.":
                        if I: imaginary += char
                        else: real += char
                    elif char in "+-" and i!=0:
                        if char=='-': imaginary=char
                        I = True
                self.real = float(real) if '.' in real else int(real)
                self.imaginary = float(imaginary) if '.' in imaginary else int(imaginary)
        if len(args)==2: #If it gives the real and imaginary parts
            self.real = args[0]
            self.imaginary = args[1]
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.imaginary<0: return str(self.real) + '-' + str(abs(self.imaginary)) + 'i'
        return str(self.real) + '+' + str(self.imaginary) + 'i'
    
    def __int__(self):
        return int(self.real)
    
    def __float__(self):
        return float(self.real)
    
    def __complex__(self): #TODO this is so awkward
        pass



    def __eq__(self, other):
        if isinstance(other, (int, float)): return self.real==other and self.imaginary==0
        return self.real==other.real and self.imaginary==other.imaginary
    
    def __ne__(self, other):
        if isinstance(other, (int, float)): return self.real!=other or self.imaginary!=0
        return self.real!=other.real or self.imaginary!=other.imaginary

    def __neg__(self):
        return complex(-self.real, -self.imaginary)

    def conjugate(self):
        return complex(self.real, -self.imaginary)

    def __abs__(self):
        return sqrt(self.real*self.real + self.imaginary*self.imaginary)
    
    def norm(self):
        return self.real*self.real + self.imaginary*self.imaginary

    def __round__(self, n):
        return complex(round(self.real, n), round(self.imaginary, n))

    def __floor__(self):
        return complex(floor(self.real), floor(self.imaginary))

    def __ceil__(self):
        return complex(ceil(self.real), ceil(self.imaginary))
    
    def __hash__(self):
        return hash((self.real, self.imaginary))
    
    def __getitem__(self, key):
        if key==0 or 'r' in str(key): return self.real
        elif key==1 or 'i' in str(key): return self.imaginary
        else: raise KeyError('key \''+str(key)+'\' not valid for type \'complex\'')
    


    def __add__(self, other):
        if isinstance(other, (int, float)): return complex(self.real+other, self.imaginary)
        return complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)): return complex(self.real-other, self.imaginary)
        return complex(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other):
        # (a+bi) * (c+di) = (ac-bd) + (ad+bc)i
        if isinstance(other, (int, float)): return complex(other*self.real, other*self.imaginary)
        return complex((self.real*other.real)-(self.imaginary*other.imaginary), (self.real*other.imaginary)+(self.imaginary*other.real))
    
    def __floordiv__(self, other):
        q = self/other
        return complex((floor(q.real) if q.real>=0 else ceil(q.real)), (floor(q.imaginary) if q.imaginary>=0 else ceil(q.imaginary)))

    def __truediv__(self, other):
        # (a+bi) / (c+di) = ((ac+bd)/(c²+d²)) + ((bc-ad)/(c²+d²))i
        if isinstance(other, (int, float)): return complex(self.real/other, self.imaginary/other)
        return complex(
                (self.real*other.real + self.imaginary*other.imaginary)/(other.real*other.real + other.imaginary*other.imaginary),
                (self.imaginary*other.real - self.real*other.imaginary)/(other.real*other.real + other.imaginary*other.imaginary))
    
    def __mod__(self, other):
        # (a+bi) % (c+di) = (a+bi) - (c+di)((a+bi)//(c+di))
        return self - (other * (self//other))
    
    def __pow__(self, other, modulo=None):
        # fuck
        if modulo is None:
            if isinstance(other, int):
                temp = complex(self.real, self.imaginary)
                for i in range(other-1):
                    temp *= self
                return temp
            else: pass
    
    def __radd__(self, other):
        return self + other
    
    def __rsub__(self, other):
        if isinstance(other, (int, float)): return complex(other - self.real, -self.imaginary)
        return complex(other.real - self.real, other.imaginary - self.imaginary)

    def __rmul__(self, other):
        return self * other
    
    def __rfloordiv__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __rpow__(self, other, modulo=None):
        pass