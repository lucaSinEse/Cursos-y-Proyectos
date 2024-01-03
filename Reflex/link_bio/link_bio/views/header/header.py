import reflex as rx

def header() ->rx.Component:
    return rx.vstack(
        rx.avatar(
            name="LucaCuchi",
            size="xl"
        ),
        rx.text("@LucaCuchi"),
        rx.text("Hola, mi nombre es LucaCuchi etc etc."),
        rx.text("""Aca iria un testamento diciendo quien soy y todo eso.""")
    )