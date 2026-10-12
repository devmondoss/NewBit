# EGAP010 – Acta de Constitución: VIGIA Industrial (SIDERPERU)

- **Fuente:** `Acta_Constitucion_VIGIA_Industrial_SIDERPERU.docx`
- **Semana:** 2 · **Tipo:** **entregable del equipo** (proyecto propio, el mismo que en otros documentos aparece como NewBit / VisionOps Industrial)
- **Versión 1.0 – 21/09/2026** · "Emisión inicial" · Hecho por Luis Elías / Anthony Lopez · Revisado por Valeria Rojas (Product Owner) · Aprobado por Ricardo Salcedo (propuesto)

## Código y nombre
**PY-001 – VIGIA Industrial**, plataforma de visión por computadora para convertir cámaras existentes en sensores inteligentes configurables, con piloto en SIDERPERU.

## Visión
Las operaciones industriales necesitan información oportuna sobre seguridad y comportamiento de procesos; la revisión manual de cámaras dificulta identificar eventos, su frecuencia y priorizar acciones por zona y horario. VIGIA permite conectar cámaras, delimitar zonas y elegir reglas para generar **eventos, métricas y alertas**. SIDERPERU (Chimbote) es el primer escenario propuesto; después podría adaptarse a fábricas, almacenes y centros logísticos.

## Requisitos

### Funcionales
1. Registrar **4 cámaras IP** existentes por **RTSP** y comprobar conexión. Crear hasta **8 zonas poligonales** con horarios y reglas configurables desde la web.
2. MVP: detectar **ausencia de casco o chaleco** e **ingreso a zonas restringidas**; ajustar confianza, permanencia mínima y supresión de alertas repetidas.
3. Generar eventos con cámara, zona, fecha, regla, confianza y evidencia visual; el supervisor puede **confirmar o descartar**.
4. Alertas en el panel y **por correo**; indicadores por período, zona y tipo; **exportar CSV**.
5. Usuarios con roles **administrador, supervisor y consulta**; registro de cambios de configuración y de acciones sobre eventos.

### No funcionales y de calidad
- Procesar localmente **4 flujos a ≥ 5 fps por cámara**; latencia evento → panel **p95 ≤ 5 s**.
- Disponibilidad **≥ 95 %** durante el piloto de 2 semanas (fallas de cámara y de red se reportan por separado).
- Acceso por roles y HTTPS/TLS; **evidencias cifradas**; **respaldo diario** con una restauración validada. Retención: evidencias **30 días**, métricas sin imágenes **180 días**.
- Versionar código, modelos, configuraciones y datasets. Interfaz responsiva; capacitación básica en **4 horas**.

## Alcance
MVP modular: un **nodo local** procesa las imágenes y envía metadatos y evidencias seleccionadas al sistema web. Las cámaras se reutilizan; las reglas se configuran por zona sin tocar el núcleo. **6 sprints de 2 semanas**, con 2 semanas de preparación antes y 2 de cierre después. Equipo ejecutor: **solo Luis Fernando Elias Salazar Diaz y Anthony Lopez Yrribarren**; el PO y el sponsor son interesados del caso propuesto.

### Límites
- Piloto en **2 zonas operativas** propuestas de SIDERPERU, **4 cámaras** y hasta **10 usuarios**; ubicaciones y acceso sujetos a validación institucional.
- MVP: casco, chaleco y zonas restringidas. **Lentes y guantes quedan fuera** (difíciles de observar, requieren datos específicos).
- Hoja de ruta posterior: proximidad persona–maquinaria, aforo, permanencia, tiempos operativos, conteo de productos, placas, vehículos, obstáculos. Humo y fuego: iniciativa de validación aparte.
- **Fuera:** reconocimiento facial, identificación individual, control de maquinaria, reemplazo del CCTV, integración con ERP, despliegue en toda la planta.
- Las alertas apoyan la supervisión humana; no son un sistema certificado de seguridad ni activan sanciones. El piloto es **en modo observación**.
- Imágenes solo con autorización y reglas de acceso/retención aprobadas. **Sin acceso a planta, una demo con datos autorizados no acredita la aceptación del piloto industrial.**

### Entregables clave
1. Acta, backlog priorizado, historias de usuario y criterios de aceptación.
2. Arquitectura, inventario de cámaras, matriz de zonas y protocolo de datos.
3. Dataset documentado (entrenamiento/validación/prueba), modelos y fichas de evaluación por clase.
4. MVP: conexión de cámaras, editor de zonas, motor de reglas, registro de eventos, alertas y panel analítico.
5. Informe del piloto, pruebas funcionales, de rendimiento y de seguridad, y limitaciones.
6. Repositorio, guía de despliegue, manual, capacitación y acta de cierre.

