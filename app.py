import uuid  # Para generar los Tokens de sesión únicos
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# BASES DE DATOS EN MEMORIA
users = {} 
notas = [] 
# Diccionario para controlar sesiones activas { "token_abc_123": "nombre_usuario" }
sesiones_activas = {}

@app.route('/')
def index():
    return jsonify({"message": "API REST - Michel ESCOM (Sesiones Seguras)"})

# --- 1. SECCIÓN DE USUARIOS (REGISTRO Y LOGIN CON SESIÓN) ---

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users:
        return jsonify({"message": f"El usuario '{username}' ya existe"}), 400
    
    users[username] = generate_password_hash(password)
    print(f"DEBUG: Registro exitoso para {username}")
    return jsonify({"message": "Usuario registrado con éxito"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user_hash = users.get(username)
    
    if user_hash and check_password_hash(user_hash, password):
        # PUNTO 3: Generamos un Token Único para la sesión segura
        token = str(uuid.uuid4())
        sesiones_activas[token] = username # Guardamos quién es el dueño del token
        
        print(f"DEBUG: Sesión iniciada para {username}. Token: {token}")
        return jsonify({
            "message": "Inicio de sesión correcto",
            "token": token  # Enviamos el token al Android
        }), 200
    
    return jsonify({"message": "Error: Credenciales incorrectas"}), 401

# --- 2. SECCIÓN DE NOTAS (CRUD PROTEGIDO POR SESIÓN) ---

@app.route('/notas', methods=['GET'])
def get_notas():
    # En una sesión real, también pediríamos token aquí, 
    # pero para tu reporte, lo dejamos libre para que Chrome lo vea fácil.
    return jsonify(notas)

@app.route('/notas', methods=['POST'])
def add_nota():
    # VALIDACIÓN DE SESIÓN SEGURA (Punto 3)
    token = request.headers.get('Authorization')
    
    if not token or token not in sesiones_activas:
        print("DEBUG: Intento de acceso sin sesión activa.")
        return jsonify({"message": "Acceso denegado: Sesión no válida o expirada"}), 403
    
    data = request.get_json()
    usuario_autor = sesiones_activas[token]
    
    nueva_nota = {
        "id": len(notas),
        "contenido": data.get('contenido'),
        "autor": usuario_autor # Sabemos quién la creó gracias al Token
    }
    notas.append(nueva_nota)
    print(f"DEBUG: Nota creada por {usuario_autor}")
    return jsonify({"message": "Nota guardada con éxito", "nota": nueva_nota}), 201

@app.route('/notas/<int:id>', methods=['PUT'])
def update_nota(id):
    token = request.headers.get('Authorization')
    if token not in sesiones_activas:
        return jsonify({"message": "No autorizado"}), 403
        
    data = request.get_json()
    if 0 <= id < len(notas):
        notas[id]['contenido'] = data.get('contenido')
        return jsonify({"message": "Nota actualizada"}), 200
    return jsonify({"message": "Nota no encontrada"}), 404

@app.route('/notas/<int:id>', methods=['DELETE'])
def delete_nota(id):
    token = request.headers.get('Authorization')
    if token not in sesiones_activas:
        return jsonify({"message": "No autorizado"}), 403

    if 0 <= id < len(notas):
        notas.pop(id)
        return jsonify({"message": "Nota eliminada"}), 200
    return jsonify({"message": "ID no encontrado"}), 404

# --- 3. RUTA DE COMPROBACIÓN (DEBUG) ---
@app.route('/debug_usuarios')
def debug_usuarios():
    return jsonify({"usuarios": list(users.keys()), "sesiones_abiertas": len(sesiones_activas)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)