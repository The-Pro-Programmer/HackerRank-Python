def count_substring(string, sub_string):
    count = 0
    len1 = len(string)
    len2 = len(sub_string)
    for i in range(0, len1-len2+1):
        sub = string[i:(i+len2)]
        if sub == sub_string:
            count += 1
    return count

print(count_substring('ABCDCDC', 'CDC'))
print(count_substring('AB0000AB', 'AB'))
print(count_substring('AAAAAB', 'AA'))
print(count_substring('BOAAAAAB', 'AA'))