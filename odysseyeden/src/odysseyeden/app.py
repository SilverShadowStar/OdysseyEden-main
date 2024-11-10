"""
Odyssey Eden is an immersive adventure game that invites players to explore a vibrant world filled with unique characters, challenges, and opportunities for growth.
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class OdysseyEden(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return OdysseyEden()
