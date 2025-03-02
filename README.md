# Docker-compose-flask


🚀 1️⃣ Construcción de la imagen


docker build -t fcl2005/flask_imagen .


▶️ 2️⃣ Ejecución del contenedor


docker run -d --name flask_container -p 8000:8000 -p 9001:9001 -p 22222:22 fcl2005/flask_imagen


🖥 3️⃣ Conexión a los servicios

Para acceder a Flask: http://localhost:8000

Para Supervisor en Flask: http://localhost:9001

Para conectar vía SSH a Flask:

ssh -p 22222 root@localhost

📌 4️⃣ URL de Docker Hub
Añadir el enlace a la imagen en Docker Hub:

https://hub.docker.com/r/fcl2005/flask_imagen
