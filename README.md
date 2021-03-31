# ScriptToCaption
This Python3 program a txt file and converts it into sets of transparent PNG files. This is a very simple way to create burned-in captions for live events. This software is free to use, modify, and remix.

# Requirements
This program runs using Python3 and requires the following packages:
- PIL
- textwrap

To install these dependencies, run the command `pip install [dependency_here]`.

# How it works
First, open the ScriptToCaption.py in your favorite script editor. Most all settings should be fine for a basic caption, however, the script does allow for changing the defualt colors, fonts, and dimensions of the output PNGs. The settings are modifiable in the program. I will post more detailed instructions at a later date on how to modify the templates.

By default, the script has a six-paragraph Loreum Ipsum script. All you have to do is copy and paste your own script into the [script.txt] file and save it.

Once you dial in your settings and save your script into the txt file, just run the script using the code editor or in your terminal using [python3 ScriptToCaption.py]

When the program runs, it'll automatically create a template PNG file, create a directory for the exports, split the script into little chunks, create the images, and save them into the export directory.

It's a fairly simple script and definitely has its quirks, but it makes life way easier than having to do this manually.

# Font License Information
This script comes with Open Sans, a font created by Steve Matteson. The font follows the Apache License, Version 2.0. The font files have not been modified by myself and are free to use alongside this software. You can find more information on Open Sans [here](https://fonts.google.com/specimen/Open+Sans?preview.text_type=custom#license).
