#파일 쓰기
f = open('test.txt', 'wt', encoding='utf-8')
f.write('Hello, Python')
f.close()

#파일 읽기
f = open('test.txt', 'rt')
text = f.read()
print(text)
f.close()
print()

# print(dir(str))

data = '<<< spam and ham >>>'
result = data.strip('<>')
print(result)
print(data)
result2 = result.replace('spam', 'spam and egg')
print(result2)
lst = result2.split()
print(lst)
print(':)'.join(lst))
print()

print('MBC2580'.isalnum())
print('MBC2580'.isalpha())
print('2580'.isdigit())
print('2580'.isdecimal())
print('2580'.isnumeric())
print()


