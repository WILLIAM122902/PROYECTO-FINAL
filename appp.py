import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

# Definir el banco de perfiles existente
banco_perfiles = np.array([
    # Perfil 1
    ["Alex Campos", 21, "Femenino", "Estudiante",  0.5, 0.75, 1, 0.75, 1, 1, 1, 0.75, 1, 1, 1, 0.5, 0.75, 0.25, 0.75],
    # Perfil 2
    ["Mariana Martinez", 20, "Femenino", "Trabajador", 0.75, 1, 0.5, 0.5, 1, 0.75, 1, 0.75, 0.75, 1, 1, 0.5, 1, 0.5,1],
    # Perfil 3
    ["Jesus Daniel", 21, "Masculino", "Estudiante", 0.5, 0.75, 0.25, 0.75, 0.75, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.25, 1,0.25,0.75],
    # Perfil 4
    ["Victor", 27, "Masculino", "Estudiante", 0.25, 0.5, 0.25, 1, 1, 1, 1, 1, 0.25, 0.75, 0.5, 0.5, 1, 0.25, 1],
    # Perfil 5
    ["Blanca Rodriguez", 23, "Femenino", "Estudiante", 1, 1, 0.75, 0.75, 1, 1, 1, 0.75, 1, 1, 1, 0.75, 1, 0.5, 1],
    # Perfil 6
    ["Fernanda Escalona", 18, "Femenino", "Estudiante", 0.75, 0.75, 0.25, 0.25, 0.75, 0.5, 1, 1, 0.75, 0.75, 0.75, 0.5, 0.75, 0.25, 0.75],
    # Perfil 7
    ["Eunice", 20, "Femenino", "Estudiante", 0.75, 1, 0.5, 0.5, 0.75, 1, 1, 0.75, 0.5, 1, 0.75, 0.75, 1,1,1],
    # Perfil 8
    ["Yektli", 21, "Masculino", "Estudiante", 0.5, 0.5, 0.5, 1, 1, 0.75, 0.75, 1, 0.5, 1, 0.25, 0.25, 0.5, 0.5, 0.75],
    # Perfil 9
    ["Fernando Barron", 23, "Masculino", "Estudiante", 1, 0.75, 0.25, 0.75, 1, 0.75, 0.5, 0.5, 0.75, 0.75, 0.5, 0.75, 1, 0.5, 1],
    # Perfil 10
    ["Efrain Dionicio", 20, "Masculino", "Estudiante", 0.5, 0.75, 1, 0.5, 1, 0.75, 0.75, 0.75, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25, 0.75],
    # Perfil 11
    ["Alan Medina", 21, "Masculino", "Trabajador", 0.5, 1, 0.75, 1, 1, 0.5, 1, 1, 0.75, 0.75, 0.5, 0.5, 1, 0.5,1],
    # Perfil 12
    ["Monse de Leon", 21, "Femenino", "Estudiante", 0.5, 1, 0.25, 0.25, 1, 0.5, 1, 1, 1, 0.5, 1, 1, 0.5, 0.5,1],
    # Perfil 13
    ["Francisco Rojas", 21, "Masculino", "Estudiante", 0.75, 1, 0.25, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.75, 0.5, 0.75, 1, 0.75,1],
    # Perfil 14
    ["Alejandra Melchor", 21, "Femenino", "Estudiante", 0.75, 1, 0.25, 0.5, 1, 0.5, 0.75, 1, 0.5, 0.75, 0.75, 0.5, 1, 0.25,1],
    # Perfil 15
    ["Yessica Reyes", 27, "Femenino", "Trabajador", 0.75, 1, 0.25, 0.5, 1, 1, 1, 1, 0.75, 0.5, 1, 0.5, 0.5,1,1],
    # Perfil 16
    ["Mariana Hernandez", 25, "Femenino", "Trabajador", 0.5, 1, 0.5, 0.75, 1, 1, 1, 0.5, 1, 1, 1, 0.75, 0.75, 0.75, 0.75],
    # Perfil 17
    ["Axel", 20, "Masculino", "Estudiante", 0.5, 1, 0.25, 0.75, 1, 0.5, 1, 1, 1, 0.75, 1, 1, 1, 0.5, 1],
    # Perfil 18
    ["Jorge", 25, "Masculino", "Trabajador", 1, 1, 1, 0.5, 0.75, 0.5, 1, 0.5, 0.5, 0.75, 0.75, 0.5, 0.5, 0.5,1],
    # Perfil 19
    ["Jonas Zamarripa", 30, "Masculino", "Trabajador", 0.75, 0.75, 1, 0.5, 1, 1, 0.75, 0.5, 0.75, 1, 1, 0.25, 0.75, 0.25, 0.75],
    # Perfil 20
    ["Jean Carlo", 24, "Masculino", "Trabajador", 1, 1, 0.25, 1, 1, 0.75, 0.75, 1, 1, 0.75, 0.5, 0.5, 0.75, 0.25,1],
    # Perfil 21
    ["Leonardo", 26, "Masculino", "Trabajador", 0.75, 1, 0.25, 0.75, 1, 0.5, 0.75, 1, 0.75, 0.25, 0.5, 0.75, 0.75, 0.25,0.5],
    # Perfil 22
    ["Diana", 22, "Femenino", "Estudiante", 0.25, 1, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.75,1],
    # Perfil 23
    ["Saad Castro", 24, "Masculino", "Trabajador", 1, 1, 0.25, 0.5, 1, 0.75, 1, 1, 0.75, 1, 0.5, 0.5, 1, 0.75,1],
    # Perfil 24
    ["Miguel Padron", 25, "Masculino", "Estudiante", 0.5, 0.75, 0.5, 0.75, 1, 0.5, 0.75, 1, 0.25, 0.75, 1, 0.25, 0.75, 0.25,1]
], dtype=object)

