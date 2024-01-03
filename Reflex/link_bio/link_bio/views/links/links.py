import reflex as rx
from link_bio.components.link_button import link_button

def links() ->rx.Component:
    return rx.vstack(
        link_button("Twitch","https://www.twitch.tv/"),
        link_button("Youtube", "https://www.youtube.com/"),
        link_button("Linkedin", "https://www.linkedin.com/"),
        link_button("Netflix", "https://www.netflix.com/"),
    )