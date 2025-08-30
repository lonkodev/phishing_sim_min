# 🎓 Proyecto de Simulación Académica de Phishing

Este proyecto fue desarrollado en el marco de la asignatura **Hacking Ético (IEI-076)**, con fines **exclusivamente educativos**.  
El objetivo es **entender cómo funcionan los ataques de phishing**, mediante una **maqueta controlada**, sin afectar a terceros ni usar marcas/servicios reales.

⚠️ **Importante:**  
- Este código **no debe usarse en Internet ni contra personas reales**.  
- Solo corre en **entorno local de laboratorio**.  
- **No uses credenciales reales.** Solo datos ficticios para pruebas.  

---

## 🚀 Funcionalidad
- Página de login simulada (HTML).  
- Guarda localmente en **SQLite** los datos ingresados (usuario, “contraseña” de prueba y metadatos).  
- Muestra un **panel (/dashboard)** donde se listan los registros capturados.  

---

## 🛠️ Requisitos
- [Python 3.10+](https://www.python.org/) (recomendado Python 3.13 en macOS con Homebrew).  
- [Flask](https://flask.palletsprojects.com/)  
- SQLite (incluido en Python estándar).  

---

## 📦 Instalación y ejecución

Clona el repositorio:
```bash
git clone https://github.com/usuario/phishing-simulacion.git
cd phishing-simulacion
```

Crea y activa un entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate   # En Linux/macOS
# En Windows: venv\Scripts\activate
```

Instala dependencias:
```bash
pip install flask
```

Ejecuta el servidor:
```bash
python app.py
```

Accede en tu navegador a:
- Login simulado: [http://127.0.0.1:5000](http://127.0.0.1:5000)  
- Panel de registros: [http://127.0.0.1:5000/dashboard](http://127.0.0.1:5000/dashboard)  

---

## 📂 Estructura del proyecto
```
phishing-simulacion/
├── app.py                # Código principal Flask
├── demo.db               # Base de datos SQLite (se crea al ejecutar)
├── templates/
│   ├── login.html        # Formulario de login simulado
│   ├── success.html      # Mensaje de éxito
│   └── dashboard.html    # Panel para visualizar registros
└── README.md             # Este archivo
```

---

## 🧭 Uso académico
1. Ingresa datos ficticios en el formulario de login.  
2. Verifica en el **panel** cómo se registran usuario, contraseña, user-agent, IP y cookie de prueba.  
3. Reflexiona: ¿qué señales visuales o de URL permitirían a un usuario detectar que esto es phishing?  

---

## 📊 Evaluación sugerida
- **Diseño de la maqueta** (login simulado).  
- **Funcionalidad local** (captura en SQLite).  
- **Capturas de pantalla** del login y el panel.  
- **Análisis reflexivo**: técnicas de persuasión usadas y contramedidas posibles.  

---

## 📜 Licencia
Este proyecto se distribuye con fines **educativos**.  
Queda prohibido su uso para fines maliciosos o fuera del ámbito académico.
