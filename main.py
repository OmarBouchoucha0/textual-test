from textual import events
from textual.app import App, ComposeResult
from textual.widgets import RichLog


class InputApp(App):

    def compose(self) -> ComposeResult:
        yield RichLog()

    def on_key(self, event: events.Key) -> None:
        self.query_one(RichLog).write(event)


if __name__ == "__main__":
    app = InputApp()
    app.run()
