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

def main(page: ft.Page):
    player = Player()
    # esta variable trackea la cuenta del score
    score = ft.Text("0", size=25)
    streak = ft.Text("0", size=25)
    mult = ft.Text("0.0", size=25)
    # esta variable trackea la clave actual
    code = ft.Text(morse_list[random.randint(0, len(morse_list)) - 1], size = 75)
    # esta variable contiene la respuesta del usuario
    answer = ft.TextField(label="answer", text_align=ft.TextAlign.CENTER, width=500)

    def btn_callback(e):
        player.check_answer(answer.value, code.value)
        score.value = str(player.score)
        code.value = morse_list[random.randint(0, len(morse_list)) - 1]
        page.update()

    # el boton para mandar la respuesta
    submit_button = ft.ElevatedButton("Submit", on_click=btn_callback)

    # construccion de la interfaz
    page.add(
        ft.Container(
            content=
            ft.Column(
                controls=[

                    ft.Container(height=50),
                    ft.Container(
                        code,
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        answer,
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        submit_button,
                        alignment=ft.alignment.center
                    ),
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("Score: ", size=25),
                                    score,
                                ],
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text("Streak: ", size=25),
                                    streak,
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text("Mult: ", size=25),
                                    mult,
                                    ft.Text("x", size=25),
                                ]
                            ),
                        ],
                    ),
                ],
            ),
        )
    )
ft.app(main)
