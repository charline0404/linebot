from transitions.extensions import GraphMachine

from utils import send_text_message


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

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "比起景緻優美的風景畫 您更喜歡細緻的人像畫嗎? 請答是或否")
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