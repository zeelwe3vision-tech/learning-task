import os
import shutil

FILE_TYPES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Videos": ['.mp4', '.mkv', '.mov'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx'],
    "Audio": ['.mp3', '.wav'],}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                dest_folder = os.path.join(folder_path, category)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, dest_folder)
                moved = True
                break

        if not moved:
            try:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, other_folder)
            except Exception as e:
                print(f"Failed to move {file_path}: {e}")

    print("Files organized successfully!")

                         
if __name__ == "__main__":
    path = input("Enter folder path to organize: ")
    organize_files(path)