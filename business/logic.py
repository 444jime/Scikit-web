import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import GridSearchCV,train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
matplotlib.use('Agg')

def cargar_dataset(ruta="./data/personality_dataset.csv"):
    df = pd.read_csv(ruta)

    df['Personality'] = df['Personality'].map({ 'Introvert': 0,'Extrovert': 1})
    df['Stage_fear'] = df['Stage_fear'].map({'No': 0, 'Yes': 1})
    df['Drained_after_socializing'] = df['Drained_after_socializing'].map({'No': 0,'Yes': 1})

    X = df.drop('Personality', axis=1)
    y = df['Personality']
    return X, y

def entrenar_modelo(X,y):
    np.random.seed(42)
    param_grid = {'min_samples_split': [2,5,10,20], 'max_depth': [1,2,3]}

    grid = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=5)
    grid.fit(X,y)

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=2324)

    best_model = grid.best_estimator_
    best_model.fit(X_train,y_train)

    y_pred = best_model.predict(X_test)

    params_limpios = {}
    for clave, valor in grid.best_params_.items():
        if hasattr(valor, 'item'):
            params_limpios[clave] = valor.item()
        else:
            params_limpios[clave] = valor

    resultados = {
        'mejores_params': params_limpios,
        'mejor_score_train': round(grid.best_score_, 4),
        'score_test': round(accuracy_score(y_test, y_pred), 4),
        'matriz_confusion': confusion_matrix(y_test, y_pred).tolist(),
        'reporte_class': classification_report(y_test,y_pred),
        'modelo': best_model
    }

    return resultados

def guardar_arbol(modelo,X,filename="arbol.png"):
    plt.figure(figsize=(40,15))  

    plot_tree(modelo,feature_names=X.columns,class_names=['Introvertido','Extrovertido'],filled=True)
    path = f"presentation/static/{filename}"
    plt.savefig(path, dpi=200, bbox_inches='tight')
    plt.close()
    
    return filename