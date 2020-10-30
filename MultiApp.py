import tkinter as tk
from tkinter import filedialog
import os,time,threading

# main loop start #
window = tk.Tk()

# window sizing #
window.geometry("500x530")
window.title("MultiApp")
window.minsize(500,500)


# variables #
index = tk.IntVar()
is_empty = False
applist = []


# frame #
mainframe = tk.Frame(window,bg="#C75532")
mainframe.pack(fill="both",expand=True)


# functions #
def timer():
    time.sleep(2)
    view()
    return 

def delete():
    global index

    if index.get() == 1 and len(applist) == 1:
        removed_app = applist[index.get()-1]
        applist.pop(index.get()-1)
        print(removed_app +' removed ')
        view()
        return

    elif index.get() > len(applist) or index.get() == 0:
        for widget in canvas.winfo_children():
            widget.destroy()

        l = tk.Label(canvas, text="NO ITEM AT THIS INDEX OR NO APPS, CHECK AGAIN!",padx = 25, pady = 5,bg="#D48168",fg="white")
        l.grid(row=0,column=0,pady = 5, padx = 5, sticky="nsew")

        threading.Thread(target=timer).start()
        return

    elif len(applist) == 0:
        l = tk.Label(canvas, text="THERE ARE NO APPS TO REMOVE, ADD ONE ABOVE!",padx = 25, pady = 5,bg="#D48168",fg="white")
        l.grid(row=0,column=0,pady = 5, padx = 5, sticky="nsew")
        view()
        return

    else:
        applist.pop(index.get()-1)
        print(index.get())
        view()

    view()


def view():
    for widget in canvas.winfo_children():
        widget.destroy()

    j = 0
    for app in applist:
        if len(app) > 1:
            l = tk.Label(canvas, text=app,padx = 25, pady = 5,bg="#D48168",fg="white")
            l.grid(row=j,column=0,pady = 5, padx = 5, sticky="nsew")
            j +=1


def open_file():
    filename = filedialog.askopenfilename(title="Select File",filetypes=(("exec","*.exe"),("all files","*.*")))
    print(filename)
    if filename == '':
        pass
    else:
        if len(applist) == 8:
           
            for widget in canvas.winfo_children():
                widget.destroy()

            l = tk.Label(canvas, text="MAX 8 APPS ARE ALLOWED ONLY!",padx = 25, pady = 5,bg="#D48168",fg="white")
            l.grid(row=0,column=0,pady = 5, padx = 5, sticky="nsew")

            threading.Thread(target=timer).start()
            return
        else:
            applist.append(filename)
    
    global is_empty
    if len(filename) == 0:
        is_empty = True
    
    else:
        is_empty = False
        view()


def execute():
    print(applist)
    if len(applist[0]) <= 1:
        l = tk.Label(canvas, text="THERE ARE NO APPS ADDED, ADD ONE ABOVE!",padx = 25, pady = 5,bg="#D48168",fg="white")
        l.grid(row=0,column=0,pady = 5, padx = 5, sticky="nsew")

        threading.Thread(target=timer).start()
        return
    else:
        for app in applist:
            if len(app) < 5:
                return
            else:
                os.startfile(app)


# text-file & path creation #
if os.path.isdir('C:/MultiApp/'):
    print('ispath')
else:
    print('not a path')
    os.mkdir('C:/MultiApp/')


# loading data from file #
if os.path.isfile('C:/MultiApp/apps.txt'):
    with open('C:/MultiApp/apps.txt','r') as f:
        content = f.read()
        
        content = content.split(',')
        content = [app for app in content if len(app) > 0]

        for app in content:
            applist.append(app)
        print("apps at load",content)
        print("length of apps" + str(len(applist)))



# GUI #
frame = tk.Frame(mainframe,bg="#C75532")
frame.pack(fill="x")

label1 = tk.Label(frame,text="SELECT APPS BELOW",bg="#C75532",fg="#211617",padx = 25, pady = 2)
button = tk.Button(frame, text="SELECT", command=open_file,bg="black",fg="white",padx = 5, pady = 2)
run = tk.Button(frame, text="RUN APPS", command=execute,bg="black",fg="white",padx = 5, pady = 2)

label2 = tk.Label(frame,text="REMOVE APPS (ENTER INDEX/ROW NUMBER)",bg="#C75532",fg="#211617",padx = 25, pady = 2)
entry = tk.Entry(frame,textvariable = index ,bg="black",fg="white")

delete = tk.Button(frame, text="DELETE", command=delete,bg="black",fg="white",padx = 5, pady = 2)

label1.pack(fill='x',padx = 5, pady = 5)
button.pack(fill='x',padx = 5, pady = 5)
run.pack(fill='x',padx = 5, pady = 5)
label2.pack(fill='x',padx = 5, pady = 5)
entry.pack(fill='x',padx = 5, ipady = 5)
delete.pack(fill='x',padx = 5, pady = 5)




frame2 = tk.Frame(mainframe,bg="#C75532")

canvas = tk.Canvas(frame2,bg="#C75532")
canvas.grid_columnconfigure(0,weight=1)
canvas.pack(fill='x')


frame2.pack(fill='x')



if is_empty:
    pass
else:
    view()


# mainloop end #
window.mainloop()



# update text-file at end of program #
print("applist at exit", applist)
with open('C:/MultiApp/apps.txt', 'w') as f:
    
    for app in applist:
        f.write(app + ',')




