# Traffic Density Monitoring

## 📌 Aim
Detect vehicles from aerial drone footage using OpenCV background subtraction and contours and classify traffic density.

## 📍 Technologies Used
- Python
- OpenCV
- NumPy

## 🧠 Method
1. Read video frames.
2. Apply background subtraction (MOG2).
3. Threshold foreground mask.
4. Remove noise using morphological operations.
5. Detect contours.
6. Filter by contour area to detect vehicles.
7. Count vehicles.
8. Classify density as Low / Medium / High.

## 🟢 Output
- Vehicles are detected via bounding boxes.
- Traffic density label shown on frames.
- Foreground mask shows motion regions.

## ⚠️ Limitations
- Background subtraction only detects moving objects.
- Stationary traffic may not be counted.
- Detection can be affected by lighting, shadows, camera movement.

## 📁 Files
- `main.py` — Source code for detection.
- `Traffic_Density_Monitoring_Report.docx` — Word report.

## 📝 License
This project is open-source and free to use.
