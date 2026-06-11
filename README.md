# PyCam

PyCam is a lightweight Python-based camera monitoring system that uses computer vision to detect motion, record important events, and manage storage efficiently.

It is designed for local-first usage, making it ideal for laptops, Raspberry Pi setups, and simple camera-based monitoring projects.

---

## 🚀 Features

* Real-time camera streaming using OpenCV
* Motion detection using frame analysis
* Event-based video recording
* Automatic snapshot capture
* Timestamp overlay on video
* Storage-aware recording system (SD card / disk monitoring)
* Lightweight and fast execution

---

## 🎯 Purpose

PyCam is built to explore practical computer vision concepts such as:

* Motion detection algorithms
* Real-time video processing
* Event-driven recording systems
* Edge-device monitoring

It can be used for:

* Home monitoring setups
* Pet / habitat observation (e.g., reptiles, aquariums)
* Security and awareness systems
* Computer vision learning projects

---

## 🧠 How It Works

1. Camera feed is captured using OpenCV
2. Frames are continuously compared for motion detection
3. When motion is detected:

   * Video recording starts or continues
   * Snapshots may be saved
4. When no motion is detected:

   * Unnecessary clips may be discarded (optional logic)
5. Storage usage is monitored to prevent overflow

---

## 📦 Installation

Clone the repository:

```bash id="c1k2aa"
git clone https://github.com/YOUR_USERNAME/PyCam.git
cd PyCam
```

Install dependencies:

```bash id="k9x2bb"
pip install -r requirements.txt
```

Run the project:

```bash id="p3m8cc"
python main.py
```

---

## 📁 Project Structure

```text id="z8n1dd"
PyCam/
├── main.py
├── requirements.txt
├── recordings/
├── snapshots/
├── logs/
└── README.md
```

---

## ⚙️ Configuration

You can adjust core settings inside `main.py`:

* Motion sensitivity threshold
* Recording duration per clip
* Storage path (SD card / disk)
* Notification settings

---

## 📸 Example Output

When motion is detected, PyCam:

* Draws bounding regions on movement
* Displays “MOTION DETECTED”
* Saves video clips with timestamps
* Stores snapshots for review

---

## 🛣️ Roadmap

* [x] Motion detection
* [x] Video recording system
* [x] Snapshot capture
* [ ] AI-based object detection (person / animal)
* [ ] Mobile companion app (Android)
* [ ] Live remote streaming
* [ ] Web dashboard
* [ ] Multi-camera support
* [ ] Cloud backup option

---

## 🤝 Contributing

Contributions are welcome.

If you'd like to help improve PyCam, you can:

* Fork the repository
* Create a feature branch
* Submit a pull request

Ideas and bug reports are also appreciated.

---

## ⚠️ Disclaimer

PyCam is intended for educational and personal monitoring use only. Users are responsible for ensuring compliance with local laws and privacy regulations when using camera-based systems.

---

## 📜 License

MIT License — free to use, modify, and distribute.
