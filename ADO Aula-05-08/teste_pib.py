from ReadFile import ReadFile

read = ReadFile()
s = read.list_file('pib.txt')
dic = read.pib_total(s)
print(dic)