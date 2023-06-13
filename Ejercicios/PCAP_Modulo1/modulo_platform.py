import platform

#functions: platform(), machine(), processor(), system(), version(),
#python_implementation(), python_version_tuple()

print(platform.platform())#Windows-10-10.0.22621-SP0
#print(platform.platform())#Linux-5.15.89+-x86_64-with-glibc2.31
#print(platform.platform())#Linux-5.10.0-0.bpo.15-amd64-x86_64-with

print(platform.machine())#AMD64
#print(platform.machine())#x86_64

print(platform.processor())#AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD

print(platform.system())#Windows
print(platform.version())#10.0.22621

print(platform.python_implementation())#CPython
print(platform.python_version_tuple())#('3','11','3')

