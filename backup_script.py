import os
import shutil
from datetime import datetime

def respaldar_archivos_php(origen_dir, destino_dir):
    # Verificar si el directorio origen existe
    if not os.path.exists(origen_dir):
        print(f"Error: El directorio origen '{origen_dir}' no existe.")
        return

    # Crear el directorio destino si no existe
    if not os.path.exists(destino_dir):
        os.makedirs(destino_dir)
        print(f"Directorio remoto/seguro creado en: {destino_dir}")

    # Obtener timestamp actual (YYYYMMDD_HHMMSS)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivos_procesados = 0

    # Recorrer archivos del directorio origen
    for nombre_archivo in os.listdir(origen_dir):
        if nombre_archivo.endswith(".php"):
            ruta_origen = os.path.join(origen_dir, nombre_archivo)
            
            # Renombrar archivo
            nombre_base, ext = os.path.splitext(nombre_archivo)
            nuevo_nombre = f"{nombre_base}_{timestamp}{ext}"
            ruta_destino = os.path.join(destino_dir, nuevo_nombre)

            # Copiar archivo
            shutil.copy2(ruta_origen, ruta_destino)
            print(f"Copiado: {nombre_archivo} -> {nuevo_nombre}")
            archivos_procesados += 1

    print(f"\nRespaldo finalizado. Total archivos .php copiados: {archivos_procesados}")

if __name__ == "__main__":
    # Carpetas de prueba
    DIRECTORIO_FUENTE = "./codigo_fuente_php"
    DIRECTORIO_RESPALDO = "./remoto_seguro_backup"

    respaldar_archivos_php(DIRECTORIO_FUENTE, DIRECTORIO_RESPALDO)