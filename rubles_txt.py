def out(number):
    num = str(number)
    result = list(num)
    len_check = len(result)
    output = []
    if len(result) > 6:
        print('Слишком большое число')
    while len(result) < 6:
        zero = ['0']
        result = zero + result    
    if result[0] != '0':
        if result[0] == '9': b0 = 'девятьсот'
        if result[0] == '8': b0 = 'восемьсот'
        if result[0] == '7': b0 = 'семьсот'
        if result[0] == '6': b0 = 'шестьсот'
        if result[0] == '5': b0 = 'пятьсот'
        if result[0] == '4': b0 = 'четыреста'
        if result[0] == '3': b0 = 'триста'
        if result[0] == '2': b0 = 'двести'
        if result[0] == '1': b0 = 'сто'
        output.append(b0)
    if result[1] != '0':
        if result[1] == '9': b1 = 'девяносто'
        if result[1] == '8': b1 = 'восемьдесят'
        if result[1] == '7': b1 = 'семьдесят'
        if result[1] == '6': b1 = 'шестьдесят'
        if result[1] == '5': b1 = 'пятьдесят'
        if result[1] == '4': b1 = 'сорок'
        if result[1] == '3': b1 = 'тридцать'
        if result[1] == '2': b1 = 'двадцать'
        if result[1] == '1':
            if result[2] == '9': b1 = 'девятнадцать'
            if result[2] == '8': b1 = 'восемнадцать'
            if result[2] == '7': b1 = 'семнадцать'
            if result[2] == '6': b1 = 'шестнадцать'
            if result[2] == '5': b1 = 'пятнадцать'
            if result[2] == '4': b1 = 'четырнадцать'
            if result[2] == '3': b1 = 'тринадцать'
            if result[2] == '2': b1 = 'двенадцать'
            if result[2] == '1': b1 = 'одиннадцать'
            if result[2] == '0': b1 = 'десять'
        output.append(b1)
    if result[2] != '0':
        if result[1] != '1':
            if result[2] == '9': b2 = 'девять'
            if result[2] == '8': b2 = 'восемь'
            if result[2] == '7': b2 = 'семь'
            if result[2] == '6': b2 = 'шесть'
            if result[2] == '5': b2 = 'пять'
            if result[2] == '4': b2 = 'четыре'
            if result[2] == '3': b2 = 'три'
            if result[2] == '2': b2 = 'две'
            if result[2] == '1': b2 = 'одна'
            output.append(b2)
    if len_check > 3:
        output.append('тысяч')
    if result[2] != '0':
        if result[1] != '1':
            if result[2] == '4':
                output.pop()
                output.append('тысячи') 
            if result[2] == '3':
                output.pop()
                output.append('тысячи')
            if result[2] == '2':
                output.pop()
                output.append('тысячи')
            if result[2] == '1':
                output.pop()
                output.append('тысяча')
    if result[3] != '0':
        if result[3] == '9': b3 = 'девятьсот'
        if result[3] == '8': b3 = 'восемьсот'
        if result[3] == '7': b3 = 'семьсот'
        if result[3] == '6': b3 = 'шестьсот'
        if result[3] == '5': b3 = 'пятьсот'
        if result[3] == '4': b3 = 'четыреста'
        if result[3] == '3': b3 = 'триста'
        if result[3] == '2': b3 = 'двести'
        if result[3] == '1': b3 = 'сто'
        output.append(b3)
    if result[4] != '0':
        if result[4] == '9': b4 = 'девяносто'
        if result[4] == '8': b4 = 'восемьдесят'
        if result[4] == '7': b4 = 'семьдесят'
        if result[4] == '6': b4 = 'шестьдесят'
        if result[4] == '5': b4 = 'пятьдесят'
        if result[4] == '4': b4 = 'сорок'
        if result[4] == '3': b4 = 'тридцать'
        if result[4] == '2': b4 = 'двадцать'
        if result[4] == '1':
            if result[5] == '9': b4 = 'девятнадцать'
            if result[5] == '8': b4 = 'восемнадцать'
            if result[5] == '7': b4 = 'семнадцать'
            if result[5] == '6': b4 = 'шестнадцать'
            if result[5] == '5': b4 = 'пятнадцать'
            if result[5] == '4': b4 = 'четырнадцать'
            if result[5] == '3': b4 = 'тринадцать'
            if result[5] == '2': b4 = 'двенадцать'
            if result[5] == '1': b4 = 'одиннадцать'
            if result[5] == '0': b4 = 'десять'
        output.append(b4)
    if result[5] != '0':
        if result[4] != '1':
            if result[5] == '9': b5 = 'девять'
            if result[5] == '8': b5 = 'восемь'
            if result[5] == '7': b5 = 'семь'
            if result[5] == '6': b5 = 'шесть'
            if result[5] == '5': b5 = 'пять'
            if result[5] == '4': b5 = 'четыре'
            if result[5] == '3': b5 = 'три'
            if result[5] == '2': b5 = 'два'
            if result[5] == '1': b5 = 'один'
            output.append(b5)
    output.append('рублей')
    if result[5] != '0':
        if result[4] != '1':
            if result[5] == '4':
                output.pop()
                output.append('рубля') 
            if result[5] == '3':
                output.pop()
                output.append('рубля')
            if result[5] == '2':
                output.pop()
                output.append('рубля')
            if result[5] == '1':
                output.pop()
                output.append('рубль')
    print(str.capitalize(' '.join(output)))