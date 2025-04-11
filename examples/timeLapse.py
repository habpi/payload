# HabPi - A Simple Framework for High Altitude Sensing
#   Copyright (C) 2017 Robert Lowe <robert.lowe@maryvillecollege.edu>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
from picamera2 import Picamera2
from libcamera import Transform
import time
import os
import sys
import HabPi

#create the image directory
imgDir = HabPi.directories['dataDir'] + "/pictures"
os.mkdir(imgDir)

#get the camera
camera = Picamera2()

# set up & orientation
vflip=True
config = camera.create_still_configuration(transform=Transform(vflip=vflip))
camera.configure(config)
camera.options['quality']=95

# run the camera
camera.start()
while True:
  imgname="%d.jpg"%(int(time.time()))
  file_name= imgDir+"/"+imgname
  camera.capture_file(file_name)
  time.sleep(1)
