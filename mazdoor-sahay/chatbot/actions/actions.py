from typing import Any, Text, Dict, List

import json
import re
import requests

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


class ActionAbout(Action):
    def name(self) -> Text:
        return "action_about"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response: Text = """
About Mazdoor-Sahay:
-> Mazdoor-Sahay is a platform that has been created with the intention to bolster connections and provide adequate job opportunities to migrant labourers and create a secure platform where they can safely voice out their concerns and distresses- knowing that they will be heard.
-> Mazdoor-Sahay is a customised, user-friendly and accessible website.
-> Mazdoor-Sahay also provides an opportunity for the community consisting of charitable organisations, NGO heads, philanthropists, concerned and public-spirited citizens who wish to play an active role in helping out the migrants in times of need.
-> The creators of Mazdoor-Sahay strive to achieve the aims and ideals set forth to do their bit in the aid of India.
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

        url = "https://serversustainathon.leomessi0311.repl.co/GetJobsAll"
        jobs = requests.get(url).json()

        required_job = []

        for job in jobs:
            if location in re.split("\s|(?<!\d)[,.](?!\d)", json.loads(job[2])['location']):
                required_job = job
            else:
                required_job = None

        if required_job is not None:
            required_job_params = {
                'name': required_job[0],
                'description': required_job[1],
                'location': json.loads(required_job[2])['location'],
                'job_days': required_job[3],
                'job_pay': required_job[4],
                'job_id': required_job[5],
                'contractor_name': required_job[6],
                'contractor_user_id': required_job[7]
            }

        else:
            required_job_params = None

        if required_job_params is not None:
            response = f"""
Job found!

Name: {required_job_params['name']}
Description: {required_job_params['description']}
Location: {required_job_params['location']}
Job days: {required_job_params['job_days']} days
Job pay: INR {required_job_params['job_pay']}
Contractor name: {required_job_params['contractor_name']}
Contractor profile: https://sustainathon.leomessi0311.repl.co/Profile?id={required_job_params['contractor_user_id']}
Job post: https://sustainathon.leomessi0311.repl.co/ViewJob?id={required_job_params['job_id']}
            """
        else:
            response = f"Could not find a job in {location}!"

        dispatcher.utter_message(text=response)

        return []
