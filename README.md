# **QR Code Generator**

This Python script generates a QR code that encodes a URL (Google in this case) and saves it as an image.

## Prerequisites

Ensure you have Python installed, and install the required libraries using:

pip install qrcode
pip install Pillow

## How It Works

The script:

Imports the required libraries (qrcode and PIL from Pillow).

### Creates a QRCode object with custom settings:

➡️version=1: Defines the QR code size.(smallest)

➡️error_correction=qrcode.constants.ERROR_CORRECT_H: Enables high error correction.
ERROR_CORRECT_H allows up to 30% of the QR code to be damaged or obscured while still being readable.
This is useful when:
The QR code will be printed on surfaces that might get scratched.
You plan to overlay a logo on the QR code.
The QR code is used in harsh environments (dirt, scratches, etc.).

➡️box_size=10: Sets the size of each QR box.

➡️border=4: Adds a border around the QR code.

Adds data (Google URL) to the QR code.

Generates the QR code.

Creates an image with custom colors (red fill and white background).

Saves the image as google_web.png.


## →After running the code:Output

The generated QR code image will be saved as google_web.png in the same directory.

Example Output

The script generates a QR code similar to this (when scanned, it redirects to Google):



Customization

Modify qr.add_data("https://www.google.com") to encode a different URL or text.

Change fill_color="red" and back_color="white" to customize colors.


### o/p:-
![QR Code](google_web.png)