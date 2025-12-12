def ver_tablero():
    """Muestra las tareas formateadas como una tabla visual."""
   
    # 1. Limpieza Visual (Requisito: Higiene de Pantalla)
    limpiar_pantalla()
   
    conn = sqlite3.connect('collabsecure.db')
    cursor = conn.cursor()
   
    # 2. Consulta de Datos (Traer info útil, no solo IDs)
    cursor.execute('''
        SELECT t.id, t.titulo, t.estado, u.username
        FROM tareas t
        JOIN usuarios u ON t.user_id = u.id
    ''')
    tareas = cursor.fetchall()
    conn.close()

    # 3. Diseño de Interfaz (Requisito: Estructura Tabular)
    print("=== TABLERO DE EQUIPO TECHNOVA ===")
    # Cabeceras con espaciado fijo
    print(f"{'ID':<4} | {'TAREA':<30} | {'ESTADO':<12} | {'RESPONSABLE':<18}")
    print("-" * 75) # Separador visual
   
    if not tareas:
        print("No hay tareas registradas. Seleccione 'Nueva Tarea' para comenzar.")
   
    for t in tareas:
        # 4. Renderizado de Filas (Alineación perfecta)
        # :<30 significa "reserva 30 espacios y alinea a la izquierda"
        print(f"{t[0]:<4} | {t[1]:<30} | {t[2]:<12} | {t[3]:<18}")
   
    print("-" * 75)
