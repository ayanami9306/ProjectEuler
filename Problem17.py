num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]
word = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety']
num2word = dict(zip(num, word))

sum = 0
for i in range(1, 1001):
    if i >= 1000:
        sum += len('onethousand')
        i -= 1000
    if i >= 100:
        multiplier = int(i / 100)
        sum += len(num2word[multiplier])
        sum += len('hundred')
        i -= multiplier * 100
        if i > 0:
            sum += len('and')
    if i >= 21:
        multiplier = int(i / 10)
        sum += len(num2word[multiplier * 10])
        i -= multiplier * 10
    if i > 0:
        sum += len(num2word[i])

print(sum)