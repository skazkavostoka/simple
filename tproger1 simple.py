#На сайте tproger увидел список из 5 задач для джунов и мидлов, одна из них звучит следующим образом:
#Вам дана строка 's' с некоторым количеством слов N.
# Нужно сделать так, чтобы исходный порядок слов в строке изменился на обратный.
#При этом в исходной строке между словами может быть множество пробелов, но в результате работы скрипта
#мы должны получить предложение с одним пробелом между словами,
#без пробелов в начале предложения и после его конца.
#Время выполнения скрипта не должно превышать 1 секунду.

#Ниже прикладываю решение указанное на сайте:
def reverseString(str: str) -> str:
    # if the string is " " then return "".
    if (str == "" or str == " "):
        return ""
    ans = ''

    start = len(str) - 1

    while (start >= 0):

        # Skip multiple spaces.
        if (str[start] == ' '):
            start -= 1
        else:

            # Add space between words.
            if (len(ans) > 0):
                ans += (' ')

            j = start

            while (j >= 0 and str[j] != ' '):
                j -= 1

            # add current word to ans.
            ans += (str[j + 1: j + 1 + start - j])
            start = j

    return ans


#Не проще ли так?) и читается легко и время выполнения не уступает
s = 'ya ya  tpc     str          1    '
res = ''
x = s.split(' ')
x.reverse()
for t in x:
    if t == '':
        pass
    else:
        res += t
        res += ' '
print(res)
