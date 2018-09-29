import configparser
from ctypes import *
import time
import os
from distutils.dir_util import copy_tree
#from shutil import copytree
import logging
from colorama import init, Fore
from argparse import ArgumentParser, RawTextHelpFormatter
import sys
from distutils import log

def main(args):
    init()

    default_color = Fore.LIGHTRED_EX
    error_color = Fore.RED
    success_color = Fore.GREEN
    warning_color = Fore.YELLOW

    print(default_color)

    parser = ArgumentParser(prog='DuckyFlash',
                            description='Ducky Flash copy the files in USB Drive to Autorun',
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument('drive', help='USB drive letter'
                                      'ie: DuckyFlash E:')
    parser.add_argument('--format',
                        action='store_true',
                        help='Format the USB'
                             'ie: DuckyFlash E: --format')
    parser.add_argument('-e', '--exe',
                        default='.\dist\DuckyTails.exe',
                        help='Generate the STARTAPP.inf from executable'
                        'ie: DuckyFlash E: --exe ".\dist\DuckyTails.exe"')
    args = parser.parse_args()

    if args.format:
        try:
            print(warning_color + '[.] Starting formatting...')
            print(warning_color + '[!] DO NOT CANCEL THIS PROCESS!')
            format_drive(args.drive, 'NTFS', 'USBDrive')
            print(success_color + '[+] Drive formatted!')
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
        log.set_verbosity(log.INFO)
        log.set_threshold(log.INFO)

        from_directory = '.\dist'
        to_directory = args.drive + '\\'
        print(success_color)
        copy_tree(from_directory, to_directory, verbose=1)

        print(success_color + '\n[+] Files copied!')
    except:
        print(error_color + '[-]  Unexpected error:', sys.exc_info()[0])
        raise
    print(success_color + '[+] Quack success! ;)')

    print(default_color)


def _logpath(path, names):
    logging.info('Working in %s' % path)
    return []   # nothing will be ignored


def play_animation(color, text):
    global animation
    global i
    time.sleep(0.1)
    i += 1
    sys.stdout.write(color + "\r[" + animation[i % len(animation)] + '] ' + text)
    sys.stdout.flush()

def myFmtCallback(command, modifier, arg):
    play_animation(Fore.RED, 'Formatting...')
    return 1


def format_drive(drive, format, title):
    fm = windll.LoadLibrary('fmifs.dll')
    fmt_cb_func = WINFUNCTYPE(c_int, c_int, c_int, c_void_p)
    fmifs_unknown = 0
    fm.FormatEx(c_wchar_p(drive), fmifs_unknown, c_wchar_p(format),
                c_wchar_p(title), True, c_int(0), fmt_cb_func(myFmtCallback))


if __name__ == '__main__':
    animation = "|/-\\"
    i = 0
    sys.exit(main(sys.argv))
