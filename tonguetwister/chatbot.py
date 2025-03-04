import re
import spacy

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

        self.keyword_responses = {
            'rejestracja': "Aby się zarejestrować, kliknij przycisk 'Logowanie'. Zarejestruj się już teraz, aby korzystać z pełni funkcji naszej aplikacji!",
            'kontakt': "Aby się z nami skontaktować, kliknij przycisk 'Kontakt'. Czekamy na Twoje pytania z otwartymi ramionami.",
            'nagrać': "Kliknij przycisk 'Nagraj swój głos', aby rozpocząć nagrywanie. Twoje nagrania są dla Ciebie ważne, aby poprawić swoje umiejętności.",
            'nagranie': "Kliknij przycisk 'Nagraj swój głos', aby rozpocząć nagrywanie. Twoje nagrania są dla Ciebie ważne, aby poprawić swoje umiejętności.",
            'mikrofon': "Proszę zezwolić swojemu urządzeniu na używanie mikrofonu. Bez tego nie będziesz w stanie usłyszeć swoich wspaniałych prób!",
            'użytkownik': "Korzystaj z przycisku 'Logowanie', aby przejść do swojego konta. Twoje przygody z wymową zaczynają się tutaj!",
            'hasło': "Wpisz swoje hasło podczas logowania, aby uzyskać dostęp do wszystkich funkcji aplikacji.",
            'konto': "Kliknij przycisk 'Zarejestruj się', aby założyć nowe konto i zacząć swoją podróż z LingwoŁamkami.",
            'powrót': "Kliknij przycisk 'Wróć', aby powrócić do poprzedniego ekranu. Przemieszczaj się w aplikacji jak ryba w wodzie!",
            'lingwołamki': "Lingwołamki to aplikacja, która pomoże Ci poprawić wymowę i nabrać pewności siebie.",
            'powtórki': "Dodawaj swoje ulubione ćwiczenia do powtórek, aby zawsze mieć je pod ręką. Ćwicz do perfekcji!",
            'drukować': "Możesz wydrukować swoje ulubione ćwiczenia, klikając odpowiedni przycisk. Idealne do nauki offline!",
            'zacząć': "Przesuń palce, aby rozpocząć. Każde kliknięcie przybliża Cię do lepszej wymowy!",
            'problem': "Masz problem? Zapytaj naszego czata – jesteśmy tutaj, aby pomóc Ci na każdym kroku.",
            'problemu': "Masz problem? Zapytaj naszego czata – jesteśmy tutaj, aby pomóc Ci na każdym kroku.",
            'artykulacyjne': "Lingwołamki to zestaw ćwiczeń artykulacyjnych, głosowych i oddechowych, które możesz wykonać samodzielnie, aby poprawić swoją wymowę.",
            'głosowe': "Lingwołamki to zestaw ćwiczeń artykulacyjnych, głosowych i oddechowych, które możesz wykonać samodzielnie, aby poprawić swoją wymowę.",
            'oddechowe': "Lingwołamki to zestaw ćwiczeń artykulacyjnych, głosowych i oddechowych, które możesz wykonać samodzielnie, aby poprawić swoją wymowę.",
            'lusterko': "Kliknij przycisk 'Otwórz Lusterko', aby sprawdzić swoje ruchy w lustrze podczas ćwiczeń. Bądź swoim własnym trenerem!",
            'zemsta': "Zemsta logopedy to łamańce językowe, które znajdziesz w aplikacji Lingwołamki. Czy jesteś gotów na wyzwanie?",
            'logopeda': "Zemsta logopedy to łamańce językowe, które znajdziesz w aplikacji Lingwołamki. Czy jesteś gotów na wyzwanie?",
            'awatar': "Kliknij przycisk 'Zarządzaj Awatarem', aby dostosować swoje zdjęcie profilowe. Pokaż światu, kim jesteś!",
            'zdjęcie': "Kliknij przycisk 'Zarządzaj Awatarem', aby dostosować swoje zdjęcie profilowe. Pokaż światu, kim jesteś!",
            'kurs': "Lingwołamki oferują specjalistyczne kursy wymowy, które pomogą Ci w opanowaniu trudnych aspektów mowy.",
            'sesja': "Planowanie sesji ćwiczeniowych pomoże Ci w regularnej praktyce i osiągnięciu zamierzonych celów.",
            'pomoc': "Jeśli potrzebujesz pomocy, odwiedź sekcję 'Kontakt' lub skontaktuj się z nami bezpośrednio.",
            'artykulator': "Zarządzaj artykulatorami i dostosuj je do swoich potrzeb.",
            'ćwiczenie': "Odkrywaj i zarządzaj ćwiczeniami oraz personalizuj swoje treningi.",
            'łamaniec': "Zarządzaj łamańcami językowymi i sprawdzaj swoje umiejętności.",
            'porada': "Przeglądaj i zarządzaj poradami językowymi.",
            'ciekawostka': "Odkrywaj i zarządzaj ciekawostkami językowymi.",
            'staropolszczyzna': "Odkrywaj słowa ze staropolszczyzny."
        }

        self.negative_words = {'okropne', 'straszne', 'tragiczne', 'złe', 'smutne', 'przykre', 'beznadziejne',
                               'denerwujące', 'nudne', 'uciążliwe', 'stresujące', 'nieprzyjemne', 'irytujące',
                               'fatalne', 'przerażające', 'problematyczne', 'nieakceptowalne', 'męczące',
                               'niezadowalające', 'odpychające', 'zawstydzające', 'frustrujące', 'niszczące',
                               'potworne', 'kiepskie', 'bezwartościowe', 'nieszczęśliwe', 'depresyjne', 'żenujące',
                               'katastrofalne', 'zdradliwe', 'niedopuszczalne', 'niewygodne', 'bolesne',
                               'krępujące', 'żałosne', 'rozczarowujące', 'nieudane', 'zniechęcające', 'rozpaczliwe',
                               'wrogie', 'nieprzystępne', 'niszczycielskie', 'przytłaczające', 'zdołowane',
                               'toksyczne', 'żałobne', 'bezsilne', 'tłamszące', 'odrażające'}

        self.positive_words = {'wspaniałe', 'niesamowite', 'świetne', 'fantastyczne', 'pozytywne', 'doskonałe',
                               'radosne', 'inspirujące', 'przyjemne', 'relaksujące', 'imponujące', 'satysfakcjonujące',
                               'wyjątkowe', 'cudowne', 'piękne', 'zachwycające', 'fenomenalne', 'wartościowe',
                               'podnoszące na duchu', 'motywujące', 'porywające', 'rewelacyjne', 'ekscytujące',
                               'owocne', 'energetyzujące', 'szczęśliwe', 'optymistyczne', 'fascynujące', 'budujące',
                               'genialne', 'urocze', 'radosne', 'promienne', 'pomyślne', 'zdumiewające', 'odprężające',
                               'hojne', 'zabawne', 'pewne', 'wyborne', 'magiczne', 'natchnione', 'radosne',
                               'dobroczynne', 'życzliwe', 'spektakularne', 'harmonijne', 'kojące', 'twórcze',
                               'szlachetne', 'dobre'}

        self.negative_pattern = re.compile(r'\b(' + '|'.join(self.negative_words) + r')\b', re.IGNORECASE)
        self.positive_pattern = re.compile(r'\b(' + '|'.join(self.positive_words) + r')\b', re.IGNORECASE)

    def lemmatize_input(self, text):
        """
        Lemmatizes user text to simplify keyword searching.
        """
        doc = self.nlp(text.lower())
        return " ".join([token.lemma_ for token in doc])

    def get_custom_sentiment(self, user_input):
        """
        Analyzes the sentiment of a user's messages by checking both full forms
        and approximate matches of lemmatized words.
        """
        user_input = user_input.lower()
        doc = self.nlp(user_input)

        words = set(user_input.split())
        lemmas = {token.lemma_ for token in doc}

        def match_sentiment(word_set, sentiment_list):
            for word in word_set:
                for sentiment_word in sentiment_list:
                    if word.startswith(sentiment_word[:4]):
                        return True
            return False

        if match_sentiment(words | lemmas, self.negative_words):
            return -1
        if match_sentiment(words | lemmas, self.positive_words):
            return 1

        return 0

    def get_response(self, user_input):
        """
        Processes user input and returns an appropriate chatbot response.
        """
        user_input = user_input.lower()
        doc = self.nlp(user_input)

        words = set(user_input.split())
        lemmas = {token.lemma_ for token in doc}

        # Custom sentiment analysis
        custom_sentiment = self.get_custom_sentiment(user_input)
        if custom_sentiment == -1:
            return "Przykro mi, że masz negatywne odczucia. Może mogę jakoś pomóc?"
        elif custom_sentiment == 1:
            return "Cieszę się, że masz pozytywne nastawienie! Jak mogę Ci jeszcze pomóc?"

        # Keyword matching (original)
        for keyword, response in self.keyword_responses.items():
            if keyword in words:
                return response

        # Keyword matching (lemma)
        for keyword, response in self.keyword_responses.items():
            for lemma in lemmas:
                if keyword in lemmas or lemma.startswith(keyword[:4]):
                    return response

        return "Dziękuję za wiadomość. Jak mogę pomóc?"
