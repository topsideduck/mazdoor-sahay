from typing import Any, Text, Dict, List

import json
import requests
import ssl
from urllib.request import urlopen

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response: Text = "Hello World!"

        dispatcher.utter_message(text=response)

        return []


class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response: Text = "Hey! How are you?"

        dispatcher.utter_message(text=response)

        return []


class ActionCheerUp(Action):
    def name(self) -> Text:
        return "action_cheer_up"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response: Text = "Here is something to cheer you up:"
        image: str = "https://i.imgur.com/nGF1K8f.jpg"

        dispatcher.utter_message(text=response, image=image)

        return []


class ActionDidThatHelp(Action):
    def name(self) -> Text:
        return "action_did_that_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response: Text = "Did that help you?"

        dispatcher.utter_message(text=response)

        return []


class ActionHappy(Action):
    def name(self) -> Text:
        return "action_happy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response: Text = "Great, carry on!"

        dispatcher.utter_message(text=response)

        return []


class ActionBye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response: Text = "Good bye!"

        dispatcher.utter_message(text=response)

        return []


class ActionIAmABot(Action):
    def name(self) -> Text:
        return "action_i_am_a_bot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response: Text = "I am a bot, made by Harikeshav."

        dispatcher.utter_message(text=response)

        return []


class ActionHelp(Action):
    def name(self) -> Text:
        return "action_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response: Text = "Welcome to Mazdoor Sahay! I will be guiding you on how to use this website."

        dispatcher.utter_message(text=response)

        return []


class ActionAbout(Action):
    def name(self) -> Text:
        return "action_about"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response: Text = """
About Mazdoor Sahay:
-> It is a customised, user-friendly and accessible website.
-> Deriving its inspiration from the 10th Sustainable development goal: Reduced inequalities, Mazdoor- Sahay strives to establish a platform through which migrant labourers get adequate job opportunities and safely voice out their concerns and distresses- knowing that they will be heard.
-> It will help form a connection between migrant laborers and contractors so as to reduce the time of unemployment and increase productivity. 
-> It gives an opportunity for the community involving charitable organisations, NGO heads, philanthropists, concerned and public-spirited citizens to play an active role in helping out the migrants in times of need.   
"""
        image: str = "https://cdn.discordapp.com/attachments/925686709490946059/929004933091557426/LOGO-1.png"
        dispatcher.utter_message(text=response, image=image)

        return []


class ActionGetJob(Action):
    def name(self) -> Text:
        return "action_get_job"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = next(tracker.get_latest_entity_values("location"), None)

        url = "https://serversustainathon.leomessi0311.repl.co/GetJobs"
        result = requests.post(url)

        data = result.json()
        print(data)
        dispatcher.utter_message(text=data)

        return []
