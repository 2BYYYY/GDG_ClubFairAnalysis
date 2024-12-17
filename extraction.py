import os
import csv

def list_image_names(folder_path):
    # Only get the name because it has the data for the date and time
    # List of image extensions to check for
    image_extensions = ('.png')
    # List to store image filenames
    image_files = []

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith(image_extensions):
            image_files.append(filename)
    
    return image_files

def save_to_csv(image_names, csv_path):
    with open(csv_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header row
        csv_writer.writerow(['pictures'])
        # Write image names
        for name in image_names:
            csv_writer.writerow([name])

if __name__ == "__main__":
    folder_path = r'C:/Users/Windows 11/Pictures/Screenshots'  # Change to your folder path
    csv_path = r'C:/Users/Windows 11/Pictures/image_names.csv'  # Path where the CSV file will be saved
    
    image_names = list_image_names(folder_path)
    save_to_csv(image_names, csv_path)
    
    print(f"Image names have been saved to {csv_path}")
