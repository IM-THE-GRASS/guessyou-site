import reflex as rx


def card(image = "/male_white.png", text="Male", subtext = "99% confident"):
    return rx.vstack(
        rx.image(
            src=image,
            height="26.9vh",
            width="100%",
            object_fit="contain",  
        ),
        rx.vstack(
            rx.text(
                text,
                font_size="10.4vh",
                letter_spacing="-0.5vh",
                font_weight="bold",
                line_height="10.4vh"
            ),
            rx.text(
                subtext,
                font_size="3.5vh",
                color="#D0D0D0",
                line_height="4.9vh"
            ),
            spacing="0",
            gap="0.9vh"
        ),
        spacing="0",
        gap="1.7vh",
        padding="1.7vh",
        height="56.6vh",
        width="100%",
        bg="#1C1B1C",
        border="0.1vh solid #2C2C2C"
    ),
def age_card(big_text = "45", text="Male", subtext = "99% confident"):
    return rx.vstack(
        rx.center(
            rx.text(
                big_text,
                font_size="27.9vh",
                font_weight="bolder",
            ),
            height="26.9vh",
            width="100%",
        ),
        rx.vstack(
            rx.text(
                text,
                font_size="10.4vh",
                letter_spacing="-0.5vh",
                font_weight="bold",
                line_height="10.4vh"
            ),
            rx.text(
                subtext,
                font_size="3.5vh",
                color="#D0D0D0",
                line_height="4.9vh"
            ),
            spacing="0",
            gap="0.9vh"
        ),
        spacing="0",
        gap="1.7vh",
        padding="1.7vh",
        height="56.6vh",
        width="100%",
        bg="#1C1B1C",
        border="0.1vh solid #2C2C2C"
    ),