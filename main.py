def pali():
    try:
        text = (input('text->'))
        num = (input('num->'))
        counter = []
        for i in text:
            if i.count(num):
                counter.append(i)

        print(len(counter))

    except Exception as ex:
        print(f'Error: {ex}')
pali()