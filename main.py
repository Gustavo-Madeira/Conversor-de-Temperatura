class temperauteConverter:
    def __init__(self):
        pass
    def kelvin(self, c):
        return c + 273
    def fahrenheit(self, c):
        return (((c * 9) / 5) + 32)

calcular = temperauteConverter()
c = float(input('Digite a temperatura em °C: '))

print(f'{c}°C, convertendo, vira {calcular.fahrenheit(c)}°F e/ou {calcular.kelvin(c)}')