import reflex as rx


def card(image = "/male_white.png", text="Male", subtext = "99% confident"):
    return rx.vstack(
        rx.image(
            src=image,
            height="247px",
            width="100%",
            object_fit="contain",  
        ),
        rx.vstack(
            rx.text(
                text,
                font_size="96px",
                letter_spacing="-5px",
                font_weight="bold",
                line_height="96px"
            ),
            rx.text(
                subtext,
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
def age_card(big_text = "45", text="Male", subtext = "99% confident"):
    return rx.vstack(
        rx.center(
            rx.text(
                big_text,
                font_size="256px",
                font_weight="bolder",
            ),
            height="247px",
            width="100%",
        ),
        rx.vstack(
            rx.text(
                text,
                font_size="96px",
                letter_spacing="-5px",
                font_weight="bold",
                line_height="96px"
            ),
            rx.text(
                subtext,
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