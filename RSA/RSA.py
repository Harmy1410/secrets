import random

class RSA:
    def __init__(self):
        # Taking the plain text and getting their ascii value 
        self.plain_text = [ord(x) for x in input("Enter the text to be encrypted: ")]

        #Taking two primes as inputs.
        self.p, self.q = int(input("Enter a prime number(p): ")), int(input("Enter a prime number(q): "))

        # Computing n = p * q
        self.n = self.p * self.q
        # print("n         :", self.n)

        # Computing phi_n = (p - 1) * (q - 1)
        self.phi_n = (self.p - 1) * (self.q - 1)
        # print("phi_n     :", self.phi_n)
                
        # Getting the vlaue of e 
        self.e = self.get_e(self.phi_n)
        # print("e         :",self.e)

        # Getting the value of d
        self.d = self.get_d(self.n, self.phi_n)
        # print("d         :", self.d)

        # Encrypted text
        self.encrypted_text = []
        for i in self.plain_text:
            self.encrypted_text.append(self.encrypt(i, self.e, self.n))
        self.encrypted_text = ''.join(chr(x) for x in self.encrypted_text)
        # print(self.encrypted_text)

    # Function for GCD
    # Euclid's GCD func:
    # def gcd(self, a, b):
    #   while a != b:
    #       if a > b:
    #           a = a - b
    #       else:
    #           b = b - a
    #   return a
    
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    # Function for computing value of e
    def get_e(self, x):
        prime = []
        for i in range(2, x):
            if self.gcd(i, x):
                prime.append(i)
        return random.choice(prime)

    # Function for computing value of d
    def get_d(self, n, phi):
        for i in range(1, n):
            if ((self.e * i) % phi) == 1:
                return i

    # Encrypts the plain text
    def encrypt(self, pt, e, n):
        ct = (pt ** e) % n
        return ct

    # Decrypts the plain text
    def decrypt(self, ct, d, n):
        pt = [ord(x) for x in self.encrypted_text]
        for i in range(len(pt)):
            pt[i] = (pt[i] ** d) % n
        pt = ''.join(chr(x) for x in pt)
        return pt

# Testing
if __name__ == "__main__":
    p = RSA()
    print("ct        :", p.encrypted_text)
    print("pt        :", p.decrypt(p.encrypted_text, p.d, p.n))

    
