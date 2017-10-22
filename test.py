import tkinter as tk                # python 3

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

        def van_delete(event):  # note that you must include the event as an arg, even if you don't use it.
            van.delete(0, "end")
            return None
        def naar_delete(event):  # note that you must include the event as an arg, even if you don't use it.
            naar.delete(0, "end")
            return None

        controller.title("Project programmeren")
        label = tk.Label(self, text="Welkom by NS ",fg='blue', background='#FFD700', width=400, font='Times 16 bold', height=2)
        label.pack(side="top", fill="x")
        van = tk.Entry(self, bd=4, fg='#000080', bg='#FAFAD2', font='Times 14 bold')
        van.insert('end', 'Van')
        van.bind("<Button-1>", van_delete)      #zorgt ervoor dat de default text Van gedelete wordt na het box te klikken
        van.pack(ipady=4, pady=10)
        naar = tk.Entry(self, bd=4, fg='#000080', bg='#FAFAD2', font='Times 14 bold')
        naar.insert('end', 'Naar')
        naar.bind("<Button-1>", naar_delete)            #zorgt ervoor dat de default text Naar gedelete wordt na het box te klikken
        naar.pack(ipady=4, pady=10)
        button1 = tk.Button(self, text="Plannen", font='Times 14 bold', bg= 'blue', fg='white', activebackground='blue', activeforeground='white',
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack(ipadx=30)
        controller.geometry("300x400")
        self.configure(background='#377BDA')




class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#377BDA')
        label = tk.Label(self, text="Reisplanner",fg='blue', background='#FFD700', width=400, font='Times 16 bold', height=2)
        label.pack(side="top", fill="x")

        w = tk.Label(self, text="Vertrektijd", font='Times 16 bold',fg='blue', bg='gold')
        w.pack(pady=4)
        T = tk.Text(self, height=1, width=10)
        T.pack()
        v = tk.Label(self, text="Type Trein", font='Times 16 bold', fg='blue', bg='gold')
        v.pack(pady=4)
        K = tk.Text(self, height=1, width=20)
        K.pack()
        a = tk.Label(self, text="Eind bestemming", font='Times 16 bold', fg='blue', bg='gold')
        a.pack(pady=4)
        l = tk.Text(self, height=1, width=20)
        l.pack()

        button = tk.Button(self, text="Ga terug",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()





if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()