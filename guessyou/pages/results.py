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
                    line_height="134px",
                    font_size="96px"
                ),
                rx.text(
                    State.current_input,
                    font_weight="bold",
                    line_height="134px",
                    font_size="96px"
                ),
                rx.text(
                    " 👋",
                    font_weight="bold",
                    line_height="134px",
                    font_size="96px"
                ),
            ),
            
            rx.text(
                "I think you are:",
                font_size="48px",
                line_height="48px"
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