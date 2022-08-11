#Read data file
#Process file lines and create terraform friendly json objects

with open('../resources/ServiceData.txt') as fh:
    for line in fh:
        groups = line.split('\t')
        print('{')
        print('\t"serviceID": {\n\t\t"S": "' + groups[0] + '"\n\t},')
        print('\t"description": {\n\t\t"S": "' + groups[1].replace('\n', '') + '"\n\t}')
        print('}\n')