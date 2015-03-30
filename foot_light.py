ASCII_CHARS = [ ' ', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value/range_width] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image, new_width)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            xrange(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath, image_size):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception, e:
        print "Unable to open image file {image_filepath}.".format(image_filepath=image_filepath)
        print e
        return

    image_ascii = convert_image_to_ascii(image, image_size)
    print image_ascii

if __name__=='__main__':
    import sys
    import PIL.Image
    from PIL import *

    image_file_path = sys.argv[1]


    import urllib2
    import urllib
    import RPi.GPIO as GPIO, time, os      
    import os
    DEBUG = 1
    GPIO.setmode(GPIO.BCM)

    def RCtime (RCpin):
            reading = 0
            GPIO.setup(RCpin, GPIO.OUT)
            GPIO.output(RCpin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.setup(RCpin, GPIO.IN)
            # This takes about 1 millisecond per loop cycle
            while (GPIO.input(RCpin) == GPIO.LOW):
                    reading += 1
            image_size = (reading/12)
            image_size = image_size + 1
            os.system('cls' if os.name == 'nt' else 'clear')
            handle_image_conversion(image_file_path, image_size)

    while True:                                     
            RCtime(17)     # Read RC timing using pin #18
