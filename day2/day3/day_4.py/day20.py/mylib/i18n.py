config = 'rabotaet kak modul'
languages = {
    'ru' : {
        'go': 'идти',
        'think': 'Думать',
        'friend': 'Друг',
        'we': 'Мы',
        'edit': 'Изменить',
        'view': 'просмотр',
        'run': 'Бегать',
        'room': 'комната',
        'i': 'я',
        'number': 'число',
        'it': 'оно',
        'she': 'Она',
        'he': 'Он',
    },
    'en' : {
        'идти': 'Go'
    },
    'kg' : {
        'go': 'басуу',
        'think': 'Ойлонуу',
        'friend': 'Друг',
        'we': 'Биз',
        'edit': 'Озгортуу',
        'view': 'Коруу',
        'run': 'Чуркоо',
        'room': 'Болмо',
        'i': 'Мен',
        'number': 'Сан',
        'it': 'бул',
        'she': 'Аял',
        'he': 'Эркек',
    }
}
    
def to_translate(word,language):
    word_to_lower = word.lower()
    if language in languages:
        if word in languages[language]:
            print(word, 'NA', language, 'yazyke', languages[language][word_to_lower])


def to_translate_many(*args,**kwargs):
    for a in args:
        to_translate(a,kwargs['lang'])


# def to_translate(word,language):
#     word_to_lower = word.lower()
#     if language == 'kg' :
#         print(kg[word_to_lower])
#     elif language == 'ru':
#         print(ru[word_to_lower])
#     elif language == 'en':
#         print(en[word_to_lower])


# def to_translate_many(*args, **kwargs):
#     args_to_lower = args.lower()
#     if kwargs == languags:
#         if word in languags[kwargs]:
#             print(args, 'NA', kwargs, 'yazyke', languags[kwargs][args_to_lower])
#     print(args,kwargs)











