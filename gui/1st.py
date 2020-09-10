from tkinter import *
from tkinter import ttk
import os
count = 1
classes = []
data1= None
def next_window():
    '''
    For creating a new Toplevel window
    '''
    def widget():
        '''
        Defined to take input from existing class or create a new class
        '''
        l = ttk.Label(mainframe)
        l.grid(column=1,row=4,sticky=W)
        l['text']= 'Select or Enter Class' + str(count)
        #Combobox created
        datasel=StringVar()
        datasel.set('')
        data = ttk.Combobox(mainframe, textvariable=datasel)
        available= list([''] + os.listdir('C:/Users/ishan7/Desktop/Final Project/Model'))
        data['values'] = available
        data.grid(column=1, row=5, sticky=W)

        #Entry option created
        var=StringVar()
        var.set('')
        e=Entry(mainframe, textvariable=var)
        e.grid(column=2, row=5, sticky=W)

        #Listbox for showing choosen classes integrated with scroll bar
        Label(mainframe, text = 'Classes Selected').grid(column=1, row=6, sticky = (N,E))
        sbar = Scrollbar(mainframe,orient=VERTICAL)
        viewlist=Listbox(mainframe, height = 3)
        sbar.config(command = viewlist.yview)
        viewlist.config(yscrollcommand = sbar.set)
        viewlist.grid(row=6, column=2, sticky=N+E+S+W)
        sbar.grid(column=3,row=6, sticky=N+S)

        def call_training():
            ''' Call Progressbar main function '''
            global classes
            import progressbar
            progressbar.Main(classes)
            

        def select():
            '''
            Define and validate the classes selected or new classes choosen
            '''
            global count
            global classes
            cls= None
            #values of classes retrieved
            drop=datasel.get()
            ent=var.get()
            if drop == '' and ent != '':
                cls = ent
            elif ent == '' and drop != '':
                cls = drop
            else:
                messagebox.showwarning('WARNING','Invalid Use')
                return
            if cls in classes:
                messagebox.showwarning('WARNING','Class Already Exist')
                return
            #values of classes chooses is appended
            classes.append(cls)
            viewlist.insert(count, cls)
            #for removing the classes selected from the given list
            if cls in data['values']:
                available.remove(cls)
                data['values'] = available
            #To remove the widgets after no. of classes are selected
            datasel.set('')
            var.set('')
            if count == int(num.get()):
                l.grid_forget()
                data.grid_forget()
                e.grid_forget()
                button.grid_forget()
                train = ttk.Button(mainframe, text="TRAIN", command= call_training)
                train.grid(column=2, row=7, sticky=W)
            count += 1
            l['text']='Select or Enter Class' + str(count)
            print(classes)
        
        
        #calls the select function
        button=Button(mainframe, text="SET", command=select)
        button.grid(column=3, row=5, sticky=W)

    #for creating new pop-up window
    root = Toplevel()
    root.title('Project')
    mainframe = ttk.Frame(root, padding="5 5 5 5", borderwidth="5", relief="raised", width="500", height="400")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    #to create a classifier and enter number of classes
    ttk.Label(mainframe, text="Create name of classifier :").grid(column=1, row=1, sticky=W)
    name=StringVar()
    ttk.Entry(mainframe, textvariable=name, width=10).grid(column=2, row=1, sticky=W)
    ttk.Label(mainframe, text="Enter no. of classes to classify :").grid(column=1, row=2, sticky=W)
    num = StringVar()
    no = ttk.Entry(mainframe, width=7, textvariable=num)
    no.grid(column=2, row=2, sticky=E)
    ttk.Button(mainframe, text="DONE",command=widget).grid(column=2, row=3, sticky=E) 
        
        
        
    for child in mainframe.winfo_children(): child.grid_configure(padx=8,pady=5)
    root.mainloop()




def select1():
    '''
    Validate and use the value of entered Pre-Trained Model
    '''
    drop=datasel1.get()
    if drop == '':
        messagebox.showwarning('WARNING','No DataSet Selected')
    else:
        import dia
        data1=drop
        dia.caldia(data1)
        

root = Tk()
root.title('Project')
mainframe = ttk.Frame(root, padding="5 5 5 5", borderwidth="5", relief="raised", width="500", height="400")
mainframe.grid(column=0, row=0, sticky=(N,E,W,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#create and input Pre-Trained Model
ttk.Label(mainframe, text="Select The Pre-Trained Model :").grid(column=1, row=1, sticky=W)
datasel1=StringVar()
datasel1.set('')
data = ttk.Combobox(mainframe, textvariable=datasel1,state='readonly')
data['values'] = os.listdir('C:/Users/ishan7/Desktop/Final Project/Model')
data.grid(column=2, row=1, sticky=W)
button1 = ttk.Button(mainframe, text="SELECT", command=select1)
button1.grid(column=2, row=2, sticky=W)

ttk.Label(mainframe, text="Nothing of Interest ?").grid(column=1, row=3, sticky=W)
#Button to call Next_window function
ttk.Label(mainframe, text="Create Your Custom Model :").grid(column=1, row=4, sticky=W)
button2 = ttk.Button(mainframe, text="CREATE", command=next_window)
button2.grid(column=2, row=4, sticky=W)

        
        
        
for child in mainframe.winfo_children(): child.grid_configure(padx=8,pady=5)
root.mainloop()
