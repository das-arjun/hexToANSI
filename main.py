import sys


def hex_to_rgb(hex_str):
    """Converts a hex string to an (R, G, B) tuple."""
    hex_str = hex_str.lstrip('#')
    if len(hex_str) != 6:
        raise ValueError("Hex code must be 6 characters long (e.g., #FFFFFF).")
    return tuple(int(hex_str[i:i + 2], 16) for i in (0, 2, 4))


def convert():
    print("--- Hex/RGB to ANSI Converter ---")
    print("Supports: #FFFFFF or 255, 255, 255")
    user_input = input("Enter color: ").strip()

    try:
        # Determine if input is RGB or Hex
        if ',' in user_input:
            # Added a cleaner way to split and convert RGB
            r, g, b = [int(x.strip()) for x in user_input.split(',')]
        else:
            r, g, b = hex_to_rgb(user_input)

        # Validate RGB range
        if not all(0 <= c <= 255 for c in (r, g, b)):
            raise ValueError("RGB values must be between 0 and 255.")

        # Construct ANSI sequences
        fg_ansi = f"\\033[38;2;{r};{g};{b}m"
        bg_ansi = f"\\033[48;2;{r};{g};{b}m"

        print(f"\nResults for RGB({r}, {g}, {b}):")
        print(f"  Foreground Code: {fg_ansi}")
        print(f"  Background Code: {bg_ansi}")

        # Real-time preview
        preview_fg = fg_ansi.replace('\\033', '\033')
        preview_bg = bg_ansi.replace('\\033', '\033')
        reset_actual = '\033[0m'

        if user_input.lower() == "#faced0":
            print("PC: \"I faced 0!\"\nYou: \"Well, good for you!\"")
            """These easter eggs are funny right?"""
        elif user_input.lower() == "#deaf01":
            print("Sorry, could you speak a little louder?")
        elif user_input.lower() == "#bed021":
            print("Good night!")

        print(f"\nPreview: {preview_fg}Colored Text{reset_actual} | {preview_bg} Colored Background {reset_actual}")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    convert()
