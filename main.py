import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random

kivy.require('2.0.0')


class MemoryGame(App):
    def build(self):
        self.title = 'Memory Game'
        self.root = GridLayout(cols=4)
        self.cards = []
        self.card_values = []
        self.selected_cards = []
        self.moves = 0
        self.create_cards()
        self.create_board()
        self.create_quit_button()
        return self.root

    def create_cards(self):
        for i in range(8):
            self.card_values.append(i)
            self.card_values.append(i)

    def create_board(self):
        random.shuffle(self.card_values)
        for value in self.card_values:
            card = Button(text='', on_press=self.show_card)
            self.cards.append(card)
            self.root.add_widget(card)

    def create_quit_button(self):
        quit_button = Button(text='Quit Game', on_press=self.quit_game)
        self.root.add_widget(quit_button)

    def show_card(self, instance):
        self.moves += 1
        instance.text = str(self.card_values[self.cards.index(instance)])
        self.selected_cards.append(instance)
        if len(self.selected_cards) == 2:
            Clock.schedule_once(self.check_match, 1.5)

    def check_match(self, dt):
        card1 = self.selected_cards[0]
        card2 = self.selected_cards[1]
        if card1.text == card2.text:
            card1.disabled = True
            card2.disabled = True
        else:
            card1.text = ''
            card2.text = ''
        self.selected_cards = []

        if all(card.disabled for card in self.cards):
            self.show_win_message()

    def quit_game(self, instance):
        App.get_running_app().stop()

    def show_win_message(self):
        win_label = Label(text='Congratulations!\nYou won in {} moves.'.format(self.moves))
        self.root.add_widget(win_label)


if __name__ == '__main__':
    MemoryGame().run()
