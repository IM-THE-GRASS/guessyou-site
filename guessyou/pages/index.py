import reflex as rx
from guessyou.state import State

def index() -> rx.Component:
    return rx.box(
        rx.center(
            rx.image(
                src="/GUESSYOU.png",
                width="100%",
                height="22vh",
                object_fit="contain"
                # position="absolute",
                # left="21vw",
                # top="17vh"
            ),
            width="100vw",
            height="22vh",
            position="absolute",
            left="0vw",
            top="17vh"
        ),
        rx.center(
            rx.input(
                placeholder="What's your name?",
                size="3",
                # width="33vw",
                width=["100vw","33vw"],
                height="11vh",
                font_size="7.6vh",
                letter_spacing="-0.4vh",
                bg="#1C1B1C",
                font_weight="bold",
                value=State.current_input,
                on_change=State.on_change_input
            ),
            position="absolute",
            left="0vw",
            top="45vh",
            width="100vw",
            height="11vh",
        ),
        rx.center(
            rx.button(
                rx.image(
                    src="/Button.png",
                    height="7vh"
                ),
                as_child=True,
                variant="ghost",
                
                on_click=rx.redirect("/results")
            ),
            position="absolute",
            left="0vw",
            top="61vh",
            width="100vw"
        ),
        
    )
