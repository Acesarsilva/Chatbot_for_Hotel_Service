import random
import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def find_hotel():
  return random.choice([
    'Recife Hotel', 'Rede Andrade Onda Mar Hotel', 'Bugan Hotel Recife',
    'Transamerica Beach Class', 'Park Hotel', 'Recife Plaza Hotel',
    'Bianca Praia Hotel', 'Hotel Aconchego Recife', 'huntingdon marriott hotel'
  ])

def hotel_options():
  return [
    'Recife Hotel', 'Rede Andrade Onda Mar Hotel', 'Bugan Hotel Recife',
    'Transamerica Beach Class', 'Park Hotel', 'Recife Plaza Hotel',
    'Bianca Praia Hotel', 'Hotel Aconchego Recife'
  ]

def buildmessage(d):
    return json.dumps(d)

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_search_hotel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hotel_name = tracker.get_slot('hotel-name')
        print(hotel_name)
        if hotel_name is not None:
          options = hotel_options()
          if hotel_name in options:
            msg = buildmessage(hotel_name + ' ' + "is available")
          else:
            msg = buildmessage("I could not find this options, but there is a nice place called" + " " + find_hotel())
        else:
          msg = buildmessage("There is a nice place called" + " " + find_hotel())

        dispatcher.utter_message(text=msg)
        return []