# Copyright 2019 SocIsomer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
        image: url(/../Components/images/close.png)
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

QToolButton{
    background-color: #151515;
    color: #DDDDDD;
    border: 2px solid #303030;
}

QTextEdit{
    color: #DDD;
}

QListView {
    background-color: #151515;
    color: #DDDDDD;
    border: 2px solid #303030;
}


QScrollBar:vertical {

  border-color: rgb(0,0,0,0);
  border-width: 0px;
  border-style: solid;
  border-radius: 0px;

  background-color: rgb(0,0,0,0);
  width: 15px;
  margin: 21px 0 21px 0;
}

QScrollBar::handle:vertical {

  background-color: rgb(80,80,80,100);
  min-height: 25px;
  border-radius: 10px;

}

 QScrollBar::add-line:vertical {
    border: 1px solid grey;
  background-color: rgb(241, 241, 241);
    height: 20px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
    border: 0px solid grey;
    background-color: rgb(241, 241, 241);
    height: 1px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
      background: none;
  }

QScrollBar::up-arrow:vertical
{
  background-color:#202020;
}

QScrollBar::down-arrow:vertical
{
  image: url(:/BarIcon/Icons/downarrow.png);
}

QScrollBar:horizontal {
  border-color: rgb(227, 227, 227);
  border-width: 1px;
  border-style: solid;
  background-color: rgb(240, 240, 240);
    height: 15px;
    margin: 0px 21px 0 21px;
 }

 QScrollBar::handle:horizontal {
    background-color: rgb(200, 200, 200);
    min-width: 25px;
 }
QScrollBar::add-line:horizontal {
    border: 1px solid grey;
  background-color: rgb(241, 241, 241);
    height: 20px;
    subcontrol-position: right;
    subcontrol-origin: margin;
 }

 QScrollBar::sub-line:horizontal {
  border: 1px solid grey;
    background-color: rgb(241, 241, 241);
    height: 20px;
    subcontrol-position: left;
    subcontrol-origin: margin;
 }

 QScrollBar:left-arrow:horizontal
{
  image: url(:/BarIcon/Icons/leftarrow.png);
}

QScrollBar::right-arrow:horizontal 
{
  image: url(:/BarIcon/Icons/rightarrow.png);
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
     background: none;
}

"""
