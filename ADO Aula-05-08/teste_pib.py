from ReadFile import ReadFile
import pprint
pp = pprint.PrettyPrinter(indent=2)

read = ReadFile()
s = read.list_file('pib.txt')
d = read.list_file('regioes.txt')
dic = read.to_dict(s)
total = read.pib_total(s)
pp.pprint(dic)
# print(dic)

