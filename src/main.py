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

class Lang():
    spanish_lang = {
        "score": "puntos",
        "streak": "racha",
        "mult": "mult",
        "strikes": "fallos",
        "code_not_loaded": "Ocurrio un error al cargar codigo",
        "answer": "respuesta",
        "submit": "enviar",
        "cheatsheet": "acordeon",
        "return": "regresar",
        "play": "jugar",
        "practice": "practica",
        "settings": "ajustes",
        "difficulty": "dificultad",
        "easy": "facil",
        "medium": "medio",
        "hard": "dificil",
        "game_over": "fin del juego",
        "final_results": "resultados finales",
        "return_main_menu": "regresar al menu principal",
        "select_difficulty": "seleccionar dificultad",
        "spn": "español",
        "eng": "ingles",
        "tutorial": "tutorial",
        "next": "siguiente",
        "dialogue1": "Holaaaaaaaaa :3 y bienvenido OwO al tutorial de codigo morse, aqui encontraras todo para empezar!!!!! >w<",
        "dialogue2": "Primero un poco de historia",
        "dialogue3": "El Codigo morse es una manera de codificar texto en secuencias de dos señales diferentes llamados puntos y guiones. Su nombre esta basado en el nombre de Samuel Morse, uno de los muchos desarrolladore del codigo morse",
        "dialogue4": "en este juego aprenderas el ITU (Codigo Morse Internacional) el cual codifica 26 letras basicas latinas (A-Z) y numeros del 0 al 9",
        "dialogue5": "Como antes dicho el codigo morse codifica texto en secuencias de puntos y guiones, asi que aprendamos algunas letras",
        "dialogue6": "Empezando por el abecedario (en el modo practica puedes ver un acordeon con todas las letras)",
        "dialogue7": "Puedes practicar diciendo los simbolos en voz alta de la siguiente forma 'di dah' (A) 'dah di di dit' (B), 'dah di dah dit' (C), de esta manera empezaras a acostumbrarte al tempo del codigo morse",
        "dialogue8": "Los numeros son mas faciles de memorizar, inicias con 5 guiones (dahs), este es tu 0, despues empiezas a reemplazar los guiones con puntos (dits)",
        "dialogue9": "etc.",
        "dialogue10": "una vez tienes tienes los 5 espacios llenos de puntos empiezas a reemplazarlos con guiones otra vez",
        "dialogue11": "Con esto ya te haces una idea de como funciona, ahora practicalo en el modo practica",
    }
    english_lang = {
        "score": "score",
        "streak": "streak",
        "mult": "mult",
        "strikes": "strikes",
        "code_not_loaded": "something went wrong...",
        "answer": "answer",
        "submit": "submit",
        "cheatsheet": "cheatsheet",
        "return": "return",
        "play": "play",
        "practice": "practice",
        "settings": "settings",
        "difficulty": "difficulty",
        "easy": "easy",
        "medium": "medium",
        "hard": "hard",
        "game_over": "game over",
        "final_results": "final Results",
        "return_main_menu": "return to main menu",
        "select_difficulty": "select difficulty",
        "spn": "spanish",
        "eng": "english",
        "tutorial": "tutorial",
        "next": "next",
        "dialogue1": "Haaaaaaai :3 and welcome OwO to the Morse code tutorial, here you'll find everything you need to know to get you started!!!! >w<",
        "dialogue2": "First a little bit of history",
        "dialogue3": "Morse code is a way to encode text in sequences of two different signal durations called dots and dashes. It is named after Samuel Morse, one of the several morse code developers",
        "dialogue4": "In this game you'll learn the ITU (International Morse Code) which encodes 26 basic latin letters (A-Z) and numbers through 0 to 9",
        "dialogue5": "Like previously stated, morse code is a way to encode text in sequences of dots and dashes so how about we learn some letters",
        "dialogue6": "Starting with.... our ABCs (In practice mode you have a cheatsheet where you can view all the character translations)",
        "dialogue7": "You can practice this saying them outloud like 'di dah' (A) 'dah di di dit' (B) 'dah di dah dit', This way you'll start the sounds and timing of morse code",
        "dialogue8": "Numbers are easier to memorize, you start with five dashes (dahs) thats your 0, then you start replacing them with dots (dits)",
        "dialogue9": "and so on",
        "dialogue10": "once you have those five spaces filled with dots then you start replacing them with dashes",
        "dialogue11": "You get the gist of it, now go and practice with our practice mode",
    }
    def __init__(self):
        self.current_lang = self.spanish_lang

    def set_lang(self, lang):
        match lang:
            case "spanish":
                self.current_lang = self.spanish_lang
            case "english":
                self.current_lang = self.english_lang

