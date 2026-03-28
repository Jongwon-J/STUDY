# Add more operations to Rational
import math

class Rational:
    def __init__(self, p, q=1):
    
        if q == 0:
            raise ValueError('Denominator must not be zero')
        # isinstance : 이 객체가 내가 생각한 그 타입이 맞나? // 정수인지 아닌지 Test
        if not isinstance(p, int): 
            raise TypeError('Numerator must be an integer')
        if not isinstance(q, int):
            raise TypeError('Denominator must be an integer')
        
        g = math.gcd(p, q)
        
        self.p = p // g
        self.q = q // g
    
    # method to convert rational to float
    def __float__(self):
        return float(self.p) / float(self.q)    
    
    # method to convert rational to string for printing
    def __str__(self):
        return '%d / %d' % (self.p, self.q)
    
    # method to add two rationals - interprets self + other
    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.p * other.q + other.p * self.q, self.q * other.q)
        # -- if it's an integer...
        elif isinstance(other, int):
            return Rational(self.p + other * self.q, self.q)
        # -- otherwise, we assume it will be a float
        return float(self) + float(other)
    
    def __radd__(self, other): # interprets other + self
        return self + other # addition commutes!
    
    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.p * other.q - other.p * self.q, self.q * other.q)
        elif isinstance(other, int):
            return Rational(self.p - self.q * other, self.q)
        else:
            raise NotImplementedError('Subtraction not implemented yet')
        
    def __mul__(self, other):
        # -- if it's a rational...
        if isinstance(other, Rational):
            return Rational(self.p * other.p, self.q * other.q)
        # -- if it's an integer...
        elif isinstance(other, int):
            return Rational(self.p * other, self.q)
        else:
            raise NotImplementedError('Multiplcation not implemented yet')
    
    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.p * other.q, self.q * other.p)
        elif isinstance(other, int):
            return Rational(self.p, self.q * other)
        else:
            raise NotImplementedError('Subtraction not implemented yet')