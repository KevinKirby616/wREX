import ctypes
import pathlib


#REXCreatorInfo As it says. The original has to be ctype char arraya,
#so it might actually be better to stick all of this in a class with 
#handling methods. 
REXCreatorInfo = {
    "name"          : "",       #The name of the REX2 file’s creator.
    "copyright"     : "",       #Copyright information.
    "URL"           : "",       #Where the creator can be found on the Internet.
    "email"         : "",       #The E-mail address of the creator.
    "freetext"      : ""        #Any additional text that the creator may have added.
}


#Everything here is int32
REXSliceInfo = {
    "ppqpos"        : int,      #Zero-based PPQ position of slice in loop. The
                                #resolution is 15360 PPQ. This
                                #position is always greater than or equal to zero and less than fPPQLength,
                                #which is found in REXInfo. Note that the first slice of a loop does not
                                #necessarily have to be at PPQ position zero.
    "samplelength"  : int       #Length of rendered slice at the REX object’s output sample rate.
}


class REXInfo:
#This is sort of the Python analog of original REXInfo struct. It was this or a dict. It still may
#end up being a dict. Everything here is the ctype int32.

    channels        : int       #Number of channels. At the moment, this value
                                #always amounts to 1 or 2.
    samplerate      : int       #Sample rate of the file’s PCM data. 1.0 kHz 
                                #to 1.0 MHz.
    slicecount      : int       ##Number of slices in the object. This value
                                #may be zero.
    tempo           : int       #Tempo set when exported from ReCycle, 123.456
                                #BPM stored as 123456 etc.
    originaltempo   : int       #Original tempo of loop, as set up in ReCycle 
                                #with the Left/Right locators and the Bars/
                                #Beats/Sign controls. In the same format as fTempo.
    ppqlength       : int       #Length of loop. The resolution is always 15360 PPQ (Pulses Per Quarter-note).
                                #This means that one bar in 4/4 time amounts to 15360*4*(4/4) = 61440 Pulses,
                                #one bar in 6/8 time is 15360*4*(6/8) = 46080 pulses, etc.
    timesignnom     : int       #Time signature nominator (the “6” in “6/8”).
    timesigndenom   : int       #Time signature denominator (the “8” in “6/8”).
    bitdepth        : int       #Original bit depth of ReCycle:d file. Please note that all processing in the REX
                                #DLL is carried out in 32-bit floating point format, meaning that regardless of the
                                #original resolution of the file you will obtain the best sound quality by using the
                                #floating point data directly, and not truncating or dithering it.


class REX:
#This is the main class that will be instantiated to deal with rex files.
#this undoubtedly will have to be broken up and refactored several times as I add more
#code, as I have already beguan to do with the data structure.

    def __init__(self, filename: str) -> None:
        self.dllfile = 'REX Shared Library.dll'
        relativepath = pathlib.Path(self.dllfile)
        self.dllinstance = ctypes.windll.LoadLibrary(str(relativepath.resolve()))
        print(bool(self.dllinstance.REXInitializeDLL()))
        self.xxx : int = 5
        self._rexfile = filename
    
    def __str__(self) -> str:
        return str(self.dllinstance)

    def UninitializeDLL(self) -> None:
        print(bool(self.dllinstance.REXUninitializeDLL()))

    def create() -> None:
        pass

    def delete() -> None:
        pass

    def getinfo() -> dict:
        pass

    def getinfofrombuffer() -> dict:
        pass

    def getcreatorinfo() -> dict:
        pass

    def geetsliceinfo() -> int:
        pass

    def setoutputsamplerate() -> None:
        pass

    def renderslice() -> list:
        pass

    def createcallback() -> None:
        pass

    def startpreview() -> list:
        pass

    def stoppreview() -> None:
        pass

    def setpreviewtempo(int) -> None:
        pass

    def renderpreviewbath(int) -> list:
        pass

    def rexinfo() -> list:
        pass




class REXDataStructs:
    REXInfo : None
    REXCreatorInfo : None
    REXSliceInfo : None
    REXError : None
    REXHandle : None
    REXCallbackResult : None









shit = REX(5)

print(shit.__dict__)
print(shit.UninitializeDLL())

print(REXInfo.__dict__)
#relativepath = pathlib.Path('REX Shared Library.dll')
#REXX = ctypes.windll.LoadLibrary(str(relativepath.resolve()))
#REXX.REXInitializeDLL()
#print(REXX)