style_sheet = """
    MainFrame{
        background-color: #000;
             }

     QMenuBar {
            background-color: #151515;
            color: #BBB;
        }
    QMessageBox {
    background-color: #151515;
}

    QPushButton{
    background-color: #151515;
    color: #DDD;
    border: 1px solid #606060;
    padding: 5px;
    }

        QMenuBar::item::selected {
            background-color: #303030;
        }

        QMenu {
            background-color: #151515;
            color: #BBB;
            border: 1px solid #303030;           
        }

        QMenu::item::selected {
            background-color: #303030;
        }
    
    QLabel{
        color: #DDDDDD;
        font-size: 16px
             }  
    .TestTreeWidget{
        background-color: #505050;
        color: red
    }
    MainPanel{
        background-color: #000000;
        color: White;
        border: 70px solid red
        }
    TestPanel{
        background-color: #302020;
        border: 0px
    }
    QFrame{
        background-color: #151515;
    }
    Toolbar{
        background-color: #151515;
        border: 0px
    }
    QPlainTextEdit#stream{
        background-color: #151515;
        border: 0px;
        color: white
    
    }
    QTabWidget{
        background-color: #000000;
    }
    Step{
        background-color: #202020;
    }
    
    StepsContainer{
        background-color: #101010 0;
    }
    
    QTabWidget::pane { 
    background-color: #000000;
}
    QTabBar::tab{
        background-color: #101010;
        color: white;
        padding: 8px
    }
    QTabBar{
        background-color: #000000;
        
    }
    
    QTabBar::tab:selected, QTabBar::tab:hover{
         background-color: #303030;
         border: 3px solid #303030;
         border-bottom-color: #903030;
    }
    QTabBar::close-button{
        image: url(Gui/images/close.png)
    }

    QTreeView{
        background-color: #101010;
        border: 1px solid #303030;
        color: #BBB;
        show-decoration-selected: 1;
        }

    QTreeView:item:has-children{
        color: #BBB
    }
    QTreeView FolderTreeWidget{
        color: #FF0000;
    }
    
    QTreeView::indicator{
        background-color: #202020; 
    }
    QTreeView::indicator:checked{
        background-color: #101010;
        border-image: url(Gui/images/Play.png) 0;
    }
    QTreeView::indicator:indeterminate{
        background-color: #101010;
        border-image: url(Gui/images/SemiPlay.png) 0;
    }
    QHeaderView{
        background-color: #202020;
    }
    
    QHeaderView:section{
        background-color: #101010;
        color: white
        }
    QSplitter{
        background-color: #151515;
        border: 0px
    }
    
    QSplitter::handle{
        background-color: #202020;
        }

    QScrollBar:horizontal {
    border: 0;
    background: #404040;
    height: 15px;
}
QScrollBar::handle:horizontal {
    background: #404040;
    min-width: 20px;
}
QScrollBar::add-line:horizontal {
    border: 0px solid grey;
    background: #404040;
    width: 0px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: #202020;
}

QScrollBar::sub-line:horizontal {
    border: 0px solid grey;
    background: #404040;
    width: 0px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QTableWidget{
    background: #202020;
    color: #DDDDDD;
    font-size:14 px
}

QTableView QTableCornerButton::section {
    background: #202020;
}

SideFrameTitleFrame{
    background-color: #202020;
}

SideFrameTitleFrame QPushButton{
    background-color: #202020;
}

SideFrameTitleFrame QLabel{
    background-color: #202020;
}

 QPlainTextEdit{
    font-size: 10px
 }

QLineEdit{
    background-color: #303030;
    color: #FFFFFF;
}
QLineEdit[WRONG=true]{
    background-color: #FF0000;
    color: #FFFFFF;
}

PopUpWindow {
    background-color: #303030;
}
"""
