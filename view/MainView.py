import streamlit as st
from pydataxm.pydataxm import ReadDB
from streamlit_option_menu import option_menu

# from controller.MercadoController import MercadoController
from controller.actaController import ActaController
# from model.Consulta import Consulta
# from model.Metrica import Metrica
from view.ActaPartial import *
from view.AboutPartial import *


class MainView:

    def __init__(self) -> None:
        super().__init__()

        if 'main_view' not in st.session_state:
            self.menu_actual = "About"
            # Inicialización de las variables necesarias

            # Conexión con el controlador
            self.controller = ActaController()

            st.session_state['main_view'] = self
        else:
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller
             # Carga de las variables necesarias
        self._inicialializar_layout()

    def _inicialializar_layout(self):
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="SITGRA", page_icon='', layout="wide",
                           initial_sidebar_state="expanded")
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3 = st.columns([1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            self.menu_actual = option_menu("Menu", ["About", "Crear Acta","Evaluar Acta",
                                                    "Exportar Acta","Modificar Criterios","Ver Históricos"],
                                           icons=['house', 'gear'], menu_icon="cast", default_index=1)

    def ver_ejemplo(self):
        pass

    def controlar_menu(self):
        # Filtro opciones de menu
        if self.menu_actual == "About":
            # Welcome message
            welcome = st.expander(label="Instrucciones", expanded=True)

            # Cuando este disponible en pantalla la instruccion de welcome
            with welcome:
                st.markdown(mostrar())
                st.write("")
        elif self.menu_actual == "Crear Acta":
            crear_acta(st,self.controller)
        elif self.menu_actual == "Evaluar Acta":                        
            evaluar_acta(st,self.controller)
        elif self.menu_actual == "Ver Históricos":
            listar_actas(st,self.controller)


# Main call
if __name__ == "__main__":
    gui = MainView()
    gui.controlar_menu()
