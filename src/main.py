import flet as ft

# TODO: completar la funcion para revisar la respuesta del usuario
class Player():
    def __init__(self, score: int = 0, streak: int = 0, mult: float = 1.0):
        self.score = score
        self.streak = streak
        self.mult = mult

    def check_answer(self, answer: str, code: str):
        if answer == code:
            self.score += 100
            self.streak += 1
        elif answer != score and score > 0:
            self.score -= 100
            self.streak = 0

def main(page: ft.Page):
    # esta variable trackea la cuenta del score
    score = ft.Text("0", size=25, data=0)
    # esta variable trackea la clave actual
    code = ft.Text("placeholder", size = 75)
    # esta variable contiene la respuesta del usuario
    answer = ft.TextField(label="answer", text_align=ft.TextAlign.CENTER, width=500)
    # el boton para mandar la respuesta
    submit_button = ft.ElevatedButton("Submit", on_click=check_answer)

    # construccion de la interfaz
    page.add(
        ft.Container(
            content=
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("Score: ", size=25),
                            score,
                        ]
                    ),
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
                    )
                ],
            ),
        )
    )
ft.app(main)
