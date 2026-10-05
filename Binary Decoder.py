"""
Binary Encoder & Decoder CLI Tool
Author: Tashfiq Onbir 
GitHub: https://github.com/tashfiqonbir
Description: A simple Python script to encode text to binary and decode binary back to text.
"""

import sys

def text_to_binary(text):
    """Convert plain text to binary string."""
    try:
        return ' '.join(format(ord(char), '08b') for char in text)
    except Exception as e:
        return f"Error encoding text: {e}"

def binary_to_text(binary_string):
    """Convert binary string back to plain text."""
    try:
        # Remove any spaces if the user provided space-separated binary
        binary_values = binary_string.strip().split(' ')
        
        # If there are no spaces, try to split every 8 bits
        if len(binary_values) == 1 and len(binary_values[0]) > 8:
            binary_values = [binary_values[0][i:i+8] for i in range(0, len(binary_values[0]), 8)]
            
        text = "".join([chr(int(b, 2)) for b in binary_values if b])
        return text
    except ValueError:
        return "Invalid Binary Code! Please ensure it only contains 0s, 1s, and spaces."
    except Exception as e:
        return f"Error decoding binary: {e}"

def main():
    print("=" * 45)
    print("      BINARY ENCODER & DECODER TOOL      ")
    print("=" * 45)
    
    while True:
        print("\nChoose an option:")
        print("1. Encode Text to Binary")
        print("2. Decode Binary to Text")
        print("3. Exit")
        
        choice = input("\nEnter choice (1/2/3): ").strip()
        
        if choice == '1':
            text_input = input("\nEnter the text you want to encode:\n> ")
            binary_result = text_to_binary(text_input)
            print("\n[Encoded Binary Code]:")
            print(binary_result)
            print("-" * 45)
            
        elif choice == '2':
            binary_input = input("\nEnter the binary code you want to decode (spaces allowed):\n> ")
            text_result = binary_to_text(binary_input)
            print("\n[Decoded Plain Text]:")
            print(text_result)
            print("-" * 45)
            
        elif choice == '3':
            print("\nThank you for using the tool! Goodbye.")
            sys.exit()
            
        else:
            print("\nInvalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
