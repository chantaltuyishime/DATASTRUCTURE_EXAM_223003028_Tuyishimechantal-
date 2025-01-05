import tkinter as tk
from tkinter import messagebox

class OrderNode:
    def __init__(self, vendor_name, review, order_id):
        self.vendor_name = vendor_name  # Vendor name (e.g., "Pizza Hut")
        self.review = review  # Review rating (e.g., 5)
        self.order_id = order_id  # Unique order ID
        self.next = None  # Reference to the next order (or None if it's the last one)

class VendorOrderApp:
    def __init__(self, root):
        self.head = None  # The start of the singly linked list
        self.order_counter = 101  # Start the order ID from 101

        # GUI setup
        self.root = root
        self.root.title("Food Vendor Order Directory")

        # Set window to full screen-like size without hiding window buttons
        self.root.geometry("1920x1080")  # Set to full HD size or screen resolution
        self.root.config(bg="#F0F0F0")  # Set background color
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Vendor Name Entry
        self.vendor_name_label = tk.Label(root, text="Vendor Name:", font=("Arial", 16, "bold"), bg="#F0F0F0")
        self.vendor_name_label.pack(pady=20)
        self.vendor_name_entry = tk.Entry(root, font=("Arial", 16), width=40, borderwidth=2)
        self.vendor_name_entry.pack(pady=10)

        # Review Entry
        self.review_label = tk.Label(root, text="Review (1-5):", font=("Arial", 16, "bold"), bg="#F0F0F0")
        self.review_label.pack(pady=20)
        self.review_entry = tk.Entry(root, font=("Arial", 16), width=40, borderwidth=2)
        self.review_entry.pack(pady=10)

        # Button to add a vendor order
        self.add_button = tk.Button(root, text="Add Order", command=self.add_order, font=("Arial", 18), bg="#4CAF50", fg="white", relief="flat", bd=2, width=20)
        self.add_button.pack(pady=30)

        # Text area to display orders
        self.output_area = tk.Text(root, height=15, width=60, font=("Arial", 14), bg="#e6e6fa", fg="black", wrap=tk.WORD)
        self.output_area.pack(pady=20)

    def add_order(self):
        vendor_name = self.vendor_name_entry.get().strip()
        review = self.review_entry.get().strip()

        if not vendor_name or not review:
            self.show_error("Both fields are required!")
            return

        # Validate the review input (should be between 1 and 5)
        if not review.isdigit() or not (1 <= int(review) <= 5):
            self.show_error("Review must be a number between 1 and 5!")
            return

        # Generate a unique order ID and increment the counter
        order_id = self.order_counter
        self.order_counter += 1  # Increment the counter for the next order

        # Create a new order node with the dynamic order ID
        new_order = OrderNode(vendor_name, review, order_id)

        # Add the new order to the linked list
        self.add_to_list(new_order)

        # Display success message
        self.show_success(f"Order for {vendor_name} added with ID {order_id}.")

        # Show reminder pop-up
        self.show_reminder(order_id)

        # Update the output area to display the list of all orders
        self.display_orders()

        # Clear input fields
        self.vendor_name_entry.delete(0, tk.END)
        self.review_entry.delete(0, tk.END)

    def add_to_list(self, new_order):
        if not self.head:
            self.head = new_order  # If the list is empty, set the new order as the head
        else:
            current = self.head
            while current.next:
                current = current.next  # Traverse to the last node
            current.next = new_order  # Add the new order at the end

    def display_orders(self):
        self.output_area.delete("1.0", tk.END)  # Clear previous content

        current = self.head
        orders_list = []
        while current:
            orders_list.append(f"ID: {current.order_id}, Vendor: {current.vendor_name}, Review: {current.review}")
            current = current.next

        # Display the orders in the text area
        self.output_area.insert(tk.END, "\n".join(orders_list))

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def show_success(self, message):
        messagebox.showinfo("Success", message)

    def show_reminder(self, order_id):
        reminder_msg = f"Keep your Order ID ({order_id}) safe for future reference!"
        # Custom styling for the reminder pop-up
        reminder_window = tk.Toplevel(self.root)
        reminder_window.title("Important Reminder")
        reminder_window.geometry("400x200")
        reminder_window.config(bg="#F4A300")

        label = tk.Label(reminder_window, text="Reminder", font=("Arial", 16, "bold"), fg="white", bg="#F4A300")
        label.pack(pady=10)

        message_label = tk.Label(reminder_window, text=reminder_msg, font=("Arial", 14), fg="white", bg="#F4A300")
        message_label.pack(pady=20)

        close_button = tk.Button(reminder_window, text="Close", font=("Arial", 14), command=reminder_window.destroy, bg="#4CAF50", fg="white")
        close_button.pack(pady=10)

    def on_close(self):
        self.root.quit()  # Quit the application

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    
    app = VendorOrderApp(root)
    root.mainloop()
