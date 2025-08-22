# encode.py
import base64
import sys
import os

def encode_project(project_name):
    """
    Reads a project's main HTML file, encodes it into a data URL, and saves it to a file.
    """
    # By convention, we assume the main HTML file to encode is 'ind.html'
    input_filename = os.path.join(project_name, 'html', 'game.html')
    output_filename = os.path.join(project_name, 'url', 'url.txt')

    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Encode the HTML content to bytes, then to Base64
        html_bytes = html_content.encode('utf-8')
        encoded_bytes = base64.b64encode(html_bytes)
        encoded_string = encoded_bytes.decode('utf-8')

        # Create the full data URL
        prefix = "data:text/html;base64,"
        full_url = prefix + encoded_string
        
        # Ensure the output directory exists before writing the file
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)

        with open(output_filename, 'w') as f:
            f.write(full_url)

        print(f"✅ Successfully encoded '{input_filename}' to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python encode.py <project_name>")
        print("Example: python encode.py lights_out")
    else:
        project = sys.argv[1]
        encode_project(project)