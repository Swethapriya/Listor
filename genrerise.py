Health = {"doctor","checkup", "excercise"}
career = {"complete","study","prepare", "learn"}
Shopping = {"buy","purchase","gift","get"}
Travel = {"visit"}
Chill = {"dinner","dance","mall","salon", "watch"}


def genrerise(todo):
	t = 0
	shop = 0
	ch = 0
	h = 0
	car = 0
	words = todo.split(" ")
	for i in words:
		if(i in Travel):
			t += 1
		if(i in Shopping):
			shop += 1
		if(i in Chill):
			ch += 1
		if(i in Health):
			h += 1
		if(i in career):
			car += 1
	genres = []
	if(t>0):
		genres.append("travel")
	if(shop>0):
		genres.append("Shopping")
	if(ch>0):
		genres.append("chill")
	if(h>0):
		genres.append("Health")
	if(car>0):
		genres.append("career")
	return genres


PriorityOrder = {"Health","career","Travel","Shopping"}
LineOfImportance = 1
n = int(input("Enter the number of todo's:"))
for i in range(n):
	todo = input()
	print(genrerise(todo))