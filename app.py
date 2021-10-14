import tkinter as tk
from tkinter import Frame, filedialog, Text
import os

# holds the whole app
root = tk.Tk()

# append the files 
apps = []

# load up the tex file 
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


# function to add exe files (for windows)  
def addApp():

    # to update the apps on the screen
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="select file", filetypes=(("executables", "*.exe"), ("all files", "*.*"))) # also gives the location of the picked file 

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="#3A6351")

# run the app 
def runApps():
    for app in apps:
        os.startfile(app)


# create canvas
canvas = tk.Canvas(root, height=700, width=700, bg="#393232")
# attach the canvas to the root
canvas.pack()

# frame in the middle
frame = tk.Frame(root, bg="#F2EDD7")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# buttons 
# open files 
openFile = tk.Button(root, text="open File", padx=10, pady=5, fg="white", bg="#F58634", command=addApp)
openFile.pack()

# run apps 
runApps = tk.Button(root, text="run Apps", padx=10, pady=5, fg="white", bg="#F58634", command=runApps)
runApps.pack()

# populate the saved apps on the screen
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


# run the app
root.mainloop()



# create a file and save the apps to stay when the machine is shuted down
with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ',')


# Todo: 
# test it on windows vm 
# add a functionallity for delete the apps of single apps from the list 
# make runnable for unix systems 
# find a better design of the app 

