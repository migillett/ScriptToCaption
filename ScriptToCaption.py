from functions import check_dir, text_formatting
import os
from PIL import Image, ImageDraw, ImageFont


def create_template(template_location, bar_color, dimensions):
    if os.path.exists(template_location):
        os.remove(template_location)
        print('Deleted old template file')

    mode = 'RGBA'
    color = (0, 0, 0, 0)
    im = Image.new(mode, dimensions, color)

    draw = ImageDraw.Draw(im)
    draw.rectangle([(0, dimensions[1]*0.8), (dimensions[0], dimensions[1]*0.95)], fill=bar_color)

    im.save(template_location)
    print('Created new template file at:', template_location)


def create_slide(template, text, save_location, font_path, font_size, text_y_pos):
    bkgd = Image.open(template)
    draw = ImageDraw.Draw(bkgd)

    caption_font = ImageFont.truetype(font_path, font_size)
    text_x, text_y = text_formatting.center_text(template, caption_font, text)

    draw.text((text_x, text_y_pos), text=text, fill=(255, 255, 255), font=caption_font)
    bkgd.save(save_location)
    print('Exported slide:', save_location)


def script_to_text(template_path, script_path, export_path, font_path):
    # create export directory
    check_dir.check_for_directory(export_path)

    # create new template png file
    blue = (0, 51, 153, 255)
    grn = (0, 102, 51, 255)
    img_dimensions = (1920, 1080)
    create_template(template_path, blue, img_dimensions)

    counter = 0

    with open(script_path, 'r', encoding='utf-8') as document:
        # split out each new paragraph
        new_line = (line.rstrip() for line in document)

        # if that new paragraph is empty, drop it
        full_import_script = list(line for line in new_line if line)

        # loop through each paragraph and wrap text
        for para in full_import_script:
            # ignore file formatting
            if not para.startswith('='):
                p_wrapped = text_formatting.wrap_message(para, 50)
                for slide_text in p_wrapped:
                    counter += 1
                    export_name = os.path.join(export_path, 'caption_slide_{:04d}.png'.format(counter))
                    create_slide(
                        template=template_path, text=slide_text, save_location=export_name,
                        font_path=font_path, font_size=75, text_y_pos=890)


if __name__ == '__main__':
    cur_dir = os.path.curdir
    temp_png = str(os.path.join(cur_dir, 'template.png'))
    script = str(os.path.join(cur_dir, 'script.txt'))
    export = str(os.path.join(cur_dir, 'exported_slides'))

    script_to_text(
        template_path=temp_png,
        script_path=script,
        export_path=export,
        font_path='./fonts/OpenSans-Regular.ttf'
    )
