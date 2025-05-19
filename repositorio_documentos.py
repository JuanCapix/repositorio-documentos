import streamlit as st
import os

st.title("📂 Repositorio de Documentos")

# Campo para ingresar nombre del cliente
cliente = st.text_input("Nombre del cliente")

# Subida de archivo
uploaded_file = st.file_uploader("Sube un archivo", type=["pdf", "xlsx", "xml", "jpg", "png"])

if uploaded_file and cliente:
    # Crear carpeta del cliente si no existe
    carpeta_cliente = os.path.join("uploads", cliente)
    os.makedirs(carpeta_cliente, exist_ok=True)

    # Guardar el archivo
    ruta_archivo = os.path.join(carpeta_cliente, uploaded_file.name)
    with open(ruta_archivo, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Archivo guardado en la carpeta de {cliente}")

# Mostrar archivos subidos por cliente
if os.path.exists("uploads"):
    st.subheader("📁 Archivos guardados")
    clientes = os.listdir("uploads")
    for nombre in clientes:
        st.markdown(f"**{nombre}**")
        archivos = os.listdir(os.path.join("uploads", nombre))
        for archivo in archivos:
            st.markdown(f"- {archivo}")





