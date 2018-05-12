Travel = {"visit"}
Shopping = {"buy","purchase","gift","get"}
Chilling = {"dinner","dance","mall","salon","doctor"}
Productive = {"complete","study","prepare"}
Scheduled ={"class", "coaching", "training","match"}

def genrerise(todo):
	t = 0
	shop = 0
	c = 0
	p = 0
	s = 0
	words = todo.split(" ")
	for i in words:
		if(i in Travel):
			t += 1
		if(i in Shopping):
			shop += 1
		if(i in Chilling):
			c += 1
		if(i in Productive):
			p += 1
		if(i in Scheduled):
			s += 1
	genres = []
	if(t>0):
		genres.append("travel")
	if(shop>0):
		genres.append("Shopping")
	if(c>0):
		genres.append("chill")
	if(p>0):
		genres.append("Productive")
	if(s>0):
		genres.append("Scheduled")
	return genres



n = int(input("Enter the number of todo's:"))
for i in range(n):
	todo = input()
	print(genrerise(todo))