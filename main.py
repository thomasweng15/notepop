from tkinter import *

class scrollTxtArea:
    def __init__(self,root):
        frame=Frame(root)
        frame.pack()
        self.textPad(frame)
        return

    def textPad(self,frame):
        #add a frame and put a text area into it
        textPad=Frame(frame)
        self.text=Text(textPad,height=5,width=60)
        
        # add a vertical scroll bar to the text area
        scroll=Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)
        
        #pack everything
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT,fill=Y)
        textPad.pack(side=TOP)
        return

def main():
    root = Tk()
    foo =scrollTxtArea(root)
    root.title('Append Note')
    root.mainloop()
main()
