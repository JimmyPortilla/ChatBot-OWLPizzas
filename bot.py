from os import name
from telegram.ext import *
import logging
import connection_dbpedia as dbpedia
import connection_lojanitaPizza as lojanita
#import demo_spacy as analysis
import Constants as keys
import menu
import responses

# Set up the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

# Message error
def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')

# MENUS
def menu_command(update, context):
    update.message.reply_text("Bienvenido a LojanitaPizza en que te puedo ayudar?",
                              reply_markup=menu.main_menu_keyboard())


def main_menu(update, context):
    query = update.callback_query
    query.edit_message_text(text="Bienvenido a LojanitaPizza en que te puedo ayudar?",
                            reply_markup=menu.main_menu_keyboard())



#MENU INFORMACION
def main_informacion(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="LojanitaPizza es una pizeria que te ofrece todo a tu gusto en cuanto a pizzas, estamos ubicados en las calles 24 de mayo y Rocafuerte.\nHorarios\nDe lunes a sabado desde las 10am hasta que dure la alegria",
        reply_markup=menu.main_informacion_keyboard())


#FIRST MENU
def first_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿Qué de pizza deseas?",
        reply_markup=menu.first_menu_keyboard())


def first_submenu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿Está seguro que desea ordenar esta pizza?",
        reply_markup=menu.first_submenu_keyboard())

#SECOND MENU
def second_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="De que tamaño la quieres?",
        reply_markup=menu.second_menu_keyboard())


def second_submenu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="Aún estamos trabajando en esta función",
        reply_markup=menu.second_submenu_keyboard())


def second_submenu_1(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="Listo te avisare cuando esté listo")


#THIRD MENU
def third_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿Tipos de Carne?",
        reply_markup=menu.third_menu_keyboard())


#FOURTH MENU
def fourth_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿Tipos de embutidos?",
        reply_markup=menu.fourth_menu_keyboard())


#FIFTH MENU
def fifth_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿Tipos de especias?",
        reply_markup=menu.fifth_menu_keyboard())

#SIXTH MENU
def sixth_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿Tipos de frutas?",
        reply_markup=menu.sixth_menu_keyboard())

#SEVENTH MENU

def seventh_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿Tipos de quesos?",
        reply_markup=menu.seventh_menu_keyboard())

#EIGHTH MENU

def eighth_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿Tipos de salsas?",
        reply_markup=menu.eighth_menu_keyboard())

#NINETH MENU
def nineth_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿Tipos de vegetales?",
        reply_markup=menu.nineth_menu_keyboard())

# COMMANDS


def help_command(update, context):
    update.message.reply_text(
        "LojanitaPizza permite realizar pedidos, revisar y crear pizzas a tu gusto!"
        "\n\nPara interartuar utliza el comando /start")
       

def ingredients_command(update, context):
    user_says = " ".join(context.args)
    # update.message.reply_text("You said: " + user_says)
    update.message.reply_text(
        "Los ingredientes de  " + user_says + " son:\n\n"+dbpedia.get_response_dbpedia_ingredients(user_says.capitalize()))


def pizza_command(update, context):
    update.message.reply_text(
        "Puedes encontrar información de las siguientes pizzas :"
        "\n\nPizza de carne"
        "\nPizzas vegetarianas"
        "\nPizzas con fruta"
       
    )

#Menu de comandos
def start_command(update, context):
    update.message.reply_text(
        'Bienvenido a LojanitaPizza en que te podemos ayudar')
    update.message.reply_text(
        "Puedes usar los siguientes comandos :\n"
        "\n/formenu -> realiza tu pedido mediante un menu (recomendado)"
        #"\n/help -> muestra mas información "
        "\n/listPizzaDb -> muestra el listado de pizzas de DBpedia"
        "\n/listPizza -> muestra el listado de pizzas de LojanitaPizza"
        "\n/pizza -> muestra las pizzas que puedes buscar"
        "\n/listaCarnes -> muestra el tipo de carnes para tus pizzas "
        "\n/listaEmbutidos -> muestra los tipos de embutidos para tus pizzas ")
       #"\n/ingredients \"nombre de la pizza\" -> permite buscar los ingredientes de la pizza (utiliza el commando /pizza para ver que pizzas puedes buscar)")

