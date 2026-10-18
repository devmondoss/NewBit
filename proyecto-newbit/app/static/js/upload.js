/**
 * NewBit - Módulo de carga asíncrona de videos y gestión de catálogo (Sprint 1: HU01 / HU03)
 */

document.addEventListener('DOMContentLoaded', () => {
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('file-input');
    const progressContainer = document.getElementById('upload-progress-container');
    const progressBar = document.getElementById('upload-progress-bar');
    const progressPercent = document.getElementById('upload-progress-percent');
    const uploadStatus = document.getElementById('upload-status-text');

    if (!dropzone || !fileInput) return;

    // Prevención de comportamientos predeterminados del navegador
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    // Efectos visuales de arrastre
    ['dragenter', 'dragover'].forEach(eventName => {
        dropzone.addEventListener(eventName, () => {
            dropzone.classList.add('border-blue-500', 'bg-blue-500/10');
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, () => {
            dropzone.classList.remove('border-blue-500', 'bg-blue-500/10');
        }, false);
    });

    // Manejo de archivo soltado
    dropzone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files.length > 0) {
            handleFileUpload(files[0]);
        }
    });

    // Manejo de archivo seleccionado con explorador
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFileUpload(e.target.files[0]);
        }
    });

    function handleFileUpload(file) {
        // 1. Validación de extensión en cliente
        const allowedExts = ['.mp4', '.avi'];
        const fileName = file.name.toLowerCase();
        const isValidExt = allowedExts.some(ext => fileName.endsWith(ext));

        if (!isValidExt) {
            alert('Formato no permitido. Solo se aceptan archivos .mp4 y .avi.');
            return;
        }

        // 2. Validación de tamaño (Máx 100 MB)
        const maxSize = 100 * 1024 * 1024;
        if (file.size > maxSize) {
            alert('El archivo supera el tamaño máximo permitido de 100 MB.');
            return;
        }

        // 3. Iniciar carga con barra de progreso
        progressContainer.classList.remove('hidden');
        uploadStatus.innerText = `Subiendo "${file.name}"...`;
        progressBar.style.width = '0%';
        progressPercent.innerText = '0%';

        const formData = new FormData();
        formData.append('file', file);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/videos/upload', true);

        xhr.upload.onprogress = (e) => {
            if (e.lengthComputable) {
                const percentComplete = Math.round((e.loaded / e.total) * 100);
                progressBar.style.width = `${percentComplete}%`;
                progressPercent.innerText = `${percentComplete}%`;
                if (percentComplete === 100) {
                    uploadStatus.innerText = 'Procesando metadatos con OpenCV en el servidor...';
                }
            }
        };

        xhr.onload = () => {
            if (xhr.status === 201) {
                const res = JSON.parse(xhr.responseText);
                uploadStatus.innerText = `¡Video cargado con éxito! Recargando catálogo...`;
                progressBar.classList.remove('bg-blue-600');
                progressBar.classList.add('bg-emerald-500');
                setTimeout(() => {
                    window.location.reload();
                }, 800);
            } else {
                let errMsg = 'Error al subir el archivo.';
                try {
                    const errRes = JSON.parse(xhr.responseText);
                    errMsg = errRes.detail || errMsg;
                } catch (e) {}
                uploadStatus.innerText = `Error: ${errMsg}`;
                progressBar.classList.add('bg-red-500');
            }
        };

        xhr.onerror = () => {
            uploadStatus.innerText = 'Error de conexión con el servidor.';
            progressBar.classList.add('bg-red-500');
        };

        xhr.send(formData);
    }
});

// Función global para eliminación de videos
async function deleteVideo(videoId, videoName) {
    if (!confirm(`¿Estás seguro de que deseas eliminar permanentemente el video "${videoName}" y todos sus fotogramas extraídos?`)) {
        return;
    }

    try {
        const response = await fetch(`/api/videos/${videoId}`, {
            method: 'DELETE',
        });

        if (response.ok) {
            const row = document.getElementById(`video-row-${videoId}`);
            if (row) {
                row.remove();
            } else {
                window.location.reload();
            }
            // Actualizar si la tabla quedó vacía
            const tableBody = document.getElementById('videos-table-body');
            if (tableBody && tableBody.children.length === 0) {
                window.location.reload();
            }
        } else {
            const data = await response.json();
            alert(`No se pudo eliminar el video: ${data.detail || 'Error desconocido'}`);
        }
    } catch (err) {
        alert(`Error al comunicarse con el servidor: ${err.message}`);
    }
}
