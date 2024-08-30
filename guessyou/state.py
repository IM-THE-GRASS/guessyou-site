import reflex as rx


class State(rx.State):
    current_input:str
    def on_change_input(self, new):
        self.current_input = new
        