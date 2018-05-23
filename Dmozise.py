"""
- text annotation: identifying the list of entities and non-entities mentioned in the provided text
- text categorization: identification of up to 5 categories that describe the topic of the given text.
    The list of available categories come from DMOZ open directory. Currently, only English text can be categorized!
"""

from eventregistry import *
from eventregistry.Base import *
from eventregistry.ReturnInfo import *
import tkinter
from tkinter import *

class Analytics:
    def __init__(self, eventRegistry):
        """
        @param eventRegistry: instance of EventRegistry class
        """
        self._er = eventRegistry


    def annotate(self, text, lang = None):
        """
        identify the list of entities and nonentities mentioned in the text
        @param text: input text to annotate
        @param lang: language of the provided document (can be an ISO2 or ISO3 code). If None is provided, the language will be automatically detected
        """
        return self._er.jsonRequestAnalytics("/api/v1/annotate", { "lang": lang, "text": text })


    def categorize(self, text):
        """
        determine the set of up to 5 categories the text is about. Currently, only English text can be categorized!
        @param text: input text to categorize
        """
        return self._er.jsonRequestAnalytics("/api/v1/categorize", { "text": text })


matrix = {'Arts': {'1':0,'2':0,'3':0,'4':0}, 
          'Business': {'1':0,'2':0,'3':0,'4':0}, 
          'Computers': {'1':0,'2':0,'3':0,'4':0}, 
          'Games': {'1':0,'2':0,'3':0,'4':0},
          'Health': {'1':0,'2':0,'3':0,'4':0},
          'Home': {'1':0,'2':0,'3':0,'4':0},
          'News': {'1':0,'2':0,'3':0,'4':0},
          'Recreation': {'1':0,'2':0,'3':0,'4':0},
          'Reference': {'1':0,'2':0,'3':0,'4':0},
          'Regional': {'1':0,'2':0,'3':0,'4':0},
          'Science': {'1':0,'2':0,'3':0,'4':0},
          'Shopping': {'1':0,'2':0,'3':0,'4':0},
          'Society': {'1':0,'2':0,'3':0,'4':0},
          'Sports': {'1':0,'2':0,'3':0,'4':0},
          'Kids & Teens Directory': {'1':0,'2':0,'3':0,'4':0}
           }


file = input("Enter the file name:\n")
with open(file) as f:
    lines = f.readlines()


er = EventRegistry(apiKey = "2b02894d-06b8-47be-a5a5-e88c9711444f")
ana = Analytics(er)

for line in lines:
    try:
        line = line.replace("\n","")
        n = len(line)
        quadrant = line[-1]
        todo = line[:-4]
        categories = ana.categorize(todo) 
        genre = categories['categories'][0]['label'].replace("'","").split("/")[1]
        if(genre in matrix):
            matrix[genre][quadrant] += 1
        print(todo)
        print(genre)
        print(matrix)
    except:
        print("exception encountered while processing:")
        print(line)
        print(categories)

Q = {'1' : [],'2' :[], '3': [], '4': []}

for key in matrix:
    Q[max(matrix[key], key=matrix[key].get)].append(key)

Q1 = '\n'.join(Q['1'])
Q2 = '\n'.join(Q['2'])
Q3 = '\n'.join(Q['3'])
Q4 = '\n'.join(Q['4'])

root = Tk()
root.title("Analysis")
root.geometry("800x800")



# top = Frame(root)
# bottom = Frame(root)
# topleft = Frame(top)
# topright = Frame(top)
# bottomleft = Frame(bottom)
# bottomright = Frame(bottom)



# top.pack(side="top")
# bottom.pack(side="bottom")
# topleft.pack(side="left")
# topright.pack(side="right")
# bottomleft.pack(side="left")
# bottomright.pack(side="right")



# labelframe1 = LabelFrame(topleft, text="Focus", bg = "red4", fg ="white", relief ="solid")
# labelframe2 = LabelFrame(topright, text="Goals", bg = "blue4", fg ="white", relief ="solid")
# labelframe3 = LabelFrame(bottomleft, text="Delegate", bg = "dark green", fg ="white", relief ="solid")
# labelframe4 = LabelFrame(bottomright, text="Burnout", bg ="black", fg ="white", relief ="solid")


# labelframe1.pack(fill=None, expand=False)
# labelframe2.pack(fill=None, expand=False)
# labelframe3.pack(fill=None, expand=False)
# labelframe4.pack(fill=None, expand=False)

# one = Label(labelframe1, text= Q1, background ="red",fg ="white")
# one.pack()
# two = Label(labelframe2, text=Q2, background ="blue",fg ="white")
# two.pack()
# three = Label(labelframe3, text=Q3, background ="forest green",fg ="white")
# three.pack()
# four = Label(labelframe4, text=Q4, background ="gray15",fg ="white")
# four.pack()

w = 800
h = 800
wh = w/2
hh = h/2
wq = w/4
hq = h/4

canvas = Canvas(root, width=w, height=h)

canvas.pack()

canvas.create_rectangle(0, 0, wh, hh, fill="red")
canvas.create_rectangle(w, 0, wh, hh, fill="blue")
canvas.create_rectangle(0, h, wh, hh, fill="green")
canvas.create_rectangle(w, h, wh, hh, fill="black")
canvas.create_line(0, hh, w, hh,fill="white", width = 2)
canvas.create_line(wh, 0, wh, h,fill = "white", width = 2)


canvas.create_text(10,10,anchor= "nw",fill="white",font="Times 20 italic bold",text="Focus:")
canvas.create_text(wh+10,10,anchor= "nw",fill="white",font="Times 20 italic bold",text="Goals:")
canvas.create_text(10,hh+10,anchor= "nw",fill="white",font="Times 20 italic bold",text="Delegate:")
canvas.create_text(wh+10,hh+10,anchor= "nw",fill="white",font="Times 20 italic bold",text="Burnout:")

canvas.create_text(wq,hq,fill="white",font="Times 15 italic bold",text=Q1)
canvas.create_text(wq+wh,hq,fill="white",font="Times 15 italic bold",text=Q2)
canvas.create_text(wq,hq+hh,fill="white",font="Times 15 italic bold",text=Q3)
canvas.create_text(wq+wh,hq+hh,fill="white",font="Times 15 italic bold",text=Q4)


root.mainloop()

