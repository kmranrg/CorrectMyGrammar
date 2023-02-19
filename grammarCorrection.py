import flet as ft
from standardEnglish import StandardEnglish

def main(page: ft.Page):
    page.title = "CorrectYourGrammar"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.window_max_width = 700
    page.window_max_height = 600
    page.window_width = 700
    page.window_height = 600
    page.window_frameless = True

    logo = ft.Image(src=f"logo.jpg", width=300)
    user_input = ft.TextField(hint_text="enter any sentence...", border_radius=30)
    outputText = ft.Text("your response will be generated here...")
    
    def print_result(e):
        answer = StandardEnglish(str(user_input.value)).convertStandardEnglish()
        outputText.value = answer[2:]
        print("=>",answer)
        page.update()
    
    outputContainer = ft.Container(
        content=outputText,
        margin=20,
        padding=20,
        bgcolor="#f2f2f2",
        border_radius=30
    )

    page.add(
        logo,
        user_input,
        ft.ElevatedButton("submit", on_click=print_result),
        outputContainer,
        ft.Image(src=f"children_happy.jpg", width=500)
    )

ft.app(target=main, assets_dir="assets")