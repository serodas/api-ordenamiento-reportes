# 📂 CSV Reader & File Downloader (Paramiko + Docker)

Este proyecto permite descargar archivos desde un servidor remoto **via SSH/SFTP** a partir de un archivo **CSV** que contiene la información de las facturas y documentos asociados.  
Los archivos se organizan en carpetas locales según el número de factura y conservan la extensión original.

---

## ⚙️ Requisitos

- Python 3.9+
- Docker y Docker Compose

Dependencias Python:
- `paramiko`
- `python-dotenv`

---

## 📑 Estructura del CSV

El archivo CSV debe tener las siguientes columnas obligatorias:

| Columna           | Descripción                          |
|-------------------|--------------------------------------|
| `BECODBENE`       | Código del beneficiario              |
| `NOMBRE_DOCUMENTO`| Nombre del archivo en el servidor    |
| `FACTURA`         | Número de la factura asociada        |

Ejemplo `facturas.csv`:

```csv
BECODBENE,NOMBRE_DOCUMENTO,FACTURA
123,documento1.pdf,INV001
123,documento2.xml,INV001
456,archivo3.pdf,INV002
```

## 🔧 Configuración
El proyecto incluye un archivo .env.local de ejemplo.

Cópialo como .env antes de ejecutar:
```bash
cp .env.local .env
```

## 🚀 Uso

Ejecuta el script para descargar los archivos:

```bash
docker compose up
```
