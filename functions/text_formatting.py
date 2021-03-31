from PIL import Image, ImageDraw
import textwrap


# take text input and return its x,y midpoints
def center_text(img, font, text):
    img = Image.open(img)
    dimensions = img.size
    draw = ImageDraw.Draw(img)

    w, h = draw.textsize(text, font)

    x_mid = ((dimensions[0]/2) - w/2)
    y_mid = ((dimensions[1]/2) - h/2)

    return x_mid, y_mid


def wrap_message(message, wrap_at):
    message = textwrap.wrap(message, wrap_at)
    return message
