from msilib.schema import ControlCondition
from random import random
from model.acta import Acta

""" Este archivo contiene las funcionalidades de la vista relacionada con las actas"""


def crear_acta(st,controller):
    acta = Acta()
    acta.nombre = st.text_input("Nombre del trabajo de grado: ")
    acta.tipo = st.selectbox(
        'Tipo de trabajo de grado',
        ('Tipo 1', 'Tipo 2', 'Tipo 3'))
    acta.fecha = st.date_input("Fecha del trabajo de grado: ")
    acta.autor = st.text_input("Nombre del director: ")
    acta.jurado1 = st.text_input("Nombre del primer jurado: ")
    acta.jurado2 = st.text_input("Nombre del segundo jurado: ")

    enviado_btn = st.button("Guardar")   

    if enviado_btn:
        controller.agregar_acta(acta)
        st.write("Evaluacion agregada exitosamente")
    return controller

def evaluar_acta(st,controller):
    #TODO: mostrar actas y seleccionar una

    #obtener nombres de actas
    nombresActas=[]
    for acta in controller.actas:
        nombresActas.append(acta.nombre)    

    nombreActa = st.selectbox('Seleccionar acta a evaluar: ',(nombresActas))

    st.markdown("""---""")
    
    #obtener acta basado en el nombre
    acta = controller.getActaNombre(nombreActa)

    #listar criterios y obtener calificaciones
    for criterio in acta.criterios:
        st.write(str(criterio.id)+'. '+criterio.descripcion)
        criterio.calificacion1  = st.number_input('Agregar calificacion 1:',key=criterio.id)
        criterio.calificacion2  = st.number_input('Agregar calificacion 2:',key=criterio.id)

    #agregar comentarios generales

    acta.observaciones = st.text_area('Agrege las observaciones generales: ')  

    enviado_btn = st.button("Guardar")   

    if enviado_btn:
        st.write("Evaluacion agregada exitosamente")
        return controller


def listar_actas(st, controller):
    """Itera los elementos de actas agregados y los muestra"""
    st.title("Datos guardados... a mejorar la presentacion")
    for acta in controller.actas:
        st.write(acta.numero)
        st.write(acta.nombre)
        st.write(acta.tipo)
        st.write(acta.fecha)
        st.write(acta.autor)
        st.write(acta.director)
        st.write(acta.jurado1)
        st.write(acta.jurado2)
        st.write(acta.observaciones)
        st.write("TEST")