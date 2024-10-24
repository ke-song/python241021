import sqlite3

print()

con = sqlite3.connect(r'c:\work\sample.db')

cur = con.cursor()

cur.execute("create table if not exists PhoneBook (Name text,  PhoneNum text);")

cur.execute("insert into PhoneBook values ('derick', '010-1234-5678');")

name = 'bob'
phoneNumber = '010-1234-1111'
cur.execute("insert into PhoneBook values(?, ?);", (name, phoneNumber))

datalist = (('john', '010-1234-2222'), ('kim', '010-1234-3333'))
cur.executemany("insert into PhoneBook values(?, ?);", datalist)

cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row[0], row[1])
print(cur.fetchall())

# print(cur.fetchmany(2))

con.commit()

print()





