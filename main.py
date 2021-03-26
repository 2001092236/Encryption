from cipher import *
from math import sqrt
from copy import copy


def test_message():
    m = Message("My Message", False, a=5)
    print(m)


def test_Encryptor():
    e = CaesarEncryptor(3)
    m = Message("You are the best!!!")
    e.fit(m)


def test_Caesar():
    message = Message("1989\nOver hill, over dale,\n\
Thorough bush, thorough brier,\n\
Over park, over pale,\n\
Thorough flood, thorough fire!\n\
I do wander everywhere,\n\
Swifter than the moon's sphere;\n\
And I serve the Fairy Queen,\n\
To dew her orbs upon the green;\n\
The cowslips tall her pensioners be;\n\
In their gold coats spots you see")
    enc = CaesarEncryptor(7)
    enc.fit(message)
    shifred = enc.encrypt()
    print(shifred)
    enc.fit(shifred)
    shifred = enc.encrypt()
    print(shifred)
    decr = CaesarDecryptor(14)
    decr.fit(shifred)
    unshifred = decr.decrypt()
    print(unshifred)

    if unshifred.text != message.text:
        raise TypeError



def test_Caesar_krack():
    message = Message("1989\nOver hill, over dale,\n\
Thorough bush, thorough brier,\n\
Over park, over pale,\n\
Thorough flood, thorough fire!\n\
I do wander everywhere,\n\
Swifter than the moon's sphere;\n\
And I serve the Fairy Queen,\n\
To dew her orbs upon the green;\n\
The cowslips tall her pensioners be;\n\
In their gold coats spots you see")
    enc = CaesarEncryptor(7)
    enc.fit(message)

    shifred = enc.encrypt()

    unshif = CaesarDecryptor.decryptWithoutKey(shifred)
    if unshif.text != message.text:
        raise Exception("Wrong decrypt!")
    #print(unshif)

def test_Caesar_krack1():

    mess = Message("What does family mean to you? In a perfect world, all families should be happy and everyone should get on well together. I know a lot of families that have many problems. Brothers and sisters who don’t like each other, parents who never talk to each other. I wonder why this is. How can you live so close to your family members and feel apart from them? There is a lot of talk in the news about the breakdown of family life. Divorce is rising everywhere in the world. This means single parents have less time to spend with their children, which creates problems. Maybe the stress of modern life puts too much pressure on families. It seems as though family life was better a generation or two ago. Is this true for families in your country?")
    enc = CaesarEncryptor(14)
    enc.fit(mess)

    shifred = enc.encrypt()
    #print('shifred:\n{}'.format(shifred))
    #print()
    unshif = CaesarDecryptor.decryptWithoutKey(shifred)
    if unshif.text != mess.text:
        raise Exception("Wrong decrypt!")
    #print(unshif)

'''
test_Caesar()
test_message()
test_Encryptor()
test_Caesar_krack()
test_Caesar_krack1()'''

'''
freq = dict(a=8.2, b=1.5, c=2.8, d=4.3, e=13, f=2.2, g=2.0, h=6.1, i=7.0, j=0.15, k=0.77, l=4.0, m=2.4, n=6.7,
            o=7.5, p=1.9, q=0.095, r=6.0, s=6.3, t=9.1, u=2.8, v=0.98, w=2.4, x=0.15, y=2.0, z=0.074)

freq = [8.2, 1.5, 2.8, 4.3, 13, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8,
        0.98, 2.4, 0.15, 2.0, 0.074]


def normalize(lst):
    freq = copy(lst)
    mean = sum(freq) / len(freq)
    std = sqrt(sum([(x - mean) ** 2 for x in freq]) / len(freq))
    freq = [(x - mean) / std for x in freq]
    return freq


print(normalize(freq))

print('AAA'.lower())
'''