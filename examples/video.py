# HabPi - A Simple Framework for High Altitude Sensing
#   Copyright (C) 2025 Robert Lowe <rlowe8@utm.edu>
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
from picamera2.encoders import H264Encoder, Quality
import time
import os
import sys
import HabPi

#create the directory
vidDir = HabPi.directories['dataDir'] + "/video"
os.mkdir(vidDir)

#get the camera
camera = Picamera2()

# set up & orientation
vflip=False
config = camera.create_video_configuration(transform=Transform(vflip=vflip))
camera.configure(config)

# Encoder
encoder = H264Encoder()

while True:
  vidname="%s/%d.h264"%(vidDir, int(time.time()))
  camera.start_recording(encoder, vidname, quality=Quality.HIGH)
  #record for 10 minutes then switch the file
  time.sleep(600)
  camera.stop_recording()
