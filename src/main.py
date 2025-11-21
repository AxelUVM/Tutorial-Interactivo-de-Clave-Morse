import flet as ft
import random

from player import Player

# Esto es el diccionario que contiene las letras del codigo morse entero. se llama asi ya que son las que muestra el
# nivel facil
morse_dict_easy = {
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

# esta es la lista que se usa para elegir de manera aleatoria el codigo que se muestra en pantalla
morse_list_easy = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
    "-----",
    ".----",
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----."
]

# El diccionario que muestra las frases en codigo morse del nivel medio
morse_dict_mid = {
    "SOS": "... --- ...",
    "HELLO": ".... . .-.. .-.. ---",
    "YES": "-.-- . ...",
    "NO": "-. ---",
    "PLAY": ".--. .-.. .- -.--",
    "FUN": "..-. ..- -.",
    "NIKO": "-. .. -.- ---",
}

# lo mismo que la lista anterior pero para el nivel medio
morse_list_mid = [
    "... --- ...",
    ".... . .-.. .-.. ---",
    "-.-- . ...",
    "-. ---",
    ".--. .-.. .- -.--",
    "..-. ..- -.",
    "-. .. -.- ---",
]

# El diccionario que muestra las frases del modo dificil
morse_dict_hard = {
    "THE QUICK BROWN FOX": "- .... ./--.- ..- .. -.-. -.-/-... .-. --- .-- -./..-. --- -..-",
    "JUMP OVER THE LAZY DOG": ".--- ..- -- .--./--- ...- . .-./- .... ./.-.. .- --.. -.--/-.. --- --.",
    "MORSE CODE IS FUN": "-- --- .-. ... ./-.-. --- -.. ./.. .../..-. ..- -.",
    "SAVE THE WORLD": ".. .- ...-./- .... ./.-- --- .-. .-. -..",
    "HELLO WORLD": ".... . .-.. .-.. ---/.-- --- .-. .-.. -..",
}

# lo mismo que las otras listas pero para el nivel dificil
morse_list_hard = [
    "- .... ./--.- ..- .. -.-. -.-/-... .-. --- .-- -./..-. --- -..-",
    ".--- ..- -- .--./--- ...- . .-./- .... ./.-.. .- --.. -.--/-.. --- --.",
    "-- --- .-. ... ./-.-. --- -.. ./.. .../..-. ..- -.",
    ".. .- ...-./- .... ./.-- --- .-. .-. -..",
    ".... . .-.. .-.. ---/.-- --- .-. .-.. -..",
]

# una clase dificultad. se creo porque las funciones que son llamadas por el boton no pueden cambiar variables permanentemento entonces
# se guarda el estado de la dificultad en un objeto
class Difficulty():
    def __init__(self):
        self.set = "easy"

    def set_difficulty(self, diff):
        self.set = diff

class Mode():
    def __init__(self):
        self.set = ""

    def set_mode(self, mode):
        self.set = mode
# Boton custom para aprender como funcionaban los botones, se cambiara por 
# submit_button = ft.Button("Submit", on_click=btn_callback, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
# dentro de la funcion main para seguir el mismo patron que los otros botones
# !!!!!! SE PUEDE BORRAR PERO REEMPLAZAR POR LA LINEA ANTERIOR DENTRO DE MAIN !!!!!!
class SubBtn(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = "#282828"
        self.height = 50
        self.style = ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30))
        self.width = 300
        self.color = "#ffffff"
        self.text = text
        self.on_click = on_click

