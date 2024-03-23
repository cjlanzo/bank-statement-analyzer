categories = {
    'Bills': [
        'travelers',
        'fiber',
        'city of raleigh'
    ],
    'Subscriptions': [
        'max.com',
        'nytimes',
        'patreon',
        'netflix',
        'spotify'
    ],
    'Pets': [
        'cozycat'
    ],
    'Home': [

    ],
    'Auto': [
        'parking',
        'refuel',
        'sheetz'
    ],
    'Entertainment': [

    ],
    'Groceries': [
        'sodastream'
    ],
    'Food & Drinks': [
        'tacos',
        'pizza'
    ],
    'Personal Care': [
        'barber'
    ],
    'Misc': [
        
    ],
    'Hobbies': [
        'trc',
        'game theory',
        'mtgarena',
        'blizzard'
    ],
    'Trips': [
        'airbnb'
    ],
}

category_lookup = {}

for category, keywords in categories.items():
    for keyword in keywords:
        category_lookup[keyword] = category

def get_category_from_description(description):
    description = str.lower(description)

    for keyword, category in category_lookup.items():
        keyword = str.lower(keyword)

        if keyword in description:
            return category
        
    return 'UNKNOWN'

