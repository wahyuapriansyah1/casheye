# 🌿 Capstone Project — Casheye 

## Deskripsi
Casheye adalah aplikasi berbasis web yang membantu tunanetra mengenali uang menggunakan kamera. Aplikasi ini sudah mendukung Progressive Web App (PWA), sehingga bisa di-install di HP/PC seperti aplikasi native.

## Struktur Repository
Repository ini terdiri dari tiga bagian:

```
casheye/
├── frontend/    # Frontend (HTML, CSS, JS, PWA)
├── backend/     # Backend Laravel (REST API)
└── model/       # Model AI (PyTorch, YOLOv5, Python)
```

## Teknologi yang Digunakan
- **Frontend:** HTML, CSS, JavaScript (PWA)
- **Backend:** Laravel 10.x (REST API)
- **Model AI:** PyTorch, YOLOv5 (Python)
- **Deployment:**
  - Frontend: Static Hosting (Vercel/Netlify/Manual)
  - Backend: VPS/Server Pribadi/Laragon/XAMPP
  - Model: Python (YOLOv5), bisa di-deploy via Colab/Server

## Cara Menjalankan Lokal
### 1. Clone Repo
```bash
git clone <repo-url>
cd casheye
```

### 2. Menjalankan Backend
```bash
cd backend
cp .env.example .env
composer install
php artisan key:generate
php artisan migrate
php artisan serve
```

### 3. Menjalankan Frontend
```bash
cd ../frontend
# Jika ingin build ulang asset:
npm install
npm run build
# Untuk development:
npm run dev -- --host
```

### 4. Menjalankan Model AI (YOLOv5)
- Buka folder `model/`.
- Jalankan notebook `casheye_yolov5.ipynb` di Google Colab atau Jupyter.
- Ikuti instruksi di notebook untuk serving model.

## Struktur Branch
- **main:** branch utama untuk production-ready code.

## 🚀 Cara Menjalankan Model di Google Colab
1. Buka file notebook `casheye_yolov5.ipynb` di Google Colab.
2. Install dependencies:
   ```python
   !pip install -r requirements.txt
   ```
3. Mount Google Drive (jika perlu):
   ```python
   from google.colab import drive
drive.mount('/content/drive')
   ```
4. Jalankan sel untuk serving model dan endpoint prediksi.
5. (Opsional) Expose API dengan Ngrok:
   ```python
   from pyngrok import ngrok
   ngrok.set_auth_token("TOKEN_NGROK_KAMU")
   public_url = ngrok.connect(8000).public_url
   print(f"🌍 API dapat diakses di: {public_url}/docs")
   ```

## Endpoint Prediksi
- **POST /predict**
- **Form Data:**
  - `file` (image): File gambar uang
- **Response:**
  ```json
  {
    "label": "Rp 50.000",
    "confidence": 0.9823,
    "response_time": 0.345
  }
  ```

## Deployed Site
- https://www.casheye.my.id

## Dataset
- https://drive.google.com/drive/folders/1Am0qwBWsX9ZzIrIpQ2LzS2gilUxq-oID

## Video Presentation
- https://youtu.be/Yih2nWa8bfA

## Presentation Slides
- https://docs.google.com/presentation/d/14HF9PNM1O3lZnqoVAn0lX08RHu033ZV1/edit?usp=drivesdk&ouid=111271282451661208350&rtpof=true&sd=true
---

## Kebutuhan Sistem
- PHP: 8.2.28
- Composer: 2.x
- Web Server: XAMPP/Laragon
- Node.js: 18.x (opsional, untuk build asset)
- NPM: 9.x (opsional)
- Laravel: 10.x
- Web Browser: Chrome/Edge/Firefox
- OS: Windows, Linux, atau MacOS

## Struktur Penting
- `public/manifest.json` : Konfigurasi PWA
- `public/service-worker.js` : Service worker PWA
- `public/js/` : File JS frontend
- `public/css/` : File CSS frontend
- `resources/views/` : File Blade (HTML)
- `routes/web.php` : Routing utama

## Tools yang Digunakan
- Laravel 10.x
- Bootstrap 5.3.x
- PHP 8.2.28
- Composer 2.x
- (Opsional) Node.js 18.x & NPM 9.x
- XAMPP/Laragon (webserver)

## Catatan
- Untuk fitur kamera, gunakan browser yang mendukung akses kamera (Chrome/Edge/Firefox).
- Untuk update icon PWA, ganti file di `public/img/logo.png` dan update `manifest.json` jika perlu.
- Jika ada error permission kamera di HP, pastikan sudah memberi izin akses kamera di browser.

## Kontribusi
Pull request dan issue sangat diterima!
