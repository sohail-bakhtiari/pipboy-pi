# Pip-Boy 3000 Mk IV (Raspberry Pi Edition)

This is a customized fork of the `pipboy-pi` project, optimized for **Python 3.13**, **Raspberry Pi 3 B+**, and **5-inch HDMI LCDs**.

## 🛠 Features & Fixes in this Fork

* **Python 3.13 Compatibility:** Fixed float-to-integer rendering errors and modern `pygame-ce` integration.
* **Modernized C++ Module:** Updated `CMakeLists` and build paths for `pybind11` on newer OS versions.
* **EGL/KMS Integration:** Pre-configured for `kmsdrm` video drivers to run directly from the CLI (no desktop required).
* **Vault Boy Alignment:** Corrected 3D wireframe offsets for better visual fidelity.
* **Auto-Boot Ready:** Includes systemd service configurations for a dedicated prop experience.

---

## 🚀 Installation

### 1. Prerequisites

```bash
sudo apt update
sudo apt install cmake libgbm1 libdrm-dev libgbm-dev xinit -y

```

### 2. Environment Setup

```bash
git clone https://github.com/YOUR_USERNAME/pipboy-pi.git
cd pipboy-pi
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

### 3. Compiling the Wireframe Module

The 3D Vault Boy requires the C++ extension to be compiled locally:

```bash
cd modules/cpp
mkdir build && cd build
cmake ..
make
cp wireframe*.so ..

```

---

## 📺 Hardware Configuration (5" HDMI LCD)

To fix "EGL Not Initialized" or "Pageflip" errors on Pi 3 B+, use these settings in `/boot/firmware/config.txt`:

```text
# Use Fake KMS for better compatibility with Pygame-ce
dtoverlay=vc4-fkms-v3d
# Increase GPU memory for wireframe rendering
gpu_mem=256
# Physical shutdown button (GPIO 3 to GND)
dtoverlay=gpio-shutdown,gpio_pin=3,active_low=1,pullup=on

```

---

## 🏃 Running the Pip-Boy

### Manual Start:

```bash
source venv/bin/activate
export SDL_VIDEODRIVER=kmsdrm
export SDL_VIDEOSYNC=0
python modules/main.py

```

### Automatic Start (on Boot):

1. Copy the provided `pipboy.service` to `/etc/systemd/system/`.
2. Enable the service:

```bash
sudo systemctl enable pipboy.service
sudo systemctl start pipboy.service

```

---

## 🕹 Controls & Calibration

* **Navigation:** Use [Arrow Keys] or [WASD] to switch tabs.
* **Resolution:** Default is optimized for **800x480**. Adjust in `modules/settings.py` if using a different screen.

---

### How to use this:

1. Create a new file in your project folder: `nano README.md`.
2. Paste the text above.
3. Replace `YOUR_USERNAME` with your actual GitHub handle.
4. **Commit and push** it to your fork:
```bash
git add README.md
git commit -m "Add detailed documentation for Pi 3 setup"
git push origin main

```


