f = open('p022_names.txt', 'r')
name_data = f.readline().split(',')
f.close()
alphabet_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_number = list(i for i in range(1, 27))
alphabet = dict(zip(alphabet_letter, alphabet_number))
sum = 0
name_data.sort()
for word_index, i in enumerate(name_data):
    letter_sum = 0
    i = i.replace('"','')
    for j in i:
        letter_sum += alphabet[j]
    sum += letter_sum * (word_index+1)
print(sum)