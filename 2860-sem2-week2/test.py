#!/usr/bin/env python3
import argparse
import os
import socket
import struct
import sys
from typing import Tuple

ba = bytearray([72, 101, 108, 108, 111, ord("\n")])

def print_bytearray(array):
    output = ""
    for b in array:
        output += chr(b)
    print(output)

print_bytearray(ba)