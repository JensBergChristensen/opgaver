# EMAIL IMPORTS
import smtplib, email, os
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server
from threading import Thread
from time import sleep
from io import BytesIO
from datetime import datetime
import RPi.GPIO as GPIO

# GPIO SETUP FOR PIR SENSOR
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# CREATE WEBPAGE FOR LIVE STREAM
PAGE="""\
<html>
<head>
<title>PiCamera livestream</title>
</head>
<body>
<h1>PiCamera livestream</h1>
<img src="stream.mjpg" width="640" height="480" />
</body>
</html>
"""

# LIVESTREAM - GET OUTPUT FROM CAMERA
class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

# LIVESTREAM - SEND DATA
class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Find and make website content
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            # Send camera output to website
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

# LIVESTREAM - LIVESTRAM SERVER CREATION
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


# EMAIL - CONTENT AND VARIABLES SETUP
subject='Picamera: Motion detected'
bodyText="""\
Hello,
Motion detected by pir sensor.
10 second video clip has been attached.
Regards
Gruppe 4 :)
"""
SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=587
USERNAME='sem3projektgruppe4'
PASSWORD='sqolkoitgiazafsc'
RECIEVER_EMAIL='sem3projektgruppe4@gmail.com'

# EMAIl - FILENAME AND PATH
filename_part1="surveillance"
file_ext=".mp4"
now = datetime.now()
current_datetime = now.strftime("%d-%m-%Y_%H:%M:%S")
filename=filename_part1+"_"+current_datetime+file_ext
filepath="/home/pi/python_code/capture/"

#EMAIL - SEND FUNCTION
def send_email():
  message=MIMEMultipart()
  message["From"]=USERNAME
  message["To"]=RECIEVER_EMAIL
  message["Subject"]=subject

  message.attach(MIMEText(bodyText, 'plain'))
  attachment=open(filepath+filename, "rb")

  mimeBase=MIMEBase('application','octet-stream')
  mimeBase.set_payload((attachment).read())

  encoders.encode_base64(mimeBase)
  mimeBase.add_header('Content-Disposition', "attachment; filename= " +filename)

  message.attach(mimeBase)
  text=message.as_string()

  session=smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
  session.ehlo()
  session.starttls()
  session.ehlo()

  session.login(USERNAME, PASSWORD)
  session.sendmail(USERNAME, RECIEVER_EMAIL, text)
  session.quit
  print("Email sent")

# EMAIL - DELETE VIDEO FILE FUNCTION
def remove_file():
  if os.path.exists("/home/pi/python_code/capture/newvideo.h264"):
    os.remove("/home/pi/python_code/capture/newvideo.h264")
  else:
    print("file does not exist")

  if os.path.exists(filepath+filename):
    os.remove(filepath+filename)
  else:
    print("file does not exist")

# DEFINE CAMEREA
camera = picamera.PiCamera(resolution='640x480', framerate=24)

def livestream_start():
    camera.start_recording(output, format='mjpeg', splitter_port=1)
    # Output is used with StreamingOutput class
    try:
        address = ('ENTER IP ADDRESS FOR PI', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()

def cam_email_start():
    while True:
        i = GPIO.input(7) #pir sensor
        if i==1:
            print("Motion Detected")
            # Using splitter port 2 to avoid conflict with stream function
            camera.start_recording('/home/pi/python_code/capture/newvideo.h264', splitter_port=2)
            camera.wait_recording(timeout=10, splitter_port=2)
            camera.stop_recording(splitter_port=2)
            sleep(2)
            res=os.system("MP4Box -add /home/pi/python_code/capture/newvideo.h264 /home/pi/python_code/capture/newvideo.mp4")
            os.system("mv /home/pi/python_code/capture/newvideo.mp4 "+filepath+filename)
            send_email() # Call email send function
            sleep(2)
            remove_file() # Remove video file from raspberyy when done

# Create threads for livestream and email functions
livestream_thread = Thread(target=livestream_start)
cam_email_thread = Thread(target=cam_email_start)

livestream_thread = Thread(target=livestream_start)
cam_email_thread = Thread(target=cam_email_start)

livestream_thread.start()
cam_email_thread.start()


print("program started")

