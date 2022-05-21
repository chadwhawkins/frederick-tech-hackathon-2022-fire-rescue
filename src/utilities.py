import pathlib
from shutil import copyfile
import datetime
import pandas as pd


def create_backup(file_path: str) -> None:
    p = pathlib.Path(file_path)
    output_path = str(p).replace(p.name, "") + str(datetime.datetime.today().date()) + p.name
    copyfile(file_path, output_path)

def getShiftDataframe(dateTime):
    DateA = datetime.date(2022, 5, 20)
    diff = (DateA - dateTime).days % 3
    if diff == 0:
        return "A"
    if diff == 1:
        return "C"
    if diff == 2:
        return "B"

def write_updated_report(oldfile_path, newfile_path, df):
    create_backup(oldfile_path)
    df.to_excel(newfile_path)


