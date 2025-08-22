# generate_project_qrs.py
import qrcode
import os
import sys

def create_qr_codes_for_project(project_name):
    """
    Reads a URL from a project-specific file and generates two QR codes:
    1. The smallest possible version (lowest reliability).
    2. The most reliable version (highest reliability).

    Args:
        project_name (str): The name of the project folder.
    """
    print(f"--- Generating QR Codes for Project: {project_name} ---")

    # Construct paths based on the provided project_name
    input_file_path = os.path.join(project_name, 'url', 'url_github.txt')
    output_dir = os.path.join(project_name, 'img')
    
    # Define output paths for both QR codes
    output_smallest_path = os.path.join(output_dir, 'qr_smallest.png')
    output_reliable_path = os.path.join(output_dir, 'qr_reliable.png')

    try:
        # --- 1. Setup and Read URL ---
        
        # Ensure the project's output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Read the URL from the specified file
        with open(input_file_path, 'r') as file:
            url = file.read().strip()

        if not url:
            print(f"❌ Error: The file '{input_file_path}' is empty.")
            return

        print(f"ℹ️ Read URL from file: {url}")
        print("-" * 30)

        # --- 2. Generate Smallest QR Code (Low Reliability) ---
        print("⚙️ Generating smallest QR code (Error Level L)...")
        
        qr_small = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_small.add_data(url)
        qr_small.make(fit=True)
        
        version_small = qr_small.version
        img_small = qr_small.make_image(fill_color="black", back_color="white")
        img_small.save(output_smallest_path)

        print(f"✅ Saved smallest QR code (Version {version_small}) to '{output_smallest_path}'")
        print("-" * 30)
        
        # --- 3. Generate Most Reliable QR Code (High Reliability) ---
        print("⚙️ Generating most reliable QR code (Error Level H)...")
        
        qr_reliable = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr_reliable.add_data(url)
        qr_reliable.make(fit=True)
        
        version_reliable = qr_reliable.version
        img_reliable = qr_reliable.make_image(fill_color="black", back_color="white")
        img_reliable.save(output_reliable_path)

        print(f"✅ Saved most reliable QR code (Version {version_reliable}) to '{output_reliable_path}'")

    except FileNotFoundError:
        print(f"❌ Error: The input file '{input_file_path}' was not found.")
        print(f"Please ensure the directory '{project_name}/url/' exists and contains 'url_github.txt'.")
    except qrcode.exceptions.DataOverflowError as e:
        print(f"❌ Error: The URL is too long for any QR code version. {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Check if a command-line argument (project_name) was provided
    if len(sys.argv) != 2:
        print("Usage: python generate_project_qrs.py <project_name>")
        print("Example: python generate_project_qrs.py qr_games")
    else:
        project_name_from_cli = sys.argv[1]
        create_qr_codes_for_project(project_name_from_cli)