import reflex as rx

class State(rx.State):
    pass


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
            font_weight="bold"
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
                rx.vstack(
                    rx.image(
                        src="/male_white.png",
                        height="247px",
                        width="100%",
                        object_fit="contain",  
                    ),
                    rx.vstack(
                        rx.text(
                            "Male",
                            font_size="96px",
                            letter_spacing="-5px",
                            font_weight="bold",
                            line_height="96px"
                        ),
                        rx.text(
                            "99% confident",
                            font_size="32px",
                            color="#D0D0D0",
                            line_height="45px"
                        ),
                        spacing="0",
                        gap="8px"
                    ),
                    spacing="0",
                    gap="16px",
                    padding="16px",
                    height="520px",
                    width="100%",
                    bg="#1C1B1C",
                    border="1px solid #2C2C2C"
                ),
                rx.vstack(
                    rx.image(
                        src="/male_white.png",
                        height="247px",
                        width="100%",
                        object_fit="contain",  
                    ),
                    rx.vstack(
                        rx.text(
                            "Male",
                            font_size="96px",
                            letter_spacing="-5px",
                            font_weight="bold",
                            line_height="96px"
                        ),
                        rx.text(
                            "99% confident",
                            font_size="32px",
                            color="#D0D0D0",
                            line_height="45px"
                        ),
                        spacing="0",
                        gap="8px"
                    ),
                    spacing="0",
                    gap="16px",
                    padding="16px",
                    height="520px",
                    width="100%",
                    bg="#1C1B1C",
                    border="1px solid #2C2C2C"
                ),
                rx.vstack(
                    rx.image(
                        src="/male_white.png",
                        height="247px",
                        width="100%",
                        object_fit="contain",  
                    ),
                    rx.vstack(
                        rx.text(
                            "Male",
                            font_size="96px",
                            letter_spacing="-5px",
                            font_weight="bold",
                            line_height="96px"
                        ),
                        rx.text(
                            "99% confident",
                            font_size="32px",
                            color="#D0D0D0",
                            line_height="45px"
                        ),
                        spacing="0",
                        gap="8px"
                    ),
                    spacing="0",
                    gap="16px",
                    padding="16px",
                    height="520px",
                    width="100%",
                    bg="#1C1B1C",
                    border="1px solid #2C2C2C"
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

app = rx.App()
app.add_page(index)
app.add_page(results)
