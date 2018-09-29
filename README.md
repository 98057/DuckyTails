# DuckyTails
<img src="https://raw.githubusercontent.com/98057/DuckyTails/master/png/DuckyTails.png" width="128">

DuckyTails is a interpreter that runs Ducky Scripts from any pendrive. You don't need a USB Rubber Ducky! 

## Quickstart
### Encode your script
<img src="https://raw.githubusercontent.com/98057/DuckyTails/master/png/DuckyEncoder.png" width="128">

```
DuckyEncoder duck_code.txt
```
Obs: The payloads (.bin) from Ducky Script is not supported yet.

### Flash your USB
<img src="https://raw.githubusercontent.com/98057/DuckyTails/master/png/DuckyFlash.png" width="128">

```
DuckyFlash G:
```

Tha's it! You are ready to go!

## Tips

### Multiple scripts
You can run binary or non-binary scripts editing config.ini from your pendrive:

```
[Main]
Files = ['duck_code.txt']
```
[edited]
```
[Main]
Files = ['inject.bin', 'payload2.bin', 'duck_code.txt']
```

## Help
For more instructions:
```
DuckyEncoder -h
```

```
DuckyFlash -h
```