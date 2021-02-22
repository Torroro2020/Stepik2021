# Считываем 4 строки в цикле
original, coding, first_string, second_string = (input() for i in range(4))

# По индексу символа из оригинала берём символ на замену из кодировки,
# для каждого символа из строки, которую нужно закодировать
print(*[coding[original.find(symbol)] for symbol in first_string], sep='')
# Аналогично, только наоборот :D
print(*[original[coding.find(symbol)] for symbol in second_string], sep='')