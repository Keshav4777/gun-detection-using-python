# gun-detection-using-python
it's basically a mini project of python 
Here you go Alpha’l Sourish — a clean, professional **README.md** file for your *Weapon (Gun) Detection using Python + OpenCV* project.
You can directly paste this into your **GitHub** or **YouTube Description**.

---

# 🚨 Weapon Detection System using Python & OpenCV

This project detects **guns/weapons** in **real-time webcam**, **images**, and **video files** using **Haar Cascade Classifier** with OpenCV.
It highlights detected weapons with bounding boxes and displays real-time FPS.

---

## 🔥 Features

* ✔ Real-time **Webcam Weapon Detection**
* ✔ Detect guns in **images**
* ✔ Detect guns in **video files**
* ✔ Displays **FPS** (Frames Per Second)
* ✔ Simple to use — **3 modes**
* ✔ Uses OpenCV Haar Cascade
* ✔ Works on any device with a webcam

---

## 📂 Project Structure

```
/Weapon-Detection/
│── gun_cascade.xml       # Haar cascade file (must be in same folder)
│── weapon_detect.py      # Main Python file
│── README.md             # Documentation
```

---

## 🛠 Requirements

Make sure you have Python installed (3.7+ recommended).

Install required libraries:

```bash
pip install opencv-python
pip install imutils
```

---

## ▶️ How to Run

### **Step 1:** Download or clone this project

```bash
git clone https://github.com/yourusername/weapon-detection.git
cd weapon-detection
```

### **Step 2:** Make sure `gun_cascade.xml` is in the same folder.

### **Step 3:** Run the Python file

```bash
python weapon_detect.py
```

### **Step 4:** Choose a mode:

```
1 → Webcam Mode
2 → Image Detection
3 → Video File Detection
```

---

## 🖥️ Modes Explained

### **1️⃣ Webcam Mode**

* Opens your webcam
* Detects guns live
* Press **ESC** to exit

### **2️⃣ Image Mode**

* Give image path
* Detects guns in the image

### **3️⃣ Video Mode**

* Enter video path
* Detects weapons frame-by-frame
* Press **ESC** to exit

---

## 📌 Code Used (Main Script)

Your full Python code is already included in the repo.
You can paste the entire script into a file named:

```
weapon_detect.py
```

---

## ❗ Why Haar Cascade?

* Haar Cascades are fast
* Lightweight
* Runs smoothly even on low-end PCs
* Detects trained objects based on the XML file

However, it may not be 100% accurate.
For advanced accuracy, you can upgrade to **YOLOv8 / YOLO-NAS** later.

---

## 📸 Output Example

✔ Bounding boxes around gun
✔ “Weapon Detected” warning
✔ FPS display

---

## 🚀 Future Improvements

* Replace Haar cascade with **YOLO** for better accuracy
* Add sound alarm when weapon detected
* Add logging & email alerts
* Add recording feature

---

## 🤝 Contributing

Pull requests and improvements are welcome!

---

## 📄 License

This project is open-source.
Feel free to use it for learning, projects, and tutorials.

---


