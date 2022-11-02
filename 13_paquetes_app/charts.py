'''
Asunto: Módulo creado para crear gráficos de distinto tipo
'''
import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    '''
    Función que dibuja una gráfica de barras con las etiquetas y valores
    que el usuario pase como parámetros de entrada
    '''
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(values, labels):
    '''
    Función que dibuja una gráfica de barras con las etiquetas y valores
    que el usuario pase como parámetros de entrada
    '''
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.show()
