# generate_qr.py
import qrcode
import sys
import os

# The manual capacity table and find_smallest_qr_version function have been removed
# as we will let the qrcode library handle version detection automatically.

def create_qr_code_for_project(project_name):
    """
    Reads a data URI from a project's text file and generates the smallest
    possible QR code that can contain it.

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

        data_length = len(data_uri.encode('utf-8'))
        print(f"ℹ️ Data length: {data_length} bytes.")

        # --- START: CORRECTED LOGIC ---
        # 1. Let the library determine the best version by setting version=None.
        #    The library will automatically find the smallest QR code that fits the data.
        qr = qrcode.QRCode(
            version=None, # Let the library find the best version
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # 2. Add the data
        qr.add_data(data_uri)
        
        # 3. Compile the data into a QR code array.
        #    `fit=True` is the default, which tells the library to find the best version.
        qr.make(fit=True)
        
        # The `qr.version` attribute now holds the version that was automatically selected.
        determined_version = qr.version
        
        # Check if a version was found (it should unless data is impossibly large)
        if determined_version is None:
            print(f"❌ Error: Data is too long ({data_length} bytes) for any QR code version.")
            return
            
        print(f"ℹ️ Library selected Version {determined_version} as the smallest possible size.")
        # --- END: CORRECTED LOGIC ---

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to the output path
        img.save(output_image_name)

        print(f"✅ Successfully generated QR code (Version {determined_version}) and saved it as '{output_image_name}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
    except qrcode.exceptions.DataOverflowError as e:
        # This catch is now more specific and will trigger if the data is larger
        # than a Version 40 QR code can handle.
        print(f"❌ Error: Data is too long for any QR code version. {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_qr.py <project_name>")
        print("Example: python generate_qr.py lights_out")
    else:
        project = sys.argv[1]
        create_qr_code_for_project(project)