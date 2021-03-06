import shutil
from datetime import datetime
from pathlib import Path

oldFiles = Path('PATH')
target = Path('PATH')

#Gets the name of the current day and converts it to a string
day = datetime.now()
day = day.strftime('%A')

#Renames all the files as the original file name with the day appended to the front
for file in oldFiles.iterdir():

    #Check if the file is a file and not a folder
    if file.is_file():
        directory = file.parent
        extension = file.suffix
        old_name = file.stem

        #Creates string for new file name
        new_name = day + " " + old_name + extension

        #Gets current day in Year-Month-Date format and sets it to a string
        date = datetime.now()
        date = date.strftime('%Y-%m-%d')

        # 5) Check if the folder exists. If not, create it
        new_path = oldFiles.joinpath(date)
        if not new_path.exists():
            new_path.mkdir()
            
        #Moves the file
        new_file_path = new_path.joinpath(new_name)
        shutil.copy2(file, new_file_path)
        print("Successfully Renamed " + str(new_name) + " And Moved It To " + str(new_path))
        
    else:
        continue
