# RSA Algorithm
**RSA** is an algorithm used by modern computers to encrypt and decrypt messages. It is an **asymmetric cryptographic algorithm**. Asymmetric means that there are **two different keys**. This is also called public key cryptography, because one of the keys can be given to anyone. The other key must be kept private. The algorithm is based on the fact that finding the factors of a large composite number is difficult: when the integers are prime numbers, the problem is called prime factorization. It is also a key pair (\ public and private key\ ) generator.
## Operation
---
RSA involves a public key and private key. The public key can be known to everyone; it is used to encrypt messages. Messages encrypted using the public key can only be decrypted with the private key. The keys for the RSA algorithm are generated the following way:
1. Choose two different large random prime numbers
1. Calculate: **$n = pq$**
    * **$n$** is the modulus for the public key and the private keys
1. Calculate the totient: **$\phi (\ n\ ) = (\ p\ - \ 1\ )(\  q\  -\  1\ )$** .
1. Choose an integer **$e$** such that **$1 < e < \phi (\ n\ )$** and **$e$** is co-prime to **$\phi (\ n\ )$ ie: $e$** and **$\phi (\ n\ )$** share no factors other than 1; **$gcd (\ e, \phi (\ n\ )\ ) = 1$** .
    * **$e$** is released as the public key exponent
1. Compute **$d$** to satisfy the congruence relation **$de \equiv 1 (\ mod\ (\ \phi (\ n\ )\ )$ ie: $de = 1 + k\phi(\ n\ )$** for some integer **$k$** . (Simply to say : Calculate **$d = (\ 1\ +\ k\phi(\ n\ )\ )e$** )
    * **$d$** is kept as the private key exponent

The **public key** is made of the modulus $n$ and the public (\ or encryption\ ) exponent **$e$** .
The **private key** is made of the modulus $n$ and the private (\ or decryption\ ) exponent **$d$** which must be kept secret.

## Encrypting Message
---
Alice gives her public key **$(\ n$** & **$e\ )$** to Bob and keeps her private key secret. Bob wants to send message **M** to Alice.

First he turns **M** into a number **$m$** smaller than **$n$** by using an agreed-upon reversible protocol known as a padding scheme. He then computes the ciphertext corresponding to:
$$
    c = m^e \ \ mod\ \ \ n
$$
This can be done quickly using the method of exponentiation by squaring. Bob then sends **$c$** to Alice.

## Decrypting Message
---
Alice can recover **$m$** from **$c$** by using her private key **$d$** in the following procedure:
$$
    m = c^d\ \ mod\ \ \ n
$$
Given **$m$**, she can recover the original distinct prime numbers, applying the Chinese remainder theorem to these two congruences yields
$$
    m^ed \equiv \ m\ \ mod\ \ pq
$$
Thus,
$$
    c^d \equiv \ m\ \ mod\ \ n
$$
## A Working Example
---
1. Choose two random prime numbers.
2. **$p = 61$** and **$q = 53$** Compute **$n$ = $pq$**
3. **$n=61*53=3233$**
4. Compute the totient **$\phi (\ n\ ) = (\ p\ - \ 1\ )(\  q\  -\  1\ )$**
5. **$\phi (n)=(61-1)(53-1)=3120$**
6. Choose **$e>1$** coprime to **$3120$**
7. **$e = 17$**
8. Choose **$d$** to satisfy **$de \equiv 1\ \  mod \ \ \phi(n)$**
9. **$d=2753$**
10. **$17*2753=46801=1+15*3120$**

The **public key** is **$(n=3233, e=17)$**. For a padded message **$m$** the encryption function **$c=m^e\  mod\ \  n$** becomes: $c=m^{17}\ \ mod\ \ 3233$

The **private key** is **$(n=3233, d=2753)$**. The decryption function **$m=c^d\ \ mod\ \ n$** becomes: $m=c^{2753}\ \ mod\ \  3233$

For example, to encrypt **$m=123$**, we calculate

**$c=123^{17}\ \ mod\ \ 3233=855$** 

To decrypt **$c=855$**, we calculate

**$m=855^{2753}\ \ mod\ \ 3233=123$**

##### Source : [wikipedia](https://simple.wikipedia.org/wiki/RSA_algorithm)