from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield.textfield import MDTextField
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.scrollview import ScrollView

class VM(MDApp):
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
    def __init__(self, screen_manager, color):
        super().__init__()
        self.screen_manager = screen_manager
        
        self.arrow_button = MDIconButton(
                    icon="arrow-left-circle",
                    pos_hint={"left": 1, "top": 1},
                    theme_text_color="Custom",
                    text_color= color,
                )
        self.arrow_button.bind(on_press=self.go_to_main)
        self.add_widget(self.arrow_button)

        self.menu_button = MDIconButton(icon="menu", theme_text_color="Custom", text_color=(1, 1, 1, 1), size_hint=(0.1, 0.1), pos_hint={"right": 1, "top": 1})
        self.menu_button.bind(on_release=self.open_menu)
        self.add_widget(self.menu_button) 

    def open_menu(self, instance):
        menu_items = [{
            "text": f"{screen_name}", "on_release": lambda btn=f"{screen_name}": self.switch_screen(btn.split()[-1])
            } for screen_name in ['Main', 'Chat', 'Settings']
        ]
        self.menu = MDDropdownMenu(
            caller=self.menu_button, items=menu_items
        )
        self.menu.open()

    def go_to_main(self, instance):
        self.screen_manager.transition = SlideTransition(direction='right')
        self.screen_manager.current = 'Main'

    def switch_screen(self, screen_name):
        if(screen_name == 'Main'):
            self.screen_manager.transition = SlideTransition(direction='right')
            self.screen_manager.current = screen_name
            self.menu.dismiss()
        else:
            self.screen_manager.transition = SlideTransition(direction='left')
            self.screen_manager.current = screen_name
            self.menu.dismiss()

class MainPage(BoxLayout):
    def __init__(self, screen_manager): 
        super().__init__(orientation='vertical')
        self.screen_manager = screen_manager
        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # Set background color
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)
        self.add_widget(Menu(screen_manager, (0.2, 0.6, 0.8, 1)), index=0)
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

        self.add_widget(Menu(screen_manager, (1, 1, 1, 1)), index=0)
        
        self.chat_display_scroll = ScrollView(size_hint=(1, 1))
        self.chat_display = BoxLayout(orientation='vertical', size_hint_y=None)
        self.chat_display.bind(minimum_height=self.chat_display.setter('height'))
        self.chat_display_scroll.add_widget(self.chat_display)
        self.add_widget(self.chat_display_scroll)

        self.input_container = BoxLayout(
                orientation='horizontal', size_hint=(1, 0.1), padding=[10, 40], spacing=10
            )

            # Input field
        self.input_area = MDTextField(
                hint_text="Type here...",
                mode="round",
                max_text_length=200,
                helper_text="Character count:",
                multiline=False,
                size_hint=(0.85, 1)
            )

            # Send button
        self.send_button = MDIconButton(
                icon="send-circle",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
            )
        self.send_button.bind(on_press=self.send_message)

            # Add input field and button to the container
        self.input_container.add_widget(self.input_area)
        self.input_container.add_widget(self.send_button)

            # Add the container to the main layout
        self.add_widget(self.input_container)


    def update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def send_message(self, instance):
        message = self.input_area.text.strip()
        if message:
            message_label = Label(
                text=message,
                size_hint_y=None,
                height=self.calculate_label_height(message),
                text_size=(self.width, None),
                color=(1,1,1,1),
                valign='top',
                halign='left'
            )
            self.chat_display.add_widget(message_label)
            self.input_area.text = ""

    def send_resonse(self, instance):
        message = "placeholder for response object"
        if message:
            message_label = Label(
                text=message,
                size_hint_y=None,
                height=self.calculate_label_height(message),
                text_size=(self.width, None),
                color=(0,0,0,0),
                valign='top',
                halign='left'
            )
            self.chat_display.add_widget(message_label)

    def calculate_label_height(self, message):
        line_height = 30
        max_width = self.width
        lines = len(message) // (max_width // 10)
        return line_height * (lines + 1)

class SettingsPage(BoxLayout):
    def __init__(self, screen_manager): 
        super().__init__(orientation='vertical')
        self.screen_manager = screen_manager
        with self.canvas.before:
            Color(0.5, 0.6, 0.8, 1)  # Set background color
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)
        self.add_widget(Menu(screen_manager, (1, 1, 1, 1)), index=0)

    def update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def go_to_main(self, instance):
        self.screen_manager.transition = SlideTransition(direction='right')
        self.screen_manager.current = 'Main'


myapp = VM()
myapp.run()
