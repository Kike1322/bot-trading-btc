class CapitalManager:
    def __init__(self, initial_capital):
        self.capital = initial_capital
        self.colchon = 0
        self.beneficio_total = 0

    def repartir_beneficio(self, beneficio_neto):
        if beneficio_neto > 0:
            ganancia_personal = beneficio_neto * 0.33
            reinversion = beneficio_neto * 0.33
            reserva = beneficio_neto * 0.34  # redondeamos

            self.colchon += reserva
            self.capital += reinversion
            self.beneficio_total += ganancia_personal

            return ganancia_personal, reserva, reinversion

        else:
            perdida = abs(beneficio_neto)
            if self.colchon >= perdida:
                self.colchon -= perdida
            else:
                restante = perdida - self.colchon
                self.capital -= restante
                self.colchon = 0
            return 0, 0, -perdida
