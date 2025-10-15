from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, Button, Static
from textual.binding import Binding

class TypingTest(App):
    CSS_PATH = "home.css"
    BINDINGS = [
        Binding(key="f1",action="home",description="home"),
        Binding(key="f2",action="Stats",description="Stats"),
        Binding(key="f3",action="Leaderboard",description="Leaderboard"),
        Binding(key="ctrl+q", action="quit", description="Quit the app"),
    ]   
    def on_mount(self) -> None:
        self.theme = "tokyo-night"

    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("""
____    __    ____  _______  __        ______   ______   .___  ___.  _______ 
\\   \\  /  \\  /   / |   ____||  |      /      | /  __  \\  |   \\/   | |   ____|
 \\   \\/    \\/   /  |  |__   |  |     |  ,----'|  |  |  | |  \\  /  | |  |__   
  \\            /   |   __|  |  |     |  |     |  |  |  | |  |\\/|  | |   __|  
   \\    /\\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____ 
    \\__/  \\__/     |_______||_______| \\______| \\______/  |__|  |__| |_______|
                                                                             
please Choose a Game Mode""", id="welcome")
        yield Horizontal(
            Button("Single Player", id="single"),
            Button("Multi Player", id="multi"),
            id="menu"
        )
        yield Footer()
    
    @on(Button.Pressed, "#single")  
    def goto_single(self):
        self.exit()

    @on(Button.Pressed, "#multi")  
    def goto_multi(self):
        self.exit()


if __name__ == "__main__":
    app = TypingTest()
    app.run()
