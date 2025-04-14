import streamlit as st
import pandas as pd
import psycopg2 # pip install psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
import joblib


# Configuración de la página
st.set_page_config(
    page_title="Predicción de Accidente Cerebrovascular",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Función para conectar a la base de datos
def connect_db():
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="brainstroke",
            user="postgres",
            password="postgres",
            port="5432"
        )
        return conn
    except Exception as e:
        st.error(f"Error al conectar a la base de datos: {e}")
        return None

# Función para obtener todos los IDs de pacientes
def get_all_patient_ids():
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT id FROM patient_data ORDER BY id")
            patient_ids = [str(row[0]) for row in cur.fetchall()]
            cur.close()
            conn.close()
            return patient_ids
        except Exception as e:
            st.error(f"Error al obtener los IDs de pacientes: {e}")
            conn.close()
            return []
    return []

# Función para obtener datos de paciente por ID
def get_patient_data(patient_id):
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = sql.SQL("SELECT * FROM patient_data WHERE id = %s")
            cur.execute(query, (patient_id,))
            patient_data = cur.fetchone()
            cur.close()
            conn.close()
            return patient_data
        except Exception as e:
            st.error(f"Error al obtener datos del paciente: {e}")
            conn.close()
            return None
    return None

# Función para convertir valores 1/0 a SI/NO
def convert_to_si_no(value):
    if value == 1:
        return "SÍ"
    elif value == 0:
        return "NO"
    else:
        return value

# Título principal
st.title("Datos de Pacientes de Accidente Cerebrovascular")

# Obtener todos los IDs de pacientes para el selectbox
patient_ids = get_all_patient_ids()

# Campo de búsqueda de paciente con selectbox que permite entrada de texto
selected_id = st.selectbox(
    "ID del paciente en el RIS",
    options=patient_ids,
    index=0 if patient_ids else None,
    key="patient_selector"
)

# Línea divisoria
st.markdown("---")

# Verificar si se seleccionó un paciente
if selected_id:
    # Obtener datos del paciente
    patient_data = get_patient_data(selected_id)
    
    if patient_data:
        # Crear dos columnas para Datos Demográficos
        st.subheader("Datos Demográficos del paciente")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Género:** {patient_data['gender']}")
            st.write(f"**Edad del paciente:** {patient_data['age']}")
            st.write(f"**Casado alguna vez:** {patient_data['ever_married']}")
        
        with col2:
            st.write(f"**Tipo de trabajo:** {patient_data['work_type']}")
            st.write(f"**Tipo de residencia:** {patient_data['residence_type']}")
        
        # Línea divisoria
        st.markdown("---")
        
        # Crear dos columnas para Datos de Salud
        st.subheader("Datos de Salud del paciente")
        col3, col4 = st.columns(2)
        
        with col3:
            st.write(f"**Sufrió de Enfermedad cardíaca:** {convert_to_si_no(patient_data['heart_disease'])}")
            st.write(f"**Sufre de Hipertensión:** {convert_to_si_no(patient_data['hypertension'])}")
            st.write(f"**Nivel promedio de glucosa:** {patient_data['avg_glucose_level']}")
        
        with col4:
            st.write(f"**Índice de Masa Corporal (BMI):** {patient_data['bmi']}")
            st.write(f"**Fuma:** {patient_data['smoking_status']}")
            st.write(f"**Sufrió accidente cerebrovascular:** {convert_to_si_no(patient_data['stroke'])}")
        
        # Línea divisoria
        st.markdown("---")
        
        # Sección para la predicción (será implementada en la etapa 3)
        st.subheader("Predicción del Modelo")
        
        # Aquí se mostrará posteriormente la predicción
        st.info("La funcionalidad de predicción será implementada en la etapa 3.")
        
    else:
        st.warning(f"No se encontraron datos para el paciente con ID: {selected_id}")
else:
    st.info("Por favor, seleccione un ID de paciente para ver sus datos.")