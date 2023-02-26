from enum import Enum


class Section(Enum):
    SOUP = 'Суп'
    BAKING = 'Випічка'
    PASTA = 'Пасти'
    SALAD = 'Салати'


category_mapper = {
    "diyetichni-stravi": "Дієтичні",
    "pisnij-stil": "Пісні",
    "stravi-v-multivarczi": "У мультиварці",
    "stravi-dlya-ditej": "Для дітей",
    "pasta": "Паста",
    "solodki-stravi-ta-deserti": "Десерт",
    "vipichka": "Випічка",
    "koktejli-ta-napoyi": "Напої",
    "varennya": "Варення",
    "m-yasni-stravi": "Мясо",
    "rybne": "Риба",
    "garniri": "Гарнір",
    "ovochevi-stravi-uk": "Овочі",
    "holodni-zakuski": "Закуски",
    "garyachi-zakuski": "Закуски",
    "snidanki": "Сніданки",
    "sendvichi-ta-buterbrodi": "Сніданки",
    "salati": "Салати",
    "zakuski": "Закуски",
    "supi": "Супи",
    'borscht': "Супи",
    "drugi-stravi": "Другі страви",
}





