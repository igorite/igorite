from igor.Gui.PopUpWindows.PopUp import PopUpWindow


class LoadProjectWindow(PopUpWindow):

    def __init__(self):
        PopUpWindow.__init__(self, 'Load Project')
        self.show()
