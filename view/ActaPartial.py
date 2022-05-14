from model.acta import Acta

""" Este archivo contiene las funcionalidades de la vista relacionada con la creación de actas"""


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
        controller.agregar_evaluacion(acta)
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