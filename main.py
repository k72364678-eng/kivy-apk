from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class PasswordCheckerAppbyr
RAMKRISHNA(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="Password Strength Checker",
            font_size=24
        )

        self.password_input = TextInput(
            hint_text="Enter your password",
            password=True,
            multiline=False
        )

        check_button = Button(
            text="Check Password",
            size_hint_y=None,
            height=50
        )

        check_button.bind(on_press=self.check_password)

        self.result = Label(
            text="Enter a password to check",
            font_size=18
        )

        layout.add_widget(title)
        layout.add_widget(self.password_input)
        layout.add_widget(check_button)
        layout.add_widget(self.result)

        return layout

    def check_password(self, instance):
        password = self.password_input.text

        score = 0

        if len(password) >= 8:
            score += 1

        if any(char.isupper() for char in password):
            score += 1

        if any(char.islower() for char in password):
            score += 1

        if any(char.isdigit() for char in password):
            score += 1

        if any(char in "!@#$%^&*()-_=+[]{};:,.?/|" for char in password):
            score += 1

        if score <= 2:
            self.result.text = "Weak Password"
        elif score <= 4:
            self.result.text = "Medium Password"
        else:
            self.result.text = "Strong Password"


if __name__ == "__main__":
    PasswordCheckerApp().run()
