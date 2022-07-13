def print_formatted(number):
    max_width = len(str(bin(number)[2:]))
    for num in range(1, number+1):
        line = str(num).rjust(max_width, ' ')
        line += ' ' + format(num, 'o').rjust(max_width, ' ')
        line += ' ' + format(num, 'x').upper().rjust(max_width, ' ')
        line += ' ' + format(num, 'b').rjust(max_width, ' ')
        print(line)


print_formatted(2)