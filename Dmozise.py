"""
- text annotation: identifying the list of entities and non-entities mentioned in the provided text
- text categorization: identification of up to 5 categories that describe the topic of the given text.
    The list of available categories come from DMOZ open directory. Currently, only English text can be categorized!
"""

from eventregistry import *
from eventregistry.Base import *
from eventregistry.ReturnInfo import *

class Analytics:
    def __init__(self, eventRegistry):
        """
        @param eventRegistry: instance of EventRegistry class
        """
        self._er = eventRegistry


    def annotate(self, text, lang = None):
        """
        identify the list of entities and nonentities mentioned in the text
        @param text: input text to annotate
        @param lang: language of the provided document (can be an ISO2 or ISO3 code). If None is provided, the language will be automatically detected
        """
        return self._er.jsonRequestAnalytics("/api/v1/annotate", { "lang": lang, "text": text })


    def categorize(self, text):
        """
        determine the set of up to 5 categories the text is about. Currently, only English text can be categorized!
        @param text: input text to categorize
        """
        return self._er.jsonRequestAnalytics("/api/v1/categorize", { "text": text })


er = EventRegistry(apiKey = "2b02894d-06b8-47be-a5a5-e88c9711444f")
ana = Analytics(er)
print(ana.categorize("BJP will win the elections"))