import os
import csv
from transitions.extensions import GraphMachine
from linebot import LineBotApi
from linebot.models import MessageEvent, TextMessage, MessageTemplateAction, TextSendMessage, PostbackAction,URIAction, MessageAction, TemplateSendMessage, ButtonsTemplate
from utils import send_text_message

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

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

    def is_going_to_state9(self, event):
        text = event.message.text
        return text == '會員'

    def is_going_to_state10(self, event):
        text = event.message.text
        return text == '註冊會員'

    def is_going_to_state11(self, event):
        text = event.message.text
        return text == '登入會員'

    def is_going_to_state12(self, event):
        cmd = event.message.text.split(" ")
        return cmd[0] == '查詢'

    def is_going_to_state13(self, event):
        cmd = event.message.text.split(" ")
        return cmd[0] == '申辦'

    def is_going_to_state14(self, event):
        cmd = event.message.text.split(" ")
        return cmd[0] == '旅遊趣'

    def is_going_to_state15(self, event):
        cmd = event.message.text.split(" ")
        return cmd[0] == '吃透透'

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
        send_text_message(reply_token, "請輸入想去的地區或景點關鍵字我們將為您推薦遊客評價最好的前3個景點，使用以下形式\n旅遊趣 關鍵字\nex:旅遊趣 遊樂園")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入想去的餐廳地區及類型我們將為您推薦遊客評價最好的3間餐廳，使用以下形式\n吃透透 地區 類別\nex:吃透透 台中市 日式料理")
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
        send_text_message(reply_token, "今天您想怎麼度過您的假期呢?\n想尋找美食 請打美食\n想尋找觀光景點 請打旅遊\n實在是難以抉擇嗎?不如讓我們來幫你決定\n做一個簡單的小問卷，讓我們告訴您什麼樣的假期適合您 請打協助\n處理會員服務 請打會員\n現在加入會員就送 星巴克買一送一禮卷一張\n心動不如馬上行動")
        self.go_back()

    def on_exit_state8(self):
        print("Leaving state8")

    def on_enter_state9(self, event):
        print("I'm entering state9")

        line_bot_api = LineBotApi(channel_access_token)
        reply_token = event.reply_token

        line_bot_api.reply_message(event.reply_token, TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(title='會員服務', text='如果您尚未申辦會員請選擇註冊會員，如果您已經是會員想看會員資訊請選擇登入會員',
                                     actions=[MessageTemplateAction(label='註冊會員', text='註冊會員'),
                                              MessageTemplateAction(label='登入會員', text='登入會員')])))
        self.go_back()

    def on_exit_state9(self):
        print("Leaving state9")

    def on_enter_state10(self, event):
        print("I'm entering state10")

        reply_token = event.reply_token
        send_text_message(reply_token, "現在開始註冊會員，請用以下的形式輸入會員資訊\n申辦 您的姓名 您的聯絡方式 您想設的密碼\nex:申辦 王小明 0987987987 5487987")
        self.go_back()

    def on_exit_state10(self):
        print("Leaving state10")

    def on_enter_state11(self, event):
        print("I'm entering state11")

        reply_token = event.reply_token
        send_text_message(reply_token, "請用以下的形式輸入會員密碼\n查詢 您的密碼\nex:查詢 5487987")
        self.go_back()

    def on_exit_state11(self):
        print("Leaving state11")

    def on_enter_state12(self, event):
        print("I'm entering state12")
        reply_token = event.reply_token
        cmd = event.message.text.split(" ")
        with open('member.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)

            for row in rows:
                if row[2] == cmd[1]:
                    s = "會員姓名:"+row[0]+" 會員手機:"+row[1]+" 還有"+row[3]+"張優惠券未使用喔"
                    send_text_message(reply_token, s)

        self.go_back()

    def on_exit_state12(self):
        print("Leaving state12")

    def on_enter_state13(self, event):
        print("I'm entering state13")
        reply_token = event.reply_token
        cmd = event.message.text.split(" ")
        with open('member.csv', 'a+') as csvfile:
            writer = csv.writer(csvfile)
            d = []
            d.append(cmd[1])
            d.append(cmd[2])
            d.append(cmd[3])
            d.append(1)
            writer.writerow(d)

        send_text_message(reply_token, "申辦成功")
        self.go_back()

    def on_exit_state13(self):
        print("Leaving state13")

    def on_enter_state14(self, event):
        print("I'm entering state14")
        reply_token = event.reply_token
        cmd = event.message.text.split(" ")
        send_text_message(reply_token, "很抱歉這項服務還在開發中")

        self.go_back()

    def on_exit_state14(self):
        print("Leaving state14")

    def on_enter_state15(self, event):
        print("I'm entering state15")
        reply_token = event.reply_token
        cmd = event.message.text.split(" ")
        send_text_message(reply_token, "很抱歉這項服務還在開發中")
        self.go_back()

    def on_exit_state15(self):
        print("Leaving state15")
