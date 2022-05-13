#!/bin/usr/env python3


class Complex:

    def __init__(self, re=0, im=0):
        self.re = float(re)
        self.im = float(im)

    def __repr__(self):
        return '(' + str(self.re) + ' + ' + str(self.im) + 'i)'

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        add_re = self.re + other.re
        add_im = self.im + other.im
        return Complex(add_re, add_im)

    def __sub__(self, other):
        subtract_re = self.re - other.re
        subtract_im = self.im - other.im
        return Complex(subtract_re, subtract_im)

    def __mul__(self, other):
        return Complex(self.re*other.re - self.im*other.im, self.im*other.re + self.re*other.im)

    def __truediv__(self, other):
        selfr, selfi, otherr, otheri = self.re, self.im, \
                         other.re, other.im  # short forms
        r = float(otherr ** 2 + otheri ** 2)
        return Complex((selfr * otherr + selfi * otheri) / r, (selfi * otherr - selfr * otheri) / r)

    def __neg__(self):
        return Complex(-1*self.re, -1*self.im)

    def __invert__(self):
        return Complex(self.re, -1*self.im)


if __name__ == '__main__':

    a = Complex(4, 3)
    b = Complex(2, -3)
    c = Complex(1)
    print(a + c)
    print(-a)
    print(~a)
