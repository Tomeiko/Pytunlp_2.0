from collections import Counter
import string
texto = "123?!124!?"
cnt = Counter()
for elem in texto.lower():
    if elem in string.ascii_lowercase:
        cnt[elem] += 1
if cnt.most_common() != []:
    if cnt.most_common()[0][1] > 1:
        print("No es")
    else:
        print("Es")
else:
    print("No pusiste una palabra o frase")