import ctypes
import pathlib



class REX:
    def __init__(self) -> None:
        self._REXOBJ = 1

relativepath = pathlib.Path('REX Shared Library.dll')
REXX = ctypes.windll.LoadLibrary(str(relativepath.resolve()))
REXX.REXInitializeDLL()
print(REXX)