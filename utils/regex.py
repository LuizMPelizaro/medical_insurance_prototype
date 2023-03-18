import pickle

import numpy as np
import pandas as pd
import streamlit as st

from utils.funcs import call_model


class RegexData:
    SEX_MAPPING = {'Feminino': 'female', 'Masculino': 'male'}
    SMOKER_MAPPING = {'Sim': 'yes', 'Não': 'no'}
    REGION_MAPPING = {'Sudoeste': 'southwest', 'Sudeste': 'southeast', 'Noroeste': 'northwest', 'Nordeste': 'northeast'}

    def __init__(self, medical_data: dict):
        self.__medical_data = medical_data

    @property
    def medical_data(self):
        return self.__medical_data

    def regex_medical(self) -> dict:
        for key in ['sex', 'smoker', 'region']:
            if key in self.medical_data:
                value = self.medical_data[key][0]
                if key == 'sex':
                    self.medical_data[key] = self.SEX_MAPPING.get(value, value)
                elif key == 'smoker':
                    self.medical_data[key] = self.SMOKER_MAPPING.get(value, value)
                elif key == 'region':
                    self.medical_data[key] = self.REGION_MAPPING.get(value, value)
                else:
                    raise ValueError(f'Valor inválido  para a chave {key}')
        return self.medical_data

    def create_data_set(self) -> pd.DataFrame:
        data = self.regex_medical()
        return pd.DataFrame(data)

    @staticmethod
    def predict_model(model: pickle, data: pd.DataFrame) -> np:
        if model is not None:
            return model.predict(data)
        else:
            return None

    def return_value(self) -> None:
        data = self.create_data_set()
        model = call_model()
        value_estimated = self.predict_model(model, data)
        if value_estimated is not None and value_estimated > 0:
            st.success(f"O valor estimado para seu plano de saúde é de {np.round(value_estimated[0], 2)} dolares")
        else:
            st.warning(f"Insira valores nos campos acimas")
