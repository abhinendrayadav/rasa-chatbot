# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# adding the lookup table for all the intents in one place
# question:
#          - how will we identify the entities [using this way](lookup table using different file)


# from typing import Any, Text, Dict, List
# import requests

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#   def name(self) -> Text:
#       return "action_official_dress_code"

#   def run(self, dispatcher: CollectingDispatcher,
#           tracker: Tracker,
#           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#       dispatcher.utter_message("")

#       return []
