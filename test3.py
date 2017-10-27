import tkinter as tk
import tkinter.messagebox
from NS_API import *
.01

class NS_APP(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Project programmeren")
        self.iconbitmap(r'ns.ico')
        tk.Label(self, text="Welkom bij NS ", fg='blue', background='#FFD700', font='Times 16 bold',
              height=2).grid(columnspan=5, ipadx=130, sticky='W')


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
        button2 = tk.Button(self, text="Alle Vertrektijden", font='Times 14 bold', bg='blue', fg='white', activebackground='blue',
                            activeforeground='white', command= self.vertrekk)
        # button3 = tk.Button(self, text="Storingen?", font='Times 14 bold', bg='blue', fg='white',
        #                     activebackground='blue',
        #                     activeforeground='white', command=self.storing)

        self.van.grid(row=3, column=0, sticky='W', pady=20, padx=40)
        self.naar.grid(row=4, column=0, sticky='W', padx=40)
        button1.grid(row=6, column=0, sticky='W', pady=20, padx=100)
        button2.grid(row=12, column=0, sticky='W')
        # button3.grid(row=12, column=1, sticky='E')

    def vertrekk(self):
        toplevel = tk.Toplevel()
        toplevel.title('Another window')
        toplevel.focus_set()
        toplevel.geometry('450x4500')
        txt_frm = tk.Frame(toplevel, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

        toplevel.txt = tk.Text(txt_frm, borderwidth=3, relief="sunken", fg='blue')
        toplevel.txt.config(font=("consolas", 12), undo=True, wrap='word')
        toplevel.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        scrollb = tk.Scrollbar(txt_frm, command=toplevel.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        toplevel.txt['yscrollcommand'] = scrollb.set

        with open('vertrektijden.xml', 'r') as myXMLFile:
            content = xmltodict.parse(myXMLFile.read())
            for line in content['ActueleVertrekTijden']['VertrekkendeTrein']:
                try:
                    if line['RouteTekst']:
                        q = "Ritnummer:" + line['RitNummer'] + "\nVertrek tijd: " + line['VertrekTijd'][
                                                                                    11:19] + "\n" + \
                            line['RouteTekst'] + "\nSpoor: " + line['VertrekSpoor']['#text'] + '\n\n'

                        toplevel.txt.insert('end', q)
                except KeyError:
                    q = "Ritnummer:" + line['RitNummer'], line['VertrekTijd'][11:19] + "\nSpoor: " +line['VertrekSpoor'][
                        '#text'] + '\n\n'
                    toplevel.txt.insert('end', q)
    def plannen(self):

        beginstation = self.van.get()
        eindstation = self.naar.get()
        if beginstation == eindstation:
            tk.messagebox.showinfo("info", 'Ongeldige invoer. Vertrek station is zelfde als eindbestemming')
        request(beginstation, eindstation)
        vertrektijd = vertrektijden()
        spor = spoor(vertrektijd)
        aankomsts = aankomst(vertrektijd)
        reistij = reistijd(vertrektijd)

        label = tk.Label(self, text="Eerst volgende trein: ", font='Times 14 bold', fg='gold', bg='blue')
        label0 = tk.Label(self, text="Spoor: ", font='Times 14 bold', fg='blue')
        label1 = tk.Label(self, text="Vertrektijd: {}", font='Times 14 bold', fg='blue')
        label2 = tk.Label(self, text="Aankomst:  ", font='Times 14 bold', fg='blue')
        label3 = tk.Label(self, text="Reistijd: ", font='Times 14 bold', fg='blue')

        label.grid(row=7, column=0, sticky='W')
        label0.grid(row=8, column=0, sticky='W')
        label1.grid(row=9, column=0, sticky='W')
        label2.grid(row=10, column=0, sticky='W')
        label3.grid(row=11, column=0, sticky='W')

        label0.config(text="Spoor: {}".format(spor))
        label1.config(text="Vertrektijd: {}".format(vertrektijd))
        label2.config(text="Aankomst: {}".format(aankomsts))
        label3.config(text="Reistijd: {}\n".format(reistij))



    def info_box(self):
        beginstation = self.van.get()
        eindstation = self.naar.get()
        request(beginstation, eindstation)
        vertrektijd = vertrektijden()
        spor = spoor(vertrektijd)
        aankomsts = aankomst(vertrektijd)
        reistij = reistijd(vertrektijd)
        statuss = status(vertrektijd)
        if statuss != 'VOLGENS-PLAN':
            statuss = 'Trein is vertraagd'
        beginstation = naam_beginstation(vertrektijd)
        tk.messagebox.showinfo("info", "Extra informatie \n "
                                       "Je vertrekt van {} \n En de status van de trein is: {}".format(beginstation, statuss))

    def storing(self):
        data = storing(vertrektijd)
        storingen = striphtml(data)
        tk.messagebox.showinfo("info","Je arriveert bij {} \nOpmerking: {}".format(eindstation, storingen))


w = NS_APP()
w.mainloop()