# Funcion main
def main(page: ft.Page):
    # instancia del jugador. ir a src/player.py para ver mas
    player = Player()
    # texto del score que se muestra en pantalla
    score = ft.Text(f"Score: {player.score}", size=25)
    # texto de streak que se muestra en pantalla
    streak = ft.Text(f"Streak: {player.streak}", size=25)
    # texto de mult que se muestra en pantalla
    mult = ft.Text(f"Mult: {player.mult}", size=25)
    # texto que lleva la cuenta de los strikes
    strikes = ft.Text(f"Strikes: {player.count}", size=25)
    # esta variable trackea la clave actual
    code = ft.Text("Something went wrong", size = 50, expand=True)
    # esta variable contiene la respuesta del usuario
    answer = ft.TextField(label="answer", text_align=ft.TextAlign.CENTER, width=200)
    # Instancia de la dificultad
    diff = Difficulty()
    # Instancia del modo
    mode = Mode()

    # Funcion que reestablece los textos cuando se vuelve al menu principal
    def restore_labels():
        score.value = f"Score: {player.score}"
        streak.value = f"Streak: {player.streak}"
        mult.value = f"Mult: {player.mult}"
        strikes.value = f"Strikes: {player.count}"
    
    # EL callback hacia la funcion de player para revisar la respuesta del jugador + actualizar el socore, streak y multiplicador
    def btn_callback(e):
        match diff.set:
            case "easy":
                morse_list = morse_list_easy
                morse_dict = morse_dict_easy
            case "mid":
                morse_list = morse_list_mid
                morse_dict = morse_dict_mid
            case "hard":
                morse_list = morse_list_hard
                morse_dict = morse_dict_hard
        
        player.check_answer(answer.value, code.value, morse_dict)
        if mode.set == "play" and player.count >= 3:
            page.clean()
            page.add(game_over)
            page.update
        score.value = f"Score: {player.score}"
        streak.value = f"Streak: {player.streak}"
        mult.value = f"Mult: {player.mult}"
        code.value = morse_list[random.randint(0, len(morse_list)) - 1]
        strikes.value = f"Strikes: {player.count}"
        page.update()

    # El callback que cambia hacia la pagina de la cheatsheet en la pagina de practica
    def change_cheatsheet_page(e):
        page.clean()
        page.add(cheatsheet)
        page.update()
    
    # El callback que cambia hacia la pagina de practica desde la cheatsheet
    def return_practice_page(e):
        page.clean()
        page.add(practice)
        page.update()

    # El callback que lleva hacia la pagina de practica desde el menu principal
    def practice_page(e):
        page.clean()
        mode.set_mode("practice")
        page.add(practice)
        match diff.set:
            case "easy":
                code.value = morse_list_easy[random.randint(0, len(morse_list_easy)) - 1]
            case "mid":
                code.value = morse_list_mid[random.randint(0, len(morse_list_mid)) - 1]
            case "hard":
                code.value = morse_list_hard[random.randint(0, len(morse_list_hard)) - 1]
        page.update()
    
    # El callback que lleva hacia la pagina para jugar desde el menu principal
    def play_page(e):
        page.clean()
        mode.set_mode("play")
        page.add(play)
        match diff.set:
            case "easy":
                code.value = morse_list_easy[random.randint(0, len(morse_list_easy)) - 1]
            case "mid":
                code.value = morse_list_mid[random.randint(0, len(morse_list_mid)) - 1]
            case "hard":
                code.value = morse_list_hard[random.randint(0, len(morse_list_hard)) - 1]
        page.update()

    # El callback que lleva hacia la pagina de configuraciones
    def settings_page(e):
        page.clean()
        page.add(settings)
        page.update()

    # El callback que lleva hacia la pagina de dificultades
    def difficulty_page(e):
        page.clean()
        page.add(difficulty)
        page.update()

    # El callback que lleva hacia la pagina principal
    def return_page(e):
        player.restart_attribs()
        restore_labels()
        page.clean()
        page.add(main_page)
        page.update()
    
    # Los siguientes callbacks son para los botones de cambio de nivel
    # Easy
    # Medium
    # Hard
    # funcionan igual solo se cambia la string de dentro
    # si se cambia a cualquier otra cosa que no sea "easy", "mid" y "hard" no funcionara
    def easy_callback(e):
        diff.set_difficulty("easy")

    def mid_callback(e):
        diff.set_difficulty("mid")

    def hard_callback(e):
        diff.set_difficulty("hard")

    # el boton para mandar la respuesta
    submit_button = SubBtn("Submit", on_click=btn_callback)

    # botones que solo aparecen en la version de practica
    cheatsheet_change_button = ft.Button("Cheatsheet", on_click=change_cheatsheet_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))
    cheatsheet_return_button = ft.Button("Return", on_click=return_practice_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))

    # botones de menu principal
    play_button = ft.Button("Play", on_click=play_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    practice_button = ft.Button("Practice", on_click=practice_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    settings_button = ft.Button("Settings", on_click=settings_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    return_button = ft.Button("Return to Main Menu", on_click=return_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))
    difficulty_button = ft.Button("Difficulty", on_click=difficulty_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))

    # botones de dificultad
    easy_button = ft.Button("easy", on_click=easy_callback, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    mid_button = ft.Button("medium", on_click=mid_callback, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    hard_button = ft.Button("hard", on_click=hard_callback, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)

    # construccion de interfaces
    # Estas interfaces se aguantan como una torre de naipes, manejar con cuidado
    # interfaz de cheatsheet
    cheatsheet = ft.Column([
                ft.Row([ft.Text("A: .-", size = 25), ft.Text("      P: .--.", size = 25), ft.Text("     5: .....", size = 25)], alignment="start"),
                ft.Row([ft.Text("B: -...", size = 25), ft.Text("    Q: --.-", size = 25), ft.Text("     6: -....", size = 25)], alignment="start"),
                ft.Row([ft.Text("C: -.-.", size = 25), ft.Text("    R: .-.", size = 25), ft.Text("      7: --...", size = 25)], alignment="start"),
                ft.Row([ft.Text("D: -..", size = 25), ft.Text("     S: ...", size = 25), ft.Text("      8: ---..", size = 25)], alignment="start"),
                ft.Row([ft.Text("E: .", size = 25), ft.Text("       T: -", size = 25), ft.Text("        9: ----.", size = 25)], alignment="start"),
                ft.Row([ft.Text("E: .", size = 25), ft.Text("       U: ..-", size = 25)], alignment="start"),
                ft.Row([ft.Text("F: ..-.", size = 25), ft.Text("    V: ...-", size = 25)], alignment="start"),
                ft.Row([ft.Text("G: --.", size = 25), ft.Text("     W: .--", size = 25)], alignment="start"),
                ft.Row([ft.Text("H: ....", size = 25), ft.Text("    X: -..-", size = 25)], alignment="start"),
                ft.Row([ft.Text("I: ..", size = 25), ft.Text("      Y: -.--", size = 25)], alignment="start"),
                ft.Row([ft.Text("J: .---", size = 25), ft.Text("    Z: --..", size = 25)], alignment="start"),
                ft.Row([ft.Text("K: -.-", size = 25), ft.Text("     0: -----", size = 25)], alignment="start"),
                ft.Row([ft.Text("L: .-..", size = 25), ft.Text("    1: .----", size = 25)], alignment="start"),
                ft.Row([ft.Text("M: --", size = 25), ft.Text("      2: ..---", size = 25)], alignment="start"),
                ft.Row([ft.Text("N: -.", size = 25), ft.Text("      3: ...--", size = 25)], alignment="start"),
                ft.Row([ft.Text("O: ---", size = 25), ft.Text("     4: ....-", size = 25)], alignment="start"),
                cheatsheet_return_button,
            ], scroll=ft.ScrollMode.ALWAYS)
    
    # interfaz de practica
    practice = ft.Column([
                return_button,
                ft.Row([code], alignment="center"),
                ft.Row([answer], alignment="center"),
                ft.Row([submit_button], alignment="center"),
                ft.Row([ft.Column([score, streak, mult], alignment="center")], alignment="center"),
                ft.Row([cheatsheet_change_button], alignment="center")
            ], scroll=ft.ScrollMode.ALWAYS)
    # interfaz para jugar
    play = ft.Column([
                return_button,
                ft.Row([code], alignment="center"),
                ft.Row([answer], alignment="center"),
                ft.Row([submit_button], alignment="center"),
                ft.Row([ft.Column([score, streak, mult, strikes], alignment="center")], alignment="center"),
            ], scroll=ft.ScrollMode.ALWAYS)
    settings = ft.Column([
                return_button,
                ft.Row([ft.Text("TODO", size=50)], alignment="center")
            ], scroll=ft.ScrollMode.ALWAYS)
    # menu principal 
    main_page = ft.Column([
                ft.Row([ft.Text("Morse", size=50)], alignment="center"),
                ft.Row([play_button], alignment="center"),
                ft.Row([practice_button], alignment="center"),
                ft.Row([settings_button], alignment="center"),
                ft.Row([difficulty_button], alignment="center"),
            ], alignment="center", scroll=ft.ScrollMode.ALWAYS)
    # menu de dificultades
    difficulty = ft.Column([
                ft.Row([ft.Text("Select Difficulty", size=50)], alignment="center"),
                ft.Row([easy_button], alignment="center"),
                ft.Row([mid_button], alignment="center"),
                ft.Row([hard_button], alignment="center"),
                ft.Row([return_button], alignment="center"),
            ], alignment="center", scroll=ft.ScrollMode.ALWAYS)
    # interfaz de game over
    game_over = ft.Column([
                ft.Row([ft.Text("GAME OVER", size=50)], alignment="center"),
                ft.Row([ft.Text("Final Result", size=25)], alignment="center"),
                ft.Row([ft.Column([score, streak, mult], alignment="center")], alignment="center"),
                ft.Row([return_button], alignment="center"),
            ], scroll=ft.ScrollMode.ALWAYS)

    page.add(main_page)

# TODO: FALTA DE HACER LAS CONFIGURACIONES DEL JUEGO, SONIDO E IDIOMA, LA PAGINA YA ESTA PERO NO EXISTE FUNIONALIDAD AUN

ft.app(target=main)
