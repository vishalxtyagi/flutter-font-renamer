import os

# Define the directory where your font files are located
font_directory = input("Enter the path to your font files: ") or "."

def convert_to_underscore_case(input_str):
    result = ""
    for char in input_str:
        if char.isupper():
            result += f"_{char.lower()}"
        else:
            result += char
    # Remove the leading underscore (if any)
    result = result.lstrip("_")
    return result

# Function to rename font files
def rename_font_files(font_directory):
    for filename in os.listdir(font_directory):
        if filename.endswith(".ttf") or filename.endswith(".otf"):
            font_name, file_ext = os.path.splitext(filename)

            # Split the font name into family and style
            name_parts = font_name.split("-")
            family_name = name_parts[0]

            # Handle the case where style is not in the file name
            if len(name_parts) == 1:
                style = "Regular"
            else:
                style = name_parts[1]

            style = convert_to_underscore_case(style)

            # Create the new file name using Flutter naming conventions
            new_filename = f"{family_name}_{style}{file_ext}".lower()

            # Rename the file
            old_path = os.path.join(font_directory, filename)
            new_path = os.path.join(font_directory, new_filename)
            os.rename(old_path, new_path)

            print(f"Renamed: {filename} -> {new_filename}")

# Call the function to rename font files
rename_font_files(font_directory)
