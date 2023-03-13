import telebot
import time
from summaries import summaries
from quiz_tale_of_Ajib import quiz_tale_of_ajib
from ajib_questions import ajib_questions
from quiz_tale_of_the_porter import quiz_tale_of_the_porter
from tale_of_the_porter_questions import tale_of_the_porter_questions
from Quiz_garden import quiz_garden
from garden_questions import garden_questions
import counters
from bot_commands import bot_commands
from syllabus import syllabus_questions
from syllabus_pictures import syllabus_pictures
API_KEY = "5163766250:AAFLX2d1oB2ddyRx_ihb5TrGoO_vnVuFMBY"
bot = telebot.TeleBot(API_KEY)

commands_list = ["start", "instructions"]


@bot.message_handler(commands=[command for command in commands_list])
def instructions(message):
    bot.send_message(message.chat.id, bot_commands[message.text[1:]])

@bot.message_handler(commands=["syllabus"])
def instructions(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    SyllabusKeybordButtons = ["Syllabus", "Course description",
                              "Grading policy", "Deadline policy",
                              "Make-up policy", "Weekly Reading Journals",
                              "Final Project"]
    for button in SyllabusKeybordButtons:
        keyboard.add(telebot.types.InlineKeyboardButton(text=button, callback_data=button))
    time.sleep(1.5)
    bot.send_message(message.chat.id, "These are the most frequently asked questions.", reply_markup=keyboard)

@bot.message_handler(commands=["quizes"])
def instructions(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    SyllabusKeybordButtons = ["The Arabian Nights. The Porter and The Three Ladies",
                              "The Arabian Nights. The Tale of the Third Dervish",
                              "Garden of the Forking Paths by Jorge Luis Borges"]
    for button in SyllabusKeybordButtons:
        keyboard.add(telebot.types.InlineKeyboardButton(text=button, callback_data=button))
    bot.send_message(message.chat.id, "Choose knowledge of which text you want to test first!", reply_markup=keyboard)

@bot.message_handler(commands=["summaries"])
def instructions(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    SyllabusKeybordButtons = ["Summary of The Arabian Nights. The Porter and The Three Ladies",
                              "Summary of The Arabian Nights. The Tale of the Third Dervish",
                              "Summary of Garden of the Forking Paths by Jorge Luis Borges"]
    for button in SyllabusKeybordButtons:
        keyboard.add(telebot.types.InlineKeyboardButton(text=button, callback_data=button))
    bot.send_message(message.chat.id, "Select a text!", reply_markup=keyboard)

# syllabus replies
def Quiz_1_question(message, quiz_tale_of_ajib, quiz_counter_text_1):
    if quiz_counter_text_1 == 10:
        time.sleep(1.5)
        bot.send_message(message.chat.id, "The quiz is finished")
        time.sleep(1.5)
        ans = "You scored " + str(counters.quiz_1_score) + " points out of 9"
        bot.send_message(message.chat.id, ans)
        time.sleep(1.5)
        if(counters.quiz_1_score > 4):
            bot.send_message(message.chat.id, "Great job!")
        else:
            bot.send_message(message.chat.id, "Well, you wasn't that bad. But probably you would like to revise the text")
        counters.counter1 = 1
        counters.quiz_1_score = 0
        return

    keyboard = telebot.types.ReplyKeyboardMarkup()
    variants = "Question" + str(quiz_counter_text_1)
    SyllabusKeybordButtons = [variant for variant in quiz_tale_of_ajib[variants]]
    for button in SyllabusKeybordButtons:
        keyboard.add(telebot.types.InlineKeyboardButton(text=button, callback_data=button))
    time.sleep(1.5)
    bot.send_message(message.chat.id, ajib_questions[quiz_counter_text_1 - 1], reply_markup=keyboard)
    #Quiz1(message.text, message, quiz_counter_text_1)

def Quiz1(text, message, quiz_counter_text_1):
    time.sleep(1.5)
    if quiz_counter_text_1 == 1:
        time.sleep(1.5)
        bot.send_message(message.chat.id, "That is a quiz to test your knowledge of The Arabian Nights. The Tale of the Third Dervish. "
                                          "For each question there are 4 options. Only one of them is correct. "
                                          "The quiz should start about know. Break a leg!")
        time.sleep(1.5)
        Quiz_1_question(message, quiz_tale_of_ajib, quiz_counter_text_1)

def Quiz_2_question(message, quiz_garden, quiz_counter_text_2):
    if quiz_counter_text_2 == 10:
        time.sleep(1.5)
        bot.send_message(message.chat.id, "The quiz is finished")
        time.sleep(1.5)
        ans = "You scored " + str(counters.quiz_1_score) + " points out of 9"
        bot.send_message(message.chat.id, ans)
        time.sleep(1.5)
        if(counters.quiz_1_score > 4):
            bot.send_message(message.chat.id, "Great job!")
        else:
            bot.send_message(message.chat.id, "Well, you wasn't that bad. But probably you would like to revise the text")
        counters.counter1 = 1
        counters.quiz_1_score = 0
        return

    keyboard = telebot.types.ReplyKeyboardMarkup()
    variants = "Question" + str(quiz_counter_text_2)
    SyllabusKeybordButtons = [variant for variant in quiz_garden[variants]]
    for button in SyllabusKeybordButtons:
        keyboard.add(telebot.types.InlineKeyboardButton(text=button, callback_data=button))
    time.sleep(1.5)
    bot.send_message(message.chat.id, garden_questions[quiz_counter_text_2 - 1], reply_markup=keyboard)

def Quiz2(text, message, quiz_counter_text_2):
    time.sleep(1.5)
    if quiz_counter_text_2 == 1:
        time.sleep(1.5)
        bot.send_message(message.chat.id, "That is a quiz to test your knowledge of Garden of the Forking Paths by Jorge Luis Borges. "
                                          "For each question there are 4 options. Only one of them is correct. "
                                          "The quiz should start about know. Break a leg!")
        time.sleep(1.5)
        Quiz_2_question(message, quiz_garden, quiz_counter_text_2)

def Quiz_3_question(message, quiz_garden, quiz_counter_text_2):
    if quiz_counter_text_2 == 11:
        time.sleep(1.5)
        bot.send_message(message.chat.id, "The quiz is finished")
        time.sleep(1.5)
        ans = "You scored " + str(counters.quiz_1_score) + " points out of 10"
        bot.send_message(message.chat.id, ans)
        time.sleep(1.5)
        if(counters.quiz_1_score > 5):
            bot.send_message(message.chat.id, "Great job!")
        else:
            bot.send_message(message.chat.id, "Well, you wasn't that bad. But probably you would like to revise the text")
        counters.counter1 = 1
        counters.quiz_1_score = 0
        return

    keyboard = telebot.types.ReplyKeyboardMarkup()
    variants = "Question" + str(quiz_counter_text_2)
    SyllabusKeybordButtons = [variant for variant in quiz_tale_of_the_porter[variants]]
    for button in SyllabusKeybordButtons:
        keyboard.add(telebot.types.InlineKeyboardButton(text=button, callback_data=button))
    time.sleep(1.5)
    bot.send_message(message.chat.id, tale_of_the_porter_questions[quiz_counter_text_2 - 1], reply_markup=keyboard)

def Quiz3(text, message, quiz_counter_text_2):
    time.sleep(1.5)
    if quiz_counter_text_2 == 1:
        time.sleep(1.5)
        bot.send_message(message.chat.id, "That is a quiz to test your knowledge of The Arabian Nights. The Porter and The Three Ladies. "
                                          "For each question there are 4 options. Only one of them is correct. "
                                          "The quiz should start about know. Break a leg!")
        time.sleep(3)
        Quiz_3_question(message, quiz_tale_of_the_porter, quiz_counter_text_2)


def quiz_mode(message, quiz_options, function, lets_move):
    for question in quiz_options.values():
        for answer in question.keys():
            if message.text == answer:
                deletekeybord = telebot.types.ReplyKeyboardRemove()
                if question[message.text] == True:
                    counters.quiz_1_score += 1
                    time.sleep(1.5)
                    bot.send_message(message.chat.id, "That is correct", reply_markup=deletekeybord)
                else:
                    for answer_value in question.values():
                        if answer_value == True:
                            ans = "That is incorrect. The actual answer is '" + \
                                  list(question.keys())[list(question.values()).index(True)] + "'"
                            time.sleep(1.5)
                            bot.send_message(message.chat.id, ans, reply_markup=deletekeybord)
                counters.counter1 += 1
                time.sleep(1.5)
                if counters.counter1 != lets_move:
                    bot.send_message(message.chat.id, "Let's move to the next question")
                function(message, quiz_options, counters.counter1 )

@bot.message_handler(content_types=['text'])
def send_text(message):
    ########################################################################
    if message.text in syllabus_pictures.keys():
        photo = open(syllabus_pictures[message.text], "rb")
        time.sleep(1.5)
        #bot.send_photo(message.chat.id, photo)

    if message.text in syllabus_questions.keys():
        time.sleep(1.5)
        bot.send_message(message.chat.id, syllabus_questions[message.text])
    #########################################################################
    if message.text in summaries.keys():
        time.sleep(1.5)
        #bot.send_photo()
        #time.sleep(1)
        bot.send_message(message.chat.id, summaries[message.text])
    #########################################################################
    if message.text == "The Arabian Nights. The Porter and The Three Ladies":
        time.sleep(1.5)
        photo = open('photos/arab_nights_the_porter.png', 'rb')
        #bot.send_photo(message.chat.id, photo)
        deletekeybord = telebot.types.ReplyKeyboardRemove()
        time.sleep(1.5)
        bot.send_message(message.chat.id, "You chose The Arabian Nights. The Porter and The Three Ladies",
                         reply_markup=deletekeybord)
        Quiz3(message.text, message, counters.counter1)

    if message.text == "The Arabian Nights. The Tale of the Third Dervish":
        time.sleep(1.5)
        photo = open('photos/arab_nights_the_third_dervish.png', 'rb')
        #bot.send_photo(message.chat.id, photo)
        deletekeybord = telebot.types.ReplyKeyboardRemove()
        time.sleep(1.5)
        bot.send_message(message.chat.id, "You chose The Arabian Nights. The Tale of the Third Dervish",
                         reply_markup=deletekeybord)
        Quiz1(message.text, message, counters.counter1)
    if message.text == "Garden of the Forking Paths by Jorge Luis Borges":
        time.sleep(1.5)
        photo = open('photos/garden_of_forking_paths.png', 'rb')
        #bot.send_photo(message.chat.id, photo)
        deletekeybord = telebot.types.ReplyKeyboardRemove()
        time.sleep(1.5)
        bot.send_message(message.chat.id,
                         "You chose Garden of the Forking Paths by Jorge Luis Borges",
                         reply_markup=deletekeybord)
        Quiz2(message.text, message, counters.counter1)

    quiz_mode(message, quiz_tale_of_ajib, Quiz_1_question, 10)
    quiz_mode(message,quiz_garden ,Quiz_2_question, 10)
    quiz_mode(message, quiz_tale_of_the_porter, Quiz_3_question, 11)
    #########################################################################
bot.polling()