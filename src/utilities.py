import pathlib
from shutil import copyfile
import datetime

def create_backup(file_path: str) -> None:
    p = pathlib.Path(file_path)
    output_path = str(p).replace(p.name, "") + str(datetime.datetime.today().date()) + p.name
    copyfile(file_path, output_path)

