import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import datetime as dt


class MainApp(App):

    def initialize(self):
        self.store = JsonStore('mana_daily_spend.json')
        # will be button:
        if not self.store.exists('budget'):
            self.make_budget()
        self.update_surplus()

    def update_surplus(self):
        last_updated = self.get_saved(key='updated', name='amount')
        last_updated = dt.datetime.strptime(last_updated, '%Y-%m-%d %H:%M')
        days = (dt.datetime.now() - last_updated).days
        surplus = float(self.get_saved(key='surplus', name='amount'))
        surplus += days * float(self.get_saved(key='budget', name='amount'))
        self.update_saved(key='surplus', name='amount', value=surplus)
        self.update_saved(
            key='updated',
            name='amount',
            value=dt.datetime.now().strftime('%Y-%m-%d %H:%M'))

    def build(self):
        self.initialize()
        layout = BoxLayout(padding=10, orientation="vertical")
        h_layout = BoxLayout(padding=10)
        left_layout = BoxLayout(padding=10, orientation="vertical")
        right_layout = BoxLayout(padding=10, orientation="vertical")

        surplus_label = Label(
            text='surplus',
            font_size=24,
            size_hint=(.2, .2),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.surplus_amount = Label(
            text=self.get_saved(key='surplus', name='amount'),
            font_size=55,
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.surplus_input = TextInput(
            multiline=False,
            readonly=False,
            halign="right",
            size_hint=(.2, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            font_size=24,)
        surplus_button = Button(
            text="Change",
            size_hint=(.2, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            background_color=[0,1,0,1])
        surplus_button.bind(on_press=self.on_press_surplus)

        budget_name = Label(
            text='Daily Limit',
            font_size=24,
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.budget_label = Label(
            text=self.get_saved(key='budget', name='amount'),
            font_size=24,
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.budget_input = TextInput(
            multiline=False,
            readonly=False,
            halign="right",
            font_size=55,)
        budget_button = Button(
            text="Change",
            background_color=[0,1,0,1])
        budget_button.bind(on_press=self.on_press_budget)

        spent_name = Label(
            text='Spent Amount',
            font_size=24,
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.spent_input = TextInput(
            multiline=False,
            readonly=False,
            halign="right",
            font_size=55,)
        spent_button = Button(
            text="Add Transaction",
            background_color=[0,1,0,1])
        spent_button.bind(on_press=self.on_press_spent)

        left_layout.add_widget(budget_name)
        left_layout.add_widget(self.budget_label)
        left_layout.add_widget(self.budget_input)
        left_layout.add_widget(budget_button)

        right_layout.add_widget(spent_name)
        right_layout.add_widget(self.spent_input)
        right_layout.add_widget(spent_button)

        h_layout.add_widget(left_layout)
        h_layout.add_widget(right_layout)
        layout.add_widget(surplus_label)
        layout.add_widget(self.surplus_amount)
        layout.add_widget(self.surplus_input)
        layout.add_widget(surplus_button)
        layout.add_widget(h_layout)
        return layout

    def on_press_surplus(self, instance):
        try:
            self.surplus_amount.text = int(self.surplus_input.text)
            self.update_saved(
                key='surplus',
                name='amount',
                value=int(self.surplus_input.text))
        except:
            pass
        self.surplus_input.text = ''

    def on_press_budget(self, instance):
        try:
            self.budget_label.text = int(self.budget_input.text)
            self.update_saved(
                key='budget',
                name='amount',
                value=int(self.budget_input.text))
        except:
            pass
        self.budget_input.text = ''
    def on_press_spent(self, instance):
        try:
            surplus = self.get_saved(key='surplus', name='amount')
            surplus = str(float(surplus or 0) - float(self.spent_input.text))
            self.surplus_amount.text = surplus
            self.update_saved(
                key='surplus',
                name='amount',
                value=surplus)
        except:
            pass
        self.spent_input.text = ''


    def make_budget(self):
        self.store.put('budget', amount=20)
        self.store.put('surplus', amount=0)
        self.store.put('updated',
            amount=dt.datetime.now().strftime('%Y-%m-%d %H:%M'))

    def get_saved(self, key: str, name: str):
        if self.store.exists(key):
            return str(self.store.get(key)[name])
        return 'unknown'

    def update_saved(self, key: str, name: str, value: int):
        self.store.put(key, **{name: value})


if __name__ == '__main__':
    app = MainApp()
    app.run()
