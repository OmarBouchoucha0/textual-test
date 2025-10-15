from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, Button, Static

class TypingTest(App):
    CSS_PATH = "home.css"
    
    def on_mount(self) -> None:
        self.theme = "gruvbox"
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("""
____    __    ____  _______  __        ______   ______   .___  ___.  _______ 
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__   
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|  
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____ 
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|
                                                                             
please Choose a Game Mode""", id="welcome")
        yield Horizontal(
            Button("Single Player"),
            Button("Multi Player"),
            id="menu"
        )
        yield Footer()

if __name__ == "__main__":
    app = TypingTest()
    app.run()
