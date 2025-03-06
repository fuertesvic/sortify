import os
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import tkinter as tk
from tkinter import filedialog,ttk,messagebox
import time

def read_tag_from_image(path):
    """Checks the metadata (specifically, the 'tags' of an image in *path* and returns it as a string"""
    img = Image.open(path)
    try: return str(img.text['Tags'])
    except KeyError: return ' '

def add_tag_to_image(path,tag,people=None):
    """Creates a PNG metadata object for a image in *path*, appends a new 'Tag' and saves the image with updated metadata."""
    img = Image.open(path)      # Open image
    metadata = PngInfo()        # PNG metadata Object from PIL PngImagePlugin
    tags = []                   
    tags.extend(read_tag_from_image(path).split()) # Reads and formats the existing tags into a list
    ## This means that tags with spaces e.g. "my friends" will be split into two... so for now, all tags need to NOT have spaces, e.g. my_friends   

    tags.append(tag)                                    # Appends the new tag to insert into the list
    metadata.add_text("Tags",",".join(tags))            # Encodes the metadata into the image

    if people: metadata.add_text("people",people) 
    img.save(path,"PNG",pnginfo=metadata)               

def remove_tags_from_image(path,tags_to_remove=None):
    """Creates an empty metadata object file to overwrite the existing one, thus removing the tags from an image."""
    print(f"Remove Tags from image called with params {path} and {tags_to_remove}")
    if tags_to_remove:
        current_tags = read_tag_from_image(path[0]).split(',')
        [current_tags.remove(tag) for tag in tags_to_remove]
        img = Image.open(path[0])
        metadata = PngInfo()
        metadata.add_text("Tags",",".join(current_tags))
        img.save(path[0],"PNG",pnginfo=metadata)
       

    else:
        img = Image.open(path)
        metadata = PngInfo()
        img.save(path,'PNG',pnginfo=metadata)


def add_tag_to_multiple_images(paths,tags,people=None):
    """Adds a tag to the images selected and passed, and opens a message box informing the user of the changes made."""
    filenames = []
    for path in paths:
        add_tag_to_image(path,tags,people)
        filenames.append(os.path.basename(path))

    messagebox.showinfo(' ',f"S'ha afegit l'etiqueta '{tags}' a {len(filenames)} fitxer(s):\n\n{','.join(filenames)}")
    
def check_tags(metadata,tag):
    print(f"Tag: {tag} in Metadata: {metadata} Split: {metadata.split()}")
    print(tag in metadata.split())
    return tag in metadata.split(',')

def match_files_with_tag(folder_path,files,tag):
    """Receives a list of files with their respectives paths, and check if their metadata matches with a given tag.
    Stores and returns the files that match."""
    print("Match files with tag called!")

    paths = [f"{folder_path}/{file}" for file in files]
    matching = []

    for file in paths:
        
        metadata = read_tag_from_image(file)
        
        if check_tags(metadata,tag): 
            
            matching.append(os.path.basename(file))
    
    return matching

def print_initial_screen():
    wipe_screen()
    title = tk.Label(root, text = "Benvingut/da a sortiFy!", font=("Arial",20))
    subtitle = tk.Label(root, text = "Quina acció vol realitzar?", font =("Arial",16))
    button1 = tk.Button(root, text="Navegar una carpeta: consultar / afegir / eliminar etiquetes", command=option1, font=("Arial",16))
    button2 = tk.Button(root, text="Fer una cerca d'imatges que continguin una etiqueta concreta", command=option2, font=("Arial",16))

    title.place(x=200,y=20)
    subtitle.place(x=150,y=150)
    button1.place(x=80,y=200)
    button2.place(x=80,y=250)
    
def wipe_screen():
    # Destroy all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()

def option1():
    wipe_screen()
    folder_path = ask_folder()
    load_folder(folder_path)

def option2():
    wipe_screen()
    keyword = get_input_tag()
    folder_path = ask_folder()
    load_folder(folder_path,keyword)

def get_input_tag():
    """Opens a window for the user to input a tag, waits for the user to sumbit the input and then returns it"""

    def submit():
        """Stores the value that user has inputted and closes dialog window"""
        user_input.set(entry.get())  
        input_window.destroy() 

    input_window = tk.Toplevel(root) # Open Window
    input_window.geometry("200x100+500+300")

    user_input = tk.StringVar() # Sets tkinter varaible, allowing the execution to wait untill this variable is set.
    
    tk.Label(input_window,text="Introdueix etiqueta").pack() # Input window text
    entry = tk.Entry(input_window)                           
    entry.pack()
    
    tk.Button(input_window, text= 'OK', command=submit).pack() # Submit button

    root.wait_variable(user_input) # Wait untill there's an input
    
    return user_input.get()

def get_selected_files(file_list,folder_path):
    """Gets the tkinter Treeview (the list with all files, size, moddate, tags) and returns a list with the full paths of the images selected by the user"""
    files = []
    selected_files = file_list.selection()
    
    for item in selected_files:
        mydict = file_list.item(item)
        files.append(f"{folder_path}/{mydict['values'][0]}") 
    return files

