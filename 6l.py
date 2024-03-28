def stol():
    d={'Дания': 'Копенгаген',
       'Болгария': 'София',
       'Греция': 'Афины',
       'Япония': 'Токио',
       'Латвия': 'Рига'}
    for key, value in d.items():
        print(key, '-', value)
    c=input('Введите страну: ')
    print('Столица -', d.get(c))
    st=list(d)
    st.sort()
    for i in st:
        print(i, '-', d[i])
def Erudite():
    d={1:'АВЕИНОРСТ',
       2:'ДКЛМПУ',
       3:'БГЁЬЯ',
       4:'ЙЫ',
       5:'ЖЗХЦЧ',
       8:'ШЭЮ',
       10:'ФЩЪ'}
    m=list(d)
    slovo=input('Введите слово(используйте ТОЛЬКО ЗАГЛАВНЫЕ буквы!): ')
    res=0
    for i in range(len(slovo)):
        for j in m:
            if slovo[i] in d[j]:
                res=res+j
                break
    print('Стоимость слова', slovo, '=', res)
