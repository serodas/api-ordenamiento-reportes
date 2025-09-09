# 📄 HISCLI Batch Reporter

Este proyecto permite procesar un archivo CSV con códigos `mrcodcons`, consultar la API de **HISCLI**, descargar los PDFs resultantes y generar un reporte en formato CSV con el estado de cada consulta.

---

## 🚀 Funcionalidad

- Lee un archivo CSV de entrada (`data.csv`) con una columna llamada `mrcodcons`.
- Envía solicitudes **POST** en lotes (batching) de 10 en 10 hacia la API: https://hiscli.comfamiliar.com:8888/api/v1/reporte/ordenamiento
- Guarda los **PDFs** en la carpeta `downloads/`.
- Genera un archivo `resultado.csv` con tres columnas:
- `mrcodcons`
- `mensaje` → `OK` o `ERROR`
- `observacion` → detalle del éxito o error.
- Entre cada batch se aplica un **delay de 4 segundos** para no saturar la API.

---

## 📂 Estructura de salida

- `downloads/` → carpeta con todos los PDFs descargados.
- `resultado.csv` → archivo de resumen con estado de cada código.

Ejemplo de `resultado.csv`:

```csv
mrcodcons,mensaje,observacion
56794062,ERROR,HTTP 500. Respuesta: ...
56790671,ERROR,Error de conexión: Expecting value...
56828352,OK,PDF guardado correctamente en downloads/56828352.pdf
```

## 🚀 Uso

Ejecuta el script para descargar los archivos:

```bash
docker compose up
```
