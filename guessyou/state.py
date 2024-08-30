import reflex as rx
import requests

class State(rx.State):
    current_input:str
    
    nation_flag:str
    nation_text:str
    nation_subtext:str
    
    gender_img:str
    gender_text:str
    gender_subtext:str
    
    age_img:str
    age_text:str
    age_subtext:str
    
    
    def on_change_input(self, new):
        self.current_input = new
    def load_result(self):
        nation = requests.get(f"https://api.nationalize.io/?name={self.current_input}")
        nation_data = nation.json()
        nation_id = nation_data["country"][0]["country_id"]
        nation_info = requests.get(f"https://restcountries.com/v3.1/alpha/{nation_id}").json()
        nation_name = nation_info[0]["name"]["common"]
        self.nation_text = nation_name
        self.nation_subtext = nation_data["country"][0]["probability"] * 100
        self.nation_subtext = f"{round(self.nation_subtext)}% sure"
        