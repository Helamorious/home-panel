# Home-Panel

## Introduction

This project is to create a touchscreen interface for controlling smart home integrations with HomeAssistant

## Hardware

[Raspberry Pi 3 Model B](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)\
[Rasbperry Pi PoE HAT](https://www.raspberrypi.com/products/poe-hat/)\
[Raspberry Pi Touch Display](https://www.raspberrypi.com/products/raspberry-pi-touch-display/)\
[PIR Sensor](https://projects.raspberrypi.org/en/projects/physical-computing/11)

## Software Installation

1. Install the Rasberry Pi OS Lite (32-bit) using the [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Update Raspberry Pi OS

```bash
sudo apt update
sudo apt upgrade
```

3. Install Chromium and dependancies

```bash
sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox
sudo apt-get install --no-install-recommends chromium-browser
```

4. Configure OpenBox

Add the following to */etc/xdg/openbox/autostart*

```bash
# Remove exit errors from the config files that could trigger a warning
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/'Local State'
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/; s/"exit_type":"[^"]\+"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences

# Run Chromium in kiosk mode
while true; do chromium-browser --noerrdialogs --disable-infobars --kiosk $KIOSK_URL; sleep 1; done
```

Configure the Kiosk URL as an environment variable */etc/xdg/openbox/environment*

```bash
export KIOSK_URL=http://homeassistant.local:8123/lovelace-homehub/menu
```

5. Setup X server

Update the Pi user bash profile *~/.bash_profile*

```bash
[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx -- -nocursor
```

Source the new bash profile 

```bash
source ~/.bash_profile
```

6. I had issues with the touch part of the Touch Panel. I had to disable DRM VC4 V3D driver, open */boot/config.txt* and comment out the following line

```bash
# Enable DRM VC4 V3D driver
#dtoverlay=vc4-kms-v3d
```

## References

[desertbot.io](https://desertbot.io/blog/raspberry-pi-touchscreen-kiosk-setup) Raspberry Pi Touchscreen Kiosk Setup (10 Steps, Buster)