import os
import zipfile

def create_cbz_from_subfolders(base_directory):
    """遍历二级文件夹并创建 CBZ 文件."""
    for first_level_folder in os.listdir(base_directory):
        first_level_path = os.path.join(base_directory, first_level_folder)
        if os.path.isdir(first_level_path):
            for second_level_folder in os.listdir(first_level_path):
                second_level_path = os.path.join(first_level_path, second_level_folder)
                if os.path.isdir(second_level_path):
                    create_cbz_for_folder(second_level_path, first_level_path)

def create_cbz_for_folder(folder_path, output_directory):
    """将指定文件夹压缩为 CBZ 文件."""
    folder_name = os.path.basename(folder_path)
    zip_filename = os.path.join(output_directory, f"{folder_name}.zip")
    
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, relative_path)
    
    cbz_filename = zip_filename.replace('.zip', '.cbz')
    os.rename(zip_filename, cbz_filename)

if __name__ == "__main__":
    # 获取当前脚本所在的目录
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # 创建 CBZ 文件
    create_cbz_from_subfolders(BASE_DIR)
