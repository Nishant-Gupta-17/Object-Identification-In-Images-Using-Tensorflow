import tkinter
from tkinter import ttk
import time
import threading
import classifier
 
def task(root1):
    '''
    Define your Progress Bar function,
    '''
    ft = ttk.Frame(root1,padding="5 5 5 5", borderwidth="5", relief="raised", width="500", height="400")
    ft.grid(column=0, row=0)
    ft.columnconfigure(0, weight=1)
    ft.rowconfigure(0, weight=1)
    ft.title("Progres")
    pb_hD = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')
    pb_hD.grid(column=1,row=1)
    pb_hD.start(25)
    root1.mainloop()


def process_of_unknown_duration(root1,classes):
    '''
    # Define the process of unknown duration with root1 as one of the input And once done, add root1.quit() at the end.
    '''
    classifier.cal(classes)
    print ('Done')
    root1.destroy()



def Main(classes):
    '''
    # Now define our Main Functions, which will first define root1, then call for call for "task(root1)" --- that's your progressbar, and then call for thread1 simultaneously which will  execute your process_of_unknown_duration and at the end destroy/quit the root1.
    '''
    root1 = tkinter.Tk()
    t1=threading.Thread(target=process_of_unknown_duration, args=(root1,classes))
    t1.start()
    task(root1)  # This will block while the mainloop runs
    t1.join()

#Now just run the functions by calling our Main() function,
if __name__ == '__main__':
    Main()
