from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import connection_lojanitaPizza as lojanita
#"""url='https://github.com/jahurtadod/sematic-app-demo'"""
#MENU PRINCIPAL
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Informacion', callback_data='mi')],
                [InlineKeyboardButton(
                    'Solicitar una pizza', callback_data='m1')],
                [InlineKeyboardButton(
                    'Tipos de Carnes', callback_data='m6')],
                [InlineKeyboardButton(
                    'Tipos de Embutidos', callback_data='m7')],
                [InlineKeyboardButton(
                    'Tipos de Especias', callback_data='m8')],
                [InlineKeyboardButton(
                    'Tipos de Frutas', callback_data='m9')],
                [InlineKeyboardButton(
                    'Tipos de Quesos', callback_data='ma')],
                [InlineKeyboardButton(
                    'Tipos de Salsas', callback_data='me')],
                [InlineKeyboardButton(
                    'Tipos de Vegetales', callback_data='mo')],
                [InlineKeyboardButton('Crear una pizza', callback_data='m2')]]
    return InlineKeyboardMarkup(keyboard)


def main_informacion_keyboard():
    keyboard = [[InlineKeyboardButton('Menu Principal', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

#FIRTS MENU
def first_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Menu Principal', callback_data='main')]]

    qres = lojanita.get_response_pizzas()

    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        keyboard.insert(0, [InlineKeyboardButton(
            name, callback_data='m3')])

    return InlineKeyboardMarkup(keyboard)

def first_submenu_keyboard():
    keyboard = [[InlineKeyboardButton('Si, proceder a pagar',
                                      url='https://github.com/JimmyPortilla/ChatBot-OWLPizzas')],
                [InlineKeyboardButton('No, Menu Principal', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

#SECOND MENU
def second_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Personal', callback_data='m4')],
                [InlineKeyboardButton('Mediana', callback_data='m4')],
                [InlineKeyboardButton('Grande', callback_data='m4')],
                [InlineKeyboardButton('Menu Principal', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def second_submenu_keyboard():
    keyboard = [[InlineKeyboardButton('De acuerdo', callback_data='m5')],
                [InlineKeyboardButton('Menu Principal', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

#THIRD MECU
def third_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Menu Principal', callback_data='main')]]

    qres = lojanita.get_response_carnes()

    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        keyboard.insert(0, [InlineKeyboardButton(
            name, callback_data='m3')])
    return InlineKeyboardMarkup(keyboard)

#FOURTH MENU

def fourth_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Menu Principal', callback_data='main')]]

    qres = lojanita.get_response_embutidos()

    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        keyboard.insert(0, [InlineKeyboardButton(
            name, callback_data='m3')])
    return InlineKeyboardMarkup(keyboard)


#FIFTH MENU

def fifth_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Menu Principal', callback_data='main')]]

    qres = lojanita.get_response_especias()

    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        keyboard.insert(0, [InlineKeyboardButton(
            name, callback_data='m3')])
    return InlineKeyboardMarkup(keyboard)


#SIXTH MENU

def sixth_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Menu Principal', callback_data='main')]]

    qres = lojanita.get_response_frutas()

    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        keyboard.insert(0, [InlineKeyboardButton(
            name, callback_data='m3')])
    return InlineKeyboardMarkup(keyboard)


#SEVENTH MENU

def seventh_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Menu Principal', callback_data='main')]]

    qres = lojanita.get_response_quesos()

    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        keyboard.insert(0, [InlineKeyboardButton(
            name, callback_data='m3')])
    return InlineKeyboardMarkup(keyboard)


#EIGHTH MENU

def eighth_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Menu Principal', callback_data='main')]]

    qres = lojanita.get_response_salsas()

    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        keyboard.insert(0, [InlineKeyboardButton(
            name, callback_data='m3')])
    return InlineKeyboardMarkup(keyboard)


#NINETH MENU

def nineth_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Menu Principal', callback_data='main')]]

    qres = lojanita.get_response_vegetales()

    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        keyboard.insert(0, [InlineKeyboardButton(
            name, callback_data='m3')])
    return InlineKeyboardMarkup(keyboard)
