import flet as ft

def main(page: ft.Page):
    def check_answer():
        pass

    score = ft.Text("0", size=25, data=0)
    code = ft.Text("placeholder", size = 75)
    answer = ft.TextField(label="answer", text_align=ft.TextAlign.CENTER, width=500)
    submit_button = ft.ElevatedButton("Submit", on_click=check_answer)

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
