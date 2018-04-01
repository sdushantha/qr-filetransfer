# qr-filetransfer
> Transfer files over WiFI from your computer to your smartphone from the terminal
## Installation

```bash
# clone the repo
> git clone https://github.com/sdushantha/qr-filetransfer.git

# install the requirements
> pip3 install -r requirements.txt
```


## Usage
```
usage: qr-filetransfer.py [-h] -f FILE
```

**Note:** Both devices needs to be connected to the same network


Transfer a single file
```bash
python3 qr-filetransfer.py -f /path/to/file.txt
```


Transfer a full directory. **Note:** the directory gets zipped before being transferred
```bash
python3 qr-filetransfer.py -f /path/to/directory
```

## Example
![screenshot](screenshot.png)
