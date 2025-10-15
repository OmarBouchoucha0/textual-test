from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Button, Static

class TypingTest(App):
    CSS_PATH = "home.css"
    
    def on_mount(self) -> None:
        self.theme = "gruvbox"
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("[bold]Welcome![bold]\nSelect a game mode below to start typing", id="Welcome")
        yield Horizontal(
            Button("Single Player"),
            Button("Multi Player"),
        )
        yield Footer()

if __name__ == "__main__":
    app = TypingTest()
    app.run()
