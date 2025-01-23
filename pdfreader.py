import os
from PyPDF2 import PdfReader

def find_keyword_in_pdfs(directory, keyword):
    matching_files = []

    # Traverse through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):  # Check if the file is a PDF
            file_path = os.path.join(directory, filename)
            
            try:
                # Read the PDF file
                reader = PdfReader(file_path)
                for page in reader.pages:
                    text = page.extract_text()
                    if text and keyword.lower() in text.lower():  # Check for keyword (case-insensitive)
                        matching_files.append(filename)
                        break  # No need to search further in this file
            except Exception as e:
                print(f"Could not read {filename}: {e}")
    
    return matching_files

# Example usage
if __name__ == "__main__":
    directory_path = input("Enter the directory path: ").strip()
    keyword_to_search = input("Enter the keyword to search: ").strip()
    
    result_files = find_keyword_in_pdfs(directory_path, keyword_to_search)
    if result_files:
        print("PDF files containing the keyword:")
        for file in result_files:
            print(file)
    else:
        print("No PDF files found containing the keyword.")
