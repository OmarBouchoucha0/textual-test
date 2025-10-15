from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal
from textual.widgets import Header, Footer, Button, Static
from textual.binding import Binding

class BaseScreen(Screen):
    """Base screen with header and footer template."""
    
    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
        ("f1", "app.show_home", "Home"),
        ("f2", "app.show_stats", "Stats"),
        ("f3", "app.show_leaderboard", "Leaderboard"),
    ]
    
    def compose(self) -> ComposeResult:
        yield from self.content()  # Call child screen's content method
        yield Footer()
    
    def content(self) -> ComposeResult:
        """Override this method in child screens to add content."""
        yield Static("Base screen - override content() method")

class HomeScreen(BaseScreen):
    """The home/main menu screen."""
    
    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
        ("f1", "app.show_home", "Home"),
        ("f2", "app.show_stats", "Stats"),
        ("f3", "app.show_leaderboard", "Leaderboard"),
    ]
    
    def content(self) -> ComposeResult:
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
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""
        if event.button.id == "single":
            self.app.push_screen("single_player")
        elif event.button.id == "multi":
            self.app.push_screen("multi_player")

class SinglePlayerScreen(BaseScreen):
    """Single player game screen."""
    
    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
        ("f1", "app.show_home", "Home"),
        ("f2", "app.show_stats", "Stats"),
        ("f3", "app.show_leaderboard", "Leaderboard"),
    ]
    
    def content(self) -> ComposeResult:
        yield Static("Single Player Mode", id="title")
        yield Static("Start typing when ready...")


class MultiPlayerScreen(Screen):
    """Multi player game screen."""
    
    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
        ("f1", "app.show_home", "Home"),
        ("f2", "app.show_stats", "Stats"),
        ("f3", "app.show_leaderboard", "Leaderboard"),
    ]
    
    def content(self) -> ComposeResult:
        yield Static("Multi Player Mode", id="title")
        yield Static("Waiting for opponent...")

class StatsScreen(Screen):
    """Stats screen."""
    
    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
        ("f1", "app.show_home", "Home"),
        ("f2", "app.show_stats", "Stats"),
        ("f3", "app.show_leaderboard", "Leaderboard"),
    ]
    
    def content(self) -> ComposeResult:
        yield Static("Your Statistics", id="title")
        yield Static("WPM: 0\nAccuracy: 0%\nGames Played: 0")


class LeaderboardScreen(Screen):
    """Leaderboard screen."""
    
    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
        ("f1", "app.show_home", "Home"),
        ("f2", "app.show_stats", "Stats"),
        ("f3", "app.show_leaderboard", "Leaderboard"),
    ]
    
    def content(self) -> ComposeResult:
        yield Static("Global Leaderboard", id="title")
        yield Static("1. Player1 - 120 WPM\n2. Player2 - 115 WPM\n3. Player3 - 110 WPM")

class TypingTest(App):
    CSS_PATH = "home.css"
    SCREENS = {
        "home": HomeScreen,
        "single_player": SinglePlayerScreen,
        "multi_player": MultiPlayerScreen,
        "stats": StatsScreen,
        "leaderboard": LeaderboardScreen,
    }
    
    def on_mount(self) -> None:
        self.theme = "textual-dark"
        self.push_screen("home")  # Start with home screen
    
    def action_show_home(self) -> None:
        """Navigate to home screen."""
        self.switch_screen("home")
    
    def action_show_stats(self) -> None:
        """Navigate to stats screen."""
        self.push_screen("stats")
    
    def action_show_leaderboard(self) -> None:
        """Navigate to leaderboard screen."""
        self.push_screen("leaderboard")

if __name__ == "__main__":
    app = TypingTest()
    app.run()
