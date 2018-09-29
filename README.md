# DuckyTails
![](https://raw.githubusercontent.com/98057/DuckyTails/master/png/DuckyTails.png)

DuckyTails is a interpreter that runs Ducky Scripts from any pendrive. You don't need a USB Rubber Ducky! 

## Quickstart
### Encode your script
![](https://raw.githubusercontent.com/98057/DuckyTails/master/png/DuckyEncoder.png)
```
DuckyEncoder duck_code.txt
```
Obs: The payloads (.bin) from Ducky Script is not supported yet.

### Flash your USB
![](https://raw.githubusercontent.com/98057/DuckyTails/master/png/DuckyFlash.png)
```
DuckyFlash G:
```

Tha's it! You are ready to go!

## Tips

### Multiple scripts
You can run multiple binary or non-binary scripts editing config.ini from your pendrive:

```
[Main]
Files = ['duck_code.txt']
```
After edit:
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
