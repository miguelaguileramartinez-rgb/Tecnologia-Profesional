import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("Calculadora Profesional de Rebajas")
st.markdown("Bienvenido. Introduzca el porcentaje de su rebaja para calcular el precio final.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio_original = st.sidebar.number_input("Coste Inicial (€)", min_value=0, max_value=200, value=60)
descuento = st.sidebar.slider("Descuento aplicado (€)", 0, 100, 50)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular Precio Final"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    ahorro = precio_original * (descuento / 100)
    precio_final = precio_original - ahorro
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu Precio Final es:", value=f"{precio_final:.2f}")

    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if descuento => 50:
            st.success("Precio Regalado")
            st.write("Aproveche la oferta.")
        if descuento < 25:
            st.error("Cuestionable")
            st.write("espera a una rebaja mas baja.")
        elif 25 <= descuento < 50:
            st.warning("Razonable")
            st.write("es una buena oferta.")
        
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula matemática aplicada en el proceso:")
    st.latex(r'''Precio Final = PrecioOriginal * (descuento / 100) ''')
    st.balloons()
