# CollabSecure: Plataforma Ligera de Colaboración Segura
CollabSecure es una aplicación de interfaz de línea de comandos (CLI) diseñada para solucionar los problemas de coordinación y seguridad digital de la empresa TechNova Learning. Permite la gestión centralizada de tareas implementando principios de Security by Design (Seguridad por Diseño).

#📋 Contexto del Proyecto
El Área de Innovación de TechNova detectó tres problemas críticos:

Uso de plataformas no autorizadas (Shadow IT).

Falta de prácticas de seguridad (contraseñas en texto plano).

Pobre coordinación entre los equipos.

Solución: CollabSecure elimina la dependencia de herramientas externas inseguras, centralizando la información en una base de datos local y encriptada.

    🚀 Características Principales
        🔐 Seguridad Ética: Las contraseñas nunca se guardan en texto plano. Se utiliza hashlib (SHA-256) para encriptarlas.

        👁️ Privacidad: Los caracteres de la contraseña se ocultan al escribir (getpass), evitando el shoulder surfing.

        🗂️ Persistencia Local: Uso de SQLite3 para almacenar usuarios y tareas sin necesidad de servidores externos.

        📊 Tablero de Tareas: Visualización en formato de tabla para ver el estado y responsable de cada actividad.

        🧹 Interfaz Limpia: Limpieza automática de pantalla para mantener el orden visual.

    🛠️ Requisitos Previos
        Python 3.x instalado en tu sistema.

No requiere instalación de librerías externas (usa solo librerías estándar de Python).

#💻 Instalación y Ejecución
Clonar el repositorio:

Bash

git clone https://github.com/TU_USUARIO/CollabSecure.git
cd CollabSecure
Ejecutar la aplicación:

Bash

python main.py
Nota: Al ejecutarlo por primera vez, el sistema creará automáticamente el archivo collabsecure.db.

#🔑 Usuarios Pre-cargados (Acceso Rápido)
Para facilitar las pruebas, el sistema incluye una función de seeding que crea automáticamente las cuentas del equipo si no existen.

Contraseña por defecto para todos: 12345

        Usuario                 Rol (Simulado)
    Alessandro Parodi       Arquitectura / Seguridad
    Rommel Muñoz                 QA / Testing
    Jonas Cajina            Frontend / Visualización
    Eduardo Cruz             Backend / Funcionalidad

También puedes usar la opción [2] Registrarse para crear un usuario nuevo.

#📂 Estructura del Código
main.py: Archivo único que contiene toda la lógica (MVC simplificado).

iniciar_db(): Configuración de SQLite y creación de tablas.

encriptar_pass(): Lógica de seguridad SHA-256.

ver_tablero(): Renderizado de la tabla de tareas.

menu_interno(): Flujo principal de la aplicación.

collabsecure.db: Archivo de base de datos (se genera automáticamente al ejecutar).

#🛡️ Evidencia de Seguridad
Si inspeccionas el archivo collabsecure.db con un visor de SQLite, notarás que la columna password_hash contiene cadenas encriptadas, no el texto "12345".

Ejemplo de Hash SHA-256: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8

#✒️ Autores
Proyecto desarrollado por el equipo de estudiantes para el caso de estudio de TechNova Learning:

Alessandro Parodi

Rommel Muñoz

Jonas Cajina

Eduardo Cruz