haystack = 'asdabcabdjabcdabcdababcgj'
needle = 'abcdababc'

p = [0] * len(needle)
p[0] = 0

# len(needle) should be > 0 otherwise answer is 0 (like in java impl)

j, i = 0, 1
while i < len(needle):
    if needle[j] == needle[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j - 1]

print(f'{p=}')

i = j = 0
while i < len(haystack):
    if haystack[i] == needle[j]:
        i += 1
        j += 1
        if j == len(needle):
            print('Substring starts from', i - j, haystack[i - j:i - j + len(needle)])
            break
    else:
        if j > 0:
            j = p[j - 1]
        else:
            i += 1

if i == len(haystack):
    print('Haystack doesnt contain needle')
