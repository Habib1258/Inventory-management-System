import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def update_total_price():
    total_price = sum(float(item[3].replace('$', '')) for item in data)  
    total_price_label.config(text=f"Total : ${total_price:.2f}")



def delete_selected_item():
    selected_item = tree.selection()  # Get selected item
    if selected_item:
        for item in selected_item:
            tree.delete(item)  # Remove the selected item
            for i, data_item in enumerate(data):
                if tree.item(item, "values") == data_item:
                    data.pop(i)
                    break
        update_total_price()


def edit_selected_item():
    selected_item = tree.selection()
    if not selected_item:
        return

    item = selected_item[0]
    current_values = tree.item(item, "values")

    def save_changes():
        new_id = id_entry.get()
        new_name = name_entry.get()
        new_quantity = quantity_entry.get()
        new_price = price_entry.get()

        new_values = (new_id, new_name, new_quantity, new_price)
        tree.item(item, values=new_values)

        for i, data_item in enumerate(data):
            if data_item[0] == current_values[0]:
                data[i] = new_values
                break

        update_total_price()
        edit_window.destroy()

    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Item")

    tk.Label(edit_window, text="ID:").grid(row=0, column=0)
    id_entry = tk.Entry(edit_window)
    id_entry.grid(row=0, column=1)
    id_entry.insert(0, current_values[0])

    tk.Label(edit_window, text="Product Name:").grid(row=1, column=0)
    name_entry = tk.Entry(edit_window)
    name_entry.grid(row=1, column=1)
    name_entry.insert(0, current_values[1])

    tk.Label(edit_window, text="Quantity:").grid(row=2, column=0)
    quantity_entry = tk.Entry(edit_window)
    quantity_entry.grid(row=2, column=1)
    quantity_entry.insert(0, current_values[2])

    tk.Label(edit_window, text="Price:").grid(row=3, column=0)
    price_entry = tk.Entry(edit_window)
    price_entry.grid(row=3, column=1)
    price_entry.insert(0, current_values[3])

    save_button = tk.Button(edit_window, text="Save", command=save_changes)
    save_button.grid(row=4, column=0, columnspan=2)


def exit_app():
    root.destroy()


root = tk.Tk()
root.geometry("1533x1000")
root.title("Inventory GUI")

style = ttk.Style()
style.configure("Treeview", rowheight=25) 
style.configure("Treeview.Heading", font=('Times New Roman', 18))  # Font size for headers
style.configure("Treeview", font=('Times New Roman', 16))
root.tk.call("source", "C:/Users/Habib/Downloads/Azure-ttk-theme-main/Azure-ttk-theme-main/azure.tcl")
root.tk.call("set_theme", "Dark")


image = Image.open("C:/Users/Habib/Desktop/Nouveau dossier/projects/Apps/inventory manager/assets/logop.png")


photo = ImageTk.PhotoImage(image)

img_label = tk.Label(root, image=photo)
img_label.pack()
img_label.place(x=50,y=0)

label = tk.Label(root, text="Youcef pepiniere", font=('Times New Roman', 28))
label.pack(padx=20, pady=70)

label = tk.Label(root, text="N Facture :", font=('Times New Roman', 28))
label.pack()
label.place(x=700,y=170)

facture_entry = tk.Entry(root, font=('Times New Roman', 18))
facture_entry.pack(side=tk.LEFT, padx=10)
facture_entry.place(x=900,y=183)


search_entry = tk.Entry(root, font=('Times New Roman', 18))
search_entry.pack(side=tk.LEFT, padx=10, pady=10)
search_entry.place(x=320,y=183)

search_button = tk.Button(root, text="Search", font=('Times New Roman', 14))
search_button.pack(side=tk.LEFT)
search_button.place(x=570,y=183)

tree = ttk.Treeview(root, height=10)
tree["columns"] = ("Matricule", "Product Name", "Qte", "Price")

tree.column("#0", width=0, stretch=tk.NO)  # Hide the default first column
tree.column("Matricule", anchor=tk.W, width=200)
tree.column("Product Name", anchor=tk.W, width=540)
tree.column("Qte", anchor=tk.CENTER, width=300)
tree.column("Price", anchor=tk.CENTER, width=280)

tree.heading("#0", text="", anchor=tk.W)
tree.heading("Matricule", text="Matricule", anchor=tk.W)
tree.heading("Product Name", text="Product Name", anchor=tk.W)
tree.heading("Qte", text="Quantity", anchor=tk.CENTER)
tree.heading("Price", text="Price", anchor=tk.CENTER)

# Add sample data
data = [
    ("1", "Item A", "10", "$5.99"),
    ("2", "Item B", "20", "$3.49"),
    ("3", "Item C", "15", "$7.29"),
    ("4", "Item D", "5", "$9.99")
]

for item in data:
    tree.insert("", tk.END, values=item)

total_price_label = tk.Label(root, text="Total : $0.00", font=('Times New Roman', 28))
total_price_label.pack(pady=0)
total_price_label.place(x=1180,y=170)



tree.pack(padx=0,pady=20)
tree.place(x=50,y=230)

# Add buttons
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="OK", font=("Times New Roman", 16), height=1, width=10)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text="Add", font=("Times New Roman", 16), height=1, width=10, command=update_total_price)
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text="Delete", font=("Times New Roman", 16), height=1, width=10,command=delete_selected_item)
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonframe, text="Edit", font=("Times New Roman", 16), height=1, width=10, command=edit_selected_item)
btn4.grid(row=0, column=3, sticky=tk.W+tk.E)

buttonframe.pack(fill='x', pady=20)
buttonframe.place(x=800,y=540)

buttonframe1 = tk.Frame(root)
buttonframe1.columnconfigure(0, weight=1)

btn5 = tk.Button(buttonframe1, text='New', font=("Times New Roman", 16), height=3, width=10)
btn5.grid(row=0, column=0, sticky=tk.E+tk.S, pady=10)
btn6 = tk.Button(buttonframe1, text='Inventory', font=("Times New Roman", 16), height=3, width=10)
btn6.grid(row=1, column=0, sticky=tk.E+tk.S, pady=10)
btn7 = tk.Button(buttonframe1, text='Log out', font=("Times New Roman", 16), height=3, width=10, command=exit_app)
btn7.grid(row=2, column=0, sticky=tk.E+tk.S, pady=10)

buttonframe1.pack(fill='y', padx=20)
buttonframe1.place(x=1400, y=250)



root.mainloop()
