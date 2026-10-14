from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensaje = data.get('message', '').lower()
    
    accion = "ninguna"
    parametro = ""
    respuesta_texto = "Entendido, Vicho."

    if "abre" in mensaje or "abrir" in mensaje:
        accion = "abrir_app"
        # Extrae el nombre de la app eliminando las palabras de comando
        parametro = mensaje.replace("abre", "").replace("abrir", "").replace("el", "").replace("la", "").strip()
        respuesta_texto = f"Abriendo {parametro}."
        
    elif "cierra" in mensaje or "cerrar" in mensaje:
        accion = "cerrar_app"
        parametro = mensaje.replace("cierra", "").replace("cerrar", "").replace("el", "").replace("la", "").strip()
        respuesta_texto = f"Cerrando {parametro}."
        
    elif "busca" in mensaje or "buscar" in mensaje:
        accion = "buscar_web"
        parametro = mensaje.replace("busca", "").replace("buscar", "").replace("en google", "").strip()
        respuesta_texto = f"Buscando {parametro} en la web."
    else:
        respuesta_texto = f"Recibí tu mensaje: {mensaje}. ¿Qué más hacemos en el PC?"

    return jsonify({
        "response": respuesta_texto,
        "action": accion,
        "parameter": parametro
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)