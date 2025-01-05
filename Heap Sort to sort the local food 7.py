import tkinter as tk
from tkinter import ttk, messagebox

# Vendor Heap class definition (must be defined before VendorDirectoryApp)
class VendorHeap:
    def __init__(self):
        self.vendors = []

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.vendors[left].review_score > self.vendors[largest].review_score:
            largest = left
        if right < n and self.vendors[right].review_score > self.vendors[largest].review_score:
            largest = right

        if largest != i:
            self.vendors[i], self.vendors[largest] = self.vendors[largest], self.vendors[i]
            self.heapify(n, largest)

    def build_heap(self):
        n = len(self.vendors)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

    def heap_sort(self):
        n = len(self.vendors)
        self.build_heap()

        for i in range(n - 1, 0, -1):
            self.vendors[i], self.vendors[0] = self.vendors[0], self.vendors[i]
            self.heapify(i, 0)


# Vendor class definition
class Vendor:
    def __init__(self, vendor_id, name, review_score, category):
        self.vendor_id = vendor_id
        self.name = name
        self.review_score = review_score
        self.category = category

    def __repr__(self):
        return f"{self.name} - {self.review_score} - {self.category}"


# Vendor Directory App class definition
class VendorDirectoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Local Food Vendor Directory")
        self.root.config(bg="#3b5998")  # Set background color to match

        # Set window to fullscreen by default
        self.root.attributes('-fullscreen', True)

        # Vendor heap
        self.vendor_heap = VendorHeap()

        # Treeview to display vendors
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Review", "Category"), show="headings")
        self.tree.pack(fill="both", expand=True, padx=20, pady=20)

        # Define columns
        self.tree.heading("ID", text="Vendor ID")
        self.tree.heading("Name", text="Vendor Name")
        self.tree.heading("Review", text="Review Score")
        self.tree.heading("Category", text="Category")

        self.tree.column("ID", width=100, anchor="center")
        self.tree.column("Name", width=200, anchor="center")
        self.tree.column("Review", width=100, anchor="center")
        self.tree.column("Category", width=150, anchor="center")

        # Vendor input frame
        self.input_frame = tk.Frame(self.root, bg="#3b5998")
        self.input_frame.pack(pady=10)

        # Vendor ID
        self.vendor_id_label = tk.Label(self.input_frame, text="Vendor ID:", font=("Calibri Light", 12), bg="#3b5998", fg="white")
        self.vendor_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.vendor_id_entry = tk.Entry(self.input_frame, font=("Calibri Light", 12), width=20)
        self.vendor_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Vendor Name
        self.vendor_name_label = tk.Label(self.input_frame, text="Vendor Name:", font=("Calibri Light", 12), bg="#3b5998", fg="white")
        self.vendor_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.vendor_name_entry = tk.Entry(self.input_frame, font=("Calibri Light", 12), width=20)
        self.vendor_name_entry.grid(row=1, column=1, padx=10, pady=5)

        # Review Score
        self.review_label = tk.Label(self.input_frame, text="Review Score (1-5):", font=("Calibri Light", 12), bg="#3b5998", fg="white")
        self.review_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.review_entry = tk.Entry(self.input_frame, font=("Calibri Light", 12), width=20)
        self.review_entry.grid(row=2, column=1, padx=10, pady=5)

        # Category (Combobox)
        self.category_label = tk.Label(self.input_frame, text="Category:", font=("Calibri Light", 12), bg="#3b5998", fg="white")
        self.category_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        # Predefined categories for the combobox
        categories = ["Food", "Beverages", "Desserts", "Snacks", "Groceries"]

        self.category_combobox = ttk.Combobox(self.input_frame, values=categories, font=("Calibri Light", 12), width=18)
        self.category_combobox.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Vendor", command=self.add_vendor, font=("Calibri Light", 12), bg="#4CAF50", fg="white", width=15)
        self.add_button.pack(pady=10)

        self.sort_button = tk.Button(self.root, text="Sort Vendors by Review", command=self.sort_vendors, font=("Calibri Light", 12), bg="#2196F3", fg="white", width=20)
        self.sort_button.pack(pady=10)

        # Close Button (top right)
        self.close_button = tk.Button(self.root, text="❌", command=self.close_app, font=("Arial", 14), bg="red", fg="white")
        self.close_button.place(relx=1.0, rely=0.0, anchor="ne")

        # Toggle Full Screen
        self.root.bind("<F11>", self.toggle_full_screen)
        self.root.bind("<Escape>", self.end_full_screen)

    def add_vendor(self):
        # Get input from entries
        vendor_id = self.vendor_id_entry.get()
        name = self.vendor_name_entry.get()
        try:
            review_score = int(self.review_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Review score must be a number!")
            return
        category = self.category_combobox.get()

        if not (vendor_id and name and category):
            messagebox.showerror("Input Error", "Please fill in all fields!")
            return

        if review_score < 1 or review_score > 5:
            messagebox.showerror("Input Error", "Review score must be between 1 and 5!")
            return

        # Create a new vendor object
        new_vendor = Vendor(vendor_id, name, review_score, category)
        self.vendor_heap.vendors.append(new_vendor)
        self.clear_entries()
        self.update_treeview()

    def sort_vendors(self):
        # Perform Heap Sort on vendors
        self.vendor_heap.heap_sort()
        self.update_treeview()

    def update_treeview(self):
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert the sorted vendors into the treeview
        for vendor in self.vendor_heap.vendors:
            self.tree.insert("", "end", values=(vendor.vendor_id, vendor.name, vendor.review_score, vendor.category))

    def clear_entries(self):
        # Clear all input fields
        self.vendor_id_entry.delete(0, tk.END)
        self.vendor_name_entry.delete(0, tk.END)
        self.review_entry.delete(0, tk.END)
        self.category_combobox.set('')  # Clear the combobox

    def close_app(self):
        # Confirm close application
        if messagebox.askyesno("Exit", "Do you want to quit?"):
            self.root.quit()

    def toggle_full_screen(self, event=None):
        self.root.attributes('-fullscreen', True)

    def end_full_screen(self, event=None):
        self.root.attributes('-fullscreen', False)


if __name__ == "__main__":
    root = tk.Tk()
    app = VendorDirectoryApp(root)
    root.mainloop()
