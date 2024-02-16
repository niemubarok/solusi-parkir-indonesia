import flet as ft 

class ProductPage(ft.View):
    def __init__(self, page:ft.Page):
        super(ProductPage, self).__init__(
            route="/products", horizontal_alignment=ft.CrossAxisAlignment.CENTER, vertical_alignment=ft.MainAxisAlignment.CENTER
        )
        self.page = page
        self.title = ft.Text("Products", size = 30, color="white", weight="bold")
        
        self.controls = [
            self.title
        ]