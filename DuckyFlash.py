import os
import configparser
from ctypes import *
import time
import os
from distutils.dir_util import copy_tree





def main():
    format_drive('G:\\', 'NTFS', 'USBDrive')
    f = r'.\dist\DuckyTails.exe'
    size = os.path.getsize(f)
    date = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(f)))
    hour = time.strftime('%H:%M', time.gmtime(os.path.getmtime(f)))
    config = configparser.ConfigParser()
    config['Settings'] = {'ApplicationToStart': 'DUCKYTAILS.EXE'}
    config['Data'] = {
        'FS': size,
        'DA': date,
        'TI': hour
    }

    with open('.\dist\OpenFile\STARTAPP.INF', 'w') as configfile:
        config.write(configfile)

    fromDirectory = ".\dist"
    toDirectory = "G:\\"

    copy_tree(fromDirectory, toDirectory)

def myFmtCallback(command, modifier, arg):
    print(command)
    return 1    # TRUE


def format_drive(Drive, Format, Title):
    fm = windll.LoadLibrary('fmifs.dll')
    FMT_CB_FUNC = WINFUNCTYPE(c_int, c_int, c_int, c_void_p)
    FMIFS_UNKNOWN = 0
    fm.FormatEx(c_wchar_p(Drive), FMIFS_UNKNOWN, c_wchar_p(Format),
                c_wchar_p(Title), True, c_int(0), FMT_CB_FUNC(myFmtCallback))


if __name__ == "__main__":
    main()