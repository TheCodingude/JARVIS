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

   with open(f"{path}\\index.html", "w") as f:
      f.write("<!DOCTYPE html>\n")
      f.write('<html lang="en">\n')
      f.write('<head>\n')
      f.write('   <meta charset="UTF-8">\n')
      f.write('   <meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
      f.write('   <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
      f.write('   <title>Document</title>\n')
      f.write('   <link rel="stylesheet" href="style.css">\n')
      f.write('   <script defer src="index.js"></script>\n')
      f.write('</head>\n')
      f.write('<body>\n')
      f.write('   <h1>TEST</h1>\n')
      f.write('</body>\n')
      f.write('</html>\n')

   with open(f"{path}\\style.css", "w") as f:
      f.close()

   with open(f"{path}\\script.js", "w") as f:
      f.close()

def openProject(project_path):
   
   os.system(f"code {project_path}")


createNewWebDevProject("lol")

