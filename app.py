import streamlit as st

st.set_page_config(page_title="Calculadora de Peças", page_icon="💰")
st.title("💰 Calculadora de Peças")

# Inicializa o estado
if "calculado" not in st.session_state:
    st.session_state.calculado = False
    st.session_state.c = 0
    st.session_state.j = 0
    st.session_state.CR = 0
    st.session_state.sh = 0

def resetar():
    st.session_state.calculado = False
    st.session_state.c = 0
    st.session_state.j = 0
    st.session_state.CR = 0
    st.session_state.sh = 0

# Tela de inputs
if not st.session_state.calculado:
    c = st.number_input("Quantas calças você fez?", min_value=0, step=1, value=st.session_state.c)
    j = st.number_input("Quantas jaquetas você fez?", min_value=0, step=1, value=st.session_state.j)
    CR = st.number_input("Quantas calças rasgadas?", min_value=0, step=1, value=st.session_state.CR)
    sh = st.number_input("Quantas shorts você fez?", min_value=0, step=1, value=st.session_state.sh)
    
    if st.button("Calcular Total", use_container_width=True, type="primary"):
        if any([c, j, CR, sh]):
            st.session_state.c = c
            st.session_state.j = j
            st.session_state.CR = CR
            st.session_state.sh = sh
            st.session_state.calculado = True
            st.rerun()
        else:
            st.warning("Coloca pelo menos 1 peça pra calcular 😉")

# Tela de resultado
else:
    c = st.session_state.c
    j = st.session_state.j
    CR = st.session_state.CR
    sh = st.session_state.sh
    
    total = c*0.40 + j*0.50 + CR*0.50 + sh*0.40
    total_pecas = c + j + CR + sh
    
    st.info(f"**Total de peças: {total_pecas}**")
    st.success(f"**Valor total a receber: R$ {total:.2f}**")
    
    with st.expander("Ver detalhes"):
        st.write(f"Calças: {c} x R$ 0,40 = R$ {c*0.40:.2f}")
        st.write(f"Jaquetas: {j} x R$ 0,50 = R$ {j*0.50:.2f}")
        st.write(f"Rasgadas: {CR} x R$ 0,50 = R$ {CR*0.50:.2f}")
        st.write(f"Shorts: {sh} x R$ 0,40 = R$ {sh*0.40:.2f}")
    
    st.button("Fazer novo cálculo", on_click=resetar, use_container_width=True)
