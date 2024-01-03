import reflex as rx
import datetime

def footer() ->rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        
        rx.link(
            f"Derechos de autor, todo eso, desde el 2018 hasta el {datetime.date.today().year}", 
            href="https://www.youtube.com/", 
            is_external=True
        ),
        
        rx.text(
            "con amor para el q lo lea (?"
        )
    )