# Preguntas de la encuesta
preguntas = [
    "¿Qué tanto le gusta la actividad deportiva?",
    "¿Qué tanto te gusta viajar?",
    "¿Qué tanto te gustan los animes o mangas?",
    "¿Qué tanto te gustan los videojuegos?",
    "¿Qué tanto te gusta escuchar música?",
    "¿Qué tanto te gusta leer?",
    "¿Qué tanto te gusta el cine?",
    "¿Qué tanto te gustan las mascotas?",
    "¿Qué tanto te gusta salir de fiesta?",
    "¿Qué tanto te gustan las cafeterías?",
    "¿Qué tanto te gusta bailar?",
    "¿Qué tan extrovertido te consideras?",
    "¿Qué tan importante es para ti el cuidado de la apariencia personal?",
    "¿Qué tan importante es para ti la religión?",
    "¿Qué tan importante es para ti la familia?"
]

# Valores correspondientes a las opciones de las preguntas
valores_preguntas = {
    "Nulo": 0.25,
    "Leve": 0.5,
    "Moderado": 0.75,
    "Alto": 1
}

@app.route('/')
def inicio():
    return render_template('InicioSesion.html')

@app.route('/introduccion')
def introduccion():
    return render_template('introduccion.html')

@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')

@app.route('/formulario')
def formulario():
    # Código para renderizar el formulario
    return render_template('formulario.html', preguntas=preguntas)

@app.route('/resultados', methods=['POST'])
def obtener_resultados():
    perfil_usuario = []
    for i in range(1, len(preguntas) + 1):
        pregunta = "resp" + str(i)
        respuesta = request.form[pregunta]
        valor_respuesta = float(respuesta)
        perfil_usuario.append(valor_respuesta)

    perfil_usuario = np.array(perfil_usuario)

    suma_coincidencia = np.sum(np.where(banco_perfiles[:, 4:].astype(float) == perfil_usuario.reshape(1, -1), perfil_usuario, 0), axis=1)

    umbral = 0.5
    if np.sum(suma_coincidencia) < umbral:
        mensaje_error = "No se encontraron perfiles compatibles."
        return render_template('resultados.html', mensaje_error=mensaje_error)

    perfiles_top = np.argsort(suma_coincidencia)[::-1][:3]

    perfiles = []
    for perfil_idx in perfiles_top:
        perfil = banco_perfiles[perfil_idx]
        perfiles.append({
            'nombre': perfil[0],
            'edad': perfil[1],
            'sexo': perfil[2],
            'ocupacion': perfil[3]
        })

    return render_template('resultados.html', perfiles=perfiles)


if __name__ == '__main__':
    app.run()
