# qr-filetransfer
> Transfer files over WiFi from your computer to your smartphone from the terminal

[![asciicast](https://asciinema.org/a/173861.png)](https://asciinema.org/a/173861)

## :floppy_disk: Installation

```bash
# clone the repo
$ git clone https://github.com/sdushantha/qr-filetransfer.git

# change the working directory to qr-filetransfer
$ cd qr-filetransfer

# install the requirements
$ pip3 install -r requirements.txt
```


## :hammer: Usage
```
usage: qr-filetransfer.py [-h] FILE
```

**Note:** Both devices needs to be connected to the same network

**Exiting**

To exit the program, just press ```CTRL+C```.

---

Transfer a single file
```bash
$ python3 qr-filetransfer.py /path/to/file.txt
```


Transfer a full directory. **Note:** the directory gets zipped before being transferred
```bash
$ python3 qr-filetransfer.py /path/to/directory/
```

## :star2: Credits
Inspired by the Go project [qr-filetransfer](https://github.com/claudiodangelis/qr-filetransfer)

## :scroll: License
MIT License

Copyright (c) 2018 Siddharth Dushantha
