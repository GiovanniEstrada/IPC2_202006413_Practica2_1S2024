from flask import Flask
from flask import render_template, request
from ClaseUsuario import ClaseUsuario

app = Flask(__name__)
listaUsuarios = []

@app.route("/")
def hello_world():
    return render_template("login.html")

@app.route("/POST", methods=['POST'])
def insertarUsuario():
    nombre = str(request.form.get('Nombre'))
    correo = str(request.form.get('Correo'))
    nit = str(request.form.get('Nit'))
    error = ""

    # SE VALIDA SI HAY CAMPOS VACIOS
    if nit == "" or nit == None:
        error = "Campo NIT del cliente vacío"
        
    if correo == "" or correo == None:
        error = "Campo correo electrónico vacío"

    if nombre == "" or nombre == None:
        error = "Campo nombre cliente vacío"

    # SE VALIDA QUE CLIENTE NO EXISTA
    for usuario in listaUsuarios:
        if str(usuario.nit) == str(nit):
            error = "Usuario ya existe..."
    
    if error != "":
        return render_template("login.html", error = error)


    usuario = ClaseUsuario(nombre, correo, nit)
    listaUsuarios.append(usuario)
    return render_template("login.html", success = "¡Usuario ingresado con éxito!")

@app.route("/LISTADO")
def verUsuarios():
    return render_template("listado.html", ListaUsuarios = listaUsuarios)


if __name__ == '__main__':
    app.run(port=1500, debug=True)