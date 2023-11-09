from datetime import datetime
notebook=[]
def add_note(note):
    note{"titel":input("title:"),
      "note":input("note"),
      "date":datetime.now()}
    notebook.append(note)
    return notebook
while True:
     command = input("""
chikar konam?
a=append note
e=exit
show=shownote""")
     if command = "a":
         notebook = add_note(notebook)
     elif command = "e"
         break
     elif command = "show"
          print(notebook)