import sqlite3
import hashlib
import getpass
import os
import time
from datetime import datetime

# --- CONFIGURACIÓN Y SEGURIDAD ---

def limpiar_pantalla():
    """Limpia la consola para mantener la privacidad y el orden."""
    os.system('cls' if os.name == 'nt' else 'clear')

def encriptar_pass(password):
    """
    SEGURIDAD: Convierte la contraseña en un hash SHA-256.
    Ética: Nunca guardamos la contraseña real del usuario.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def iniciar_db():
    """
    Inicializa la base de datos, crea tablas y PRE-CARGA los usuarios del equipo.
    """
    conn = sqlite3.connect('collabsecure.db')
    cursor = conn.cursor()
    
    # 1. Crear Tabla de Usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    
    # 2. Crear Tabla de Tareas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            estado TEXT DEFAULT 'Pendiente',
            fecha TEXT,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES usuarios(id)
        )
    ''')

    # 3. PRE-CARGA DE USUARIOS (SEEDING)
    # Lista de usuarios solicitados con contraseña por defecto '12345'
    usuarios_base = [
        "Alessandro Parodi",
        "Rommel Muñoz",
        "Jonas Cajina",
        "Eduardo Cruz"
    ]
    pass_default = "12345"
    hash_default = encriptar_pass(pass_default)

    print("Verificando usuarios del sistema...")
    for usuario in usuarios_base:
        try:
            # Intentamos insertar el usuario. Si ya existe, sqlite dará error y lo ignoramos.
            cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", (usuario, hash_default))
            print(f"[Sistema] Usuario '{usuario}' creado automáticamente.")
        except sqlite3.IntegrityError:
            # Si entra aquí, es porque el usuario ya existía, no hacemos nada.
            pass

    conn.commit()
    conn.close()

# --- MÓDULO DE USUARIOS ---

def registrar_usuario():
    limpiar_pantalla()
    print("=== REGISTRO DE NUEVO COLABORADOR ===")
    print("Aviso de Privacidad: Su contraseña será encriptada.\n")
    
    username = input("Ingrese un nombre de usuario: ")
    password = getpass.getpass("Cree una contraseña segura (oculta): ")
    
    if not username or not password:
        print("Error: Los campos no pueden estar vacíos.")
        time.sleep(2)
        return

    pass_hash = encriptar_pass(password)

    try:
        conn = sqlite3.connect('collabsecure.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", (username, pass_hash))
        conn.commit()
        print(f"\n¡Éxito! Usuario '{username}' registrado correctamente.")
    except sqlite3.IntegrityError:
        print("\nError: El nombre de usuario ya existe.")
    except Exception as e:
        print(f"\nError del sistema: {e}")
    finally:
        conn.close()
        time.sleep(2)

def login_usuario():
    limpiar_pantalla()
    print("=== INICIO DE SESIÓN ===")
    print("(Usuarios precargados: Alessandro Parodi, Rommel Muñoz, Jonas Cajina, Eduardo Cruz)")
    print("(Contraseña por defecto: 12345)\n")
    
    username = input("Usuario: ")
    password = getpass.getpass("Contraseña: ")
    
    pass_hash = encriptar_pass(password)
    
    conn = sqlite3.connect('collabsecure.db')
    cursor = conn.cursor()
    # Verificamos hash contra hash
    cursor.execute("SELECT id, username FROM usuarios WHERE username = ? AND password_hash = ?", (username, pass_hash))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return user # Retorna (id, username)
    else:
        print("\nAcceso Denegado: Verifique sus credenciales.")
        input("Presione Enter para intentar de nuevo...")
        return None

# --- MÓDULO DE GESTIÓN Y VISUALIZACIÓN ---

def ver_tablero():
    """Muestra las tareas formateadas como una tabla."""
    limpiar_pantalla()
    conn = sqlite3.connect('collabsecure.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT t.id, t.titulo, t.estado, u.username 
        FROM tareas t
        JOIN usuarios u ON t.user_id = u.id
    ''')
    tareas = cursor.fetchall()
    conn.close()

    print("=== TABLERO DE EQUIPO TECHNOVA ===")
    print(f"{'ID':<4} | {'TAREA':<30} | {'ESTADO':<12} | {'RESPONSABLE':<18}")
    print("-" * 75)
    
    if not tareas:
        print("No hay tareas registradas. Seleccione 'Nueva Tarea' para comenzar.")
    
    for t in tareas:
        # Formato de columnas alineadas
        print(f"{t[0]:<4} | {t[1]:<30} | {t[2]:<12} | {t[3]:<18}")
    print("-" * 75)

def crear_tarea(user_id):
    print("\n--- CREAR NUEVA TAREA ---")
    titulo = input("Descripción de la tarea: ")
    estado = "Pendiente"
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    if titulo:
        conn = sqlite3.connect('collabsecure.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tareas (titulo, estado, fecha, user_id) VALUES (?, ?, ?, ?)", 
                       (titulo, estado, fecha, user_id))
        conn.commit()
        conn.close()
        print(">> Tarea registrada y asignada a su usuario.")
    else:
        print(">> Cancelado: No se puede guardar una tarea vacía.")
    time.sleep(1.5)

def cambiar_estado():
    id_tarea = input("\nIngrese el ID de la tarea a actualizar (o Enter para cancelar): ")
    if not id_tarea: return

    print("Seleccione nuevo estado:")
    print("1. En Proceso")
    print("2. Terminado")
    opcion = input("Opción: ")
    
    if opcion == "1": nuevo_estado = "En Proceso"
    elif opcion == "2": nuevo_estado = "Terminado"
    else: return

    try:
        conn = sqlite3.connect('collabsecure.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE tareas SET estado = ? WHERE id = ?", (nuevo_estado, id_tarea))
        conn.commit()
        conn.close()
        print(">> Estado actualizado correctamente.")
    except Exception:
        print(">> Error al actualizar (Verifique que el ID exista).")
    time.sleep(1)

# --- FLUJO PRINCIPAL ---

def menu_interno(usuario):
    while True:
        ver_tablero()
        print(f"\n[Usuario: {usuario[1]}]")
        print("1. Agregar Nueva Tarea")
        print("2. Cambiar Estado de Tarea")
        print("3. Cerrar Sesión")
        
        opcion = input("Seleccione opción: ")
        
        if opcion == '1':
            crear_tarea(usuario[0])
        elif opcion == '2':
            cambiar_estado()
        elif opcion == '3':
            break

def main():
    iniciar_db() # Aquí se crean automáticamente Alessandro, Rommel, etc.
    while True:
        limpiar_pantalla()
        print("========================================")
        print("   COLLABSECURE - TECHNOVA LEARNING     ")
        print("========================================")
        print("1. Iniciar Sesión")
        print("2. Registrar Nuevo Usuario")
        print("3. Salir")
        
        opcion = input("\nOpción: ")
        
        if opcion == '1':
            usuario = login_usuario()
            if usuario:
                menu_interno(usuario)
        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            print("Cerrando sistema...")
            break

if __name__ == "__main__":
    main()