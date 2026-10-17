"""
Smoke test de verificación del entorno NewBit (Paso D-01).
Verifica compatibilidad de versiones, librerías base y motor de inferencia.
"""

import sys
import importlib

def check_component(name, import_path, version_attr="__version__"):
    try:
        mod = importlib.import_module(import_path)
        ver = getattr(mod, version_attr, "Instalado (sin atributo __version__)")
        return True, ver
    except Exception as e:
        return False, str(e)

def main():
    print("=" * 60)
    print(" NEWBIT - VERIFICACIÓN DE ENTORNO DE DESARROLLO (PASO D-01)")
    print("=" * 60)
    print(f"Intérprete Python: {sys.version.split()[0]} ({sys.executable})")
    print("-" * 60)

    checks = [
        ("FastAPI", "fastapi"),
        ("Uvicorn", "uvicorn"),
        ("Jinja2", "jinja2"),
        ("Python-Multipart", "multipart"),
        ("Aiofiles", "aiofiles"),
        ("OpenCV", "cv2"),
        ("NumPy", "numpy"),
        ("Pillow", "PIL"),
        ("Pydantic", "pydantic"),
        ("PyTorch", "torch"),
        ("Ultralytics YOLO", "ultralytics"),
    ]

    all_passed = True
    for name, module_name in checks:
        ok, detail = check_component(name, module_name)
        status = "[OK]" if ok else "[ERROR]"
        print(f"{status:<8} {name:<22}: {detail}")
        if not ok:
            all_passed = False

    print("-" * 60)

    # Verificación de aceleración por hardware
    try:
        import torch
        cuda_avail = torch.cuda.is_available()
        device_name = torch.cuda.get_device_name(0) if cuda_avail else "CPU (Ejecución estándar)"
        print(f"[INFO]   Dispositivo de cómputo : {device_name} (CUDA={cuda_avail})")
    except Exception as e:
        print(f"[WARN]   No se pudo verificar acelerador: {e}")

    # Verificación de instanciación de YOLOv8
    try:
        from ultralytics import YOLO
        print("[INFO]   Comprobando carga de arquitectura YOLOv8...")
        # Instanciar arquitectura ligera en memoria
        model = YOLO("yolov8n.pt")
        print(f"[OK]     Modelo YOLOv8 inicializado correctamente: {model.task}")
    except Exception as e:
        print(f"[ERROR]  Fallo al instanciar YOLOv8: {e}")
        all_passed = False

    print("=" * 60)
    if all_passed:
        print(">> RESULTADO: Todos los componentes están operativos y compatibles.")
        print("=" * 60)
        sys.exit(0)
    else:
        print(">> RESULTADO: Se encontraron errores en la configuración del entorno.")
        print("=" * 60)
        sys.exit(1)

if __name__ == "__main__":
    main()
