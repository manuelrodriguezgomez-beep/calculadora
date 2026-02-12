import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Calculadora de Rebajas", page_icon="🏷️")

# Título y Descripción
st.title(" Calculadora de Rebajas 🏷️")
st.markdown ("Calcula el precio despues del descuento instantaneamente")
st.write("---")

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Datos de la compra")
precio_original = st.sidebar.number_input("Precio original ($)", min_value=0.0, value=100.0, step=0.5)
porcentaje_descuento = st.sidebar.slider("Porcentaje de descuento (%)", 0, 100, 20)

# 3. Botón
if st.button("Calcular Descuento"):
    
    # Formula Matemática
    ahorro = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - ahorro
    
    # 4. Mostrar Resultados con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Mostramos el precio final como métrica principal
        st.metric(label="Precio Final:", value=f"${precio_final:.2f}", delta=f"-${ahorro:.2f}")
        
  
    # Extra: Desglose detallado
    st.write("---")
