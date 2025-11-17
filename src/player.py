class Player():
    morse_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }

    def __init__(self, score: int = 0, streak: int = 0, mult: float = 1.0):
        self.score = score
        self.streak = streak
        self.mult = mult

    def check_answer(self, answer: str, code: str):
        try:
            if self.morse_dict[answer.upper()] == code:
                self.score += 100 * self.mult
                self.streak += 1
                self.mult += 0.5
            elif self.morse_dict[answer.upper()] != code and self.score > 0:
                self.score -= 100
                self.streak = 0
                self.mult = 1.0
            else:
                self.score = 0
                self.streak = 0
                self.mult = 1.0
        except KeyError:
            self.score -= 100
            self.streak = 0
            self.mult = 1.0

    def restart_attribs(self):
        self.score = 0
        self.streak = 0
        self.mult = 1.0
