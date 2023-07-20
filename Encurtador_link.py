
import flet as ft   # Framework resposavel pelo site
import pyshorteners  # Resposavel pelo encurtador


def main(page):

    # Configurações padrões
    page.title = "Encurtador de link"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.update()

    # Função evento
    def btn_click(e):  # Caso não digite, aparecer um erro
        if not txt_link.value:
            txt_link.error_text = "Por favor, digite seu link"
            page.update()

        else:  # Encurtador
            llink = pyshorteners.Shortener()
            llink.tinyurl.short('http://www.google.com')
            link = txt_link.value

            page.add(
                ft.Text(f"Seu link é {llink.tinyurl.short(link)}",
                        size=15, weight=ft.FontWeight.W_900, selectable=True)
            )

    txt_link = ft.TextField(label="Seu link")

    page.add(
        txt_link,
        ft.ElevatedButton("Gerar link", on_click=btn_click)
    )


# Executar em browser
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
