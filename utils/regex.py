import pickle

import numpy as np
import pandas as pd
import streamlit as st

from utils.funcs import call_model


class RegexData:
    def __init__(self, medical_data: dict):
        try:
            self.__medical_data = medical_data
        except TypeError as err:
            raise print(f"Tipo de dados errado : {err}")
        except ValueError as err:
            raise print(f"Valores errado : {err}")

    @property
    def medical_data(self):
        return self.__medical_data

    def regex_medical(self) -> dict:
        for key in self.medical_data:
            if key == 'sex':
                if self.medical_data[key] == ['Feminino']:
                    self.medical_data[key] = 'female'
                elif self.medical_data[key] == ['Masculino']:
                    self.medical_data[key] = 'male'
                else:
                    raise ValueError
            if key == 'smoker':
                if self.medical_data[key] == ['Sim']:
                    self.medical_data[key] = 'yes'
                elif self.medical_data[key] == ['Não']:
                    self.medical_data[key] = 'no'
                else:
                    raise ValueError
            if key == 'region':
                if self.medical_data[key] == ['Sudoeste']:
                    self.medical_data[key] = 'southwest'
                elif self.medical_data[key] == ['Sudeste']:
                    self.medical_data[key] = 'southeast'
                elif self.medical_data[key] == ['Noroeste']:
                    self.medical_data[key] = 'northwest'
                elif self.medical_data[key] == ['Nordeste']:
                    self.medical_data[key] = 'northeast'
                else:
                    raise ValueError
        return self.medical_data

    def create_data_set(self) -> pd.DataFrame:
        try:
            return pd.DataFrame(self.regex_medical())
        except ValueError as err:
            raise err

    @staticmethod
    def predict_model(model: pickle, data: pd.DataFrame) -> np:
        if model:
            return model.predict(data)
        raise ValueError

    def return_value(self) -> None:
        try:
            data = self.create_data_set()
            model = call_model()
            value_estimated = self.predict_model(model, data)
            if value_estimated > 0:
                st.success(f"O valor estimado para seu plano de saúde é de {np.round(value_estimated[0], 2)} dolares")
            else:
                st.warning(f"Insira valores nos campos acimas")
        except ValueError as err:
            raise err
        except TypeError as err:
            raise err
