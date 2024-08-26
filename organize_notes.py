import os
import shutil

def organize_files():
    # Get the current directory where the script is located
    directory = os.path.dirname(os.path.abspath(__file__))
    
    # Define the prefixes and their corresponding subdirectories
    prefixes = {
        'HTB': '00 - notes\Course Notes\HTB',
        'THM': '00 - notes\Course Notes\THM',
        'OverTheWire': '00 - notes\Course Notes\OverTheWire'
        # Add more prefixes and subdirectories as needed
    }

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Skip if it's a directory
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        # Check if the filename starts with any of the defined prefixes
        for prefix, sub_dir in prefixes.items():
            if filename.startswith(prefix):
                # Ensure the subdirectory exists
                target_dir = os.path.join(directory, sub_dir)
                os.makedirs(target_dir, exist_ok=True)
                
                # Move the file to the corresponding subdirectory
                shutil.move(os.path.join(directory, filename), os.path.join(target_dir, filename))
                print(f"Moved: {filename} to {target_dir}")
                break  # Stop checking other prefixes for this file

if __name__ == "__main__":
    organize_files()
