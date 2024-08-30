import reflex as rx
from guessyou.components.card import card   



def results() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Hi, Josh 👋",
                font_weight="bold",
                line_height="134px",
                font_size="96px"
            ),
            rx.text(
                "I think you are:",
                font_size="48px",
                line_height="48px"
            ),
            rx.hstack(
                card(),
                card(),
                card(),
                spacing="0",
                gap="198px",
                width="1821px",
                height="637px",
                padding="50px"
            ),
            position="absolute",
            left="50px",
            top="50px"
        )
    )