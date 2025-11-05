import flet as ft
morse={ #la lista de la tarduccion del abecedario a morse 

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

def main(page: ft.Page):
    # TODO: completar la funcion para revisar la respuesta del usuario
    def check_answer():
        pass

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
