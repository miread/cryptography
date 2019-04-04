# Affine Cipher - Python Helper Class

The Affine Cipher is a monoalphabetic cipher that is slightly stronger than a
Caesar Cipher. Given the modern alphabet, the Caesar Cipher has 26 possible
keys, while the Affine Cipher has 312 possible keys. The Affine Cipher maps to
the Caesar Cipher when a = 1, and the Atbash Cipher when a = b = m - 1.

There are four factors that go into the cipher:
```
x, the position in the alphabet of the current letter
a, a number that must be coprime with the length of the alphabet
(i.e. gcd(a, m) = 1)
b, an non-negative integer
m, the length of the alphabet
```
The formula (a * x + b) % m evaluates to the position of the letter in the
alphabet to substitute.
