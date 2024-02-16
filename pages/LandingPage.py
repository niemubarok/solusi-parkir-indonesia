import flet as ft

class LandingPage(ft.View):
    def __init__(self, page:ft.Page):
        super(LandingPage, self).__init__(
            route="/", horizontal_alignment=ft.CrossAxisAlignment.CENTER, vertical_alignment=ft.MainAxisAlignment.CENTER
            
        )
        self.page = page
        self.cart_icon = ft.Icon(ft.icons.CAR_RENTAL, color="white", size=35)
        self.title = ft.Text("Solusi Parkir Indonesia", size = 30, color="white", weight="bold")
        self.subtitle = ft.Text("Semua Kebutuhan Usaha Parkir Anda", size = 15, color="white")
        self.product_button = ft.IconButton("arrow_forward", 
                                            width=54,
                                            height=54,
                                            style=ft.ButtonStyle(
                                                # bgcolor=ft.colors.BLUE_200,
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                                side=ft.BorderSide(2, "white")
                                                
                                                
                                            ),
                                            on_click=lambda e: self.page.go("/products"))
        
        self.controls = [
            self.cart_icon,
            self.title,
            ft.Divider(height=4,thickness=1, color="grey"),
            self.subtitle,
            ft.Divider(height=10, color="transparent"),
            self.product_button
            
        ]