# Funcion main
def main(page: ft.Page):
    page.window.width = 200        # window's width is 200 px
    page.window.height = 200       # window's height is 200 px
    page.window.resizable = False
    # instancia del jugador. ir a src/player.py para ver mas
    player = Player()
    glob_lang = Lang()

    dialogue1 = ft.Text(f"{glob_lang.current_lang["dialogue1"]}", expand=True, size=15)
    dialogue2 = ft.Text(f"{glob_lang.current_lang["dialogue2"]}", expand=True, size=15)
    dialogue3 = ft.Text(f"{glob_lang.current_lang["dialogue3"]}", expand=True, size=15)
    dialogue4 = ft.Text(f"{glob_lang.current_lang["dialogue4"]}", expand=True, size=15)
    dialogue5 = ft.Text(f"{glob_lang.current_lang["dialogue5"]}", expand=True, size=15)
    dialogue6 = ft.Text(f"{glob_lang.current_lang["dialogue6"]}", expand=True, size=15)
    dialogue7 = ft.Text(f"{glob_lang.current_lang["dialogue7"]}", expand=True, size=15)
    dialogue8 = ft.Text(f"{glob_lang.current_lang["dialogue8"]}", expand=True, size=15)
    dialogue9 = ft.Text(f"{glob_lang.current_lang["dialogue9"]}", expand=True, size=15)
    dialogue10 = ft.Text(f"{glob_lang.current_lang["dialogue10"]}", expand=True, size=15)
    dialogue11 = ft.Text(f"{glob_lang.current_lang["dialogue11"]}", expand=True, size=15)

    # texto del score que se muestra en pantalla
    score = ft.Text(f"{glob_lang.current_lang["score"]}: {player.score}", size=25)
    # texto de streak que se muestra en pantalla
    streak = ft.Text(f"{glob_lang.current_lang["streak"]}: {player.streak}", size=25)
    # texto de mult que se muestra en pantalla
    mult = ft.Text(f"{glob_lang.current_lang["mult"]}: {player.mult}", size=25)
    # texto que lleva la cuenta de los strikes
    strikes = ft.Text(f"{glob_lang.current_lang["strikes"]}: {player.count}", size=25)
    # esta variable trackea la clave actual
    code = ft.Text(f"{glob_lang.current_lang["code_not_loaded"]}", size = 50, expand=True)
    # esta variable contiene la respuesta del usuario
    answer = ft.TextField(label=f"{glob_lang.current_lang["answer"]}", text_align=ft.TextAlign.CENTER, width=200)

    final_results = ft.Text(f"{glob_lang.current_lang["final_results"]}", size=25)
    game_over = ft.Text(f"{glob_lang.current_lang["game_over"]}", size=50)
    select_difficulty = ft.Text(f"{glob_lang.current_lang["difficulty"]}", size=50)
    # Instancia de la dificultad
    diff = Difficulty()
    # Instancia del modo
    mode = Mode()

    # Funcion que reestablece los textos cuando se vuelve al menu principal
    def restore_labels():
        score.value = f"{glob_lang.current_lang["score"]}: {player.score}"
        streak.value = f"{glob_lang.current_lang["streak"]}: {player.streak}"
        mult.value = f"{glob_lang.current_lang["mult"]}: {player.mult}"
        strikes.value = f"{glob_lang.current_lang["strikes"]}: {player.count}"
        play_button.text = f"{glob_lang.current_lang["play"]}"
        practice_button.text = f"{glob_lang.current_lang["practice"]}"
        settings_button.text = f"{glob_lang.current_lang["settings"]}"
        difficulty_button.text = f"{glob_lang.current_lang["difficulty"]}"
        answer.label=f"{glob_lang.current_lang["answer"]}"
        return_button.text = f"{glob_lang.current_lang["return_main_menu"]}"
        submit_button.text = f"{glob_lang.current_lang["submit"]}"
        cheatsheet_change_button.text = f"{glob_lang.current_lang["cheatsheet"]}"
        cheatsheet_return_button.text = f"{glob_lang.current_lang["return"]}"
        easy_button.text = f"{glob_lang.current_lang["easy"]}"
        mid_button.text = f"{glob_lang.current_lang["medium"]}"
        hard_button.text = f"{glob_lang.current_lang["hard"]}"
        spn_button.text = f"{glob_lang.current_lang["spn"]}"
        eng_button.text = f"{glob_lang.current_lang["eng"]}"
        game_over.value = f"{glob_lang.current_lang["game_over"]}"
        final_results.value = f"{glob_lang.current_lang["final_results"]}"
        dialogue1.value = f"{glob_lang.current_lang["dialogue1"]}"
        dialogue2.value = f"{glob_lang.current_lang["dialogue2"]}"
        dialogue3.value = f"{glob_lang.current_lang["dialogue3"]}"
        dialogue4.value = f"{glob_lang.current_lang["dialogue4"]}"
        dialogue5.value = f"{glob_lang.current_lang["dialogue5"]}"
        dialogue6.value = f"{glob_lang.current_lang["dialogue6"]}"
        dialogue7.value = f"{glob_lang.current_lang["dialogue7"]}"
        dialogue8.value = f"{glob_lang.current_lang["dialogue8"]}"
        dialogue9.value = f"{glob_lang.current_lang["dialogue9"]}"
        dialogue10.value = f"{glob_lang.current_lang["dialogue10"]}"
        dialogue11.value = f"{glob_lang.current_lang["dialogue11"]}"
    
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
        score.value = f"{glob_lang.current_lang["score"]}: {player.score}"
        streak.value = f"{glob_lang.current_lang["streak"]}: {player.streak}"
        mult.value = f"{glob_lang.current_lang["mult"]}: {player.mult}"
        code.value = morse_list[random.randint(0, len(morse_list)) - 1]
        strikes.value = f"{glob_lang.current_lang["strikes"]}: {player.count}"
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

    def tutorial_page(e):
        page.clean()
        page.add(tutorial1)
        page.update()

    def tutorial1_to_tutorial2(e):
        page.clean()
        page.add(tutorial2)
        page.update()

    def tutorial2_to_tutorial3(e):
        page.clean()
        page.add(tutorial3)
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
        page.clean()
        page.add(main_page)
        page.update()

    def mid_callback(e):
        diff.set_difficulty("mid")
        page.clean()
        page.add(main_page)
        page.update()

    def hard_callback(e):
        diff.set_difficulty("hard")
        page.clean()
        page.add(main_page)
        page.update()

    def spanish_lang_callback(e):
        glob_lang.set_lang("spanish")
        restore_labels()
        page.clean()
        page.add(main_page)
        page.update()

    def english_lang_callback(e):
        glob_lang.set_lang("english")
        restore_labels()
        page.clean()
        page.add(main_page)
        page.update()
    # el boton para mandar la respuesta
    submit_button = ft.Button("Submit", on_click=btn_callback, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)

    # botones que solo aparecen en la version de practica
    cheatsheet_change_button = ft.Button(f"{glob_lang.current_lang["cheatsheet"]}", on_click=change_cheatsheet_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))
    cheatsheet_return_button = ft.Button(f"{glob_lang.current_lang["return"]}", on_click=return_practice_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))

    # botones de menu principal
    play_button = ft.Button(f"{glob_lang.current_lang["play"]}", on_click=play_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    tutorial_button = ft.Button(f"{glob_lang.current_lang["tutorial"]}", on_click=tutorial_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    practice_button = ft.Button(f"{glob_lang.current_lang["practice"]}", on_click=practice_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    settings_button = ft.Button(f"{glob_lang.current_lang["settings"]}", on_click=settings_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    return_button = ft.Button(f"{glob_lang.current_lang["return_main_menu"]}", on_click=return_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))
    difficulty_button = ft.Button(f"{glob_lang.current_lang["difficulty"]}", on_click=difficulty_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))

    # botones de dificultad
    easy_button = ft.Button(f"{glob_lang.current_lang["easy"]}", on_click=easy_callback, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    mid_button = ft.Button(f"{glob_lang.current_lang["medium"]}", on_click=mid_callback, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    hard_button = ft.Button(f"{glob_lang.current_lang["hard"]}", on_click=hard_callback, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)

    spn_button = ft.Button(f"{glob_lang.current_lang["spn"]}", on_click=spanish_lang_callback, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    eng_button = ft.Button(f"{glob_lang.current_lang["eng"]}", on_click=english_lang_callback, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)

    tut1_to_tut2 = ft.Button(f"{glob_lang.current_lang["next"]}", on_click=tutorial1_to_tutorial2, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))
    tut2_to_tut3 = ft.Button(f"{glob_lang.current_lang["next"]}", on_click=tutorial2_to_tutorial3, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))
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
                ft.Row([spn_button], alignment="center"),
                ft.Row([eng_button], alignment="center"),
            ], scroll=ft.ScrollMode.ALWAYS)
    # menu principal 
    main_page = ft.Column([
                ft.Row([ft.Text("Morse", size=50)], alignment="center"),
                ft.Row([play_button], alignment="center"),
                ft.Row([practice_button], alignment="center"),
                ft.Row([tutorial_button], alignment="center"),
                ft.Row([settings_button], alignment="center"),
                ft.Row([difficulty_button], alignment="center"),
            ], alignment="center", scroll=ft.ScrollMode.ALWAYS)
    # menu de dificultades
    difficulty = ft.Column([
                ft.Row([select_difficulty], alignment="center"),
                ft.Row([easy_button], alignment="center"),
                ft.Row([mid_button], alignment="center"),
                ft.Row([hard_button], alignment="center"),
                ft.Row([return_button], alignment="center"),
            ], alignment="center", scroll=ft.ScrollMode.ALWAYS)
    # interfaz de game over
    game_over = ft.Column([
                ft.Row([game_over], alignment="center"),
                ft.Row([final_results], alignment="center"),
                ft.Row([ft.Column([score, streak, mult], alignment="center")], alignment="center"),
                ft.Row([return_button], alignment="center"),
            ], scroll=ft.ScrollMode.ALWAYS)
    
    tutorial1 = ft.Column([
                return_button,
                ft.Row([dialogue1]),
                ft.Row([dialogue2]),
                ft.Row([dialogue3]),
                ft.Row([dialogue4]),
                ft.Row([tut1_to_tut2])
            ], scroll=ft.ScrollMode.ALWAYS)
    tutorial2 = ft.Column([
                return_button,
                ft.Row([dialogue5]),
                ft.Row([dialogue6]),
                ft.Row([ft.Text("A: .-", expand=True, size=25)]),
                ft.Row([ft.Text("B: -...", expand=True, size=25)]),
                ft.Row([ft.Text("C: -.-.", expand=True, size=25)]),
                ft.Row([dialogue7]),
                ft.Row([tut2_to_tut3])
           ], scroll=ft.ScrollMode.ALWAYS)
    tutorial3 = ft.Column([
                ft.Row([dialogue8]),
                ft.Row([ft.Text("0: -----", expand=True, size=25)]),
                ft.Row([ft.Text("1: .----", expand=True, size=25)]),
                ft.Row([ft.Text("2: ..---", expand=True, size=25)]),
                ft.Row([dialogue9]),
                ft.Row([dialogue10]),
                ft.Row([ft.Text("6: -....", expand=True, size=25)]),
                ft.Row([ft.Text("7: --...", expand=True, size=25)]),
                ft.Row([ft.Text("6: ---..", expand=True, size=25)]),
                ft.Row([dialogue11]),
                return_button,
        ], scroll=ft.ScrollMode.ALWAYS)
    page.add(main_page)

ft.app(target=main)
