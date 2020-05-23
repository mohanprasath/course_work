#!/usr/bin/env python3
import fractions

class Rational(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        numerator = (self.denominator * other.numerator) + (other.denominator * self.numerator)
        denominator = other.denominator * self.denominator
        gcd = fractions.gcd(numerator, denominator)
        return Rational(int(numerator/gcd), int(denominator/gcd))

    def __sub__(self, other):
        numerator = (other.denominator * self.numerator) - (self.denominator * other.numerator) 
        denominator = other.denominator * self.denominator
        gcd = fractions.gcd(numerator, denominator)
        return Rational(int(numerator/gcd), int(denominator/gcd))

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = other.denominator * self.denominator
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = other.numerator * self.denominator
        return Rational(numerator, denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator  
            
    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator) 
        
    def __gt__(self, other):
        return float(self.numerator)/self.denominator > float(other.numerator)/other.denominator
     
    def __lt__(self, other):
        return float(self.numerator)/self.denominator < float(other.numerator)/other.denominator

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
