import ctypes
import pathlib



class REX:
    def __init__(self, filename: 'full path to .rex file.') -> None:
        self.dllfile = 'REX Shared Library.dll'
        relativepath = pathlib.Path(self.dllfile)
        self.dllinstance = ctypes.windll.LoadLibrary(str(relativepath.resolve()))
        print(bool(self.dllinstance.REXInitializeDLL()))
        self._rexfile = filename
    
    def __str__(self) -> str:
        return str(self.dllinstance)

    def UninitializeDLL(self) -> 'unload DLL':
        print(bool(self.dllinstance.REXUninitializeDLL()))


shit = REX(5)

print(shit.UninitializeDLL())

#relativepath = pathlib.Path('REX Shared Library.dll')
#REXX = ctypes.windll.LoadLibrary(str(relativepath.resolve()))
#REXX.REXInitializeDLL()
#print(REXX)