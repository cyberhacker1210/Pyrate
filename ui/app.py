from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class PyApp(App):
    BINDINGS = [
        ("q", "quitter", "Quitter"),
    ]
    def compose(self):
        yield Header()
        yield Static("Bonjour Pyrate", id="message")
        yield Footer()
    def action_quitter(self) -> None:
        self.exit()
app = PyApp()
app.run()