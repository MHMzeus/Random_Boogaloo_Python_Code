from random import randint
def _S_(Rolling):
    for Die in range(1,5):
        Rolling.append(randint(1,6))
        if Die == 4:
            Rolling.remove(min(Rolling))
            return Rolling
Rolling = []
STR = '0'
DEX = '1'
CON = '2'
INT = '3'
WIS = '4'
CHA = '5'
stats = [STR, DEX, CON, INT, WIS, CHA]
for gen in range(1, 7):
    _S_(Rolling)
    print(Rolling, sum(Rolling))
    print("Characteristic: \nSTR(0) \nDEX(1) \nCON(2) \nINT(3) \nWIS(4) \nCHA(5)")
    _T_ = int(input('Which stat number? \nNumber: '))
    for _T_ in stats[_T_]:
        stats[int(_T_)] = sum(Rolling)
    Rolling = []
    print(stats)

File = open('numbers.txt', encoding='UTF-8')
for line in File:
    print(line)
File.close()
