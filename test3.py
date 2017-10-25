import tkinter as tk
from NS_API import *
class NS_APP(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Project programmeren")
        self.iconbitmap(r'ns.ico')
        tk.Label(self, text="Welkom bij NS ", fg='blue', background='#FFD700', font='Times 16 bold',
              height=2).grid(columnspan=5, ipadx=90, sticky='W')

        def van_delete(event):  # woord van verwijderen als er op geklikt wordt
            self.van.delete(0, "end")
            return None

        def naar_delete(event):  # woord naar verwijderen als er op geklikt wordt.
            self.naar.delete(0, "end")
            return None

        self.van = tk.Entry(self, fg='#000080', bg='#FAFAD2', font='Times 14 bold')
        self.van.insert('end', 'VAN')
        self.van.bind("<Button-1>", van_delete)
        self.naar = tk.Entry(self, fg='#000080', bg='#FAFAD2', font='Times 14 bold')
        self.naar.insert('end', 'NAAR')
        self.naar.bind("<Button-1>", naar_delete)

        button1 = tk.Button(self, text="Plannen", font='Times 14 bold', bg='blue', fg='white', activebackground='blue',
                         activeforeground='white', command= self.plannen)


        self.van.grid(row=3, column=0, sticky='W', pady=20, padx=40)
        self.naar.grid(row=4, column=0, sticky='W', padx=40)
        button1.grid(row=6, column=0, sticky='W', pady=20, padx=100)



    def plannen(self):

        beginstation = self.van.get()
        eindstation = self.naar.get()
        request(beginstation, eindstation)
        vertrektijd = vertrektijden()
        spor = spoor(vertrektijd)
        aankomsts = aankomst(vertrektijd)
        reistij = reistijd(vertrektijd)

        label0 = tk.Label(self, text="Spoor: ", font='Times 14 bold', fg='blue')
        label1 = tk.Label(self, text="Vertrektijd: {}", font='Times 14 bold', fg='blue')
        label2 = tk.Label(self, text="Aankomst:  ", font='Times 14 bold', fg='blue')
        label3 = tk.Label(self, text="Reistijd: ", font='Times 14 bold', fg='blue')

        label0.grid(row=7, column=0, sticky='W')
        label1.grid(row=8, column=0, sticky='W')
        label2.grid(row=9, column=0, sticky='W')
        label3.grid(row=10, column=0, sticky='W')
        label0.config(text="Spoor: {}".format(spor))
        label1.config(text="Vertrektijd: {}".format(vertrektijd))
        label2.config(text="Aankomst: {}".format(aankomsts))
        label3.config(text="Reistijd: {}".format(reistij))

w = NS_APP()
w.mainloop()