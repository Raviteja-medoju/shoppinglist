import tkinter as tk
from tkinter import messagebox

'''
tkinter is the standard Python library for creating graphical user interfaces (GUIs).

messagebox is a module in tkinter that allows us to display pop-up dialog boxes, like warnings and info messages.
'''


'''
This products class below defines products available in the store with their respective prices.

Each product name is a KEY, and its price is the value.

'''

products = { 
"Apple": 5,
  "Banana": 10, 
"Milk": 50, 
"Bread": 10,
  "Egg": 5, 
"Cheese": 20,
 "Book": 25,
  "Pen": 5,
  "Door mat": 80, 
"Exam pad": 75,
 "Jug": 40, 
"Water bottle": 25, 
"Dinner set": 250,
  "Sugar": 20, 
"Perfume": 100,
  "Chocolate": 10, 
"Cookies": 35, 
"Electric bulb": 100, 
"Toothpaste": 50, 
"Honey": 150, 
"Curtains": 250, 
"Tiffin box": 100,
  "Cool drink": 100, 
"Detergent powder": 50, 
} 



class SupermarketApp:
    def __init__(self, root): # The __init__ method is the constructor, called when an instance of SupermarketApp is created.

        self.root = root  #self.root is the root window of the application.
        
        self.root.title("Supermarket Bill Generator")  # the title shows on the top of the application
        
        self.cart = {}  #Initializes an empty dictionary to keep track of selected products and their quantities.
        
        self.create_widgets() #self.create_widgets() sets up the user interface by calling the create_widgets method.
        
        
        
        
    
    def create_widgets(self): # This method creates the GUI components
        tk.Label(self.root, text="Select Products:").grid(row=0, column=0, padx=15, pady=10)  #A label prompting users to select products is created and placed in the first row.
        
        self.product_vars = {} #This object stores IntVar instances (to track the checkbox state) and entry fields for each product.
        
        for i, product in enumerate(products.keys()): #A loop iterates through each product in the products dictionary
            
            var = tk.IntVar() #For each product, an IntVar variable is created to store its selection status (checked or not).
            
            self.product_vars[product] = (var, tk.Entry(self.root, width=5))
            
            tk.Checkbutton(self.root, text=product, variable=var).grid(row=i + 1, column=0, sticky='w')  #A Checkbutton is created to allow the user to select the product, tied to the IntVar variable.
            
            tk.Label(self.root, text="Quantity:").grid(row=i + 1, column=1)  #A Label and an Entry widget are added to accept the quantity for each selected product.
            self.product_vars[product][1].grid(row=i + 1, column=2)
        
        tk.Button(self.root, text="Generate Bill", command=self.generate_bill).grid(row=len(products) + 1, column=0, columnspan=3, pady=10) #a "Generate Bill" button is created, linked to the generate_bill method that calculates and displays the bill.
    
    def generate_bill(self):  #This method calculates the total bill based on selected products and quantities:
        
        self.cart.clear()  # clearing the cart clears any previous entries
        
        total = 0.0  # setting up the total to 0 before calling the function.
        
        for product, (var, entry) in self.product_vars.items(): #For each product, it checks if the checkbox (var.get() == 1) is selected.
            if var.get() == 1:
                try:
                    quantity = int(entry.get()) #If selected, it retrieves the quantity from the corresponding Entry widget.
                    if quantity > 0:
                        self.cart[product] = quantity #If the quantity is valid (positive integer), it adds the item and its quantity to self.cart and updates the total.
                        total += products[product] * quantity
                except ValueError:
                    messagebox.showwarning("Input Error", f"Invalid quantity for {product}. Please enter a number.")  #If an invalid quantity is entered, it shows a warning using messagebox.
        
        if self.cart:
            bill = "\n--- Bill ---\n"  # creatring a label.
            for item, quantity in self.cart.items():
                price = products[item] #If items are in self.cart, a formatted bill is created with each product, quantity, and total price.
                item_total = price * quantity
                bill += f"{item} x {quantity} @ ₹{price:.2f} = ₹{item_total:.2f}\n"  #The total cost is calculated and appended at the end.
            bill += f"Total: ₹{total:.2f}\n"
            messagebox.showinfo("Bill", bill)  #The bill is displayed using messagebox.showinfo.
        else:
            messagebox.showwarning("No Items", "Please select at least one product.")  #If no items are selected, it shows a warning.



'''
This block initializes the tkinter root window, creates an instance of SupermarketApp, 
and starts the GUI event loop with root.mainloop(), which waits for user interactions.
'''

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketApp(root)
    root.mainloop()