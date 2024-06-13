from abc import ABC, abstractmethod

# Clase abstracta que define la estructura para una Cuenta Bancaria
class CuentaBancaria(ABC):

    def __init__(self, numero_cuenta, titular):
        self.numero_cuenta = numero_cuenta
        self.titular = titular

    class CuentaAhorro(CuentaBancaria):

        def __init__(self, numero_cuenta, titular, balance_inicial=0):
            super().__init__(numero_cuenta, titular)
            self.__balance = balance_inicial  # Atributo privado

        def obtener_balance(self):
            return self.__balance

        def depositar(self, monto):
            if monto > 0:
                self.__balance += monto

        def retirar(self, monto):
            if 0 < monto <= self.__balance:
                self.__balance -= monto
