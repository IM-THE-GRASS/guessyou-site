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
    def get_nation_info(self, input):
        response = requests.get(f"https://api.nationalize.io/?name={input}")
        data = response.json()
        print(data)
        id = data["country"][0]["country_id"]
        info = requests.get(f"https://restcountries.com/v3.1/alpha/{id}").json()
        name = info[0]["name"]["common"]
        probability = data["country"][0]["probability"] * 100
        return name, probability, id
    def get_age_info(self, input):
        response = requests.get(f"https://api.agify.io/?name={input}")
        data = response.json()
        age = data["age"]
        return age
    def get_gender_info(self, input):
        response = requests.get(f"https://api.genderize.io/?name={input}")
        data = response.json()
        gender = data["gender"]
        probability = data["probability"] * 100
        return gender, probability
    def on_change_input(self, new):
        self.current_input = new
    def load_result(self):
        if not self.current_input:
            return rx.redirect("/")
        
        nation_name, nation_probability, nation_id = self.get_nation_info(self.current_input)
        
        self.nation_text = nation_name
        self.nation_subtext = f"{round(nation_probability)}% Probability"
        self.nation_flag = f"https://flagcdn.com/w320/{nation_id.lower()}.png"
        
        age = self.get_age_info(self.current_input)
        self.age_text = age
        
        gender, gender_probability = self.get_gender_info(self.current_input)
        self.gender_text = gender.title()
        self.gender_subtext = f"{round(gender_probability)}% Probability"
        if gender == "male":
            self.gender_img = "/male_white.png"
        else:
            self.gender_img = "/female_white.png"