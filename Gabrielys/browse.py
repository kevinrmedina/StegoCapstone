import tkinter as tk
from tkinter import filedialog as fd


class Browse(tk.Frame):
    # Creates a frame that contains a button when clicked lets the user to select
    # a file and put its filepath into an entry.

    def __init__(self, master, initialdir='', filetypes=()):
        super().__init__(master)
        self.filepath = tk.StringVar()
        self._initaldir = initialdir
        self._filetypes = filetypes
        self._create_widgets()
        self._display_widgets()

    def _create_widgets(self):
        self._entry = tk.Entry(self, textvariable=self.filepath)
        self._button = tk.Button(self, text="Browse...", command=self.browse)

    def _display_widgets(self):
        self._entry.pack(fill='x', expand=True)
        self._button.pack(anchor='se')

    def browse(self):
      # Browses a .png file or all files and then puts it on the entry.
       
        self.filepath.set(fd.askopenfilename(initialdir=self._initaldir,
                                             filetypes=self._filetypes))


if __name__ == '__main__':
    root = tk.Tk()

    file_browser = Browse(root, initialdir=r"C:\Users",
                                filetypes=(('Portable Network Graphics','*.png'),
                                           ("All files", "*.*")))
    file_browser.pack(fill='x', expand=True)

    root.mainloop()

# " https://codereview.stackexchange.com/questions/184589/basic-file-browse "
