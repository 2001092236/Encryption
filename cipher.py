from enum import Enum
from math import sqrt
from copy import copy


class CipherSuite(Enum):
    Caesar = "Caesar"


class Message:
    def __init__(self, text="", encrypted=False, **params):
        self.text = text
        self.encrypted = encrypted
        self.params = params

    def __str__(self):
        ans = ""
        if self.encrypted:
            ans += "The message is encrypted by {}\n".format(self.params['TypeEncoder'])
            ans += "Encryptor params: {}\n".format(self.params)
        else:
            ans += "True message is: \n"
        ans += self.text
        ans += '\n'
        return ans


class Encryptor:
    def __init__(self):
        self.message = Message()

    def fit(self, mess):
        self.message = mess

    def encrypt(self) -> Message:  ###will be write in the sons
        pass

class Decryptor:
    def __init__(self):
        self.message = Message()

    def fit(self, mess):
        self.message = mess

    def decrypt(self) -> Message:  ###will be write in the sons
        pass



class CaesarEncryptor(Encryptor):
    def nxt(ch, cnt=1):
        num = ord(ch)
        if ord('A') <= num <= ord('Z'):
            L = ord('A')
            R = ord('Z')
        if ord('a') <= num <= ord('z'):
            L = ord('a')
            R = ord('z')

        num_in_alf = num - L + cnt
        num_in_alf %= (R - L + 1)
        return chr(num_in_alf + L)

    def __init__(self, shift=3):
        super(CaesarEncryptor, self).__init__()
        self.shift = shift

    def fit(self, mess):
        super().fit(mess)
        # self.message.params['TypeEncoder'] = CipherSuite.Caesar
        # self.message.params['Shift'] = self.shift

    def encrypt(self) -> Message:
        text = []
        for i in self.message.text:
            if i.isalpha():
                # print("i = {}, nxt(i) = {}".format(i, CaesarEncryptor.nxt(i, self.shift)))
                text.append(CaesarEncryptor.nxt(i, self.shift))
            else:
                text.append(i)
        text = ''.join(text)
        return Message(text, True, Shift=self.shift, TypeEncoder=CipherSuite.Caesar)


class CaesarDecryptor(Decryptor):
    freq_lst_norm = [1.3307608641458593, -0.7247142826803677, -0.3258907467290103, 0.13429025629178679,
                     2.8033400738124103, \
                     -0.5099631479373291, -0.5713206150067688, 0.6865074599167432, 0.9626160617292217,
                     -1.1388771853990851, \
                     -0.9486690374838224, 0.042254055687627405, -0.44860568086788954, 0.8705798611250622,
                     1.1160097294028206, \
                     -0.6019993485414886, -1.155750488843181, 0.6558287263820235, 0.7478649269861829,
                     1.6068694659583376, \
                     -0.3258907467290103, -0.8842436970609108, -0.44860568086788954, \
                     -1.1388771853990851, -0.5713206150067688, -1.1621930228854722]

    def normalize(lst):
        freq = copy(lst)
        mean = sum(freq) / len(freq)
        std = sqrt(sum([(x - mean) ** 2 for x in freq]) / len(freq))
        freq = [(x - mean) / std for x in freq]
        return freq

    def distance(lst):
        ans = 0.0
        for i in range(26):
            ans += (lst[i] - CaesarDecryptor.freq_lst_norm[i]) ** 2
        return ans

    def __init__(self, shift):
        super(CaesarDecryptor, self).__init__()
        self.shift = shift


    def fit(self, mess):
        self.message = mess
        # self.message.params['TypeEncoder'] = CipherSuite.Caesar
        # self.message.params['Shift'] = self.shift

    def decrypt(self) -> Message:
        text = []
        for i in self.message.text:
            if i.isalpha():
                text.append(CaesarEncryptor.nxt(i, -self.shift))
            else:
                text.append(i)
        text = ''.join(text)
        return Message(text, False)

    def decryptWithoutKey(message):
        text = message.text.lower()
        distances = []
        for sh in range(26):
            enc = CaesarEncryptor(sh)
            enc.fit(Message(text))
            re = enc.encrypt()
            stat = []
            for ch in range(26):
                stat.append(re.text.count(chr(ch + ord('a'))))
            stat = CaesarDecryptor.normalize(stat)
            distances.append((CaesarDecryptor.distance(stat), sh))
        distances.sort()

        targetShift = 26 - distances[0][1]
        #print('shift = {}'.format(targetShift))
        decr = CaesarDecryptor(targetShift)
        decr.fit(message)
        return decr.decrypt()

#class Vigener