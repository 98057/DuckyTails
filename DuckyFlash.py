import os
import configparser
from ctypes import *
import time
import os
from distutils.dir_util import copy_tree
from colorama import init, Fore, Back, Style

def main(args):
    init()
    import argparse
    parser = argparse.ArgumentParser(prog='DuckyTails USB Flasher', description='Ducky USB Flasher copy the files in USB Drive to Autorun')
    parser.add_argument('drive', help='USB drive letter i.e: DuckyFlash E:')
    parser.add_argument('--format', action='store_true', help='Format the USB ie: DuckyFlash E: --format')
    parser.add_argument('-e', '--exe', default='.\dist\DuckyTails.exe', help='Generate the STARTAPP.inf from executable ie: DuckyFlash E: --exe .\dist\DuckyTails.exe')
    parser.add_argument('-f', default='.\dist', help='Copy from directory i.e.: DuckFlash --from ".\dist"')
    parser.add_argument('-t', help='Copy to directory i.e.: DuckFlash --from ".\dist" --to "E:\Directory"')

    args = parser.parse_args()
    if args.format:
        try:
            print('[.] Starting formating...')
            format_drive(args.drive, 'NTFS', 'USBDrive')
            print(Fore.GREEN + '[+] Drive formated!')
        except:
            print(Fore.RED + '[-]  Unexpected error:', sys.exc_info()[0])
            raise

    print(Style.RESET_ALL)

    if os.path.exists(args.exe):
        try:
            print('[.] Generating STARTAPP.inf file from ' + args.exe + '...')
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
            print(Fore.GREEN + '[+] STARTAPP.inf file generated from ' + args.exe + '!')
            print(Style.RESET_ALL)
            print('[.] Saving STARTAPP.inf ...')
            with open('.\dist\OpenFile\STARTAPP.INF', 'w') as configfile:
                config.write(configfile)
            print(Fore.GREEN + '[+] STARTAPP.inf saved!')
        except:
            print(Fore.RED + '[-]  Unexpected error:', sys.exc_info()[0])
            raise
    else:
        print(Fore.RED + '[-] File ' + args.exe + ' not exists!')
    print(Style.RESET_ALL)
    try:
        print('[.] Copying files to USB drive ' + args.drive)
        from_directory = args.f
        if args.t:
            to_directory = args.t
        else:
            to_directory = args.drive

        copy_tree(from_directory, to_directory)
        print(Fore.GREEN + '[+] Files copied!')
    except:
        print(Fore.RED + '[-]  Unexpected error:', sys.exc_info()[0])
        raise
    print(Fore.GREEN + '[+] Done! ;)')

    print(Style.RESET_ALL)

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
