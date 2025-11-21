# Clase que maneja al jugador

class Player():
    # definicion de atributos
    def __init__(self, score: int = 0, streak: int = 0, mult: float = 1.0):
        self.score = score
        self.streak = streak
        self.mult = mult
        self.count = 0
    
    # La funcion que checa si la respuesta es correcta, acepta una respuesta (string) un codigo (string) y el diccionario de respuestas (dependiendo de la dificultad)
    def check_answer(self, answer: str, code: str, morse_dict: dict):
        try:
            if morse_dict[answer.upper()] == code:
                self.score += 100 * self.mult
                self.streak += 1
                self.mult += 0.5
            elif morse_dict[answer.upper()] != code and self.score > 0:
                self.score -= 100
                self.streak = 0
                self.mult = 1.0
                self.count += 1
            else:
                self.score = 0
                self.streak = 0
                self.mult = 1.0
                self.count += 1
        except KeyError:
            if self.score > 0:
                self.score -= 100
                self.streak = 0
                self.mult = 1.0
                self.count += 1
            else:
                self.score = 0
                self.streak = 0
                self.mult = 1.0
                self.count += 1
    
    # Funcion que reinicia los atributos cuando se vuelve al menu principal
    def restart_attribs(self):
        self.score = 0
        self.streak = 0
        self.mult = 1.0
        self.count = 0
