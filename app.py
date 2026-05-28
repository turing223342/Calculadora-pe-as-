import streamlit as st

st.set_page_config(page_title="Calculadora de Peças")
st.title("💰 Calculadora de Peças")

c = st.number_input("Quantas calças você fez?", min_value=0, step=1)
j = st.number_input("Quantas jaquetas você fez?", min_value=0, step=1)
CR = st.number_input("Quantas calças rasgadas?", min_value=0, step=1)
sh = st.number_input("Quantas shorts você fez?", min_value=0, step=1)

if st.button("Calcular Total"):
    total = c*40 + j*50 + CR*50 + sh*40
    st.divider()
    st.write(f"Calças: R$ {c*40:.2f}")
    st.write(f"Jaquetas: R$ {j*50:.2f}") 
    st.write(f"Rasgadas: R$ {CR*50:.2f}")
    st.write(f"Shorts: R$ {sh*40:.2f}")
    st.success(f"**Valor total a receber: R$ {total:.2f}**")
