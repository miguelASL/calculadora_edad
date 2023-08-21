"""La función "calculateAge()" toma el nombre y la fecha de nacimiento del usuario, y muestra la edad del usuario en años. La función "age()" recibe la fecha de nacimiento del usuario y calcula la edad del usuario en años.

El código está bien organizado y es fácil de entender. Los comentarios proporcionan información útil sobre lo que hace cada parte del código.

Aquí hay algunos detalles adicionales sobre el código:

La función "calculateAge()" utiliza la clase "Person" para crear un nuevo objeto "Person". Luego, se utiliza el objeto "Person" para llamar a la función "age()" y calcular la edad del usuario.
La función "age()" recibe la fecha de nacimiento del usuario y utiliza la función "datetime.date.today()" para obtener la fecha actual. Luego, se calcula la edad del usuario restando la fecha de nacimiento de la fecha actual.
El widget "textArea" se utiliza para mostrar la edad del usuario. El widget "textArea" es un widget de tkinter que se utiliza para mostrar texto.
El widget "button" se utiliza para activar la función "calculateAge()". El widget "button" es un widget de tkinter que se utiliza para activar una función."""

import datetime
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Calculadora Exacta")
window.geometry("620x780")
name = tk.Label(text= "Name")
name.grid(column= 0, row= 1)
year = tk.Label(text = "Year")
year.grid(column= 0, row= 2)
month = tk.Label(text= "Month")
month.grid(column= 0, row= 3)
date = tk.Label(text= "Day")
date.grid(column= 0, row= 4)
nameEntry = tk.Entry()
nameEntry.grid(column= 1, row= 1)
yearEntry = tk.Entry()
yearEntry.grid(column= 1, row= 2)
monthEntry = tk.Entry()
monthEntry.grid(column= 1, row= 3)
dateEntry = tk.Entry()
dateEntry.grid(column= 1, row= 4)
def calculateAge():
    name = nameEntry.get()
    person = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))
    textArea = tk.Text(master=window, height=10, width=25)
    textArea.grid(column=1, row=6)
    answer = " Heyy {person}!!!. You are {age} years old!!! ".format(person=name, age=person.age())
    textArea.insert(tk.END, answer)
button = tk.Button(window, text="Calculate Age", command=calculateAge)
button.grid(column=1, row=5)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age
image = Image.open('/home/mike/python/__pycache__/download.jpeg')
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)
window.mainloop()