def ask_folder():
    """Asks the user what folder to work on"""
    return filedialog.askdirectory(title="Seleccioni una carpeta") 
     
def add_tag(file_list,folder_path):
    """Adds a tag to the selected files. Then, returns to the folder Treeview visualization"""
    paths = get_selected_files(file_list,folder_path)
    user_input = get_input_tag()
    add_tag_to_multiple_images(paths,user_input)
    load_folder(folder_path)

def remove_tag_from_one_image(file_list,folder_path):
    print("hi")
    path = get_selected_files(file_list,folder_path)
    if len(path) > 1:
        error_window = tk.Toplevel(root)
        tk.Message(error_window,text="Error: Ha de seleccionar una única imatge!").pack()
        ok_btn = tk.Button(error_window,text="D'acord", command = lambda: load_folder(folder_path))
        ok_btn.pack()
        
    else:
        def show_selected():
            selected_tags = [item for item, var in zip(items, check_vars) if var.get()]
            remove_tags_from_image(path,selected_tags)
            load_folder(folder_path)
            
        tags = read_tag_from_image(path[0])
        new_window = tk.Toplevel(root)
        tk.Label(new_window, text = "Seleccioni les etiquetes a eliminar").pack()
        frame = tk.Frame(new_window)
        frame.pack()

        items = tags.split(',')
        check_vars = []

        for item in items:
            var = tk.BooleanVar()
            check_vars.append(var)
            chk = tk.Checkbutton(frame, text = item, variable = var)
            chk.pack()

        ok_btn = tk.Button(new_window, text="Ok", command=show_selected)
        ok_btn.pack(pady=5)

def remove_tag_from_all(file_list,folder_path):
    """Removes all tags from the selected files. Then, returns to the folder Treeview visualization"""

    def no_option():
        confirmation_window.destroy() 

    def yes_option():
        for path in paths:
            remove_tags_from_image(path)
        load_folder(folder_path)

    paths = get_selected_files(file_list,folder_path)
    confirmation_window = tk.Toplevel()
    tk.Label(confirmation_window,text="Està segur que vol fer-ho?").pack()
    tk.Button(confirmation_window,text='No',command=lambda:no_option()).pack(side='left')
    tk.Button(confirmation_window,text='Si',command=lambda:yes_option()).pack(side='right')
    
def load_folder(folder_path,search=None):
    wipe_screen()
    columns = ("File","Size", "ModTime", "Labels")
    file_list = ttk.Treeview(root,columns=columns,show="headings",selectmode="extended")    # Treeview object from TkInter to navigate the folder files
    
    # Back to main menu button
    backbutton = tk.Button(text="Torna al Menú principal",command=print_initial_screen)
    backbutton.pack(side='right')
    
    # GUI details for the TreeView
    file_list.heading("File", text="Fitxer")
    file_list.heading("Size", text="Mida (bytes)")
    file_list.heading("ModTime", text="Data de darrera modificació")
    file_list.heading("Labels", text="Etiquetes")
    if search: tk.Label(root,text=f"Resultats de la cerca per a la etiqueta: {search}").pack()
    file_list.column("File", width=200)
    file_list.column("Size", width=100)
    file_list.column("ModTime", width=150)
    file_list.column("Labels", width=100)

    file_list.pack(expand=True,fill="both")

    files = os.listdir(folder_path)
    if search: files = match_files_with_tag(folder_path,files,search)
   
    if files:
        # Prints list of files
        for file in files:
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):

                file_size = os.path.getsize(file_path)
                mod_time = os.path.getmtime(file_path)                                  # Get last modification time
                mod_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time)) # Format time
                
                labels = read_tag_from_image(file_path)    
        
                file_list.insert("","end", values=(file, file_size, mod_time, labels))
    
    # Option to select all
    def select_all():
        file_list.selection_set(file_list.get_children())  # Select all rows

    # Option to add tags 
    addtag_button = tk.Button(text="Afegeix etiqueta", command=lambda:add_tag(file_list,folder_path))
    addtag_button.pack()
    
    tk.Button(text = "Selecciona tots", command = select_all).pack(side='bottom')

    # Option to remove tags 
    removetag_button = tk.Button(text="Esborra totes les etiquetes d'imatges seleccionades", command=lambda:remove_tag_from_all(file_list,folder_path))
    removetag_button.pack(side = 'left')

    remove_single_tag_button = tk.Button(text="Esborra una o més etiquetes d'una sola imatge", command = lambda: remove_tag_from_one_image(file_list,folder_path))
    remove_single_tag_button.pack(side = 'left')
   
    
     
if __name__ == "__main__":
    root = tk.Tk()                      # Sets the main GUI window, with a name and Size
    root.title("SortiFy")
    root.geometry("1400x800")
    print_initial_screen()              # Print welcome screen with user options as buttons
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()                     
    