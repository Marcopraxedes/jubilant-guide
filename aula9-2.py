class ContaCorrente:
    def __init__(self, saldo, percentual_imposto):
        self.__saldo = saldo
        self.__percentual_imposto = percentual_imposto
    @property   
    def saldo(self):
        return self.__saldo
    @property
    def percentual_imposto(self):
        return self.__percentual_imposto
    @property
    def calcular_imposto(self):
        return self.__saldo - (self.__saldo * self.__percentual_imposto)
    
class Poupança(ContaCorrente):
    def __init__(self, saldo, percentual_imposto):
        super().__init__(saldo, percentual_imposto)
    
class ContaImposto(ContaCorrente):
    def __init__(self, saldo, percentual_imposto):
        super().__init__(saldo, percentual_imposto)
        
imposto = ContaCorrente(20000000, 0.10)
print(imposto.saldo)
print(imposto.percentual_imposto)
print(imposto.calcular_imposto)
