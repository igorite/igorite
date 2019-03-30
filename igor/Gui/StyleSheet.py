style_sheet = """
    MainFrame{
        background-color: #000;
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
        background-color: #10101 0;
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
        background-color: #000000
    }
    
    QTabBar::tab:selected{
         background-color: #303030;
         border: 3px solid #303030;
         border-bottom-color: #903030;
    }
    QTreeView{
        background-color: #101010;
        border: 1px solid #303030;
        color: #6060FF;
        show-decoration-selected: 1;
        }

    QTreeView:item:has-children{
        color: #BBB
    }
    
    QTreeView::indicator:checked{
        background-color: #700000;
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
    border: 2px solid grey;
    background: #32CC99;
    height: 15px;
    margin: 0px 20px 0 20px;
}
QScrollBar::handle:horizontal {
    background: white;
    min-width: 20px;
}
QScrollBar::add-line:horizontal {
    border: 2px solid grey;
    background: #32CC99;
    width: 20px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    border: 2px solid grey;
    background: #32CC99;
    width: 20px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QTableWidget{
    background: #202020;
    color: #DDDDDD


}

QTableView QTableCornerButton::section {
    background: red;
    border: 2px outset red;
}






"""
