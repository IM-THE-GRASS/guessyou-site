import reflex as rx
from guessyou.state import State

def index() -> rx.Component:
    return rx.box(
        rx.image(
            src="/GUESSYOU.png",
            width="1117px",
            height="204px",
            position="absolute",
            left="401px",
            top="156px"
        ),
        rx.input(
            placeholder="What's your name?",
            size="3",
            position="absolute",
            left="636px",
            top="410px",
            width="636px",
            height="100px",
            font_size="70px",
            letter_spacing="-4px",
            bg="#1C1B1C",
            font_weight="bold",
            value=State.current_input,
            on_change=State.on_change_input
        ),
        rx.button(
            rx.image(
                src="/Button.png",
                width="256px",
                height="64px"
            ),
            as_child=True,
            variant="ghost",
            position="absolute",
            left="832px",
            top="560px",
            on_click=rx.redirect("/results")
        )
    )