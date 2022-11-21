import streamlit as st
from PIL import Image

from utils import funcs
from utils.regex import RegexData

image_top = Image.open('img/img_topo.jpg')
table_imc_image = Image.open('img/table_imc.png')

st.set_page_config(
    page_title="Simulador de plano",
    page_icon='💉',
    initial_sidebar_state='auto',
    layout='centered'
)

st.markdown("## Simulador de preço de plano de saúde")

st.image(image_top)

age = st.number_input("Idade", min_value=1, max_value=100, value=1, step=1)

sex = st.selectbox(
    'Sexo :',
    ['Feminino', 'Masculino']
)

bmi = st.number_input("IMC:", min_value=1.0, max_value=100.0, value=1.0)

st.markdown("Caso não saiba calcular o imc , clique no botão abaixo ⬇️")

with st.expander("Clique aqui"):
    st.markdown("### Calculadora de IMC:")

    st.latex(r'''
        Imc =
        \left(\frac{Peso}{Altura²}\right)
        ''')

    weight = st.number_input("Peso:", min_value=1.0, max_value=500.0)

    height = st.number_input("Altura:", min_value=1.0, max_value=3.0)

    funcs.func_bmi(weight, height)

    st.image(table_imc_image)

children = st.number_input("Numero de filhos", min_value=0, max_value=10, value=0, step=1)

smoker = st.selectbox(
    "Fumante: ",
    ['Sim', 'Não']
)

region = st.selectbox(
    "Região: ",
    ['Sudoeste', 'Sudeste', 'Noroeste', 'Nordeste']
)

data = {
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region': [region]
}

data = RegexData(data)

st.markdown(f"### Resultados da simulação")

data.return_value()

st.markdown("Projeto feito com o intuito de estudos na area de Data Science , erros de calculo podem acontecer.")
