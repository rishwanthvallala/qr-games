# decode.py
import base64
import sys

def decode_from_file(input_filename, output_filename):
    """Reads a data URL from a file, decodes it, and saves it as HTML."""
    try:
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
    if len(sys.argv) != 3:
        print("Usage: python decode.py <input_file_with_url> <output_html_file>")
        print("Example: python decode.py game_url.txt decoded_game.html")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        decode_from_file(input_file, output_file)