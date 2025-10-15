from textual.app import App, ComposeResult
from textual.widgets import Static

class TypingTest(App):
    def compose(self) -> ComposeResult:
        yield Static("HELLO WORLD")

if __name__ == "__main__":
    app = TypingTest()
    app.run()
