# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:27:48 2019

@author: admin
"""

import re
from dateutil.parser import parse
import json
from wand.image import Image
#from PIL import Image
#import sys
from pyocr import pyocr
#from pyocr import builders
from PIL import Image as PI
#from PIL import Image
#import pyocrL
import pyocr.builders
import io
#

#def get_text(path):
 #   tool = pyocr.get_available_tools()[0]
  #  lang = tool.get_available_languages()[0]

   # req_image = []
    #final_text = []

 #   image_pdf = Image(filename=path, resolution=300)
  #  image_jpeg = image_pdf.convert('jpeg')

   # for img in image_jpeg.sequence:
    #    img_page = Image(image=img)
     #   req_image.append(img_page.make_blob('jpeg'))

    #for img in req_image:
     #   txt = tool.image_to_string(
        #        PI.open(io.BytesIO(img)),
      #          lang=lang,
       #         builder=pyocr.builders.TextBuilder()
         #       )
        #final_text.append(txt)

        #return final_text


    #text = get_text("C:/Users/user/Desktop/ImageExtraction/align_North1.pdf")[0].split('\n')

   # class data_dictionary(dict):
    #    def add(self, key, value):
     #       self[key] = value

    #def findWord(w):
     #   return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
#date
    #def is_date(string, fuzzy=False):
     #   try:
      #      parse(string, fuzzy=fuzzy)
       #     return True
        #except ValueError:
         #   return False
    #if __name__ == "__main__":
     #   data = data_dictionary()
      #  data.add('Header', text[0])

#bill amount
   # for line in text:
    #   x = 'Grand Total'
     #  if findWord(x)(line):
      #     amount = re.search('\$?([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(\.[0-9][0-9])?$|$', line).group()
       #    data.add('Amount', amount)
        #   break
#date
    #for line in text:
     #   if is_date(line):
      #      is_date = line
       #     break
##mobile
    #for line in text:
     #   x = 'Contact No'
      #  if findWord(x)(line):
       #     mobile = re.search('((\+)?(\d{2}[-])?(\d{10}){1})?(\d{11}){0,1}?$|$', line).group()
        #    data.add(x, mobile)
         #   break
    #for line in text:
     #   x = 'GSTIN'
      #  if findWord(x)(line):
       #     gst = re.search('\$?([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(\.[0-9][0-9])?$|$', line).group()
        #    data.add(x, gst)
         #   break

#products
    #for i, line in enumerate(text):
     #   x = 'Item'
      #  if findWord(x)(line):
       #     start = i+1
        #    break
    #for j, line in enumerate(text):
     #   x = 'Grand Total'
      #  if findWord(x)(line):
       #     end = j
        #    break
    #products = []
    #new = text[start : end]
    #for i, line in enumerate(new):
     #   products.append(line)

    #data.add('Products', products)

    #j = json.dumps(data)