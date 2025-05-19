import streamlit as st
import os

# ----------------------------------------
# 🎛️ CONFIGURACIÓN GENERAL
# ----------------------------------------

st.set_page_config(page_title="Gestión de Documentos", layout="wide")
st.title("📁 Plataforma de Gestión de Documentos")

# Sidebar de navegación
modo = st.sidebar.selectbox("¿Qué deseas hacer?", ["Subir documentos", "Consultar expediente"])

# Tipo de cliente y operación
tipo_cliente = st.sidebar.selectbox("Tipo de cliente", ["Persona Física", "Persona Moral"])
tipo_operacion = st.sidebar.selectbox("Tipo de operación", ["SOFOM", "Leasing"])

# ----------------------------------------
# 📄 DOCUMENTOS REQUERIDOS SEGÚN COMBINACIÓN
# ----------------------------------------

documentos_requeridos = {
    ("Persona Física", "SOFOM"): ["INE", "CURP", "Comprobante de domicilio"],
    ("Persona Física", "Leasing"): ["INE", "RFC", "Estado de cuenta"],
    ("Persona Moral", "SOFOM"): ["Acta constitutiva", "Poder notarial", "RFC", "Comprobante fiscal"],
    ("Persona Moral", "Leasing"): ["Acta constitutiva", "Estados financieros", "RFC", "Identificación representante"]
}

docs_esperados = documentos_requeridos.get((tipo_cliente, tipo_operacion), [])

# ----------------------------------------
# 📥 SUBIDA DE DOCUMENTOS
# ----------------------------------------

if modo == "Subir documentos":
    cliente = st.text_input("Nombre del cliente").strip()

    if cliente:
        st.subheader(f"📤 Subir documentos para: {cliente}")
        carpeta_cliente = os.path.join("uploads", cliente.upper().replace(" ", "_"))
        os.makedirs(carpeta_cliente, exist_ok=True)

        for doc in docs_esperados:
            uploaded_file = st.file_uploader(f"📎 {doc}", type=["pdf", "jpg", "png"], key=doc)
            if uploaded_file:
                nombre_archivo = doc.lower().replace(" ", "_") + ".pdf"
                with open(os.path.join(carpeta_cliente, nombre_archivo), "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"✅ {doc} guardado correctamente.")

    else:
        st.warning("🔍 Ingresa el nombre del cliente para habilitar los campos.")

# ----------------------------------------
# 🔎 CONSULTA DE EXPEDIENTES
# ----------------------------------------

elif modo == "Consultar expediente":
    cliente = st.text_input("Buscar cliente").strip()

    if cliente:
        carpeta_cliente = os.path.join("uploads", cliente.upper().replace(" ", "_"))
        st.subheader(f"📂 Expediente de: {cliente}")

        if os.path.exists(carpeta_cliente):
            archivos_actuales = os.listdir(carpeta_cliente)

            for doc in docs_esperados:
                archivo = doc.lower().replace(" ", "_") + ".pdf"
                if archivo in archivos_actuales:
                    st.checkbox(f"{doc}", value=True, disabled=True)
                else:
                    st.checkbox(f"{doc}", value=False, disabled=True)
        else:
            st.warning("📭 Aún no se ha subido ningún documento para este cliente.")
    else:
        st.info("🔍 Ingresa el nombre del cliente para buscar su expediente.")
