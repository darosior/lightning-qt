# pylightning-qt
*bitcoin-qt for C-Lightning, as simple as : `lightning-cli gui`*
![lightning-qt screenshot](https://pixeldrain.com/api/file/XZAf7AdX)
  
## What is it ?
lightning-qt is a Python plugin for [C-lightning](https://github.com/ElementsProject/lightning), a [Lightning Network](https://github.com/bitcoin/bitcoin/tree/master/src/qt) daemon. It enables the use of a [bitcoin-qt](https://github.com/bitcoin/bitcoin/tree/master/src/qt)-like Graphical User Interface (actually, part of the icons and forms have been taken from bitcoin-qt and modified) via the RPC interface.  
  
## Why ?
Currently does not have a GUI, and I think that having one which looks like bitcoin-qt is great for people coming from [bitcoin-core](https://github.com/bitcoin/bitcoin), which most of the C-Lightning users do (or have at least ever used bitcoin-qt). Having it directly available from the RPC is also quite convenient.  
  
## How to install it ?
For more informations about plugins and their installations you can checkout the [lightningd/plugins](https://github.com/lightningd/plugins) repository (which has a great list of plugins too). For a quick solution :  
```shell
git clone https://github.com/darosior/pylightning-qt && cd pylightning-qt
pip3 install -r requirements.txt
# And just start lightningd like
lightningd --plugin=gui.py
```
  
## How to use it ?
Just launch `lightning-cli gui` :D.  
  
## Contributing
Any contribution (issue, PR) is welcome.
We use [forms](forms/)(ui files) to design pages : these are handled by PyQt5 with the `pyuic5` command line tool (installed with `pip install PyQt5`). If you modify a ui file (you may want to use [QDesigner](https://doc.qt.io/qt-5/qtdesigner-manual.html)), you can regenerate the Python code like :
```shell
pyuic5 forms/channelspage.ui -o forms/ui_channelsPage.py
```
Images are handled in the [qrc](gui.qrc) file : if you modify this resource file (for instance to add an image/icon), you can regenerate the Python code with :
```shell
pyrcc5 gui.qrc -o resources.py
```
Also, if you help me on this project you may want to use the very handy [auto-reload plugin](https://github.com/lightningd/plugins/tree/master/autoreload). Please also note that PyQt5 has *__a very bad__* way to handle exception in slots : in short you cannot `except` a raised exception in a [slot](https://doc.qt.io/qt-5/signalsandslots.html), so be carefull and happy debuging ;).  
   
## Licence
BSD 3-clauses clear
