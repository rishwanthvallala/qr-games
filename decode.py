# decode.py
import base64
import sys
import os

def decode_project(project_name):
    """
    Reads a data URL from a project's url file, decodes it, and saves it as an HTML file.
    """
    input_filename = os.path.join(project_name, 'url', 'url.txt')
    output_filename = os.path.join(project_name, 'html', f'decoded_{project_name}.html')

    try:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        
        with open(input_filename, 'r') as f:
            url_string = f.read().strip()

        prefix = "data:text/html;base64,"
        if not url_string.startswith(prefix):
            print(f"Error: The content of '{input_filename}' does not start with '{prefix}'.")
            return

        # Correctly extract the Base64 part of the string
        encoded_data = url_string.split(',', 1)[1]
        
        # Decode the data
        decoded_bytes = base64.b64decode(encoded_data)
        html_content = decoded_bytes.decode('utf-8')

        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✅ Successfully decoded '{input_filename}' to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decode.py <project_name>")
        print("Example: python decode.py lights_out")
    else:
        project = sys.argv[1]
        decode_project(project)