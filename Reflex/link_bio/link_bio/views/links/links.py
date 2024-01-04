import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() ->rx.Component:
    return rx.vstack(
        title("Titulo que me de la gana"),
        link_button("Twitch","directos","https://www.twitch.tv/"),
        link_button("Youtube","videos", "https://www.youtube.com/"),
        link_button("Linkedin","laburo", "https://www.linkedin.com/"),
        link_button("Netflix","entretenimiento", "https://www.netflix.com/"),
        width = "100%"
    )