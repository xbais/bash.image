import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Specify the input image to open.")
args = parser.parse_args()
print("The URL of the input image is = ", args.input)
