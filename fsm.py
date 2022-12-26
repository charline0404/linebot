import os
from transitions.extensions import GraphMachine
from linebot import LineBotApi
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage,ButtonsTemplate,MessageTemplateAction
from utils import send_text_message

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

n = 0

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text == "協助"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text == "旅遊"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text == "美食"

    def is_going_to_state4(self, event):
        text = event.message.text
        return text == "我94個社畜"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text == "還..好?一般般吧"

    def is_going_to_state6(self, event):
        text = event.message.text
        return text == '終於可以出來放風了9453'

    def is_going_to_state7(self, event):
        text = event.message.text
        return text == '很快就要回去蹲了'

    def is_going_to_state8(self, event):
        text = event.message.text
        return text == '不行! 再讓我想想'

    def on_enter_state1(self, event):
        print("I'm entering state1")
        line_bot_api = LineBotApi(channel_access_token)
        reply_token = event.reply_token

        line_bot_api.reply_message( event.reply_token,TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(title='問題一',text='覺得自己工時長嗎?',
            actions=[MessageTemplateAction(label='是',text='我94個社畜'),MessageTemplateAction(label='否',text='還..好?一般般吧')]
                )))

        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇想去的地區或景點關鍵字")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇想去的地區或景點關鍵字")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

    def on_enter_state4(self, event):
        print("I'm entering state4")

        line_bot_api = LineBotApi(channel_access_token)
        reply_token = event.reply_token

        line_bot_api.reply_message(event.reply_token, TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(title='問題二', text='本次假期長嗎?',
                                     actions=[MessageTemplateAction(label='是', text='終於可以出來放風了9453'),
                                              MessageTemplateAction(label='否', text='很快就要回去蹲了')])))

        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")

        line_bot_api = LineBotApi(channel_access_token)
        reply_token = event.reply_token

        line_bot_api.reply_message(event.reply_token, TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(title='找到答案了!!!', text='準備好看結果了嗎?',
                                     actions=[MessageTemplateAction(label='是', text='旅遊'),
                                              MessageTemplateAction(label='否', text='不行! 再讓我想想')])))

        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")

    def on_enter_state6(self, event):
        print("I'm entering state6")

        line_bot_api = LineBotApi(channel_access_token)
        reply_token = event.reply_token

        line_bot_api.reply_message(event.reply_token, TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(title='找到答案了!!!', text='準備好看結果了嗎?',
                                     actions=[MessageTemplateAction(label='是', text='旅遊'),
                                              MessageTemplateAction(label='否', text='不行! 再讓我想想')])))

        self.go_back()

    def on_exit_state6(self):
        print("Leaving state6")

    def on_enter_state7(self, event):
        print("I'm entering state7")

        line_bot_api = LineBotApi(channel_access_token)
        reply_token = event.reply_token

        line_bot_api.reply_message(event.reply_token, TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(title='找到答案了!!!', text='準備好看結果了嗎?',
                                     actions=[MessageTemplateAction(label='是', text='美食'),
                                              MessageTemplateAction(label='否', text='不行! 再讓我想想')])))

        self.go_back()

    def on_exit_state7(self):
        print("Leaving state7")

    def on_enter_state8(self, event):
        print("I'm entering state8")
        reply_token = event.reply_token
        send_text_message(reply_token, "今天您想怎麼度過您的假期呢?\n想尋找美食 請打美食\n想尋找觀光景點 請打旅遊\n實在是難以抉擇嗎?不如讓我們來幫你決定\n做一個簡單的小問卷，讓我們告訴您什麼樣的假期適合您 請打協助")
        self.go_back()

    def on_exit_state8(self):
        print("Leaving state8")
