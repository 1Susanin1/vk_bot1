import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import time
import postgreDB


class VkinderBot():

    def __init__(self, token, pg_link) -> None:
        self.vk = vk_api.VkApi(token=token)
        self.longpoll = VkLongPoll(self.vk)
        self.DB = postgreDB.PostgreDB(pg_link)
        self.keyboard = VkKeyboard(inline=True)

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    request = event.text
                    self.keyboard.add_button("Начать поиск", color=VkKeyboardColor.POSITIVE)
                    self.keyboard.add_button("Настроить параметры")
                    user_position = self.DB.get_user_position(event.user_id)
                    if user_position == 0:
                        self.write_msg(event.user_id, "Добро пожаловать в Vkinder")
                    if request == "привет":
                        self.write_msg(event.user_id, "Хай")
                    elif request == "пока":
                        self.write_msg(event.user_id, "Пока((")
                    else:
                        self.write_msg(event.user_id, "Не поняла вашего ответа...")

    def write_msg(self, user_id, message):
        self.vk.method('messages.send', {'user_id': user_id, 
                                         'message': message,
                                         'keyboard': self.keyboard.get_keyboard(), 
                                         'random_id': time.time()})