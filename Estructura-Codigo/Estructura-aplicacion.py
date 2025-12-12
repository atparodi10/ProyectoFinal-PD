# 1. IMPORTACIÓN DE LIBRERÍAS
# Se cargan las herramientas necesarias para base de datos, seguridad y sistema.
import sqlite3      # Para la base de datos local
import hashlib      # Para encriptar contraseñas (SHA-256)
import getpass      # Para ocultar la contraseña al escribir
import os           # Para limpiar la pantalla
import time         # Para pausas visuales
from datetime import datetime # Para registrar fechas

# ---------------------------------------------------------
# BLOQUE 1: CONFIGURACIÓN Y UTILIDADES (Backend / Seguridad)
# ---------------------------------------------------------

def limpiar_pantalla():
    """Detecta el sistema operativo y limpia la consola."""
    pass

def encriptar_pass(password):
    """
    Recibe una contraseña en texto plano.
    Retorna el hash SHA-256 (Cifrado unidireccional).
    """
    pass

def iniciar_db():
    """
    1. Conecta a 'collabsecure.db'.
    2. Crea la tabla 'usuarios' si no existe.
    3. Crea la tabla 'tareas' (con llave foránea) si no existe.
    4. Verifica e inserta los usuarios por defecto (Alessandro, Rommel, etc.)
    """
    pass

# ---------------------------------------------------------
# BLOQUE 2: GESTIÓN DE USUARIOS (Auth Module)
# ---------------------------------------------------------

def registrar_usuario():
    """
    1. Pide usuario y contraseña (usando getpass).
    2. Encripta la contraseña.
    3. Hace un INSERT en la base de datos.
    4. Maneja errores si el usuario ya existe.
    """
    pass

def login_usuario():
    """
    1. Pide credenciales.
    2. Compara el hash de la entrada con el hash de la BD.
    3. Retorna los datos del usuario si es correcto, o None si falla.
    """
    pass

# ---------------------------------------------------------
# BLOQUE 3: GESTIÓN DE TAREAS (Core Logic)
# ---------------------------------------------------------

def ver_tablero():
    """
    Hace un SELECT con JOIN para traer tareas + nombres de usuarios.
    Imprime la información formateada como una tabla visual.
    """
    pass

def crear_tarea(user_id):
    """
    Recibe el ID del usuario logueado.
    Pide descripción de la tarea.
    Hace un INSERT en la tabla 'tareas' vinculándola al user_id.
    """
    pass

def cambiar_estado():
    """
    Pide el ID de la tarea.
    Hace un UPDATE en SQL para cambiar de 'Pendiente' a 'Terminado'.
    """
    pass

# ---------------------------------------------------------
# BLOQUE 4: INTERFAZ Y FLUJO DE CONTROL (Frontend CLI)
# ---------------------------------------------------------

def menu_interno(usuario):
    """
    Bucle while True para el menú de usuario logueado.
    Opciones: 
      [1] Nueva Tarea 
      [2] Cambiar Estado 
      [3] Cerrar Sesión
    """
    pass

def main():
    """
    Función Principal (Entry Point).
    1. Ejecuta iniciar_db().
    2. Muestra el menú de bienvenida (Login / Registro / Salir).
    3. Dirige el flujo según la opción elegida.
    """
    pass

# PUNTO DE ARRANQUE
if __name__ == "__main__":
    main()