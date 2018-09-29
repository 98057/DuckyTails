![](https://github.com/98057/DuckyTails/blob/master/png/DuckyTails.png =250x250)
# DuckyTails
DuckyTails is a interpreter that runs Ducky Scripts from any pendrive. You don't need a USB Rubber Ducky

## Quickstart
### Encode your script
```
DuckyEncoder duck_code.txt
```
Make sure that your ducky_code.txt is in the folder.

Obs: The payloads (.bin) from Ducky Script is not supported yet.

### Flash your USB
```
DuckyFlash G:
```

Done! You are ready to go!

##Tips

###Multiple scripts
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

##Help
For more instructions:
```
DuckEncoder -h
```

```
DuckFlash -h
```