import os


def createVsCodeNewProject(type, name):
   path = f"C:\\Users\\sharp\\Desktop\\{name}"

   os.makedirs(path) 

   with open(f"{path}\\main.py", "w") as f:
      if type == "":
         f.close()
      elif type == "gui":
         f.write("from tkinter import *\n\n\n\n")
         f.write("window = Tk()\n")
         f.write(f'window.title("{name}")\n\n')       
         f.write("window.mainloop()")

   os.system(f"code {path}")

def createNewWebDevProject(name):
   path = f"C:\\Users\\sharp\\Desktop\\{name}"

   os.makedirs(path)

   with open(f"index.html", "w") as f:
      f.close()

   with open("style.css", "w") as f:
      f.close()

   with open("script.js", "w") as f:
      f.close()

def openProject(project_path):
   
   os.system(f"code {project_path}")


openProject("C:\\Users\\sharp\\Desktop\\Old-Programming-Language")