## Riesgos (con responsable)
| Riesgo | Respuesta | Resp. |
|---|---|---|
| Datos insuficientes o permisos tardíos | Gestionar acceso desde la semana 1; punto de decisión al final de la semana 2 | Luis |
| Polvo, oclusión e iluminación | Revisar cámaras, etiquetar casos locales, medir por condición | Luis |
| Saturación del nodo o caída de red | Prueba temprana de 4 flujos, cola local, ajustar resolución | Anthony |
| Exceso de falsas alertas | Calibrar umbrales y permanencia, deduplicar, validar con supervisores | Ambos |
| Exposición de imágenes o rechazo de trabajadores | Limitar acceso, informar, minimizar evidencias, borrado verificable | Anthony + TI |
| Sobrecarga del equipo o expansión de alcance | Priorizar el MVP; control de cambios | Luis + PO |

## Cronograma de hitos
| Hito | Inicio | Fin |
|---|---|---|
| Inicio, acta y validación de acceso al piloto | 21/09/2026 | 02/10/2026 |
| **Sprint 1:** requisitos, cámaras, arquitectura y protocolo de datos | **05/10/2026** | **16/10/2026** |
| Sprint 2: dataset inicial, conexión de flujos y línea base | 19/10 | 30/10 |
| Sprint 3: casco, chaleco y evaluación del modelo | 02/11 | 13/11 |
| Sprint 4: editor de zonas, reglas y eventos | 16/11 | 27/11 |
| Sprint 5: integración, alertas, panel y pruebas de carga | 30/11 | 11/12 |
| Sprint 6: piloto de 2 semanas y evaluación de aceptación | 14/12 | 25/12 |
| Ajustes, manuales, capacitación y entrega | 28/12 | 06/01/2027 |
| Revisión final y cierre | 07/01/2027 | 08/01/2027 |

Duración: 16 semanas. Los feriados se confirman antes del sprint 6.

## Recursos financieros
| Concepto | Base | Monto S/ |
|---|---|---|
| Luis: coordinación, datos y Computer Vision | 320 h × S/ 35 | 11,200.00 |
| Anthony: plataforma web, integración y pruebas | 320 h × S/ 30 | 9,600.00 |
| Nodo de inferencia | 1 equipo con accesorios | 2,800.00 |
| UPS y adecuación menor de red | 1 lote | 900.00 |
| Servidor web y BD del piloto | 4 meses × S/ 95 | 380.00 |
| Almacenamiento de evidencias | 4 meses × S/ 20 | 80.00 |
| Cómputo GPU temporal | Bolsa controlada | 600.00 |
| Dominio, correo y monitoreo | 4 meses | 240.00 |
| Visitas, instalación y capacitación | 4 jornadas × S/ 250 | 1,000.00 |
| Cámaras, portátiles y software abierto | Recursos existentes | 0.00 |
| **Subtotal** | | **26,800.00** |
| Contingencia 15 % | | 4,020.00 |
| **TOTAL** | | **30,820.00** |

S/ 20,800 son dedicación valorizada de los dos integrantes (20 h/semana × 16 semanas = 640 h). Si esa dedicación se aporta sin desembolso, la **caja máxima es S/ 10,020**. Sin sueldos de PO ni sponsor. TC presupuestal S/ 3.80; importes referenciales al 21/09/2026; tributos por validar.

## Interesados
| Interesado | Rol |
|---|---|
| Luis Fernando Elias Salazar Diaz | Líder y desarrollador de Computer Vision: coordina, prepara datos, valida modelos |
| Anthony Lopez Yrribarren | Full stack: web, integración, infraestructura, seguridad, pruebas |
| Valeria Rojas Medina | Product Owner **propuesto**; coordinadora de mejora operativa de SIDERPERU |
| Ricardo Salcedo Paredes | Sponsor **propuesto**; gerente de operaciones de SIDERPERU |
| Mariana Torres Cárdenas | Representante propuesta de SST: valida reglas y evidencias |
| Jorge Ponce Aguilar | Representante propuesto de TI: cámaras, red, despliegue, protección |
| Supervisores y trabajadores de zonas piloto | Usuarios y personas afectadas |

Nombres y cargos institucionales **ficticios** para el caso académico; no expresan vínculo ni aprobación real de SIDERPERU.

