/**
 * NewBit - Control interactivo de calibración de umbrales YOLOv8 (Sprint 2: HU11)
 */

document.addEventListener('DOMContentLoaded', () => {
    const sliderConf = document.getElementById('slider-confidence');
    const valConf = document.getElementById('val-confidence');

    const sliderIou = document.getElementById('slider-iou');
    const valIou = document.getElementById('val-iou');

    const sliderFps = document.getElementById('slider-fps');
    const valFps = document.getElementById('val-fps');

    const badgeSensitivity = document.getElementById('sensitivity-badge');
    const form = document.getElementById('calibration-form');
    const btnSave = document.getElementById('btn-save-calibration');
    const btnReset = document.getElementById('btn-reset-calibration');
    const saveStatus = document.getElementById('save-status');

    if (!sliderConf || !sliderIou || !sliderFps) return;

    // Actualización dinámica de valores y badges
    function updateConfidenceVisuals() {
        const conf = parseFloat(sliderConf.value);
        valConf.innerText = conf.toFixed(2);

        if (conf < 0.35) {
            badgeSensitivity.innerText = 'Sensibilidad Alta · Poca Luz / Nocturno';
            badgeSensitivity.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-purple-500/10 text-purple-300 border border-purple-500/20';
        } else if (conf <= 0.65) {
            badgeSensitivity.innerText = 'Sensibilidad Equilibrada · Recomendada';
            badgeSensitivity.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-blue-500/10 text-blue-300 border border-blue-500/20';
        } else {
            badgeSensitivity.innerText = 'Sensibilidad Estricta · Alta Iluminación';
            badgeSensitivity.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/20';
        }
    }

    function updateIouVisuals() {
        valIou.innerText = parseFloat(sliderIou.value).toFixed(2);
    }

    function updateFpsVisuals() {
        valFps.innerText = parseFloat(sliderFps.value).toFixed(1) + ' FPS';
    }

    sliderConf.addEventListener('input', updateConfidenceVisuals);
    sliderIou.addEventListener('input', updateIouVisuals);
    sliderFps.addEventListener('input', updateFpsVisuals);

    // Inicializar visuales al cargar
    updateConfidenceVisuals();
    updateIouVisuals();
    updateFpsVisuals();

    // Guardado asíncrono sin recarga
    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            btnSave.disabled = true;
            btnSave.innerHTML = `<svg class="animate-spin w-4 h-4 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg> <span>Guardando...</span>`;

            const payload = {
                confidence: parseFloat(sliderConf.value),
                iou: parseFloat(sliderIou.value),
                target_fps: parseFloat(sliderFps.value),
                changed_by: document.getElementById('input-user')?.value || 'Jorge (TI)',
                note: document.getElementById('input-note')?.value || 'Calibración manual de planta',
            };

            try {
                const response = await fetch('/api/calibration', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload),
                });
                const data = await response.json();

                if (response.ok) {
                    saveStatus.classList.remove('hidden');
                    saveStatus.innerText = '¡Parámetros calibrados y guardados con éxito!';
                    setTimeout(() => {
                        window.location.reload();
                    }, 800);
                } else {
                    alert(`Error al guardar: ${data.detail || 'Fallo desconocido'}`);
                    btnSave.disabled = false;
                    btnSave.innerHTML = `<span>Guardar Calibración</span>`;
                }
            } catch (err) {
                alert(`Error de red: ${err.message}`);
                btnSave.disabled = false;
                btnSave.innerHTML = `<span>Guardar Calibración</span>`;
            }
        });
    }

    // Botón de restablecimiento
    if (btnReset) {
        btnReset.addEventListener('click', async () => {
            if (!confirm('¿Deseas restablecer los umbrales a los valores predeterminados de fábrica (Confianza: 0.50, IoU: 0.45, FPS: 5.0)?')) {
                return;
            }

            try {
                const response = await fetch('/api/calibration/reset', { method: 'POST' });
                if (response.ok) {
                    window.location.reload();
                } else {
                    alert('Error al restablecer valores de fábrica.');
                }
            } catch (err) {
                alert(`Error de red: ${err.message}`);
            }
        });
    }
});
