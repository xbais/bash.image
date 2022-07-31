import os
import sys
import argparse
import PIL
import numpy as np

image = [] # Image pixels will be added to this list later on...

def linspace():
    """
    Prints an extra blank line...
    """	
    print("\n")

def get_term_width():
    """
    Gets the maximum width of image that will fit the terminal in current window-size.
    """
    return

def rgb2bw(r:int, g:int, b:int):
    """
    Converts the rgb value to a greyscale value.
    """
    grey_shade = null
    grey_shade = (r+g+b)/(3*256) # Linear
    return grey_shade

def get_nearest_term_col():
    """
    Gets the x-term colour nearest to the given rgb value.
    """
    return

SHAPES = {"small-circle":"⏺", "small-rect":"∎", "large-square": "■", "mid-square": "◼", "small-square":"◾"}
    
class pixel():
        def __init__(self, color, shape):
            self.color = color
            self.shape = shape
        def render(self):
            return

class image():
    def __init__(self, width, height):
        self.height = height
        self.width = width
    def reduce_res():
        """
        Reduces the resolution of the image.
        """
        return

print("Checking terminal colour depth...")
os.system("echo $TERM")
linspace()

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Specify the input image to open.", type=str)
parser.add_argument("-bw", "--greyscale", help="Renders image in grayscale", action="store_true")
args = parser.parse_args()

image_url = args.input

if(image_url):
    if args.greyscale:
        # Render the image in greyscale
        print("Rendering image in greyscale...")
        pass

else:
    print("No image URL provided")
