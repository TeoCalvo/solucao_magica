import string
import os

string.digits # numeros
string.ascii_lowercase # todas letras minusculas
string.punctuation # Todos de pontuação


from PIL import ImageFont, ImageDraw, Image  
import numpy as np
#############################
img_width = 128
img_height = 128
font_size = 120
branco = (255, 255, 255) 
preto = (0, 0, 0)

fonts_files = [ os.path.join("data", i) for i in os.listdir( os.path.join("data", 'fonts') )]
#############################

def make_char_font( char, font_name ):
    font = ImageFont.truetype( os.path.join("data","fonts",f"{font_name}.ttf"), font_size)
    image = Image.new("RGB", (img_width, img_height), (255,255,255))
    draw = ImageDraw.Draw(image)  

    text_width, text_height = draw.textsize(char, font)
    position_x =  (img_width - text_width)/2
    position_y = (img_height - text_height)

    if (position_y < 0):
        position_y = position_y * 2
    else:
        position_y = position_y / 2

    draw.text((position_x, position_y), char, (0,0,0), font=font, align='center')
    # draw.multiline_text((position_x, position_y), caracter, fill=(0,0,0), font=font, spacing=-1, align="center")
    image.save( os.path.join("data", f"{char}" ,f"{font_name}.jpg" ) )

def make_font(char):
    try:
        os.makedirs(os.path.join( "data", f"{char}" ))
    except:
        pass

    for f in fonts_files:
        font_name = f.split("/")[-1].split(".")[0]
        make_char_font( char, font_name )
    
for c in string.ascii_letters:
    make_font(c)