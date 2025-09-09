import csv
import requests
import urllib3
from itertools import islice
import os
import time

# Desactiva warnings por verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DOWNLOADS_DIR = "downloads"
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

# URL del endpoint
URL = "https://hiscli.comfamiliar.com:8888/api/v1/reporte/ordenamiento"

# Archivos de entrada/salida
CSV_FILE = "data.csv"
OUTPUT_FILE = "resultado.csv"

BATCH_SIZE = 10  # tamaño del batch
BATCH_SLEEP = 4  # segundos de espera entre lotes


def consumir_api(mrcodcons: str):
    """Hace el POST a la API y guarda el PDF si la respuesta es exitosa."""
    payload = {"mrcodcons": int(mrcodcons)}
    try:
        response = requests.post(URL, json=payload, timeout=30, verify=False)

        if response.status_code == 200:
            # Guardar PDF
            filename = os.path.join(DOWNLOADS_DIR, f"{mrcodcons}.pdf")
            with open(filename, "wb") as f:
                f.write(response.content)
            return ("OK", f"PDF guardado correctamente en {filename}")
        else:
            return (
                "ERROR",
                f"HTTP {response.status_code}. Respuesta: {response.text.strip()}",
            )

    except requests.exceptions.RequestException as e:
        return ("ERROR", f"Error de conexión: {e}")


def batch_iterator(iterable, size):
    """Genera listas de tamaño 'size' a partir de un iterable."""
    it = iter(iterable)
    for first in it:
        batch = [first] + list(islice(it, size - 1))
        yield batch


def main():
    resultados = []

    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        mrcodcons_list = [row["mrcodcons"] for row in reader if row.get("mrcodcons")]

        for i, batch in enumerate(batch_iterator(mrcodcons_list, BATCH_SIZE), start=1):
            print(f"=== Procesando batch {i} con {len(batch)} registros ===")
            for mrcodcons in batch:
                mensaje, observacion = consumir_api(mrcodcons)
                resultados.append([mrcodcons, mensaje, observacion])

            # Espera entre lotes
            print(f"⏳ Esperando {BATCH_SLEEP} segundos antes del siguiente batch...")
            time.sleep(BATCH_SLEEP)

    # Guardar resultados en CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["mrcodcons", "mensaje", "observacion"])
        writer.writerows(resultados)

    print(f"🏁 Procesamiento finalizado. Resultados guardados en {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
