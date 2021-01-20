# autodisplay
A set of scripts to enable raspberrypints launching on startup including automation of powering the display on and off.

Usage:
Add kiosh.sh and display.py to directory in your root, such as:   /home/pi/scripts
Make sure to chmod +x

Replace /etc/xdg/lxsession/LXDE-pi/autostart with the one in this repo.

Reboot your rpi and it will automatically go into kiosk mode, launch raspberry pints and turn the hdmi on/off with the motion sensor.
