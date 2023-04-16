import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

# Define the Tkinter application
class SVDCompressionApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("SVD Image Compression App")
        self.master.geometry("800x520")
        self.master.resizable(False, False)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    # Create the widgets for the application
    def create_widgets(self):
        # Create the label for the browse button
        self.browse_label = tk.Label(self, text="Select an image to compress:")
        self.browse_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Create the browse button for selecting the image
        self.browse_button = tk.Button(self, text="Browse", command=self.select_image)
        self.browse_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Create the label for the k value input
        self.k_label = tk.Label(self, text="Enter the k value (recommended: 50-500):")
        self.k_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Create the entry for the k value input
        self.k_entry = tk.Entry(self)
        self.k_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Create the compress button
        self.compress_button = tk.Button(self, text="Compress", command=self.compress_image)
        self.compress_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Create the save button
        self.save_button = tk.Button(self, text="Save Compressed Image", command=self.save_image)
        self.save_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        # Create the canvas for displaying the original image
        self.original_canvas = tk.Canvas(self, width=380, height=380, bg="white", highlightthickness=0)
        self.original_canvas.grid(row=3, column=0, padx=10, pady=10)

        # Create the canvas for displaying the compressed image
        self.compressed_canvas = tk.Canvas(self, width=380, height=380, bg="white", highlightthickness=0)
        self.compressed_canvas.grid(row=3, column=1, padx=10, pady=10)

        # Initialize the variables
        self.image_path = ""
        self.original_image = None
        self.compressed_image = None

    # Function to select the image
    def select_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.display_original_image()

    # Function to display the original image
    def display_original_image(self):
        self.original_image.thumbnail((300, 300))
        self.original_photo = ImageTk.PhotoImage(self.original_image)
        self.original_canvas.create_image(0, 0, anchor="nw", image=self.original_photo)

    # Function to compress the image using SVD
    def compress_image(self):
        if not self.original_image:
            return

        # Split the image into color channels
        r, g, b = self.original_image.split()

        # Convert each color channel to a grayscale numpy array
        r_array = np.array(r.convert("L"))
        g_array = np.array(g.convert("L"))
        b_array = np.array(b.convert("L"))

        # Get the k value from the entry
        k = int(self.k_entry.get())

        # Perform the SVD on each color channel numpy array
        U_r, S_r, V_r = np.linalg.svd(r_array)
        U_g, S_g, V_g = np.linalg.svd(g_array)
        U_b, S_b, V_b = np.linalg.svd(b_array)

        # Truncate the matrices using the k value
        U_k_r = U_r[:, :k]
        S_k_r = np.diag(S_r[:k])
        V_k_r = V_r[:k, :]

        U_k_g = U_g[:, :k]
        S_k_g = np.diag(S_g[:k])
        V_k_g = V_g[:k, :]

        U_k_b = U_b[:, :k]
        S_k_b = np.diag(S_b[:k])
        V_k_b = V_b[:k, :]

        # Reconstruct the compressed color channels
        r_compressed_array = U_k_r.dot(S_k_r).dot(V_k_r)
        r_compressed_array = np.clip(r_compressed_array, 0, 255).astype("uint8")

        g_compressed_array = U_k_g.dot(S_k_g).dot(V_k_g)
        g_compressed_array = np.clip(g_compressed_array, 0, 255).astype("uint8")

        b_compressed_array = U_k_b.dot(S_k_b).dot(V_k_b)
        b_compressed_array = np.clip(b_compressed_array, 0, 255).astype("uint8")

        # Reconstruct the compressed image with the same color channels
        compressed_array = np.stack((r_compressed_array, g_compressed_array, b_compressed_array), axis=-1)
        self.compressed_image = Image.fromarray(compressed_array)

        # Display the compressed image
        self.display_compressed_image()


    # Function to display the compressed image
    def display_compressed_image(self):
        self.compressed_image.thumbnail((300, 300))
        self.compressed_photo = ImageTk.PhotoImage(self.compressed_image)
        self.compressed_canvas.create_image(0, 0, anchor="nw", image=self.compressed_photo)
    
        

# Function to save the compressed image
    def save_image(self):
        if not self.compressed_image:
            return

        # Get the filename to save the image as
        filename = filedialog.asksaveasfilename(defaultextension=".jpg")

        # Save the image
        if filename:
            self.compressed_image.save(filename)

root = tk.Tk()
app = SVDCompressionApp(master=root)
app.mainloop()
