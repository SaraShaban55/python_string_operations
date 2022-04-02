#


def prom_1(x, y, n):
    try:

        index = x.find(y)
        if index == 0 and n == 1:
            return(0)
        if index == -1:
            return(-1)

        while n > 1 and index != -1 or index == 0:
            index = x.find(y, index+len(y))
            x.replace(x[index], '*')
            n = n-1
        return(index)
    except AttributeError:
        print('there is an AttributeError,so please enter a string in the next time')


prom_1('sara shaban sara shaban', 'sara', 2)


def prom_2(first, second):
    if first == second:
        return (True)

    if len(first)-1 <= len(second):
        if '*' not in (first):
            return (False)
        else:
            return(True)
    else:
        return (False)


prom_2('*s', 's')


def prom_3(word_1):
    try:
        word_1 = word_1.lower()
        word_1 = word_1.replace(' ', '')
        word_2 = list(word_1)
        word_2.reverse()
        word_3 = ''.join(word_2)
        if word_1 == word_3:
            return(True)
        else:
            return(False)

    except AttributeError:
        print('there is an AttributeError,so please enter a string')


prom_3(123)


def bouns(word):
    sub = ''
    length_word = len(word)

    for i in range(length_word//2):
        if word[i] in sub:
            continue
        sub = sub+word[i]
        if length_word % len(sub) == 0:
            if sub*(length_word//len(sub)) == word:
                x = length_word//len(sub)
                print(sub, x)

    else:
        print(word, '1')


bouns('abababee')
