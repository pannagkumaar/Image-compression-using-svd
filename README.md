# Image-compression-using-svd
This is a Python application for image compression using Singular Value Decomposition (SVD). It allows users to select an image, specify a compression level using the k value, and save the compressed image. The application displays both the original and compressed images side by side. The compressed image is reconstructed using truncated SVD on the color channels of the original image. The application uses the Tkinter GUI toolkit and the Pillow library for image processing.



## Installation

Install Image-compression-using-svd with

```bash
  git clone https://github.com/pannagkumaar/Image-compression-using-svd
  cd Image-compression-using-svd
  pip install -r requirements.txt
  
```
    
## Usage

```javascript
python3 compress.py

```
* Click the "Browse" button to select an image to compress.  
* Enter the k value in the input field (recommended: 50-500).  
* Click the "Compress" button to compress the image.  
* Click the "Save Compressed Image" button to save the compressed image.  
* You can view the original image and the compressed image side by side in the application.  


## Features

- A graphical user interface (GUI) created using the Tkinter library.
- The ability to select an image to compress using a browse button.
- An entry for the user to input the value of k (the number of singular values to keep during compression).
- A compress button to initiate the image compression process.
- A save button to save the compressed image.
- The original image is displayed in one canvas and the compressed image is displayed in another canvas.
- Uses the numpy and PIL libraries to perform Singular Value Decomposition (SVD) on the image to compress it.
- Compresses each color channel of the image separately using SVD.
- Uses the truncated SVD matrices to reconstruct the compressed color channels and create the compressed image.
- Displays the compressed image in the GUI for the user to see.
- Supports images in various formats including JPEG, PNG, BMP, and GIF.
- Provides a recommended value range for k (50-500) to the user.
- Includes error handling for cases when the user tries to compress an image before selecting one.
- The code is organized into functions for better readability and maintainability.
- The GUI layout is responsive and scales with the size of the window.



