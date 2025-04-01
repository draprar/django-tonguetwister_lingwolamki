import pickle
import random
import re
import spacy
import requests
import wikipedia


class Chatbot:
    """
    A chatbot class that processes user input, checks for sentiment,
    and responds based on predefined keywords or sentiment.
    """

    def __init__(self):
        """
        Initialize the chatbot with predefined keywords and sentiment words.
        """
        self.nlp = spacy.load("pl_core_news_sm")

        self.keyword_responses = self.load_data("tonguetwister/data/keywords.pkl")
        self.negative_words = self.load_data("tonguetwister/data/negative_words.pkl")
        self.positive_words = self.load_data("tonguetwister/data/positive_words.pkl")
        self.unanswered_questions = set()
        self.negative_pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, self.negative_words)) + r')\b',
                                           re.IGNORECASE)
        self.positive_pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, self.positive_words)) + r')\b',
                                           re.IGNORECASE)

    @staticmethod
    def load_data(filepath):
        """Loads data from a pickle file."""
        try:
            with open(filepath, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error loading file {filepath}: {e}")
            return {} if 'keywords' in filepath else set()

    def save_unanswered_questions(self, filepath="tonguetwister/data/unanswered.pkl", flush_threshold=5):
        """Saves unanswered questions to a pickle file only when threshold is met."""
        if len(self.unanswered_questions) % flush_threshold == 0:
            with open(filepath, "wb") as f:
                pickle.dump(self.unanswered_questions, f)

    def lemmatize_input(self, text):
        """
        Lemmatizes user text using SpaCy to simplify keyword searching.
        """
        doc = self.nlp(text.lower())
        return " ".join([token.lemma_ for token in doc])

    def get_custom_sentiment(self, user_input):
        """
        Analyzes the sentiment of a user's messages by checking both full forms
        and approximate matches of lemmatized words.
        """
        user_input = user_input.lower()
        words = set(user_input.split())
        lemmas = set(self.lemmatize_input(user_input).split())

        def match_sentiment(word_set, sentiment_list):
            return any(word.startswith(sentiment_word[:4]) for word in word_set for sentiment_word in sentiment_list)

        if match_sentiment(words | lemmas, self.negative_words):
            return -1
        if match_sentiment(words | lemmas, self.positive_words):
            return 1

        return 0

    @staticmethod
    def query_wikipedia(query):
        """
        Queries Wikipedia for a short summary of the given query.
        """
        wikipedia.set_lang("pl")
        try:
            return wikipedia.summary(query, sentences=1, auto_suggest=True)
        except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError):
            return "Nie znalazłem dokładnej informacji na ten temat. Możesz spróbować inaczej sformułować pytanie?"
        except (requests.Timeout, requests.RequestException):
            return "Nie udało się uzyskać informacji. Spróbuj ponownie za chwilę."

    def get_response(self, user_input):
        """
        Processes user input and returns an appropriate chatbot response.
        """
        user_input = user_input.lower()
        words = set(user_input.split())
        lemmas = set(self.lemmatize_input(user_input).split())

        # Greetings
        greetings = ["cześć", "hej", "siema", "witaj", "dzień dobry"]
        if user_input in greetings:
            return random.choice(["Cześć! Jak mogę pomóc?", "Hej! Co dla Ciebie?", "Witaj! Jak się masz?"])

        # Keyword matching (original)
        for keyword, responses in self.keyword_responses.items():
            if keyword in words:
                return random.choice(responses) if isinstance(responses, list) else responses

        # Keyword matching (lemma)
        for keyword, responses in self.keyword_responses.items():
            if keyword in lemmas or any(lemma.startswith(keyword[:4]) for lemma in lemmas):
                return random.choice(responses) if isinstance(responses, list) else responses

        # Custom sentiment analysis
        custom_sentiment = self.get_custom_sentiment(user_input)
        if custom_sentiment == -1:
            return "Przykro mi, że masz negatywne odczucia. Może mogę jakoś pomóc?"
        elif custom_sentiment == 1:
            return "Cieszę się, że masz pozytywne nastawienie! Jak mogę Ci jeszcze pomóc?"

        # Check for Wikipedia requests
        wiki_phrases = ["powiedz mi o", "informacje o", "co to jest", "kim jest", "czym jest", "co oznacza",
                        "co wiadomo o"]

        for phrase in wiki_phrases:
            if user_input.startswith(phrase):
                topic = user_input.replace(phrase, "").strip()
                if topic:
                    return self.query_wikipedia(topic)

        # Store unanswered questions for later review
        self.unanswered_questions.add(user_input)
        self.save_unanswered_questions()

        return "Dziękuję za wiadomość. Jak mogę pomóc?"
