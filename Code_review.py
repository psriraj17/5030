
def turkish(str):
    lower_map = {
        ord(u'I'): u'ı',
        ord(u'İ'): u'i',
        }
    lower_str = str.translate(lower_map)
    print(lower_str.lower())

def irish(str):
    vowels= ['A','E','I','O','U','Á','É','Í','Ó','Ú']
    for i in range(len(vowels)):
        if  str[1] == vowels[i]  and str[0] == str[0].lower():
            str = str.replace(str[1], "-"+str[1])
            print(str.lower())
    else:
        print(str.lower())

def Greek(word):
    #ΠΣhΣgfΣdsΌΛΗΣΣΣΣ
        leng = len(word) - 1
        for i in range(leng):
            if (word[i] == "Σ"):
                I = u"\u03C3"
                print(I, end='')
            else:
                print(word[i].lower(), end='')
        if (word[-1] == "Σ"):
            I = u"\u03C2"
            print(I, end='')

if __name__ == '__main__':

 lang = input("Enter your language (insert either symbol or language name):  ")
 str  = input("Enter your String:  " )
 if lang== "Turkish" or lang== "turkish" or lang== "tr":
    turkish(str)
 if lang== "Irish" or lang== "ga" or lang== "irish":
     irish(str)
 if lang== "Greek" or lang== "el" or lang== "greek":
     Greek(str)
else:
     print(str.lower())