#Pizzas desde DBPEDIA
def types_command_dbpedia(update, context):
    qres = dbpedia.get_response_dbpedia_pizzas()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name, comment, image_url = result['name']['value'], result['comment']['value'], result['image']['value']
        update.message.reply_text('Nombre de la pizza : ' + name +
                                  "\n\nDescripción : " + comment + "\n" + image_url)

#Lista de Pizzas
def types_command_listaPizza(update, context):
    qres = lojanita.get_response_pizzas()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text('Pizza ' + name)

#Listas de Carnes
def types_command_carnes(update, context):
    qres = lojanita.get_response_carnes()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text('Pizza de ' + name)


#Listas de EMBUTIDOS
def types_command_embutidos(update, context):
    qres = lojanita.get_response_embutidos()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text( name)


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    listNoun = []
    listVerb = []
    # response = responses.get_response(text)
    # update.message.reply_text(response)
    # update.message.reply_text("te amo")
    doc = analysis.spacy_info(text)
    for w in doc:
        update.message.reply_text(
            w.text + " es un " + w.pos_ + " lemma: " + w.lemma_)
        if w.pos_ == "NOUN":
            print("NOUN " + w.text)
            listNoun.append(w.text)
        if w.pos_ == "VERB":
            print("VERB " + w.text)
            listVerb.insert(0, w.lemma_)

    response = responses.get_response(listVerb[0])
    if (response):
        update.message.reply_text("Tu intención es pedir :")
        for list in listNoun:
            if list == "pizza":
                update.message.reply_text(
                    " -  \""+list+"\" :\n"+dbpedia.get_response_dbpedia(list.capitalize()))
            else:
                temp = "pizzas que contiende " + list + " :\n"
                qres = dbpedia.get_response_dbpedia_food(list)
                for i in range(len(qres['results']['bindings'])):
                    result = qres['results']['bindings'][i]
                    label = result['label']['value']
                    temp += "\n - " + label

                update.message.reply_text(temp)

    else:
        text = "No entendí lo que escribiste\n\nUsaste las siguientes intenciones :\n"
        for w in listVerb:
            temp = " - " + w + "\n"
            text += temp
        text += "\n(Utiliza una sola acción para entender tu mensaje)"
        update.message.reply_text(text)

    # if len(listVerb) == 1:
    #     print(listVerb[0])
    #     response = responses.get_response(listVerb[0])
    #     update.message.reply_text("Tu intención \""+listVerb[0]+"\" ")

    #     update.message.reply_text(
    #         "Encontrado información entorno a tu mensaje")
    #     for list in listNoun:
    #         update.message.reply_text(
    #             "Información sobre \""+list+"\" :\n\n"+dbpedia.get_response_dbpedia(list.capitalize()))


if __name__ == '__main__':
    updater = Updater(token=keys.API_KEY, use_context=True)

    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('formenu', menu_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('listPizzaDb', types_command_dbpedia))
    dp.add_handler(CommandHandler('listaCarnes',types_command_carnes))
    dp.add_handler(CommandHandler('listaEmbutidos',types_command_embutidos))
    dp.add_handler(CommandHandler('listPizza', types_command_listaPizza))
    dp.add_handler(CommandHandler('pizza', pizza_command))
    dp.add_handler(CommandHandler(
        'ingredients', ingredients_command, pass_args=True))

    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(main_informacion, pattern='mi'))
    dp.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(third_menu, pattern='m6'))
    dp.add_handler(CallbackQueryHandler(fourth_menu, pattern='m7'))
    dp.add_handler(CallbackQueryHandler(fifth_menu, pattern='m8'))
    dp.add_handler(CallbackQueryHandler(sixth_menu, pattern='m9'))
    dp.add_handler(CallbackQueryHandler(seventh_menu, pattern='ma'))
    dp.add_handler(CallbackQueryHandler(eighth_menu, pattern='me'))
    dp.add_handler(CallbackQueryHandler(nineth_menu, pattern='mo'))

    dp.add_handler(CallbackQueryHandler(first_submenu, pattern='m3'))

    dp.add_handler(CallbackQueryHandler(second_submenu, pattern='m4'))
    dp.add_handler(CallbackQueryHandler(second_submenu_1, pattern='m5'))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
