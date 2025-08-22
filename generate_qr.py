# generate_qr.py
import qrcode
import base64
import sys
import os

def create_qr_code_for_project(project_name):
    """
    Reads a data URI from a project's text file and generates a QR code from its content.

    Args:
        project_name (str): The name of the project folder (e.g., "lights_out").
    """
    file_path = os.path.join(project_name, 'url', 'url.txt')
    output_image_name = os.path.join(project_name, 'img', 'qr_code.png')
    
    try:
        # Read the full data URI from the file
        with open(file_path, 'r') as file:
            data_uri = file.read().strip()

        # Check if the content is a valid data URI
        if not data_uri.startswith('data:text/html;base64,'):
            print(f"Error: The content of '{file_path}' does not appear to be a valid data URI.")
            return

        # Generate the QR code from the data URI
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data_uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to the root directory
        img.save(output_image_name)

        print(f"✅ Successfully generated QR code from '{file_path}' and saved it as '{output_image_name}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_qr.py <project_name>")
        print("Example: python generate_qr.py lights_out")
    else:
        project = sys.argv[1]
        create_qr_code_for_project(project)