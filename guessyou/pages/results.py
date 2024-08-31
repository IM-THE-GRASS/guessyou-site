import reflex as rx
from guessyou.components.card import card, age_card  
from guessyou.state import State
from reflex_lottiefiles import LottieFiles

@rx.page(on_load=State.load_result)
def results() -> rx.Component:
    return rx.box(
        rx.cond(
            State.loading,
            rx.center(
                rx.vstack(
                    rx.center(
                        rx.heading("Loading, please wait"),
                        width="90vw",
                    ),
                    LottieFiles(
                        src="https://lottie.host/5ff06a80-3f45-4dd3-8737-f4cf62ba3d48/X5hdVEjbNK.lottie",
                        autoplay=True,
                        loop=True,
                        width="90vw",
                        height=["40vh", "40vh", "40vh"],
                    ),
                    heght="100vh",
                    wdth="100vw"
                ),
                
                width="90vw",
                height="80vh"
                
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Hi, ",
                        font_weight="bold",
                        line_height="15vh",
                        font_size=["15vh", "10vh"]
                    ),
                    rx.text(
                        State.current_input,
                        font_weight="bold",
                        line_height="15vh",
                        font_size=["15vh", "10vh"]
                        
                    ),
                    rx.text(
                        " 👋",
                        font_weight="bold",
                        line_height="15vh",
                        font_size=["15vh", "10vh"]
                        
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
                rx.tablet_and_desktop(
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
                        padding="5vh",
                        margin_bottom="5vh"
                    ),  
                    
                    
                ),
                rx.mobile_only(
                    rx.vstack(
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
                    
                    
                ),
                position="absolute",
                left="3vw",
                top="5vh",
                spacing="0",
                gap="1vh"
            )
            
            
            
        ),
        
        on_mount=State.loading_true
    )
