
row = ''
with open('resources/userdata.txt') as f:
    lines = f.readlines()
    n = len(lines)
    for i in range(0, n):
        line = lines[i]
        if(line.startswith('<tr>')):
            j = i
            for j in range(i, n):
                if(lines[j].startswith('</tr>')):
                    break
                if(lines[j].startswith('<td class="text-left">')):
                    row += ((lines[j].replace('<td class="text-left">', '').replace('</td>', '').replace('\n', '')) + '\t')
            row += '\n'
            i = j

resultFile = open('resources/formattedData.txt.txt', 'a')
resultFile.write(row)
resultFile.close()