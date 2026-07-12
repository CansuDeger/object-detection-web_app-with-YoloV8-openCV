from flask import Flask, request, render_template, url_for
from ultralytics import YOLO
import os, uuid, shutil

app = Flask(__name__)
model = YOLO('best.pt')

UPLOAD_FOLDER = 'static/uploads'
TAHMIN_FOLDER = 'static/tahmin'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TAHMIN_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    sonuc = None
    tahmin_yolu = None
    bocek_sayisi = 0

    if request.method == 'POST':
        dosya = request.files.get('goruntu')
        if dosya:
            # Dosyayı kaydet
            dosya_adi = f'{uuid.uuid4().hex}.jpg'
            kayit_yolu = os.path.join(UPLOAD_FOLDER, dosya_adi)
            dosya.save(kayit_yolu)

            # Tahmin yap
            results = model.predict(
                source      = kayit_yolu,
                conf        = 0.50,
                iou         = 0.45,
                save        = True,
                show_labels = True,
                show_conf   = True,
                project     = 'static/tahmin_temp',
                name        = 'result',
                exist_ok    = True,
            )

            # Tahmin edilen dosyanın gerçek yolunu bul
            save_dir = results[0].save_dir
            tahmin_kaynak = os.path.join(save_dir, dosya_adi)

            # static/tahmin/ klasörüne kopyala
            tahmin_hedef = os.path.join(TAHMIN_FOLDER, dosya_adi)
            if os.path.exists(tahmin_kaynak):
                shutil.copy(tahmin_kaynak, tahmin_hedef)
            else:
                # Uzantı farklı olabilir, klasördeki ilk dosyayı al
                dosyalar = os.listdir(save_dir)
                if dosyalar:
                    shutil.copy(
                        os.path.join(save_dir, dosyalar[0]),
                        tahmin_hedef
                    )

            bocek_sayisi = len(results[0].boxes)
            tahmin_yolu  = f'tahmin/{dosya_adi}'

            sonuc = {
                'bocek_sayisi' : bocek_sayisi,
                'mesaj'        : f'{bocek_sayisi} patates böceği tespit edildi!' if bocek_sayisi > 0 else 'Böcek tespit edilmedi.',
                'tehlike'      : 'yüksek' if bocek_sayisi > 5 else 'orta' if bocek_sayisi > 0 else 'yok',
            }

    return render_template('index.html', sonuc=sonuc, tahmin_yolu=tahmin_yolu)

if __name__ == '__main__':
    app.run(debug=True)