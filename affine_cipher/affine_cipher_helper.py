import math

class AffineCipher:
    def __init__(self, alphabet, a, b):
        self.alphabet = alphabet
        self.a = a
        self.b = b
        self.m = len(self.alphabet)
        if math.gcd(self.a, self.m) != 1:
            raise ValueError('first key must be coprime with {}'.format(self.m))
        if self.b < 0:
            raise ValueError('second key must be non-negative')


    def encode(self, contents):
        output = ""
        for letter in contents:
            index = (self.a * self.alphabet.find(letter) + self.b) % self.m
            output += self.alphabet[index]
        return output

    def decode(self, contents):
        output = ""
        a_mmi = math.gcd(self.a, self.b)
        for letter in contents:
            index = (modInverse(self.a, self.m) * (self.alphabet.find(letter) - self.b)) % self.m
            output += self.alphabet[index]
        return output

def modInverse(a, m):
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return None

# Usage example

abc = "abcdefghijklmnopqrstuvwxyz"
c = AffineCipher(abc, 5, 8)
print(c.encode('affinecipher'))
print(c.decode('ihhwvcswfrcp'))
