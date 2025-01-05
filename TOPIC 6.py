import tkinter as tk
from tkinter import ttk, messagebox


# Vendor Directory using a Doubly Linked List
class VendorDirectory:
    def __init__(self):
        self.vendors = []

    def add_vendor(self, vendor_id, vendor_name, vendor_review, category):
        vendor_data = f"ID: {vendor_id}, Name: {vendor_name}, Category: {category}, Review: {vendor_review}"
        self.vendors.append(vendor_data)

    def get_all_vendors(self, category=None):
        if category:
            return [vendor for vendor in self.vendors if f"Category: {category}" in vendor]
        return self.vendors


# Main Application Class
class VendorApp:
    def __init__(self, root):
        self.vendor_directory = VendorDirectory()

        # GUI Setup
        self.root = root
        self.root.title("Food Vendor Directory")
        self.root.attributes("-fullscreen", True)  # Make the window full-screen
        self.root.config(bg="#3b5998")

        # Header
        self.header = tk.Label(self.root, text="Food Vendor Directory", font=("Calibri Light", 24), bg="#3b5998", fg="white")
        self.header.pack(fill="x", pady=10)

        # Vendor Information Input
        self.input_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.input_frame.pack(pady=10)

        self.name_label = tk.Label(self.input_frame, text="Vendor Name:", font=("Calibri Light", 14), bg="#f4f4f9")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.input_frame, font=("Calibri Light", 14), width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.review_label = tk.Label(self.input_frame, text="Review (1-5):", font=("Calibri Light", 14), bg="#f4f4f9")
        self.review_label.grid(row=1, column=0, padx=10, pady=5)
        self.review_entry = tk.Entry(self.input_frame, font=("Calibri Light", 14), width=30)
        self.review_entry.grid(row=1, column=1, padx=10, pady=5)

        self.category_label = tk.Label(self.input_frame, text="Category:", font=("Calibri Light", 14), bg="#f4f4f9")
        self.category_label.grid(row=2, column=0, padx=10, pady=5)
        self.category_var = tk.StringVar()
        self.category_menu = ttk.Combobox(self.input_frame, textvariable=self.category_var, font=("Calibri Light", 14), state="readonly", width=28)
        self.category_menu['values'] = ("Select Category", "Vegetarian", "Non-Vegetarian", "Vegan", "Desserts")
        self.category_menu.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        self.button_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Vendor", font=("Calibri Light", 14), command=self.add_vendor, bg="#4CAF50", fg="white", width=15)
        self.add_button.grid(row=0, column=0, padx=10, pady=5)

        self.display_button = tk.Button(self.button_frame, text="Display Vendors", font=("Calibri Light", 14), command=self.display_vendors, bg="#FF5722", fg="white", width=15)
        self.display_button.grid(row=0, column=1, padx=10, pady=5)

        self.exit_button = tk.Button(self.root, text="❌", font=("Arial", 14), command=self.confirm_exit, bg="#FF0000", fg="white", relief="flat", width=5)
        self.exit_button.place(x=self.root.winfo_screenwidth() - 50, y=5)  # Close button at top right

        # Treeview for displaying vendors in a hierarchical manner
        self.tree = ttk.Treeview(self.root, columns=("Vendor ID", "Vendor Name", "Review"), show="tree headings")
        self.tree.heading("Vendor ID", text="Vendor ID")
        self.tree.heading("Vendor Name", text="Vendor Name")
        self.tree.heading("Review", text="Review")
        self.tree.pack(pady=20, expand=True, fill="both")

    def add_vendor(self):
        vendor_name = self.name_entry.get().strip()
        vendor_review = self.review_entry.get().strip()
        category = self.category_var.get()

        # Check if inputs are valid
        if not vendor_name or not vendor_review or category == "Select Category":
            self.show_error("Please fill all fields correctly.")
            return

        if not vendor_review.isdigit() or not (1 <= int(vendor_review) <= 5):
            self.show_error("Review must be a number between 1 and 5.")
            return

        # Add vendor to the directory
        vendor_id = len(self.vendor_directory.vendors) + 1
        self.vendor_directory.add_vendor(vendor_id, vendor_name, vendor_review, category)

        self.name_entry.delete(0, tk.END)
        self.review_entry.delete(0, tk.END)
        self.category_var.set("Select Category")
        self.show_success("Vendor added successfully!")

    def display_vendors(self):
        # Get all vendors from the directory
        self.tree.delete(*self.tree.get_children())  # Clear previous entries
        category = self.category_var.get()

        vendors = self.vendor_directory.get_all_vendors(category if category != "Select Category" else None)
        created_categories = set()

        for vendor in vendors:
            vendor_data = vendor.split(", ")
            vendor_id = vendor_data[0].split(":")[1].strip()
            vendor_name = vendor_data[1].split(":")[1].strip()
            category = vendor_data[2].split(":")[1].strip()
            vendor_review = vendor_data[3].split(":")[1].strip()

            # Create category if not exists
            if category not in created_categories:
                category_node = self.tree.insert("", "end", text=category, values=("Category", "", ""))
                created_categories.add(category)

            # Insert vendor under category
            self.tree.insert(category_node, "end", text=vendor_name, values=(vendor_id, vendor_name, vendor_review))

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def show_success(self, message):
        messagebox.showinfo("Success", message)

    def confirm_exit(self):
        response = messagebox.askyesno("Quit", "Do you want to quit?")
        if response:
            self.root.quit()


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = VendorApp(root)
    root.mainloop()
