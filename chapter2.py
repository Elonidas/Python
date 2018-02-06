






import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


win=tk.Tk()


win.title("Python WIN")

a_label=ttk.Label(win, text="Enter name:")
a_label.grid(column=0, row=0)

def click_me():
	action.configure(text="Hello "+ name.get()+ " "+number_chosen.get())

name=tk.StringVar()
name_entered=ttk.Entry(win, width=12 ,textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(win, text="Greet", command=click_me)
action.grid(column=2, row=1)

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number=tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state="readonly")
number_chosen['values'] =(1,2,4,42,100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

colors =["Red","Blue","Gold"]

def radCall():
	radSel=radVar.get()
	if	 radSel == 0: win.configure(background=colors[0])
	elif radSel == 1: win.configure(background=colors[1])
	elif radSel == 2: win.configure(background=colors[2])

radVar = tk.IntVar()

radVar.set(99)

for col in range(3):
	curRad = tk.Radiobutton(win, text=colors[col], variable=radVar,
	                        value=col, command=radCall)
	curRad.grid(column=col, row=5, sticky=tk.W)



scrol_w =50
scrol_h =3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

buttons_frame = ttk.LabelFrame(win, text="Labels in a Frame ")
buttons_frame.grid(column=0, row=7, padx=20, pady=20)

for col in range(3):
		ttk.Label(buttons_frame, text="Label %s" %(col+1)).grid(column=0, row=col, sticky=tk.W)


for child in buttons_frame.winfo_children():
		child.grid_configure(padx=0,pady=20)



name_entered.focus()

win.mainloop()
