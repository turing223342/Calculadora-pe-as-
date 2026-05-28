import streamlit as st

st.set_page_config(page_title="Calculadora de Peças", page_icon="💰")
st.title("💰 Calculadora de Peças")

# Controla se já calculou ou não
if 'calculado' not in st.session_state:
    st.session_state.calculado = False

def calcular():
    st.session_state.calculado = True

def voltar():
    st.session_state.calculado = False

# Se NÃO calculou ainda: mostra os campos
if not st.session_state.calculado:
    c = st.number_input("Quantas calças você fez?", min_value=0, step=1, value=None, placeholder="Digite a quantidade")
    j = st.number_input("Quantas jaquetas você fez?", min_value=0, step=1, value=None, placeholder="Digite a quantidade")
    CR = st.number_input("Quantas calças rasgadas?", min_value=0, step=1, value=None, placeholder="Digite a quantidade")
    sh = st.number_input("Quantas shorts você fez?", min_value=0, step=1, value=None, placeholder="Digite a quantidade")
    
    # Salva os valores pra usar depois
    st.session_state.c = c or 0
    st.session_state.j = j or 0
    st.session_state.CR = CR or 0
    st.session_state.sh = sh or 0
    
    st.button("Calcular Total", on_click=calcular, use_container_width=True, type="primary")

# Se JÁ calculou: mostra só o resultado
else:
    c = st.session_state.c
    j = st.session_state.j
    CR = st.session_state.CR
    sh = st.session_state.sh
    
    total = c*0.40 + j*0.50 + CR*0.50 + sh*0.40
    
    st.success(f"**Valor total a receber: R$ {total:.2f}**")
    
    with st.expander("Ver detalhes"):
        st.write(f"Calças: {c} x R$ 0,40 = R$ {c*0.40:.2f}")
        st.write(f"Jaquetas: {j} x R$ 0,50 = R$ {j*0.50:.2f}") 
        st.write(f"Rasgadas: {CR} x R$ 0,50 = R$ {CR*0.50:.2f}")
        st.write(f"Shorts: {sh} x R$ 0,40 = R$ {sh*0.40:.2f}")
    
    st.button("Fazer novo cálculo", on_click=voltar, use_container_width=True)
