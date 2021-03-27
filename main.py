from cipher import *
from math import sqrt
from copy import copy
import argparse

messages = ["1989\nOver hill, over dale,\n\
Thorough bush, thorough brier,\n\
Over park, over pale,\n\
Thorough flood, thorough fire!\n\
I do wander everywhere,\n\
Swifter than the moon's sphere;\n\
And I serve the Fairy Queen,\n\
To dew her orbs upon the green;\n\
The cowslips tall her pensioners be;\n\
In their gold coats spots you see",
            "What does family mean to you? In a perfect world, all families should be happy and everyone should get on well together. I know a lot of families that have many problems. Brothers and sisters who don’t like each other, parents who never talk to each other. I wonder why this is. How can you live so close to your family members and feel apart from them? There is a lot of talk in the news about the breakdown of family life. Divorce is rising everywhere in the world. This means single parents have less time to spend with their children, which creates problems. Maybe the stress of modern life puts too much pressure on families. It seems as though family life was better a generation or two ago. Is this true for families in your country?", \
            ]


def test_message():
    m = Message("My Message", False, a=5)
    print(m)


def test_Encryptor():
    e = CaesarEncryptor(3)
    m = Message("You are the best!!!")
    e.fit(m)


def test_Caesar():
    message = Message(messages[0])
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
        raise Exception("Wrong decrypt! Caesar")


def test_Caesar_krack():
    message = Message(messages[0])
    enc = CaesarEncryptor(7)
    enc.fit(message)

    shifred = enc.encrypt()

    unshif = CaesarDecryptor.decryptWithoutKey(shifred)
    if unshif.text != message.text:
        raise Exception("Wrong decrypt! Caesar krack")
    # print(unshif)


def test_Caesar_krack1():
    mess = Message(messages[1])
    enc = CaesarEncryptor(14)
    enc.fit(mess)

    shifred = enc.encrypt()
    # print('shifred:\n{}'.format(shifred))
    # print()
    unshif = CaesarDecryptor.decryptWithoutKey(shifred)
    if unshif.text != mess.text:
        raise Exception("Wrong decrypt krack Caesar 1!")
    # print(unshif)


def test_Vigner():
    mess = Message("ATTACKATDAWN")
    enc = VigenerEncryptor("LEMON")
    enc.fit(mess)
    shifred = enc.encrypt()
    print(shifred)


def test_Vigner1():
    mess = Message(messages[0])
    enc = VigenerEncryptor("lEmON")
    enc.fit(mess)
    shifred = enc.encrypt()
    # print(shifred)

    dec = VigenerDecryptor("LeMon")
    dec.fit(shifred)
    unshifred = dec.decrypt()
    # print(unshifred)
    if unshifred.text != mess.text:
        raise Exception("Wrong decrypt Vigener!")


def test_Vernam():
    mess = Message("Ciper")
    enc = VernamEncryptor("lEmON")
    enc.fit(mess)
    shifred = enc.encrypt()
    print(shifred)
    dec = VernamDecryptor("LeMon")
    dec.fit(shifred)
    unshifred = dec.decrypt()
    print(unshifred)
    print(dec.message.text)
    if unshifred.text != mess.text:
        raise Exception("Wrong decrypt Vernam!")


from random import randint

def test_Vernam1():
    mess = Message(messages[0])
    keyw = [chr(ord('a') + randint(0, 25)) for i in mess.text if i.isalpha()]
    enc = VernamEncryptor(keyw)
    enc.fit(mess)
    shifred = enc.encrypt()
    #print(shifred)
    dec = VernamDecryptor(keyw)
    dec.fit(shifred)
    unshifred = dec.decrypt()
    #print(unshifred)
    if unshifred.text != mess.text:
        raise Exception("Wrong decrypt Vernam1!")


class StoreDictKeyPair(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        self._nargs = nargs
        super(StoreDictKeyPair, self).__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        my_dict = {}
        print
        "values: {}".format(values)
        for kv in values:
            k, v = kv.split("=")
            my_dict[k] = v
        setattr(namespace, self.dest, my_dict)

parcer = argparse.ArgumentParser(description='In')
parcer.add_argument('--mode', type=str)
parcer.add_argument('--path_from', type=str)
parcer.add_argument('--path_to', type=str)
parcer.add_argument('--typeCipher', type=str)
parcer.add_argument('--params', dest="my_dict", action=StoreDictKeyPair, nargs="+", metavar="KEY=VAL")

args = parcer.parse_args()

fin = open(args.path_from, 'r')
fout = open(args.path_to, 'w')

text = fin.read()

mess = Message(text)

if args.typeCipher == 'Caesar':
    enc = CaesarEncryptor(int(args.my_dict['shift']))
    dec = CaesarDecryptor(int(args.my_dict['shift']))

if args.typeCipher == 'Vigener':
    enc = VigenerEncryptor(args.my_dict['keyword'])
    dec = VigenerDecryptor(args.my_dict['keyword'])

if args.typeCipher == 'Vernam':
    enc = VernamEncryptor(args.my_dict['keyword'])
    dec = VernamDecryptor(args.my_dict['keyword'])

if args.mode == 'Enc':
    obj = enc

if args.mode == 'Dec':
    obj = dec

obj.fit(mess)

if args.mode == 'Enc':
    text = obj.encrypt()

if args.mode == 'Dec':
    text = obj.decrypt()

fout.write(text.text)

fin.close()
fout.close()
'''
parcer = argparse.ArgumentParser(description='In')
parcer.add_argument('first', type=str)
parcer.add_argument('second', type=str)
args = parcer.parse_args()
print("First: {}, Second: {}".format(args.first, args.second))

test_Caesar()
test_message()
test_Encryptor()
test_Caesar_krack()
test_Caesar_krack1()
test_Vigner1()
test_Vernam()
test_Vernam1()


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

t = [['a'] * 26 for i in range(26)]
t[0][1] = '6'
t[1][0] = '4'
for i in range(26):
    for j in range(26):
        t[i][j] = chr(ord('a') + (i + j) % 26)

for i in range(26):
    for j in range(26):
        print(t[i][j], end='')
    print()

for i in enumerate(range(1, 5, 2)):
    print(i)
'''
