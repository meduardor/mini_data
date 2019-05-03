#!/usr/bin/env python3

import writer
import os
import sys


def ReadDataJson(filename):
    if os.access("filename", os.R_OK):
        with open("filename") as dataRead:
            return dataRead.read()
