# autodisplay
A set of scripts to enable raspberrypints launching on startup including automation of powering the display on and off.

Usage:
Add kiosh.sh and display.py to directory in your root, such as:   /home/pi/scripts
Make sure to chmod +x

Replace /etc/xdg/lxsession/LXDE-pi/autostart with the one in this repo.

Update /boot/config.txt based on your resolution settings:

  For 1920x1080 use:
  hdmi_group=2
  hdmi_mode=82

  Additional options can be found here:
  https://www.raspberrypi.org/documentation/configuration/config-txt/video.md
  
  Set this flag if you have black borders around your display:
  disable_overscan=1
  
  You can also set your screen orientation options here if you choose to turn your monitor to portrait using the <b>display_rotate</b> parameter.
  
  You may need to add this flag as well:
  hdmi_force_unplug=1

Reboot your rpi and it will automatically go into kiosk mode, launch raspberry pints and turn the hdmi on/off with the motion sensor.
