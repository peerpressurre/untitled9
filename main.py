#ex1(1)
def capital():
    try:
        text = (input('text->'))
        words = text.split()
        for word in words:
            if text.count(word)>0:
                orig = text
                bom = text[0].upper() + text[1:]
                text = text.replace(orig, bom)

        print(text)

    except Exception as ex:
        print(f'Error: {ex}')
capital()
#ex1(2)
def digits():
    try:
        text = (input('text->'))
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        counter = []
        for i in text:
            if i.isdigit():
                counter.append(i)

        print(len(counter))

    except Exception as ex:
        print(f'Error: {ex}')
digits()




#ex1(3)
def symbols():
    try:
        text = (input('text->'))
        counter = text.count('!') + text.count('?') + text.count('.') + text.count(':') + text.count(';') + text.count(',')
        print(counter)

    except Exception as ex:
        print(f'Error: {ex}')


symbols()



#ex1(4)
def uno():
    try:
        text = (input('text->'))
        counter = text.count('!')
        print(counter)


         #counter += 1
    except Exception as ex:
        print(f'Error: {ex}')


uno()