import tkinter as tki # Tkinter -> tkinter in Python3
import xmltodict, requests
class App(object):

    def __init__(self):
        self.root = tki.Tk()

    # create a Frame for the Text and Scrollbar
        txt_frm = tki.Frame(self.root, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tki.Text(txt_frm, borderwidth=3, relief="sunken", fg='blue')
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set


        with open('vertrektijden.xml', 'r') as myXMLFile:
            content = xmltodict.parse(myXMLFile.read())
            for line in content['ActueleVertrekTijden']['VertrekkendeTrein']:
                try:
                    if line['RouteTekst']:
                        q = "Ritnummer:" + line['RitNummer']+"\nVertrek tijd: "+line['VertrekTijd'][11:19]+"\n"+ \
                            line['RouteTekst'], line['VertrekSpoor']['#text'] + '\n\n'
                        # q = q.replace('{', '')
                        self.txt.insert('end', q)
                except KeyError:
                    q = "Ritnummer:" + line['RitNummer'], line['VertrekTijd'][11:19], line['VertrekSpoor'][
                        '#text'] + '\n\n'
                    self.txt.insert('end', q)

app = App()
app.root.mainloop()