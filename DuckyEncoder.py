# -*- encoding: utf-8 -*-
import base64
input_file = 'duck_code2.txt'
output_file = '.\dist\inject.bin'

duck_text = open(input_file, 'rb').read()
duck_bin = base64.b64encode(duck_text)

with open(output_file, 'wb') as f:
    f.write(duck_bin)

print(duck_bin)
