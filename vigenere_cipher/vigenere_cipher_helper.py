class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.key_len = len(self.key)
        self.alphabet = alphabet
        self.alphabet_len = len(self.alphabet)

    def encode(self, text):
        output = ""
        count = 0
        for letter in text:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                index += self.alphabet.index(self.key[count])
                if index >= self.alphabet_len:
                    index -= self.alphabet_len
                output += self.alphabet[index]
                if count == self.key_len - 1:
                    count = 0
                else:
                    count += 1
            else:
                output += letter
                if count == self.key_len - 1:
                    count = 0
                else:
                    count += 1

        return output

    def decode(self, text):
        output = ""
        count = 0
        for letter in text:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                index -= self.alphabet.index(self.key[count])
                if index < 0:
                    index += self.alphabet_len
                output += self.alphabet[index]
                if count == self.key_len - 1:
                    count = 0
                else:
                    count += 1
            else:
                output += letter
                if count == self.key_len - 1:
                    count = 0
                else:
                    count += 1

        return output

# Usage sample
abc = "abcdefghijklmnopqrstuvwxyz"
key = "lemon"

cipher = VigenereCipher(key, abc)

print(cipher.encode("attackatdawn"))
print(cipher.decode("lxfopvefrnhr"))
