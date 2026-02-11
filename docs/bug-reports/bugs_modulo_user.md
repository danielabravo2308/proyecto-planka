
# 🐞 Bug Report



| Campo | Descripción |
|------|------------|
| 🆔 **ID** | BUG-001 |
| 📌 **Título** | El sistema permite crear usuario , al ingresar un tipo de dato invalido en el campo nombre|
| 🧪 **Módulo / Feature** | Usuario |
| 🌍 **Ambiente** | Windows 11 
| 📋 **Precondiciones** | Ingresar Token Valido |
| 🔄  **Pasos para reproducir** | 1. Enviar POST `http://localhost:3000/api/users` <br> 2. Ingresar en el payload del campo name un valor numerico  `123` <br> 3. Ejecutar request |
|✅ **Resultado esperado** | El sistema debe devolver error 400 
|  ❌ **Resultado actual** | El usuario se crea correctamente (200) 
| ⚠ **Severidad** | Baja |
| 🚦 **Prioridad** | Baja |
| 📝 **Notas** | Falta validación del campo name |

