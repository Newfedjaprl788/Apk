from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return MDBoxLayout(
            orientation="vertical",
            children=[
                MDLabel(
                    text="Привет из APK!",
                    halign="center",
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),
                )
            ],
        )


if __name__ == "__main__":
    MainApp().run()
