favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

for langeuage in set(favorite_languages.values()):
    print(langeuage)

for lang2 in set(favorite_languages.items()):
    print(lang2)

for lang3 in list(favorite_languages.items()):
    print(lang3)