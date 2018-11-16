# qr-filetransfer

<p>
<a href="https://pypi.org/project/qr-filetransfer/"><img src="https://img.shields.io/badge/release-v1.1-blue.svg"></a>
<img src="https://img.shields.io/github/issues-closed-raw/sdushantha/qr-filetransfer.svg">
</p>

> Transfer files over WiFi from your computer to your smartphone from the terminal

[![asciicast](https://asciinema.org/a/173861.png)](https://asciinema.org/a/173861)

## 💾 Installation

You will find the most updated version of ```qr-filetransfer``` here. But if you want the most stable version, use ```pip``` to install it

### Pip Install

Global Install

```pip install qr-filetransfer```

Local Install

```pip install --user qr-filetransfer```

### Git Install

```bash
# clone the repo
$ git clone https://github.com/sdushantha/qr-filetransfer.git

# change the working directory to qr-filetransfer
$ cd qr-filetransfer

# install the requirements
$ pip3 install -r requirements.txt
```


## 🔨 Usage
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

## 🌟 Credits
Inspired by the Go project [qr-filetransfer](https://github.com/claudiodangelis/qr-filetransfer)

## 📜 License
MIT License

Copyright (c) 2018 Siddharth Dushantha
