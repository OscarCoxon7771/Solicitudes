from flask import Flask, request, render_template, make_response



app = Flask(__name__)
@app.route("/")
def home():
    return "Página de inicio"

# Ruta para parametros de la URL
@app.route("/consulta")
def ruta_consulta():
    producto=request.args.get("product")
    talla=request.args.get("size")
    if producto and talla is None:
        return f"No se ha proporcionado el producto o la talla"
    if producto is None:
        return f"No se ha proporcionado el producto"
    if talla is None:
        return f"No se ha proporcionado la talla"
    if talla is None and producto is None:
        return f"No se ha proporcionado el producto ni la talla"
    


    return f"Se está consultando el producto {producto} de talla {talla}"

#Ruta para capturar datos por el cuerpo de solicitud para el body
listado=[]
@app.route("/registro", methods = ["GET"])
def ruta_registro():
   # listado = [{"Nombre":"Juanito", "Correo":"juan@gmail.com"}]
    return render_template("formulario.html", listado=listado)

@app.route("/registro", methods = ["POST"])
def procesar_registro():
    nombre=request.form.get("Nombre")
    correo=request.form.get("Correo")
    estudiantes={"Nombre":nombre, "Correo":correo}
    listado.append(estudiantes)
    # print(nombre)
    return f"El estudiante a registrar es: {nombre} y su correo es: {correo}"

# Parametros en la ruta
@app.route("/estudiantes/<string:area>/<int:grupo>")
def mostrar_estudiantes(area, grupo):
    return f"El programa de formación consultado es {area} y el grupo consultado es la variable {grupo}"

# Solicitud tipo 4
@app.route('/ver-headers')
def ver_headers():
    agente_usuario = request.headers.get('User-Agent')
    return f"Tu navegador es: {agente_usuario}"

# Gestion de cookies
@app.route('/crear-cookie')
def crear_cookie():
    respuesta = make_response("Cookie creada!") #Es un mensaje de respuesta
    respuesta.set_cookie('usuario_logueado', 'true')
    return respuesta

@app.route('/leer-cookie')

def leer_cookie():
    valor = request.cookies.get('usuario_logueado')
    return f"Valor de la cookie: {valor}"



if __name__ == "__main__":
    app.run(debug=True)