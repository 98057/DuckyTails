import pyautogui
import configparser
import base64
import mimetypes
import time


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    files = eval(config.get("Main", "Files"))

    for f in files:
        global last_command
        global default_delay

        last_command = ""
        duck_text = ""
        default_delay = 0
        mime = mimetypes.guess_type(f)

        if mime[0] == 'application/octet-stream':
            duck_bin = open(f, 'rb').read()
            duck_text = base64.b64decode(duck_bin)
            duck_text = duck_text.decode('ascii')
            duck_text = duck_text.splitlines()

        elif mime[0] == 'text/plain':
            duck_text = open(f, 'r').readlines()

        for line in duck_text:
            execute_command(line)
            last_command = line


def execute_command(cmd):
    global default_delay
    global last_command
    time.sleep(default_delay)

    cmd = cmd.split(' ', 1)

    if '-' in cmd[0]:
        cmd[0] = cmd[0].split('-', 1)
        if len(cmd) > 1:
            cmd = cmd[0] + [cmd[1]]
        else:
            cmd = cmd[0]
        execute_hotkey(cmd)
    elif cmd[0] == 'DELAY':
        cmd[1] = eval(cmd[1])/1000
        time.sleep(cmd[1])
    elif cmd[0] == 'DEFAULT_DELAY':
        default_delay = eval(cmd[1]) / 1000
    elif cmd[0] == 'STRING':
        pyautogui.typewrite(cmd[1].rstrip())
    elif cmd[0] == 'GUI' or cmd[0] == 'WINDOWS':
        cmd[0] = 'win'
        execute_hotkey(cmd)
    elif cmd[0] == 'MENU' or cmd[0] == 'APP':
        pyautogui.hotkey('shift', 'f10')
    elif cmd[0] == 'CTRL' or cmd[0] == 'SHIFT' or cmd[0] == 'ALT':
        execute_hotkey(cmd)
    elif cmd[0] == 'CONTROL':
        cmd[0] = 'ctrl'
        execute_hotkey(cmd)
    elif cmd[0] == 'DOWNARROW':
        pyautogui.press('down')
    elif cmd[0] == 'LEFTARROW':
        pyautogui.press('left')
    elif cmd[0] == 'RIGHTARROW':
        pyautogui.press('right')
    elif cmd[0] == 'UPARROW':
        pyautogui.press('up')
    elif cmd[0] == 'REPEAT':
        for x in range(0, eval(cmd[1])):
            execute_command(last_command)
    else:
        execute_hotkey(cmd)


def execute_hotkey(cmd):
    cmd[0] = cmd[0].rstrip().lower()
    if len(cmd) > 1:
        cmd[1] = cmd[1].split(' ')
        [x.strip().lower() for x in cmd[1]]
        pyautogui.hotkey(cmd[0], *cmd[1], interval=0.1)
    else:
        print(cmd[0])
        pyautogui.hotkey(cmd[0])


if __name__ == "__main__":
    default_delay = 0
    last_command = ""

    main()