import datetime as dt
from kivy.app import App
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class ManaDailySpend(App):

    def initialize(self):
        self.store = JsonStore('mana_daily_spend.json')
        # will be button:
        if not self.store.exists('budget'):
            self.make_budget()
        self.update_surplus()

    @staticmethod
    def str_int(value):
        try:
            return str(int(value))
        except ValueError as e:
            return str(int(float(value)))
        except Exception as e:
            return value

    def update_surplus(self):
        last_updated = self.get_saved(key='updated', name='amount')
        last_updated = dt.datetime.strptime(last_updated, '%Y-%m-%d')
        days = (dt.datetime.now() - last_updated).days
        surplus = float(self.get_saved(key='surplus', name='amount'))
        surplus += days * float(self.get_saved(key='budget', name='amount'))
        self.update_saved(key='surplus', name='amount', value=ManaDailySpend.str_int(surplus))
        self.update_saved(
            key='updated',
            name='amount',
            value=dt.datetime.now().strftime('%Y-%m-%d'))

    def build(self):
        self.initialize()
        layout = BoxLayout(padding=10, orientation="vertical")
        high_layout = BoxLayout(padding=10, orientation="horizontal")
        low_layout = BoxLayout(padding=10, orientation="horizontal")
        high_left_layout = BoxLayout(padding=10, orientation="vertical")
        high_right_layout = BoxLayout(padding=10, orientation="vertical")
        low_left_layout = BoxLayout(padding=10, orientation="vertical")
        low_right_layout = BoxLayout(padding=10, orientation="vertical")

        surplus_label = Label(
            text='surplus',
            font_size=24,
            size_hint=(.2, .2),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.surplus_amount = Label(
            text=ManaDailySpend.str_int(self.get_saved(key='surplus', name='amount')),
            font_size=55,
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.surplus_input = TextInput(
            multiline=False,
            readonly=False,
            input_filter='int',
            halign="right",
            size_hint=(.5, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            font_size=24,)
        surplus_button = Button(
            text="Change",
            size_hint=(.5, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            background_color=[0,1,1,1])
        surplus_button.bind(on_press=self.on_press_surplus)
        self.surplus_input.bind(on_text_validate=self.on_press_surplus)

        budget_name = Label(
            text='Daily Limit',
            font_size=24,
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.budget_label = Label(
            text=ManaDailySpend.str_int(self.get_saved(key='budget', name='amount')),
            font_size=24,
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.budget_input = TextInput(
            multiline=False,
            readonly=False,
            input_filter='int',
            halign="right",
            font_size=55,)
        budget_button = Button(
            text="Change",
            background_color=[0,1,1,1])
        budget_button.bind(on_press=self.on_press_budget)
        self.budget_input.bind(on_text_validate=self.on_press_budget)

        spent_name = Label(
            text='Spent Amount',
            font_size=24,
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.spent_label = Label(
            text=ManaDailySpend.str_int(self.get_saved(key='spent', name='amount')),
            font_size=24,
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        self.spent_input = TextInput(
            text=ManaDailySpend.str_int(self.budget_label.text),
            multiline=False,
            readonly=False,
            input_filter='int',
            halign="right",
            font_size=55,)
        spent_button = Button(
            text="Add Transaction",
            background_color=[0,1,1,1])
        spent_button.bind(on_press=self.on_press_spent)
        self.spent_input.bind(on_text_validate=self.on_press_spent)

        buttup = Button(text='↑ Increase', font_size=32, background_color=[1,0,1,1])
        buttdn = Button(text='↓ Decrease', font_size=32, background_color=[1,1,0,1])
        buttup.bind(on_press=self.button_up)
        buttdn.bind(on_press=self.button_dn)

        low_left_layout.add_widget(budget_name)
        low_left_layout.add_widget(self.budget_label)
        low_left_layout.add_widget(self.budget_input)
        low_left_layout.add_widget(budget_button)

        low_right_layout.add_widget(buttup)
        low_right_layout.add_widget(buttdn)

        high_right_layout.add_widget(spent_name)
        high_right_layout.add_widget(self.spent_label)
        high_right_layout.add_widget(self.spent_input)
        high_right_layout.add_widget(spent_button)

        high_left_layout.add_widget(surplus_label)
        high_left_layout.add_widget(self.surplus_amount)
        high_left_layout.add_widget(self.surplus_input)
        high_left_layout.add_widget(surplus_button)

        high_layout.add_widget(high_left_layout)
        high_layout.add_widget(high_right_layout)
        low_layout.add_widget(low_left_layout)
        low_layout.add_widget(low_right_layout)

        layout.add_widget(high_layout)
        layout.add_widget(low_layout)
        return layout

    def button_up(self, instance):
        self.spent_input.text = str(int(self.spent_input.text) + 10)

    def button_dn(self, instance):
        self.spent_input.text = str(int(self.spent_input.text) - 10)

    def on_press_surplus(self, instance):
        try:
            self.surplus_amount.text = ManaDailySpend.str_int(self.surplus_input.text)
            self.update_saved(
                key='surplus',
                name='amount',
                value=int(self.surplus_input.text))
        except:
            pass
        self.surplus_input.text = ''

    def on_press_budget(self, instance):
        try:
            self.budget_label.text = ManaDailySpend.str_int(self.budget_input.text)
            self.update_saved(
                key='budget',
                name='amount',
                value=int(self.budget_input.text))
        except:
            pass
        self.budget_input.text = ''

    def on_press_spent(self, instance):
        try:
            last_spent = float(self.spent_input.text)
            surplus = self.get_saved(key='surplus', name='amount')
            surplus = str(float(surplus or 0) - last_spent)
            self.surplus_amount.text = ManaDailySpend.str_int(surplus)
            self.spent_label.text = ManaDailySpend.str_int(self.spent_input.text)
            self.update_saved(
                key='surplus',
                name='amount',
                value=surplus)
            self.update_saved(
                key='spent',
                name='amount',
                value=last_spent)
        except:
            pass
        self.spent_input.text = ''

    def make_budget(self):
        self.store.put('spent', amount=0)
        self.store.put('budget', amount=20)
        self.store.put('surplus', amount=0)
        self.store.put('updated',
            amount=dt.datetime.now().strftime('%Y-%m-%d'))

    def get_saved(self, key: str, name: str):
        if self.store.exists(key):
            return str(self.store.get(key)[name])
        return 'unknown'

    def update_saved(self, key: str, name: str, value: int):
        self.store.put(key, **{name: value})


if __name__ == '__main__':
    app = ManaDailySpend()
    app.run()
