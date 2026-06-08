import os
import zipfile
import sys

def compress_folder(folder_path, output_zip):
    """
    Compresses the content of a folder into a ZIP file.
    """
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        sys.exit(1)
        
    print(f"Compressing folder '{folder_path}' to '{output_zip}'...")
    
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Keeps the structure from the parent folder
                archive_name = os.path.relpath(file_path, os.path.dirname(folder_path))
                zipf.write(file_path, archive_name)
                
    print(f"Success : File '{output_zip}' created successfully.")

if __name__ == "__main__":
    # Default Configuration
    target_folder = "example_pack"
    output_filename = "example_pack.zip"
    
    # Still allowing command-line arguments to override defaults
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
    if len(sys.argv) > 2:
        output_filename = sys.argv[2]
        
    compress_folder(target_folder, output_filename)