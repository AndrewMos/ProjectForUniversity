import glob
import operator
import datetime

# Jjj Uuu 00211585215
# Kkk Iii 03210304614
def add_sitizen():
	check = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
	city = input()
	data = input().split()
	name = data[0]
	surname = data[1]
	pesel = data[2]
	if (len(pesel) != 11):
		print ('Pesel len is bad')
		return 0
	temp = 0
	for i in range(10):
		temp += int(pesel[i])*check[i]
	temp = temp%10
	if (temp != 0):
		temp = 10 - temp
	if (temp != int(pesel[10])):
		print('Pesel is bad')
		return 0
	citizen = Citizen(city, pesel, name, surname)
	return citizen


def rewrite_result(citizens_list):
	f = open("results.txt", "w")
	cities = [ c.city for c in citizens_list ]
	cities = list(set(cities))
	cities.sort()
	for ct in cities:
		f.write(ct + "\n")
		people = [ c for c in citizens_list if c.city == ct]
		for person in people:
			f.write(person.info() + "\n")


class Citizen:
	def __init__(self, city, pesel, name, surname):
		self.city = city.replace(' ', '')
		self.pesel = pesel.replace(' ', '')
		self.name = name.replace(' ', '')
		self.surname = surname.replace(' ', '')
	def info(self):
		return (self.name + " " + self.surname + " " + self.pesel).replace('\n', ' ')

def check_time():
	print (str(datetime.datetime.now()))
