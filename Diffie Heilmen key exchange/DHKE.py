class KeyExchange:

    def __init__(self, q, private_key):
        self.q, self.x = q, private_key

    def getAlpha(self):

        alphas = []
        for i in range(1, self.q):
            vals = [(i**x % self.q) for x in range(1, self.q)]
            for j in range(1, self.q):
                if vals.count(j) > 1:
                    break
            else:
                alphas.append(i)

        alphas.sort()
        return alphas[len(alphas) - 2]


    def getPublicKey(self):
        return (self.getAlpha() ** self.x) % self.q

    def key(self, ry):
        return (ry ** self.x) % self.q


# ----- TEST -----

q, jpr, bpr = 907, 507, 467
john = KeyExchange(q, jpr)
jpu = john.getPublicKey()

bill = KeyExchange(q, bpr)
bpu = bill.getPublicKey()

print(john.key(bpu), bill.key(jpu))
