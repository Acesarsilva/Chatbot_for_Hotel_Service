import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def buildmessage(d):
    return json.dumps(d)

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_search_hotel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots = domain['slots']
        print("searching HOTEEEEEEEEEEEL")
        print(slots)
        msg = buildmessage("um belo hotel qualuqer")
        dispatcher.utter_message(text=msg)
        return []