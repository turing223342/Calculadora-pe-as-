import streamlit as st

st.set_page_config(page_title="Calculadora de Peças", page_icon="💰")
st.title("💰 Calculadora de Peças")

# Controla se já calculou ou não
if 'calculado' not in st.session_state:
    st.session_state.calculado = False

# Se NÃO calculou ainda: mostra os campos
if not st.session_state.calculado:
    c = st.number_input("Quantas calças você fez?", min_value=0, step=1, value=0)
    j = st.number_input("Quantas jaquetas você fez?", min_value=0, step=1, value=0)
    CR = st.number_input("Quantas calças rasgadas?", min_value=0, step=1, value=0)
    sh = st.number_input("Quantas shorts você fez?", min_value=0, step=1, value=0)
    
    if st.button("Calcular Total", use_container_width=True, type="primary"):
        # Salva os valores só quando clica, pra pegar o valor atualizado dos inputs
        st.session_state.c = c
        st.session_state.j = j
        st.session_state.CR = CR
        st.session_state.sh = sh
        st.session_state.calculado = True
        st.rerun()

# Se JÁ calculou: mostra só o resultado
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
        st.write(f
