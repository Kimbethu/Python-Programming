def read_and_write_file():
    # Ask the user for the input file name
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        # Process the content (e.g., add line numbers)
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]
        
        # Ask for the output file name
        output_filename = input("Enter the name of the file to write the modified content to: ")

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content successfully written to {output_filename}.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You cannot read/write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()