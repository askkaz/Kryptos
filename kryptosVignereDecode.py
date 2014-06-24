__author__ = 'kaz'
#adamkaz@gmail.com
# These functions can be used to decrypt a passage of text, using the vigenere method from sections 1 & 2 of Kryptos


def containsdupes(word_in):
    dupe = False
    for char in word_in:
        if word_in.count(char) > 1:
            dupe = True
            break
    return dupe


def makedictionary(word_in):
    #returns a string that begins with word_in, followed by the remaining letters of the alphabet

    if containsdupes(word_in) or not word_in.isalpha():
        raise Exception('The top word cannot contain any duplicate characters or numbers')

    else:
        dictionary = word_in
        full_alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in full_alphabet:
            if char not in dictionary:
                dictionary += char
        return dictionary

def buildvigeneretable(dictionary, side_word):
    table = ['']*side_word.__len__()
    for k in range(side_word.__len__()):
        table[k]=dictionary[dictionary.find(side_word[k]):]+dictionary[:dictionary.find(side_word[k])]
    return table

def decodevigenere(top_word, side_word, encrypted_text):
    decrypted_text=''
    dictionary=makedictionary(top_word)
    table=buildvigeneretable(dictionary, side_word)
    side_word_len=side_word.__len__()
    side_index=0
    for i in range(0,encrypted_text.__len__()):
        if '?'==encrypted_text[i]:
            decrypted_text += '?'
        else:
            decrypted_text += dictionary[table[side_index].find(encrypted_text[i])]
            side_index += 1
            if side_index == side_word_len:
                side_index = 0

    return decrypted_text

print(decodevigenere('kryptos','palimpsest','EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD'.lower()))
print(decodevigenere('kryptos','abscissa','VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKK?DQMCPFQZDQMMIAGPFXHQRLG\
TIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVH?DWK\
BFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUM\
UNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGEWJLLAETG'.lower()))
