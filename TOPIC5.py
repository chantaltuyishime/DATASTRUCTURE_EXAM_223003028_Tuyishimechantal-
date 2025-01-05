import tkinter as tk
from tkinter import messagebox

# Node Class for Doubly Linked List
class Node:
    def __init__(self, name, review):
        self.name = name
        self.review = review
        self.next = None
        self.prev = None

# Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_vendor(self, name, review):
        new_node = Node(name, review)
        if not self.head:  # If list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_vendor(self, name):
        current = self.head
        while current:
            if current.name == name:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next

    def display_vendors(self):
        vendors = []
        current = self.head
        while current:
            vendors.append(f"Vendor: {current.name}, Review: {current.review}")
            current = current.next
        return vendors

    def traverse_backward(self):
        vendors = []
        current = self.tail
        while current:
            vendors.append(f"Vendor: {current.name}, Review: {current.review}")
            current = current.prev
        return vendors


# GUI Application Class
class VendorApp:
    def __init__(self, root):
        self.dll = DoublyLinkedList()  # Initialize the Doubly Linked List
        self.root = root
        self.root.title("Food Vendor Directory")
        
        # Fullscreen
        self.root.attributes("-fullscreen", True)

        # Set background color and font
        self.default_font = "Calibri Light"
        self.font_size = 14
        self.root.config(bg="#f4f4f9")

        # Header
        self.header = tk.Label(root, text="Food Vendor Directory", font=(self.default_font, 30, "bold"), bg="#4CAF50", fg="white")
        self.header.pack(fill="x", pady=20)

        # Input fields
        self.input_frame = tk.Frame(root, bg="#f4f4f9", pady=20)
        self.input_frame.pack(pady=20)

        self.name_label = tk.Label(self.input_frame, text="Vendor Name:", font=(self.default_font, self.font_size), bg="#f4f4f9")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.input_frame, font=(self.default_font, self.font_size), width=30, relief="flat", bd=2)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.review_label = tk.Label(self.input_frame, text="Review (1-5):", font=(self.default_font, self.font_size), bg="#f4f4f9")
        self.review_label.grid(row=1, column=0, padx=10, pady=10)
        self.review_entry = tk.Entry(self.input_frame, font=(self.default_font, self.font_size), width=30, relief="flat", bd=2)
        self.review_entry.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        self.button_frame = tk.Frame(root, bg="#f4f4f9", pady=20)
        self.button_frame.pack(pady=20)

        self.add_button = tk.Button(self.button_frame, text="Add Vendor", command=self.add_vendor, font=(self.default_font, self.font_size), relief="flat", bg="#4CAF50", fg="white", width=15)
        self.add_button.grid(row=0, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Vendor", command=self.delete_vendor, font=(self.default_font, self.font_size), relief="flat", bg="#FF5722", fg="white", width=15)
        self.delete_button.grid(row=0, column=1, padx=10, pady=10)

        self.display_button = tk.Button(self.button_frame, text="Display Vendors", command=self.display_vendors, font=(self.default_font, self.font_size), relief="flat", bg="#2196F3", fg="white", width=15)
        self.display_button.grid(row=0, column=2, padx=10, pady=10)

        # Output Area
        self.output_area = tk.Text(root, height=10, width=70, font=(self.default_font, self.font_size), wrap=tk.WORD, bg="#e6e6fa", fg="black", bd=2)
        self.output_area.pack(pady=20)

        # Close Button (Top-Right Corner) with Green Color
        self.close_button = tk.Button(root, text="❌", command=self.confirm_close, font=(self.default_font, 16), fg="white", bg="#4CAF50", relief="flat", bd=2)
        self.close_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)  # Place at the top-right corner

    def add_vendor(self):
        name = self.name_entry.get().strip()
        review = self.review_entry.get().strip()

        if not name or not review:
            messagebox.showerror("Error", "Both fields are required!")
            return

        try:
            review = int(review)
            if review < 1 or review > 5:
                messagebox.showerror("Error", "Review must be a number between 1 and 5!")
                return
        except ValueError:
            messagebox.showerror("Error", "Review must be a valid number!")
            return
        
        self.dll.add_vendor(name, review)
        messagebox.showinfo("Success", f"Vendor '{name}' added successfully!")
        
        self.name_entry.delete(0, tk.END)
        self.review_entry.delete(0, tk.END)

    def delete_vendor(self):
        name = self.name_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Vendor name is required to delete!")
            return

        self.dll.delete_vendor(name)
        messagebox.showinfo("Success", f"Vendor '{name}' deleted successfully!")

        self.name_entry.delete(0, tk.END)

    def display_vendors(self):
        self.output_area.delete("1.0", tk.END)
        
        vendors_forward = self.dll.display_vendors()
        vendors_backward = self.dll.traverse_backward()

        self.output_area.insert(tk.END, "Vendors (Forward Traversal):\n")
        self.output_area.insert(tk.END, "\n".join(vendors_forward) + "\n\n")
        
        self.output_area.insert(tk.END, "Vendors (Backward Traversal):\n")
        self.output_area.insert(tk.END, "\n".join(vendors_backward) + "\n")

    def confirm_close(self):
        # Ask user for confirmation to close the application
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.quit()  # Close the application


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = VendorApp(root)

    root.mainloop()
