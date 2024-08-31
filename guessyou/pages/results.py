import reflex as rx
from guessyou.components.card import card, age_card  
from guessyou.state import State

@rx.page(on_load=State.load_result)
def results() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(
                    "Hi, ",
                    font_weight="bold",
                    line_height="15vh",
                    font_size="10vw"
                ),
                rx.text(
                    State.current_input,
                    font_weight="bold",
                    line_height="15vh",
                    font_size="10vw"
                ),
                rx.text(
                    " 👋",
                    font_weight="bold",
                    line_height="15vh",
                    font_size="10vw"
                ),
                spacing="0",
                gap = "0.5vh"
            ),
           
            rx.text(
                "I think you are:",
                font_size="5vh",
                line_height="5vh",
                margin_top="2.5vh",
                margin_left="0.3vw"
            ),
            rx.hstack(
                card(
                    image=State.gender_img,
                    text=State.gender_text,
                    subtext=State.gender_subtext    
                ),
                age_card(
                    big_text=State.age_text,
                    text=State.age_text,
                    subtext="years old"    
                ),
                card(
                    image=State.nation_flag,
                    text=State.nation_text,
                    subtext=State.nation_subtext    
                ),
                spacing="0",
                gap="10vw",
                width="95vw",
                height="69vh",
                padding="5vh"
            ),
            position="absolute",
            left="3vw",
            top="5vh",
            spacing="0",
            gap="1vh"
        )
    )
