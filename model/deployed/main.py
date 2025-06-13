from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
import torch
from ultralytics import YOLO

app = FastAPI()

# Lokasi model
MODEL_PATH = "my_model.pt"

# Inisialisasi model (gunakan CPU)
model = None

@app.on_event("startup")
async def load_model_on_startup():
    global model
    try:
        model = YOLO(MODEL_PATH).to("cpu")  # <<< PENTING: pastikan pakai CPU
        print("Model YOLOv11 berhasil dimuat di CPU.")
    except Exception as e:
        print(f"Error memuat model: {e}")
        raise

@app.post("/detect/")
async def predict_uang(file: UploadFile = File(...)):
    if model is None:
        return {"error": "Model belum dimuat."}

    try:
        image_bytes = await file.read()
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        results = model.predict(source=img, conf=0.5, iou=0.7, verbose=False)

        best_nominal = "Nominal tidak terdeteksi"
        best_confidence = 0.0

        if results and len(results) > 0:
            detections = results[0]

            if detections.boxes is not None and len(detections.boxes) > 0:
                scores = detections.boxes.conf
                labels = detections.boxes.cls

                nominal_names = {
                    0: "seratus ribu rupiah",
                    1: "sepuluh ribu rupiah",
                    2: "seribu rupiah",
                    3: "dua puluh ribu rupiah",
                    4: "dua ribu rupiah",
                    5: "lima puluh ribu rupiah",
                    6: "lima ribu rupiah"
                }

                max_score_index = torch.argmax(scores).item()
                best_confidence = scores[max_score_index].item()
                predicted_class_id = labels[max_score_index].item()

                best_nominal = nominal_names.get(predicted_class_id, f"ID tidak dikenal: {predicted_class_id}")

        return {
            "nominal_uang": best_nominal,
            "confidence": best_confidence
        }

    except Exception as e:
        print(f"Error saat prediksi: {e}")
        return {"error": f"Terjadi kesalahan saat prediksi: {e}"}
