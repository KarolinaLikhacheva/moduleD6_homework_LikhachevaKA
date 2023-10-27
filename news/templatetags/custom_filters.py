from django import template

register = template.Library()

# Здесь определяем список нежелательных слов, которые нужно цензурировать
stop_words = [
    'война',
    'войне'
]

@register.filter(name='censor')
def censor(value):
    for w in stop_words:
        value = value.replace(w, '***')
    return value

