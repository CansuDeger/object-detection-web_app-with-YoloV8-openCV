# 🥔 Patates Böceği Tespit Sistemi

YOLOv8 tabanlı derin öğrenme modeli ile patates böceği (*Leptinotarsa decemlineata*) tespiti yapan web uygulaması.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📸 Uygulama Görseli

> Kullanıcı fotoğraf yükler → Model böcekleri tespit eder → Sonuç kutucuklarla işaretlenerek gösterilir.

---

## 🎯 Proje Hakkında

Bu proje, tarım alanlarında patates böceği tespitini otomatize etmek amacıyla geliştirilmiştir. Kullanıcı bir bitki fotoğrafı yükler, YOLOv8 modeli böcekleri gerçek zamanlı olarak tespit eder ve tehlike seviyesini belirtir.

### Özellikler

- Fotoğraf yükleme ile anlık böcek tespiti
- Tespit edilen böcek sayısına göre tehlike seviyesi (Yok / Orta / Yüksek)
- Böceklerin bounding box ile işaretlenmiş görüntüsü
- Sade ve kullanıcı dostu arayüz
- %50 altı güven skorlu tespitleri filtreleme

---

## 🧠 Model Bilgileri

| Özellik | Değer |
|---|---|
| Model | YOLOv8m |
| Sınıf sayısı | 1 (patates_bocegi) |
| Eğitim görüntüsü | 1319 |
| Validation görüntüsü | 376 |
| Test görüntüsü | 181 |
| Epochs | 100 |
| Image size | 640 |
| mAP50 | 0.857 |
| mAP50-95 | 0.387 |
| Precision | 0.800 |
| Recall | 0.815 |
| GPU | NVIDIA T4 / A100 |

---

## 📁 Klasör Yapısı

```
patates-bocegi-tespit/
├── app.py                  # Flask backend
├── best.pt                 # Eğitilmiş YOLOv8 modeli
├── requirements.txt        # Gerekli kütüphaneler
├── templates/
│   └── index.html          # Web arayüzü
└── static/
    ├── uploads/            # Yüklenen fotoğraflar
    └── tahmin/             # Tahmin sonuçları
```

---

## ⚙️ Kurulum

### Gereksinimler

- Python 3.10+
- pip

### Adımlar

```bash
# 1. Repoyu klonla
git clone https://github.com/kullaniciadi/patates-bocegi-tespit.git
cd patates-bocegi-tespit

# 2. Sanal ortam oluştur (opsiyonel ama önerilir)
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# 3. Kütüphaneleri yükle
pip install -r requirements.txt

# 4. Modeli yerleştir
# best.pt dosyasını ana klasöre koy

# 5. Uygulamayı başlat
python app.py
```

Tarayıcıda aç: **http://127.0.0.1:5000**

---

## 📦 requirements.txt

```
flask
ultralytics
pillow
```

---

## 🚀 Kullanım

1. Tarayıcıda `http://127.0.0.1:5000` adresine git
2. **Tıkla veya sürükle** alanına bitki fotoğrafı yükle
3. **Böcek Tespiti Yap** butonuna tıkla
4. Sonucu gör:
   - 🟢 **Böcek yok** — Tarlada sorun görünmüyor
   - 🟡 **Az böcek** — Takip edin
   - 🔴 **Çok böcek** — İlaçlama önerilir

---

## 🏋️ Modeli Yeniden Eğitmek

Google Colab'da eğitmek için:

```python
from ultralytics import YOLO

model = YOLO('yolov8m.pt')

model.train(
    data    = 'dataset/dataset.yaml',
    epochs  = 100,
    imgsz   = 640,
    batch   = 16,
    device  = 0,
)
```

### Dataset Yapısı

```
dataset/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
└── dataset.yaml
```

### dataset.yaml

```yaml
path: ./dataset
train: train/images
val: valid/images
test: test/images

nc: 1
names: ['patates_bocegi']
```

---

## 📊 Eğitim Sonuçları

| Epoch | mAP50 | mAP50-95 | Precision | Recall |
|---|---|---|---|---|
| 1 | 0.553 | 0.189 | 0.552 | 0.602 |
| 50 | 0.862 | 0.375 | 0.796 | 0.816 |
| 100 | 0.857 | 0.387 | 0.800 | 0.815 |

---

## 🛠️ Teknolojiler

- **[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)** — Nesne tespiti modeli
- **[Flask](https://flask.palletsprojects.com/)** — Python web framework
- **[OpenCV](https://opencv.org/)** — Görüntü işleme
- **[Google Colab](https://colab.research.google.com/)** — Model eğitimi (T4/A100 GPU)

---

## 🌍 İnternete Açmak

### Railway.app (Ücretsiz)

```bash
# Railway CLI kur
npm install -g @railway/cli

# Login
railway login

# Deploy
railway up
```

### Ngrok (Geçici)

```bash
pip install pyngrok
ngrok http 5000
```




