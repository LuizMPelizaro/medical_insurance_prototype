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

    def regex(self) -> None:
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
