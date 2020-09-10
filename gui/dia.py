from tkinter import *
from tkinter import ttk
import os


def check():
    '''
    assign and validate for the "Done" button
    '''
    fo=pathfo.get()
    fi=pathfi.get()
    if fo == '' and fi !='':
        print(fi)
    elif fi == '' and fo !='':
        print(fo) 
    elif fi == '' and fo == '':
        messagebox.showwarning('WARNING','SELECT FILE/FOLDER')
        return
    else :
        messagebox.showwarning('WARNING','CAN SELECT ONLY ONE OPTION')
        return


def dialog_folder(var1):
    '''
    assign and validate for "BROWSE(Folder)" button
    '''
    feedbackfo = filedialog.askdirectory()
    if feedbackfo == '':
        return
    var1.set(feedbackfo)
    

def dialog_file(var2):
    '''
    assign and validate for "BROWSE(File)" button
    '''
    feedbackfi = filedialog.askopenfilename()
    if feedbackfi == '':
        return
    var2.set(feedbackfi)
def caldia(data1):
    ''' Receives Data from the Pre-Defined Data models and passes it to the Testing entry'''
    #defining of root and frame
    root = Tk()
    root.title("Testing")
    mainframe = ttk.Frame(root, padding="5 5 5 5", borderwidth="5", relief="raised", width="500", height="400")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    #Entry from the Folder Browse Button
    pathfo = StringVar()
    ttk.Label(mainframe, text="Select the Folder which Contains the Test Images :").grid(column=1, row=1, sticky=W)
    button1 = ttk.Button(mainframe, text="Browse", command=  lambda:dialog_folder(pathfo))
    button1.grid(column=2, row=1, sticky=W)
    entry1 = ttk.Entry(mainframe, width=100, textvariable= pathfo)
    entry1.grid(column=3, row=1, sticky=W)

    ttk.Label(mainframe, text="OR").grid(column=2, row=2, sticky=(W,E))

    #Entry from the File Browse Button
    pathfi = StringVar()
    ttk.Label(mainframe, text="Select the Image To Test :").grid(column=1, row=3, sticky=W)
    button2 = ttk.Button(mainframe, text="Browse", command= lambda:dialog_file(pathfi))
    button2.grid(column=2, row=3, sticky=W)
    entry2 = ttk.Entry(mainframe, width=100, textvariable= pathfi)
    entry2.grid(column=3, row=3, sticky=W)

    #Button for the final submission
    button3 = ttk.Button(mainframe, text="Done", command=check)
    button3.grid(column=1, row=4 ,sticky=W)

    #for padding among all the widgets
    for child in mainframe.winfo_children(): child.grid_configure(padx=8,pady=5)
    root.mainloop()
