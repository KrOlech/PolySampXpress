from ctypes import Structure, c_char, c_uint


class DeviceInformation(Structure):
    _fields_ = [
        ("Manufacturer", c_char * 5),
        ("ManufacturerId", c_char * 3),
        ("ProductDescription", c_char * 9),
        ("Major", c_uint),
        ("Minor", c_uint),
        ("Release", c_uint),
    ]
