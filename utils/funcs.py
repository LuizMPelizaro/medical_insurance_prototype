import pickle

import numpy as np
import streamlit as st


def call_model() -> pickle:
    with open(r"./models/model.pickle", "rb") as input_model:
        model = pickle.load(input_model)
    return model


def func_bmi(weight: float, height: float) -> None:
    try:
        st.success(f"Valor IMC: {np.round(weight / height ** 2, 2)}")
    except ValueError as err:
        st.error(f"Insira valores validos {err}")
