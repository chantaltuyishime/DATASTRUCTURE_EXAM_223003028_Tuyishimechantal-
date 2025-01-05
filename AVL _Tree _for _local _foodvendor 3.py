import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import PIL for handling images

# Node class for both trees
class Node:
    def __init__(self, name, review):
        self.name = name
        self.review = review
        self.left = None
        self.right = None
        self.height = 1  # Required for AVL Tree

# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, name, review):
        if not root:
            return Node(name, review)
        elif name < root.name:
            root.left = self.insert(root.left, name, review)
        else:
            root.right = self.insert(root.right, name, review)
        return root

    def search(self, root, name):
        if not root or root.name == name:
            return root
        elif name < root.name:
            return self.search(root.left, name)
        return self.search(root.right, name)

    def inorder(self, root, result=[]):
        if root:
            self.inorder(root.left, result)
            result.append(f"{root.name}: {root.review}")
            self.inorder(root.right, result)
        return result

# AVL Tree class
class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, root):
        return root.height if root else 0

    def balance_factor(self, root):
        return self.height(root.left) - self.height(root.right) if root else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, root, name, review):
        if not root:
            return Node(name, review)
        elif name < root.name:
            root.left = self.insert(root.left, name, review)
        else:
            root.right = self.insert(root.right, name, review)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # Balance the tree
        balance = self.balance_factor(root)
        if balance > 1 and name < root.left.name:  # Left Left
            return self.rotate_right(root)
        if balance < -1 and name > root.right.name:  # Right Right
            return self.rotate_left(root)
        if balance > 1 and name > root.left.name:  # Left Right
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and name < root.right.name:  # Right Left
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, name):
        if not root or root.name == name:
            return root
        elif name < root.name:
            return self.search(root.left, name)
        return self.search(root.right, name)

    def inorder(self, root, result=[]):
        if root:
            self.inorder(root.left, result)
            result.append(f"{root.name}: {root.review}")
            self.inorder(root.right, result)
        return result


# GUI Application
class VendorApp:
    def __init__(self, root):
        self.binary_tree = BinaryTree()
        self.avl_tree = AVLTree()
        self.binary_tree.root = None
        self.avl_tree.root = None

        # GUI Elements
        self.root = root
        self.root.title("Food Vendor Directory")

        # Make the window full screen but allow space for the close button
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")

        # Set background color or image
        self.bg_color = "#f0f8ff"  # Set a light blue background color
        self.root.config(bg=self.bg_color)

        # Set a blank icon to remove the default Tkinter logo
        blank_icon = tk.PhotoImage(width=1, height=1)  # Create a blank (1x1) image
        root.iconphoto(True, blank_icon)

        # Add Close button in the top-left corner
        self.close_button = tk.Button(self.root, text="❌", font=("Arial", 16), command=self.close_window, bg="#FF6347", fg="white", bd=0, relief="flat")
        self.close_button.place(x=10, y=10)  # Position it in the top-left corner

        # Header
        self.header = tk.Label(root, text="Food Vendor Directory", font=("Arial", 20, "bold"), bg="#3b5998", fg="white")
        self.header.pack(fill="x", pady=10)

        # Input Fields Frame
        self.input_frame = tk.Frame(root, bg=self.bg_color)
        self.input_frame.pack(pady=10)

        self.name_label = tk.Label(self.input_frame, text="Vendor Name:", font=("Arial", 14), bg=self.bg_color)
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.input_frame, font=("Arial", 14), width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.review_label = tk.Label(self.input_frame, text="Review:", font=("Arial", 14), bg=self.bg_color)
        self.review_label.grid(row=1, column=0, padx=10, pady=5)
        self.review_entry = tk.Entry(self.input_frame, font=("Arial", 14), width=30)
        self.review_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg=self.bg_color)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Vendor", font=("Arial", 14), command=self.add_vendor, bg="#4CAF50", fg="white", width=15, relief="flat", bd=2)
        self.add_button.grid(row=0, column=0, padx=10, pady=5)

        self.search_button = tk.Button(self.button_frame, text="Search Vendor", font=("Arial", 14), command=self.search_vendor, bg="#008CBA", fg="white", width=15, relief="flat", bd=2)
        self.search_button.grid(row=0, column=1, padx=10, pady=5)

        self.display_button = tk.Button(self.button_frame, text="Display Vendors", font=("Arial", 14), command=self.display_vendors, bg="#FF5722", fg="white", width=15, relief="flat", bd=2)
        self.display_button.grid(row=0, column=2, padx=10, pady=5)

        # Output Area
        self.output_area = tk.Text(root, height=10, width=70, font=("Arial", 14), bg="#e6e6fa", fg="black", wrap=tk.WORD)
        self.output_area.pack(pady=20)

    def close_window(self):
        self.root.quit()  # Close the application

    def add_vendor(self):
        name = self.name_entry.get().strip()
        review = self.review_entry.get().strip()

        if not name or not review:
            self.show_error("Both fields are required!")
            return

        # Add vendor to both trees
        self.binary_tree.root = self.binary_tree.insert(self.binary_tree.root, name, review)
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, name, review)
        self.show_success(f"Vendor '{name}' added successfully!")
        self.name_entry.delete(0, tk.END)
        self.review_entry.delete(0, tk.END)

    def search_vendor(self):
        name = self.name_entry.get().strip()
        if not name:
            self.show_error("Vendor name is required!")
            return

        node_bt = self.binary_tree.search(self.binary_tree.root, name)
        node_avl = self.avl_tree.search(self.avl_tree.root, name)

        if node_bt:
            self.show_success(f"Found in Binary Tree: {node_bt.name} - {node_bt.review}")
        else:
            self.show_error("Vendor not found in Binary Tree.")

        if node_avl:
            self.show_success(f"Found in AVL Tree: {node_avl.name} - {node_avl.review}")
        else:
            self.show_error("Vendor not found in AVL Tree.")

    def display_vendors(self):
        self.output_area.delete("1.0", tk.END)
        bt_list = self.binary_tree.inorder(self.binary_tree.root, [])
        avl_list = self.avl_tree.inorder(self.avl_tree.root, [])

        self.output_area.insert(tk.END, "Binary Tree Vendors:\n")
        self.output_area.insert(tk.END, "\n".join(bt_list) + "\n\n")

        self.output_area.insert(tk.END, "AVL Tree Vendors:\n")
        self.output_area.insert(tk.END, "\n".join(avl_list))

    def show_error(self, message):
        self.create_popup("Error", message, "#FF6F6F", "#FF0000")

    def show_success(self, message):
        self.create_popup("Success", message, "#4CAF50", "#FFFFFF")

    def create_popup(self, title, message, bg_color, fg_color):
        # Create a Toplevel pop-up window
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("400x200")
        popup.config(bg=bg_color)

        label = tk.Label(popup, text=title, font=("Arial", 16, "bold"), fg=fg_color, bg=bg_color)
        label.pack(pady=10)

        message_label = tk.Label(popup, text=message, font=("Arial", 12), fg=fg_color, bg=bg_color)
        message_label.pack(pady=20)

        close_button = tk.Button(popup, text="Close", font=("Arial", 12), command=popup.destroy, bg="#FF5722", fg="white")
        close_button.pack(pady=10)

# Run the GUI Application
if __name__ == "__main__":
    root = tk.Tk()
    app = VendorApp(root)
    root.mainloop()
