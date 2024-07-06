import re
# re.sub(pattern, repl, string)

str1 = re.sub('[346]', 'x', '03-5454-68284')
print(str1)

str1 = re.sub('[.,:;!?]', '', "He has three pets: a cat, a dog and a giraffe, doesn't he?")
print(str1)

str1 = re.sub('\(a\)|あっとまーく|＠', '@', 'accountname＠test.ecc.u-tokyo.ac.jp')
print(str1)

str1 = re.sub(r'[ \t\n][ \t\n]*', ' ', 'Hello,\n    World!\tHow are you?')
print(str1)
