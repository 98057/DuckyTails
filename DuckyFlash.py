import os
import configparser
from ctypes import *
import time
import os
from distutils.dir_util import copy_tree
from colorama import init, Fore, Back, Style
from argparse import ArgumentParser, RawTextHelpFormatter


def main(args):
    init()

    default_color = Fore.LIGHTRED_EX
    error_color = Fore.RED
    success_color = Fore.GREEN
    warning_color = Fore.YELLOW

    print(default_color)

    parser = ArgumentParser(prog='DuckyFlash', description='Ducky USB Flash copy the files in USB Drive to Autorun', formatter_class=RawTextHelpFormatter)
    parser.add_argument('drive', help='USB drive letter \nie: DuckyFlash E:')
    parser.add_argument('--format', action='store_true', help='Format the USB \nie: DuckyFlash E: --format')
    parser.add_argument('-e', '--exe', default='.\dist\DuckyTails.exe', help='Generate the STARTAPP.inf from executable \nie: DuckyFlash E: --exe ".\dist\DuckyTails.exe"')
    parser.add_argument('-f', '--from', default='.\dist', help='Copy from directory \nie: DuckFlash --from ".\dist"')
    args = parser.parse_args()
    if args.format:
        try:
            print(warning_color + '[.] Starting formating...')
            format_drive(args.drive, 'NTFS', 'USBDrive')
            print(success_color + '[+] Drive formated!')
        except:
            print(error_color + '[-]  Unexpected error:', sys.exc_info()[0])
            raise

    print(default_color)

    if os.path.exists(args.exe):
        try:
            print(warning_color + '[.] Generating STARTAPP.inf file from ' + args.exe + '...')
            f = args.exe
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
            print(success_color + '[+] STARTAPP.inf file generated from ' + args.exe + '!')
            print(default_color)
            print(warning_color + '[.] Saving STARTAPP.inf ...')
            with open('.\dist\OpenFile\STARTAPP.INF', 'w') as configfile:
                config.write(configfile)
            print(success_color + '[+] STARTAPP.inf saved!')
        except:
            print(error_color + '[-]  Unexpected error:', sys.exc_info()[0])
            raise
    else:
        print(error_color + '[-] File ' + args.exe + ' not exists!')
    print(default_color)
    try:
        print(warning_color + '[.] Copying files to USB drive ' + args.drive)
        from_directory = args.f
        if args.t:
            to_directory = args.t
        else:
            to_directory = args.drive

        copy_tree(from_directory, to_directory)
        print(success_color + '[+] Files copied!')
    except:
        print(error_color + '[-]  Unexpected error:', sys.exc_info()[0])
        raise
    print(error_color + '[+] Quack success! ;)')

    print(default_color)

def myFmtCallback(command, modifier, arg):
    print('[.] Formating...')
    return 1


def format_drive(Drive, Format, Title):
    fm = windll.LoadLibrary('fmifs.dll')
    FMT_CB_FUNC = WINFUNCTYPE(c_int, c_int, c_int, c_void_p)
    FMIFS_UNKNOWN = 0
    fm.FormatEx(c_wchar_p(Drive), FMIFS_UNKNOWN, c_wchar_p(Format),
                c_wchar_p(Title), True, c_int(0), FMT_CB_FUNC(myFmtCallback))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
