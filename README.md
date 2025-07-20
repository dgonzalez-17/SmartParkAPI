# SmartParkAPI 🚗📡

**SmartParkAPI** es una API REST desarrollada como parte de mi proyecto de grado universitario.  
El objetivo fue construir una solución backend para la **gestión inteligente de parqueaderos**, que permitiera administrar usuarios, espacios disponibles y asignaciones, usando un stack moderno basado en **Python y FastAPI**.

---

## 🎯 Funcionalidades principales

- Gestión de parqueaderos disponibles.
- Asignación de espacios.
- Control de entradas y salidas.
- Consulta del estado actual de los parqueaderos.
- Conexión a Bot de Telegram y gestión desde allí de todo lo relacionado con los parqueaderos.

---

## 🛠️ Tecnologías usadas

- **FastAPI** – Framework ligero y rápido para construir APIs en Python.
- **Pydantic** – Validación de datos y esquemas.
- **Uvicorn** – Servidor ASGI para desarrollo.
- **Python 3.9+**
- Base de datos (adaptable, originalmente para MongoDB).

---

## 🗂️ Estructura del proyecto
```bash
SmartParkAPI/
├── config/ # Configuración de variables, BD, etc.
├── controllers/ # Rutas y lógica de entrada
├── models/ # Modelos de base de datos
├── schemas/ # Esquemas de validación (Pydantic)
├── services/ # Lógica de negocio
├── utils/ # Funciones auxiliares
├── main.py # Punto de entrada principal
└── requirements.txt # Dependencias
```

## ⚙️ Cómo correr el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/dgonzalez-17/SmartParkAPI.git
cd SmartParkAPI
```
2. Crear y activar entorno virtual
```bash
python -m venv venv
source venv/bin/activate   # En Linux/macOS
venv\Scripts\activate      # En Windows
```
3. Instalar dependencias
```bash
pip install -r requirements.txt
```
4. Ejecutar el servidor
```bash
uvicorn main:app --reload
```
Accede a la documentación automática de la API en:
📚 http://localhost:8000/docs
