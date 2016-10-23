'''Uses a dictionary to store the search keywords for GBF raids. User will select the raid of interest for the Streaming API.'''

## Magnas
#Tiamat = u"Lv50 ティアマト・マグナ"
#Colo = u"Lv70 コロッサス・マグナ"
#Leviathan = u"Lv60 リヴァイアサン・マグナ"
#Yggdrasil = u"Lv60 ユグドラシル・マグナ"
#Luminiera/Chev = u"Lv75 シュヴァリエ・マグナ"
#Celeste = u"Lv75 セレスト・マグナ"

## Qilin
#Qilin = u"Lv100 黒麒麟"

## Primals (non-HL)
#Apollo = u"Lv100 アポロン"
#Twin Elements = u"Lv100 フラム＝グラス"
#Nezha = u"Lv100 ナタク"
#Medusa = u"Lv100 メドゥーサ"
#D. Angel Olivia = u"Lv100 Dエンジェル・オリヴィエ"
#Macula Marius= u"Lv100 マキュラ・マリウス"

options = {"1": ("Tiamat", u"Lv50 ティアマト・マグナ"), "2": ("Colo", u"Lv70 コロッサス・マグナ"), "3": ("Leviathan", u"Lv60 リヴァイアサン・マグナ"), "4": ("Yggdrasil", u"Lv60 ユグドラシル・マグナ"),
           "5": ("Luminiera", u"Lv75 シュヴァリエ・マグナ"),"6": ("Celeste", u"Lv75 セレスト・マグナ"), "7": ("Qilin", u"Lv100 黒麒麟"), "8": ("Apollo", u"Lv100 アポロン"),
           "9": ("Twin Elements", u"Lv100 フラム＝グラス"), "10": ("Nezha", u"Lv100 ナタク"), 
           "11": ("Medusa", "Lv100 メドゥーサ"), "12": ("D.Angel Olivia", u"Lv100 Dエンジェル・オリヴィエ"), "13": ("Macula Marius", u"Lv100 マキュラ・マリウス")}

def choose_a_raid(dic):
    print("{:<14} {:>14} \n".format("\033[4m" + 'Number' + '\033[0m', '\033[4m' + 'Raid'))    
    options_int = {int(key) : value for key, value in dic.items()}
    for key, value in options_int.items():
        the_name, the_value = value 
        print("{:<12} {:<1}".format(key, the_name))
    print('\033[0m' +'\nChoose a raid by its corresponding number\n' + '\033[0m')
    
    while True:   
        choice = str(input('>> '))
        if choice in options.keys():
            search = options[choice][1]
            return search
        else:
            print('Not valid. Try again by entering the raid\'s corresponding number.')
