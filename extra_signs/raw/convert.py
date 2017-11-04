#!/usr/bin/env python3
from PIL import Image
import math
import os


files = sorted([fname for fname in os.listdir('.') if fname.endswith('.png')])
for idx, fname in enumerate(files):
  print(fname)
  img = Image.open(fname)

  width, height = img.size
  diff = width - height
  dl = max(int(math.floor(diff / 2)), 0)
  dr = max(int(math.ceil(diff / 2)), 0)
  dt = max(int(math.floor(-diff / 2)), 0)
  db = max(int(math.ceil(-diff / 2)), 0)
  squared = img.crop([
    dl,
    dt,
    width - dr,
    height - db,
  ])
  resized = img.resize(
    (32, 32),
    Image.LANCZOS,
  )

  resized.save('../processed/{}.png'.format(idx))
