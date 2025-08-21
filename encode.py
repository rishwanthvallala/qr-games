# encode.py
import base64
import sys

def encode_to_file(input_filename, output_filename):
    """Reads an HTML file, encodes it into a data URL, and saves it to a file."""
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

        with open(output_filename, 'w') as f:
            f.write(full_url)

        print(f"✅ Successfully encoded '{input_filename}' to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encode.py <input_html_file> <output_file_for_url>")
        print("Example: python encode.py my_game.html my_game_url.txt")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        encode_to_file(input_file, output_file)