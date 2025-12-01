from flask import Flask, render_template, request
from business.logic import cargar_dataset, entrenar_modelo, guardar_arbol
import datetime

app = Flask(__name__,
            template_folder="./presentation/templates",
            static_folder='./presentation/static')

print("entrenando modelo inicial...")

print("modelo listo")

@app.route("/", methods = ['GET'])
def index():
    X, y = cargar_dataset()
    resultados_dict = entrenar_modelo(X, y)

    modelo = resultados_dict['modelo']    
    
    img_name = guardar_arbol(modelo, X, filename="arbol_default.png")
    return render_template("IntrovertVsExtrovert.html", resultados_dict=resultados_dict, img_name=img_name)

@app.route("/load", methods = ['GET','POST'])
def load_csv():
    if request.method == 'POST':
        if "file" not in request.files:
            return render_template("SecondTree.html", error = "No se subió ningun archivo")
        file = request.files["file"]

        if file.filename == "":
            return render_template("SecondTree.html", error="El archivo está vacio")
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"./data/uploaded_{timestamp}.csv"

        file.save(path)

        X, y = cargar_dataset(path)
        resultados_dict = entrenar_modelo(X, y)

        modelo = resultados_dict['modelo']       
        nombre_imagen_dinamico = f"arbol_usuario_{timestamp}.png"    
        img_name = guardar_arbol(modelo, X, filename=nombre_imagen_dinamico)

        return render_template("SecondTree.html", resultados_dict=resultados_dict, img_name=img_name)
    return render_template("SecondTree.html")


if __name__ == '__main__':
    app.run(debug=True,host='localhost',port = 8000)