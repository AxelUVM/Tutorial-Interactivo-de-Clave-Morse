import flet as ft
import random

from player import Player

morse_list = [
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

def main(page: ft.Page):
    player = Player()
    # esta variable trackea la cuenta del score
    score = ft.Text(f"Score: {player.score}", size=25)
    streak = ft.Text(f"Streak: {player.streak}", size=25)
    mult = ft.Text(f"Mult: {player.mult}", size=25)
    # esta variable trackea la clave actual
    code = ft.Text(morse_list[random.randint(0, len(morse_list)) - 1], size = 75)
    # esta variable contiene la respuesta del usuario
    answer = ft.TextField(label="answer", text_align=ft.TextAlign.CENTER, width=200)

    def restore_labels():
        score.value = f"Score: {player.score}"
        streak.value = f"Streak: {player.streak}"
        mult.value = f"Mult: {player.mult}"

    def btn_callback(e):
        player.check_answer(answer.value, code.value)
        score.value = f"Score: {player.score}"
        streak.value = f"Streak: {player.streak}"
        mult.value = f"Mult: {player.mult}"
        code.value = morse_list[random.randint(0, len(morse_list)) - 1]
        page.update()

    def change_cheatsheet_page(e):
        page.clean()
        page.add(cheatsheet)
        page.update()

    def return_practice_page(e):
        page.clean()
        page.add(practice)
        page.update()

    def practice_page(e):
        page.clean()
        page.add(practice)
        page.update()

    def play_page(e):
        page.clean()
        page.add(play)
        page.update()

    def settings_page(e):
        page.clean()
        page.add(settings)
        page.update()

    def return_page(e):
        player.restart_attribs()
        restore_labels()
        page.clean()
        page.add(main_page)
        page.update()
    # el boton para mandar la respuesta
    submit_button = SubBtn("Submit", on_click=btn_callback)

    # botones que solo aparecen en la version de practica
    cheatsheet_change_button = ft.Button("Cheetsheet", on_click=change_cheatsheet_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))
    cheatsheet_return_button = ft.Button("Return", on_click=return_practice_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))

    # botones de menu principal
    play_button = ft.Button("Play", on_click=play_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    practice_button = ft.Button("Practice", on_click=practice_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    settings_button = ft.Button("Settings", on_click=settings_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)), height=100, width=300)
    return_button = ft.Button("Return to Main Menu", on_click=return_page, bgcolor="#282828", color="#ffffff", style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)))

    # construccion de interfaces
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
            ])
    
    # interfaz de practica
    practice = ft.Column([
                return_button,
                ft.Row([code], alignment="center"),
                ft.Row([answer], alignment="center"),
                ft.Row([submit_button], alignment="center"),
                ft.Row([ft.Column([score, streak, mult], alignment="center")], alignment="center"),
                ft.Row([cheatsheet_change_button], alignment="center")
            ])
    # interfaz para jugar
    play = ft.Column([
                return_button,
                ft.Row([code], alignment="center"),
                ft.Row([answer], alignment="center"),
                ft.Row([submit_button], alignment="center"),
                ft.Row([ft.Column([score, streak, mult, ft.Text("Time Left: Placeholder"), ft.Text("Strikes: Placeholder")], alignment="center")], alignment="center"),
            ])
    settings = ft.Column([
            return_button,
            ft.Row([ft.Text("HAAAAAAAAAAAAAAAAAAAAAAI :3", size=50)], alignment="center")
        ])
    # menu principal 
    main_page = ft.Column([
                ft.Row([ft.Text("Morse", size=50)], alignment="center"),
                ft.Row([play_button], alignment="center"),
                ft.Row([practice_button], alignment="center"),
                ft.Row([settings_button], alignment="center"),
                ], alignment="center")

    page.add(main_page)
ft.app(main)
