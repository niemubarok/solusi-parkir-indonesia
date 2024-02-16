import flet as ft
from pages.LandingPage import LandingPage
from pages.ProductsPage import ProductPage




def main(page: ft.Page):
    
    def router(e):
        page.views.clear()
        if e.route == "/":
            lp = LandingPage(page)
            page.views.append(lp)
        elif e.route == "/products":
            pp = ProductPage(page)
            page.views.append(pp)
        
        page.update()

    page.on_route_change = router
    page.go("/")

ft.app(main)
