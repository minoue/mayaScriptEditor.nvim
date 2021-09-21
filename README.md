# mayaScriptEditor.nvim

Send buffer contents to maya

\* **Works only for python scripts** *

## Requirements
* nvim
* pynvim

## Install

1. Install pynvim
    ```
    pip3 install pynvim
    ```

2. Copy mayaScriptEditor.py to ~/.config/nvim/rplugin/python3

## How to use

1. Open command port in maya
    ```
    from maya import cmds
    cmds.commandPort(name=":54321", prefix='python', sourceType="mel")
    ```

2. Open maya script, and run
    ```
    :SendToMaya
    ```
