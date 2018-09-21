import json
import tkinter as tk
from os import system
from platform import system as platform

class fileIO:
    def __init__(self, config_fname='config.json'):
        self.config_fname = config_fname
        with open(self.config_fname, 'r') as f:
            self.config = json.loads(f.read())
        self.fname = self.config["note_file"].strip()
        self.prev_category = self.config["prev_category"].strip()

    def get_prev_category(self):
        return self.prev_category

    def update(self, category, text):
        category = "uncategorized" if category is None else category
        category_formatted = "# " + category + '\n'
        text_formatted = "* " + text + '\n'

        lines = None
        index = None
        with open(self.fname, "r") as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                if "# " + category + '\n' == line:
                    index = idx
            f.close()

        with open(self.fname, "w") as f:
            if index is not None and lines is not None:
                lines.insert(index + 1, text_formatted)

            f.writelines(lines)

            if index is None:
                f.write(category_formatted)
                f.write(text_formatted)

            f.close()

        with open(self.config_fname, "w") as f:
            self.config["prev_category"] = category
            json.dumps(self.config)

class noteGui:
    def __init__(self):
        self.root = tk.Tk()
        self.fileIO = fileIO()
        prev_category = self.fileIO.get_prev_category()
        self.scrollTxtArea = scrollTxtArea(self.root, prev_category)
        self.root.title('Note')
        self.root.bind('<Shift-Return>', lambda x: x)
        self.root.bind('<Return>', self.close)
        self.root.bind("<FocusIn>", self.handle_focus)

        if platform() == 'Darwin':  # How Mac OS X is identified by Python
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python" to true' ''')

    def handle_focus(self, evt):
        if evt.widget == self.root:
            self.root.focus_set()
            self.scrollTxtArea.setFocus()

    def close(self, evt=None):
        category, text = self.scrollTxtArea.getText()
        self.root.destroy()
        if text != None:
            self.fileIO.update(category, text)
    
    def run(self):
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.attributes("-topmost", False)
        self.root.focus_force()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.mainloop()

class scrollTxtArea:
    def __init__(self, root, prev_category):
        frame=tk.Frame(root)
        frame.pack()
        self.prev_category = prev_category
        self.textPad(frame)

    def textPad(self,frame):
        #add a frame and put a text area into it
        textPad=tk.Frame(frame)
        self.entry = tk.Entry(textPad)
        self.entry.insert(0, self.prev_category)
        self.text=tk.Text(textPad, height=3, width=40)
        
        #pack everything
        self.entry.pack(side=tk.TOP, fill='x')
        self.text.pack(side=tk.LEFT)
        textPad.pack(side=tk.TOP)

    def getText(self):
        category = self.entry.get().strip()
        text = self.text.get("1.0", tk.END).strip() 
        return (category, text) if text != "" else (None, None)

    def setFocus(self):
        self.text.focus_set()

if __name__ == '__main__':
    ng = noteGui()
    ng.run()
