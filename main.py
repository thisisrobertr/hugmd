from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class VM(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.main = MainPage(self.screen_manager)
        screen = Screen(name='Main')
        screen.add_widget(self.main)
        self.screen_manager.add_widget(screen)

        self.chat = ChatPage(self.screen_manager)
        screen = Screen(name='Chat')
        screen.add_widget(self.chat)
        self.screen_manager.add_widget(screen)
        
        self.settings = SettingsPage(self.screen_manager)
        screen = Screen(name='Settings')
        screen.add_widget(self.settings)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    
class Menu(FloatLayout):
    def __init__(self, screen_manager):
        super().__init__()
        self.screen_manager = screen_manager
        self.dropdown = DropDown()

        for screen_name in ['Main', 'Chat', 'Settings']:
            btn = Button(text=f"{screen_name}", size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.switch_screen(btn.text.split()[-1]))
            self.dropdown.add_widget(btn)

        self.menu_button = Button(text="Menu", size_hint=(0.1, 0.1), pos_hint={"right": 1, "top": 1})
        self.menu_button.bind(on_release=self.dropdown.open)
        self.add_widget(self.menu_button)

    def switch_screen(self, screen_name):
        if(screen_name == 'Main'):
            self.screen_manager.transition = SlideTransition(direction='right')
            self.screen_manager.current = screen_name
            self.dropdown.dismiss()

        else:
            self.screen_manager.transition = SlideTransition(direction='left')
            self.screen_manager.current = screen_name
            self.dropdown.dismiss()
           
class MainPage(BoxLayout):
    def __init__(self, screen_manager): 
        super().__init__(orientation='vertical')
        self.screen_manager = screen_manager
        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # Set background color
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)
        self.add_widget(Menu(screen_manager), index=0)
        button = Button(text="Prompt 1", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        button.bind(on_press=self.go_to_chat)
        self.add_widget(button)

        button = Button(text="Prompt 2", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        button.bind(on_press=self.go_to_chat)
        self.add_widget(button)

        button = Button(text="Prompt 3", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        button.bind(on_press=self.go_to_chat)
        self.add_widget(button)

        button = Button(text="Chat", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        button.bind(on_press=self.go_to_chat)
        self.add_widget(button)

    def update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def go_to_chat(self, instance):
        self.screen_manager.transition = SlideTransition(direction='left')
        self.screen_manager.current = 'Chat'
        
class ChatPage(BoxLayout):
    def __init__(self, screen_manager): 
        super().__init__(orientation='vertical')
        self.screen_manager = screen_manager
        with self.canvas.before:
            Color(0.5, 0.9, 0.8, 1)  # Set background color
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)
        self.add_widget(Menu(screen_manager), index=0)
        button = Button(text="Main", size_hint=(0.1, 0.1))
        button.bind(on_press=self.go_to_main)
        self.add_widget(button)

        self.chat_display = BoxLayout(orientation='vertical', size_hint=(1, 0.8))
        self.add_widget(self.chat_display)

        self.input_area = BoxLayout(size_hint=(1, 0.2))
        self.input_field = TextInput(hint_text="Type your message here...", multiline=False)
        self.send_button = Button(text="Send")
        self.send_button.bind(on_press=self.send_message)
        self.input_area.add_widget(self.input_field)
        self.input_area.add_widget(self.send_button)
        self.add_widget(self.input_area)
        
    def update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def go_to_main(self, instance):
        self.screen_manager.transition = SlideTransition(direction='right')
        self.screen_manager.current = 'Main'

    def send_message(self, instance):
        message = self.input_field.text
        if message.strip():
            self.chat_display.add_widget(Label(text=message, size_hint_y=None, height=30))
            self.input_field.text = ""

class SettingsPage(BoxLayout):
    def __init__(self, screen_manager): 
        super().__init__(orientation='vertical')
        self.screen_manager = screen_manager
        with self.canvas.before:
            Color(0.5, 0.6, 0.8, 1)  # Set background color
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)
        self.add_widget(Menu(screen_manager), index=0)
        button = Button(text="Main", size_hint=(0.1, 0.1), pos_hint={"left": 1, "top": 1})
        button.bind(on_press=self.go_to_main)
        self.add_widget(button)
        
    def update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def go_to_main(self, instance):
        self.screen_manager.transition = SlideTransition(direction='right')
        self.screen_manager.current = 'Main'


myapp = VM()
myapp.run()
