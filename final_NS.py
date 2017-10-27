import tkinter as tk
import tkinter.messagebox
from NS_API import *


class NS_APP(tk.Tk):
    '''
    Opmaak van de hoofdframe
    '''
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Project programmeren")
        '''Kleine NS icoon boven de programma '''
        self.iconbitmap(r'ns.ico')
        ''' Eerste Label binnen de hoofdframe en de layout'''
        tk.Label(self, text="Welkom bij NS ", fg='blue', background='#FFD700', font='Times 16 bold',
              height=2).grid(columnspan=5, ipadx=90, sticky='W')


        def van_delete(event):  # woord VAN verwijderen als er op geklikt wordt
            self.van.delete(0, "end")
            return None

        def naar_delete(event):  # woord NAAR verwijderen als er op geklikt wordt.
            self.naar.delete(0, "end")
            return None

        '''Twee entryfields binnen de gui Van en Naar. '''
        self.van = tk.Entry(self, fg='#000080', bg='#FAFAD2', font='Times 14 bold')
        self.van.insert('end', 'VAN')
        self.van.bind("<Button-1>", van_delete)
        self.naar = tk.Entry(self, fg='#000080', bg='#FAFAD2', font='Times 14 bold')
        self.naar.insert('end', 'NAAR')
        self.naar.bind("<Button-1>", naar_delete)


        '''Het aanmaken van de buttons en de layout binnen de gui. Het zijn er drie. '''
        button1 = tk.Button(self, text="Plannen", font='Times 14 bold', bg='blue', fg='white', activebackground='blue',
                         activeforeground='white', command= self.plannen)
        button2 = tk.Button(self, text="Alle Vertrektijden", font='Times 14 bold', bg='blue', fg='white', activebackground='blue',
                            activeforeground='white', command= self.vertrekk)
        button3 = tk.Button(self, text="Storingen?", font='Times 14 bold', bg='blue', fg='white',
                            activebackground='blue',
                            activeforeground='white', command=self.storing)

        '''' Plaatsing van de buttons op de gui  '''
        self.van.grid(row=3, column=0, sticky='W', pady=20, padx=40)
        self.naar.grid(row=4, column=0, sticky='W', padx=40)
        button1.grid(row=6, column=0, sticky='W', pady=20, padx=100)
        button2.grid(row=12, column=0, sticky='W', pady=5)
        button3.grid(row=13, column=0, sticky='W')

    def vertrekk(self):
        '''
        De functie vertrekk wordt er gebruikt als er op de knop Alle vertrektijden wordt geklikt.
         '''
        beginstation = self.van.get()
        if beginstation == 'VAN' or beginstation == '':
            tk.messagebox.showinfo('Ongeldige invoer.', 'Voer a.u.b een geldige vertrek station')
        else:
            '''
            De textbox frame wordt hier aangemaakt na het klikken van vertrektijden.
            '''
            request_vertrektijd(beginstation)
            toplevel = tk.Toplevel()
            toplevel.iconbitmap(r'ns.ico')
            toplevel.title('Alle vertrek tijden van ' + beginstation.capitalize())
            toplevel.focus_set()
            toplevel.geometry('450x500')
            txt_frm = tk.Frame(toplevel, width=600, height=600)
            txt_frm.pack(fill="both", expand=True)
            # zorgt dat de text field lengte aan de gui past
            txt_frm.grid_propagate(False)
            # text field past aan de groote van de frame
            txt_frm.grid_rowconfigure(0, weight=1)
            txt_frm.grid_columnconfigure(0, weight=1)
            '''
            De textbox area (niet in dezelfde root frame) wordt hier aangemaakt na het klikken van vertrektijden.
            '''
            toplevel.txt = tk.Text(txt_frm, borderwidth=3, relief="sunken", fg='blue')
            toplevel.txt.config(font=("consolas", 12), undo=True, wrap='word')
            toplevel.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

            ''' Het textbox zelfkrijgt een scrollbar hier  '''
            scrollb = tk.Scrollbar(txt_frm, command=toplevel.txt.yview)
            scrollb.grid(row=0, column=1, sticky='nsew')
            toplevel.txt['yscrollcommand'] = scrollb.set


        with open('vertrektijden.xml', 'r') as myXMLFile:
            ''' Hier wordt de textbox van tkinter gecreerd en alle vertrektijden van de xml bestand gelezen en geschreven '''
            content = xmltodict.parse(myXMLFile.read())
            for line in content['ActueleVertrekTijden']['VertrekkendeTrein']:
                    q = "Ritnummer:" + line['RitNummer'] + "\nVertrek tijd: " + line['VertrekTijd'][11:19] + "\n" + \
                        "Spoor: "+line['VertrekSpoor']['#text']+"\nEindbestemming is "+ \
                        line['EindBestemming']+ "\n\n"
                    toplevel.txt.insert('end', q)   # Alle vertrek tijden wordt ingeschreven binnen de loop


    def plannen(self):
        '''
           De functie plannen wordt gebruikt nadat er Begin en eind bestemming is ingevoerd in de GUI.
           Hierbij wordt de van en naar entry field gelezen
           '''
        try:
            beginstation = self.van.get()
            eindstation = self.naar.get()
            if beginstation == eindstation:
                tk.messagebox.showinfo("info", 'Ongeldige invoer. Vertrek station is zelfde als eindbestemming')
            elif eindstation == 'NAAR':
                tk.messagebox.showinfo('Ongeldige invoer.', 'Voer a.u.b een geldige Bestemming station')

            request(beginstation, eindstation)
            vertrektijd = vertrektijden()
            spor = spoor(vertrektijd)
            aankomsts = aankomst(vertrektijd)
            reistij = reistijd(vertrektijd)

            ''' Het aanmaken van de labels voor de geplande trein. '''
            label = tk.Label(self, text="Eerst volgende trein: ", font='Times 14 bold', fg='gold', bg='blue')
            label0 = tk.Label(self, text="Spoor: ", font='Times 14 bold', fg='blue')
            label1 = tk.Label(self, text="Vertrektijd: {}", font='Times 14 bold', fg='blue')
            label2 = tk.Label(self, text="Aankomst:  ", font='Times 14 bold', fg='blue')
            label3 = tk.Label(self, text="Reistijd: ", font='Times 14 bold', fg='blue')

            ''' Het positioneren van de labels voor de geplande trein. '''
            label.grid(row=7, column=0, sticky='W')
            label0.grid(row=8, column=0, sticky='W')
            label1.grid(row=9, column=0, sticky='W')
            label2.grid(row=10, column=0, sticky='W')
            label3.grid(row=11, column=0, sticky='W')

            ''' Het schrijven  van de labels voor de geplande trein. '''
            label0.config(text="Spoor: %s" %(spor))
            label1.config(text="Vertrektijd: {}".format(vertrektijd))
            label2.config(text="Aankomst: {}".format(aankomsts))
            label3.config(text="Reistijd: {}\n".format(reistij))
        except KeyError:
            tk.messagebox.showinfo('Ongeldige invoer.', 'Voer a.u.b een geldige station')



    def storing(self):
        '''
            De functie storing wordt gebruikt als er op de knop storingen wordt geklkit.
            Het leest de bestand storingen.xml
        '''
        beginstation = self.van.get()
        request_vertrektijd(beginstation)
        data = storing()
        storingen = striphtml(data)
        if beginstation == 'VAN' or beginstation == '':
            tk.messagebox.showinfo('Ongeldige invoer.', 'Voer a.u.b een geldige station')
        else:
            tk.messagebox.showinfo("info","Je bent op station:  {} \n{}".format(beginstation.capitalize(), storingen))


w = NS_APP() # Hier wordt de main programma aan w toegekend
w.mainloop() # Hier wordt de main programma gestart