## Requisitos de aprobación
Éxito = demostración integral + informe de un piloto autorizado. Metas **propuestas**, no resultados:
- 4 cámaras y 8 zonas configuradas; flujo detección → evento → alerta → revisión → reporte completo.
- Casco, chaleco e intrusión: **precisión ≥ 90 % y sensibilidad ≥ 85 %** por tipo, en un conjunto de prueba independiente con **≥ 100 eventos positivos por tipo y 10 h de video negativo**.
- Evaluación **por eventos** (una alerta ↔ un evento real, tolerancia de 2 s); separar datos por **secuencia y día** (sin fotogramas del mismo video en entrenamiento y prueba); errores por cámara y condición.
- Rendimiento y disponibilidad con 4 flujos; **p95 medido sobre ≥ 200 eventos**.
- Pruebas funcionales críticas, permisos, respaldo y restauración aprobados; sin defectos críticos/altos abiertos.
- Documentación, repositorio y capacitación; el PO valida utilidad, SST las reglas, TI el despliegue; el sponsor formaliza la aceptación.
Si faltan datos o no se alcanzan los umbrales: se documenta la brecha y se acuerda corrección, reducción formal de alcance o cierre sin aceptación técnica.

## Criterios de culminación
- **Cierre normal:** entregables aceptados, indicadores documentados, observaciones resueltas, costos conciliados, transferencia de accesos/código/manuales; queda registrada la decisión de pasar o no a producción.
- **Cancelación/replanteo:** sin autorización de datos o cámaras, inviabilidad técnica, retiro del patrocinio o variación de costo/plazo no aprobada. El sponsor decide el cierre anticipado.

## Product Owner y sponsor
- **PO:** Valeria Rojas Medina · reporta a Ricardo Salcedo · prioriza el backlog, define criterios operativos, acepta o rechaza incrementos; **no autoriza ampliaciones presupuestales**. Avances semanales, revisión de incrementos cada 2 semanas; cambios de módulos, cámaras, presupuesto o fecha requieren decisión del sponsor.
- **Sponsor:** Ricardo Salcedo Paredes · SIDERPERU · gerente de operaciones (propuesto) · 21/09/2026. Estado: **propuesta académica**; la aprobación institucional y el acceso a cámaras deben formalizarse antes del piloto. Sin firmas de terceros.

## Análisis

- **Es un Acta muy sólida y honesta**: separa metas propuestas de resultados, dice que sin acceso a planta no se acredita el piloto, y define umbrales medibles, retención de datos, plan de respaldo y responsables por riesgo. Es notablemente más completa que el ejemplo del docente.
- **Cuentas verificadas:** 11,200 + 9,600 + 2,800 + 900 + 380 + 80 + 600 + 240 + 1,000 + 0 = **26,800**; 15 % = 4,020; total **30,820**; dedicación 20,800; caja máxima 10,020. Todo cuadra.
- **El alcance creció respecto al discovery y la presentación.** El discovery/PPT plantean **1 cámara · 1 zona · 1 regla (casco)**, RTSP "después" y 4 sprints. El Acta pide **4 cámaras por RTSP, 8 zonas, 3 reglas (casco, chaleco, zona restringida), alertas por correo, CSV, roles y 6 sprints**. Los documentos técnicos de `semana-03` y `semana-04` están escritos para el MVP 1-1-1; la propuesta es mantenerlo como **primer experimento (sprints 1–3)** y escalar a 4 cámaras/8 zonas hacia el sprint 5.
- **Exigencia de datos alta:** ≥ 100 eventos positivos por tipo y 10 h de video negativo requieren acceso real a cámaras o un dataset autorizado muy amplio. Es el riesgo central; el Acta ya fija una decisión al final de la semana 2 del proyecto (que coincide con el 02/10, ya pasada).
- **Estamos al inicio del Sprint 1** (05–16/10): requisitos, cámaras, arquitectura y protocolo de datos. Los entregables de ese sprint son exactamente el inventario de cámaras, la matriz de zonas y el protocolo de datos.
- **A resolver:** (1) código `PY-001` aquí vs `PY-CV-001` en Roles; (2) sin Scrum Master formal (la presentación pone a Luis); (3) el curso pide un Scrum Team de 1 PO + 1 SM + 3 developers en el ejemplo, y este equipo es de 2: confirmar con el docente cómo se evalúa; (4) la decisión de acceso al piloto del 02/10 no tiene evidencia en el repo.
