from ctypes import *
nativeLib = cdll.LoadLibrary("library/libfunction.so")

mode = "\x00"
add_blk = 00
num_blk = 01
snr = create_string_buffer("\xFF\xFF\xFF\xFF\xFF\xFF")
print repr(snr.raw)
buffer = (c_ubyte*16)()

tag = nativeLib.API_PCDRead(mode, add_blk, num_blk, byref(snr), byref(buffer))
for i in range(0,15):
	print buffer[i]
