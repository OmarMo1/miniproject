import tkinter as tk
# from NS_API import *
import xmltodict, requests
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")



    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        self.iconbitmap(r'ns.ico')

        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def van_delete(event):  # # woord van verwijderen als er op geklikt wordt
            van.delete(0, "end")
            return None
        def naar_delete(event):  # woord naar verwijderen als er op geklikt wordt.
            naar.delete(0, "end")
            return None


        controller.title("Project programmeren")
        tk.Label(self, text="Welkom bij NS ",fg='blue', background='#FFD700', font='Times 16 bold', height=2).grid(columnspan=5, ipadx=90)
        # van = self.StringVar()

        van = tk.Entry(self, fg='#000080', bg='#FAFAD2', font='Times 14 bold')
        van.insert('end', 'VAN')
        van.bind("<Button-1>", van_delete)
        van.grid(row=3, column=1, pady=30, padx=20)
        naar = tk.Entry(self, fg='#000080', bg='#FAFAD2', font='Times 14 bold')
        naar.insert('end', 'NAAR')
        naar.bind("<Button-1>", naar_delete)
        naar.grid(row=4, column=1)
        beginstation = van.get()
        eindstation = naar.get()



        button1 = tk.Button(self, text="Plannen", font='Times 14 bold', bg='blue', fg='white', activebackground='blue',
                            activeforeground='white',
                                                command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=6, columnspan=2, pady=20, ipadx=20)
        controller.geometry("325x450")
        self.configure(background='#377BDA')




class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#377BDA')
        tk.Label(self, text="Reisplanner ", fg='blue', background='#FFD700', font='Times 16 bold', height=2).grid(row=1,
            columnspan=5, ipadx=100)
        tk.Label(self, text="Vertrektijd:",font='Times 16 bold', fg='blue', bg='gold').grid(row=2, column=0, columnspan=2, pady=20)
        tk.Entry(self, font='Times 12 bold', fg='blue').grid(row=2, column=2, pady=20)
        tk.Label(self, text="Trein soort:",font='Times 16 bold', fg='blue', bg='gold').grid(row=3, column=0, columnspan=2, pady=20)
        tk.Entry(self, font='Times 12 bold', fg='blue').grid(row=3, column=2, pady=20)
        tk.Label(self, text="Bestemming: ",font='Times 16 bold', fg='blue', bg='gold').grid(row=4, column=0, columnspan=2, pady=20)
        tk.Entry(self, font='Times 12 bold', fg='blue').grid(row=4, column=2, pady=20)
        tk.Label(self, font='Times 16 bold', fg='gold').grid(row=5, column=0, columnspan=5)

        #
        # button = tk.Button(self, text="Ga terug",
        #                    command=lambda: controller.show_frame("StartPage"))
        # button.pack()





if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()