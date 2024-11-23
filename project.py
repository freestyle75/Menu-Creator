def create_menu(menu_items, restaurant_name, greeting, currency, file_name):
    greetings = {
        'english': 'Welcome',
        'turkish': 'Hoşgeldiniz',
        'italian': 'Benvenuto',
        'french': 'Accueillir',
        'spanish': 'bienvenido',
    }

    currencies = {
        'dollar': '$',
        'euro': '€',
        'tl': '₺'
    }

    with open(file_name, 'w') as file:
        title_length = 50
        chosen_greeting = greetings.get(greeting.lower(), 'Welcome')
        currency_symbol = currencies.get(currency.lower(), '$')  # Default to dollar if invalid currency
        title = f"{'*' * 30} {chosen_greeting} to {restaurant_name} {'*' * (title_length - len(restaurant_name) - len(chosen_greeting) - 9)}\n"
        file.write(title)
        file.write(f"{'Currency:'.ljust(25)} => {currency_symbol.rjust(10)}\n\n")

        categories = {}
        for dish_name, (category, price) in menu_items.items():
            if category not in categories:
                categories[category] = []
            categories[category].append((dish_name, price))

        for category, dishes in categories.items():
            file.write(f"\n{'-' * 15} {category.capitalize()} {'-' * 15}\n")
            for dish_name, price in dishes:
                file.write(f"{dish_name.ljust(25)} => {currency_symbol}{price.rjust(10)}\n")

def select_greeting_language():
    valid_languages = ['english', 'turkish', 'italian', 'french', 'spanish']

    while True:
        greeting_choice = input("Enter the greeting language (e.g., english, turkish, italian): ").lower()
        if greeting_choice in valid_languages:
            return greeting_choice
        elif greeting_choice == 'stop':
            print("Invalid Language. Program stopped.")
            return None
        else:
            print("Invalid Language. Please try again.")

def select_currency():
    valid_currencies = ['dollar', 'euro', 'tl']

    while True:
        currency_choice = input("Enter the currency (e.g., dollar, euro, tl): ").lower()
        if currency_choice in valid_currencies:
            return currency_choice
        elif currency_choice == 'stop':
            print("Invalid Currency. Program stopped.")
            return None
        else:
            print("Invalid Currency. Please try again.")

def main():
    print("Welcome to the Menu Creator!")
    menu_items = {}

    while True:
        dish_name = input("Enter dish name (or 'stop' to finish): ")
        if dish_name.lower() == 'stop':
            break

        price = input("Enter price: ")
        category = input("Enter category (e.g., starters, drinks, dessert): ")
        menu_items[dish_name] = (category, price)

    restaurant_name = input("Enter your restaurant name: ")
    greeting_choice = select_greeting_language()

    if greeting_choice is None:
        return

    currency_choice = select_currency()

    if currency_choice is None:
        return

    file_name = input("Enter your menu file name (e.g., restaurant_menu.txt): ")
    create_menu(menu_items, restaurant_name, greeting_choice, currency_choice, file_name)
    print(f"Menu created successfully for '{restaurant_name}' in '{file_name}'!")

if __name__ == "__main__":
    main()

