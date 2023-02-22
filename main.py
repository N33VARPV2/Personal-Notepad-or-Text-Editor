import tkinter as tk
from tkinter import filedialog

current_file = None

def new_file():
    global current_file
    text.delete("1.0", tk.END)
    current_file = None

def save_file():
    global current_file
    if not current_file:
        current_file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not current_file:
            return
    with open(current_file, "w") as f:
        f.write(text.get("1.0", tk.END))

def open_file():
    global current_file
    current_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not current_file:
        return
    text.delete("1.0", tk.END)
    with open(current_file, "r") as f:
        text.insert("1.0", f.read())

def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if text.selection_get():
            selected = text.selection_get()
            text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    if text.selection_get():
        selected = text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)

def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = text.index(tk.INSERT)
            text.insert(position, selected)

root = tk.Tk()
root.title("Notepad")

text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+X)")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+C)")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="(Ctrl+V)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=text.edit_undo, accelerator="(Ctrl+Z)")
edit_menu.add_command(label="Redo", command=text.edit_redo, accelerator="(Ctrl+Y)")

root.bind("<Control-Key-x>", cut_text)
root.bind("<Control-Key-c>", copy_text)
root.bind("<Control-Key-v>", paste_text)

root.mainloop()
