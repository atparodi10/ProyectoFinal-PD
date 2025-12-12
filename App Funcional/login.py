def login_usuario():
    """
    Gestiona el inicio de sesión validando credenciales contra la base de datos.
    Retorna: Una tupla (id, username) si es correcto, o None si falla.
    """
    limpiar_pantalla()
    print("=== INICIO DE SESIÓN ===")
   
    # 1. Entrada de Datos (Requisito: Privacidad)
    username = input("Usuario: ")
    # Usamos getpass para que no se vean los caracteres al escribir
    password = getpass.getpass("Contraseña: ")
   
    # 2. Procesamiento de Seguridad (Requisito: Ética de Datos)
    # Convertimos lo que escribió el usuario a SHA-256
    pass_hash = encriptar_pass(password)
   
    conn = sqlite3.connect('collabsecure.db')
    cursor = conn.cursor()
   
    # 3. Verificación en Base de Datos
    # Buscamos si existe alguien con ese Usuario Y ese Hash exacto
    cursor.execute("SELECT id, username FROM usuarios WHERE username = ? AND password_hash = ?",
                   (username, pass_hash))
   
    user = cursor.fetchone() # Devuelve el usuario o None (vacío)
    conn.close()
   
    if user:
        return user # ¡Éxito! Retornamos la identidad para iniciar la sesión
    else:
        print("\nAcceso Denegado: Verifique sus credenciales.")
        input("Presione Enter para intentar de nuevo...")
        return None
