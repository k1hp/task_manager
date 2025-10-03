from fastapi import APIRouter
import importlib
# from app.users.schemas import UserCreateSchema

class NamesConverter(str):
    IRREGULAR_PLURALS = {
        # Человек и животные
        'children': 'child',
        'men': 'man',
        'women': 'woman',
        'people': 'person',
        'persons': 'person',
        'feet': 'foot',
        'teeth': 'tooth',
        'mice': 'mouse',
        'geese': 'goose',
        'lice': 'louse',
        'oxen': 'ox',

        # Латинские и греческие заимствования
        'data': 'datum',
        'media': 'medium',
        'criteria': 'criterion',
        'phenomena': 'phenomenon',
        'analyses': 'analysis',
        'bases': 'basis',
        'crises': 'crisis',
        'hypotheses': 'hypothesis',
        'theses': 'thesis',
        'indices': 'index',
        'matrices': 'matrix',
        'vertices': 'vertex',
        'appendices': 'appendix',

        # Другие исключения
        'knives': 'knife',
        'leaves': 'leaf',
        'lives': 'life',
        'wives': 'wife',
        'halves': 'half',
        'shelves': 'shelf',
        'wolves': 'wolf',

        # Неизменяемые
        'sheep': 'sheep',
        'fish': 'fish',
        'deer': 'deer',
        'species': 'species',
        'aircraft': 'aircraft',
    }

    PLURAL_RULES = [
        # Особые случаи
        (('quizzes',), 'quiz'),
        (('buses',), 'bus'),
        (('fishes',), 'fish'),

        # Стандартные правила
        (('ises', 'yses'), 'is'),  # analyses -> analysis
        (('xes',), 'x'),  # boxes -> box
        (('ses',), 's'),  # buses -> bus
        (('ches',), 'ch'),  # churches -> church
        (('shes',), 'sh'),  # dishes -> dish
        (('zes',), 'z'),  # quizzes -> quiz
        (('men',), 'man'),  # women -> woman
        (('ves',), 'f'),  # leaves -> leaf
        (('ves',), 'fe'),  # knives -> knife
        (('ies',), 'y'),  # cities -> city
        (('oes',), 'o'),  # potatoes -> potato
        (('i',), 'us'),  # foci -> focus
        (('a',), 'um'),  # data -> datum
        (('s',), ''),  # cats -> cat
    ]

    def __new__(cls, plural_word: str):
        singular = cls.convert(plural_word).capitalize()
        instance = super().__new__(cls, singular)
        instance.original = plural_word
        return instance

    @classmethod
    def convert(cls, plural_word: str) -> str:
        """Статический метод для конвертации"""
        word = plural_word.lower().strip()

        # Проверяем неправильные формы
        if word in cls.IRREGULAR_PLURALS:
            return cls.IRREGULAR_PLURALS[word]

        # Применяем правила
        for plural_endings, singular_ending in cls.PLURAL_RULES:
            for ending in plural_endings:
                if word.endswith(ending):
                    base = word[:-len(ending)]
                    # Проверяем особые случаи
                    if ending == 'ves' and base.endswith('el'):
                        return base + 'f'  # shelves -> shelf
                    return base + singular_ending

        # Если слово уже в единственном числе или неизвестно
        return word

    def is_plural(self) -> bool:
        """Проверяет, было ли слово во множественном числе"""
        return self.original.lower() != self.lower()

    @classmethod
    def to_singular(cls, word: str) -> str:
        """Альтернативный статический метод"""
        return cls.convert(word)


def generate_routes(group_name: str) -> APIRouter:

    router = APIRouter(prefix=f"/{group_name}", tags=[group_name])
    singular = NamesConverter(group_name)
    schemas = importlib.import_module(f"app.{group_name}.schemas")
    create_schema = getattr(schemas, f"{singular}CreateSchema")
    @router.get("/")
    def get_many():
        return {}

    @router.get("/{user_id}")
    def get_one(user_id: int):
        return {}

    @router.post("/")
    def create(user: create_schema):
        return {}

    @router.put("/{user_id}")
    def update(user_id: int):
        return {}

    @router.patch("/{user_id}")
    def full_update(user_id: int):
        return {}

    @router.delete("/{user_id}")
    def delete(user_id: int):
        return {}



    return router


router = generate_routes("users")