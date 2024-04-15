import os

# Указываем путь к вашей директории
directory = "/Users/engorgen/Documents/Dev/FirstPngBotP/Kurtki"

# Перебираем все папки в директории и переименовываем их
for i in range(1, 126):
    old_folder = os.path.join(directory, str(i))
    new_folder = os.path.join(directory, str(250 + i))
    if os.path.exists(old_folder):
        os.rename(old_folder, new_folder)
    else:
        print(f"Folder {old_folder} does not exist.")
