import base64
from colorama import init, Fore, Back, Style
from argparse import ArgumentParser, RawTextHelpFormatter
import os
def main(args):
    init()

    default_color = Fore.BLUE
    error_color = Fore.RED
    success_color = Fore.GREEN
    warning_color = Fore.YELLOW

    print(default_color)

    parser = ArgumentParser(prog='DuckyEncoder',
                                     description='Ducky Encoder converts duck script to binary ' +
                                                 warning_color +'\n[!] Not compatible with Official Duck Encoder yet!' + default_color,
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('script', default='duck_code.txt', help='Ducky Script \nie: DuckyEncoder duck_code.txt')
    parser.add_argument('-o', '--output', default='.\dist\inject.bin', help='Binary output file \nie: DuckyEncoder duck_code.txt -o inject.bin')
    args = parser.parse_args()

    input_file = args.script
    output_file = args.output

    if os.path.exists(input_file):
        print(warning_color + '[.] Loading file ' + input_file + '...')

        try:
            duck_text = open(input_file, 'rb').read()
            print(success_color + '[+] File ' + input_file + ' loaded.')
        except IOError:
            print(error_color + '[-] Cannot read file ' + input_file + '!')
            raise

        print(warning_color + '[.] Encoding binary ' + output_file + '...')
        try:
            duck_bin = base64.b64encode(duck_text)
            print(success_color + '[+] File ' + output_file + ' encoded.')
        except:
            print(error_color + '[-] Unexpected error:', sys.exc_info()[0])
            raise

        print(warning_color + '[.] Saving binary ' + output_file + '...')
        try:
            with open(output_file, 'wb') as f:
                f.write(duck_bin)
            print(success_color + '[+] File ' + output_file + ' saved.')
        except IOError:
            print(error_color + '[-] Cannot save file file ' + input_file)
            raise

        print(success_color + '[+] Quack Success! ;)')
    else:
        print(error_color + '[-] File ' + input_file + ' not exists!')

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
