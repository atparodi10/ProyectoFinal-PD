def registrar_usuario():
	"""
	Crea una nueva identidad en el sistema garantizando unicidad y seguridad.
	Maneja el ingreso de datos y su almacenamiento permanente.
	"""
	limpiar_pantalla()
	print("=== REGISTRO DE NUEVO COLABORADOR ===")

	# 1. Definición de la Identidad
	username = input("Ingrese un nombre de usuario: ")
	# Usamos getpass para proteger la contraseña desde el primer momento
	password = getpass.getpass("Cree una contraseña segura (oculta): ")

	if not username or not password:
		print("Error: Los campos no pueden estar vacíos.")
		time.sleep(2)
		return

	# 2. Encriptación Inmediata (Antes de guardar)
	pass_hash = encriptar_pass(password)

	try:
		conn = sqlite3.connect('collabsecure.db')
		cursor = conn.cursor()

		# 3. Persistencia de la Identidad (Ingreso a BD)
		# Intentamos guardar. Si el usuario ya existe, SQLite lanzará un error.
		cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)",
					   (username, pass_hash))

		conn.commit()
		print(f"\n¡Éxito! Usuario '{username}' registrado correctamente.")

	except sqlite3.IntegrityError:
		# 4. Control de Identidad Única
		print("\nError: El nombre de usuario ya existe. Elija otro.")
	except Exception as e:
		print(f"\nError del sistema: {e}")
	finally:
		conn.close()
		time.sleep(2)