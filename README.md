# Pip-Boy 3000 Mk IV (Raspberry Pi Edition)

This is a customized fork of the `pipboy-pi` project, optimized for **Python 3.13**, **Raspberry Pi 3 B+**, and **5-inch HDMI LCDs (800x480)**.

## 🛠 Features & Fixes in this Fork

* **KMSDRM Integration:** Successfully forced `kmsdrm` video driver usage. Fixed EGL initialization by installing `xinit` and managing the DRM render node.
* **Pathing Overhaul:** Updated `modules/paths.py` to use project-root relative paths instead of parent-directory `../` links, ensuring the app runs correctly from the root folder.
* **Audio Optimization:** Updated `pygame.mixer` to use a 4096-byte buffer and 2-channel stereo to eliminate "stuttering" on Pi 3 B+ hardware.
* **Vault Boy Alignment:** Manually calibrated the `status_tab.py` offsets (`+5x, -34y`) to fix the "sinking head" animation bug.
* **800x480 Native Support:** Pre-configured for standard 5-inch HDMI screens.

---

## 🚀 Installation

### 1. Prerequisites

You must install these system libraries for the graphics and audio to initialize correctly without a desktop environment:

```bash
sudo apt update
sudo apt install cmake libgbm1 libdrm-dev libgbm-dev xinit -y

```

### 2. Environment Setup

```bash
git clone https://github.com/sohail-bakhtiari/pipboy-pi.git
cd pipboy-pi
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

### 3. Compiling the Wireframe Module

```bash
cd modules/cpp
mkdir build && cd build
cmake ..
make
cp wireframe*.so ..

```

---

## 📺 Hardware Configuration

### Config.txt Tweaks

Edit `/boot/firmware/config.txt` (or `/boot/config.txt`) to ensure the GPU can handle the 3D wireframes and allow direct shutdown:

```text
# Use Fake KMS for Pi 3 B+ compatibility
dtoverlay=vc4-fkms-v3d
gpu_mem=256

# Physical shutdown/wake button (GPIO 3 to GND)
dtoverlay=gpio-shutdown,gpio_pin=3,active_low=1,pullup=on

```

---

## 🏃 Running the Pip-Boy

### Manual Start

```bash
cd ~/pipboy-pi
source venv/bin/activate
python modules/main.py

```

### Automatic Start (on Boot)

Create a service file at `/etc/systemd/system/pipboy.service`:

```ini
[Unit]
Description=Pip-Boy Boot Service
After=multi-user.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/pipboy-pi
ExecStart=/home/pi/pipboy-pi/venv/bin/python /home/pi/pipboy-pi/modules/main.py
Restart=always

[Install]
WantedBy=multi-user.target

```

Enable it with: `sudo systemctl enable pipboy.service`

---

## 🔧 Key Code Changes

* **`main.py`**: Forced `kmsdrm` and initialized `pygame.mixer` before `pygame.init` to capture the correct audio frequency.
* **`settings.py`**: Changed `RASPI = True` and set `SCREEN_WIDTH = 800`, `SCREEN_HEIGHT = 480`.
* **`status_tab.py`**: Adjusted head offset calculation to prevent the head entering the body during the walking animation.

---
