import streamlit as st

st.set_page_config(page_title="Calculadora de Peças", page_icon="💰")
st.title("💰 Calculadora de Peças")

c = st.number_input("Quantas calças você fez?", min_value=0, step=1)
j = st.number_input("Quantas jaquetas você fez?", min_value=0, step=1)
CR = st.number_input("Quantas calças rasgadas?", min_value=0, step=1)
sh = st.number_input("Quantas shorts você fez?", min_value=0, step=1)

if st.button("Calcular Total"):
    total = c*0.40 + j*0.50 + CR*0.50 + sh*0.40
    
    st.divider()
    st.subheader("Resumo:")
    st.write(f"Calças: R$ {c*0.40:.2f}")
    st.write(f"Jaquetas: R$ {j*0.50:.2f}") 
    st.write(f"Rasgadas: R$ {CR*0.50:.2f}")
    st.write(f"Shorts: R$ {sh*0.40:.2f}")
    st.success(f"**Valor total a receber: R$ {total:.2f}**")
