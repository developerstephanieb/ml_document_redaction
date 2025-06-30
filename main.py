import argparse
from redactor import redact_text

def main():
    """
    Main function to parse arguments and run the redaction process.
    """
    parser = argparse.ArgumentParser(
        description="Redact sensitive information from a text file."
    )
    parser.add_argument(
        "--input-file",
        type=str,
        required=True,
        help="Path to the input text file."
    )
    parser.add_argument(
        "--output-file",
        type=str,
        required=True,
        help="Path to save the redacted output file."
    )
    args = parser.parse_args()

    print(f"Reading from: {args.input_file}")

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            original_text = f.read()
    except FileNotFoundError:
        print(f"Error: Input file not found at {args.input_file}")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Perform the redaction
    redacted_content = redact_text(original_text)

    try:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(redacted_content)
        print(f"Successfully redacted text and saved to: {args.output_file}")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")


if __name__ == "__main__":
    main()
