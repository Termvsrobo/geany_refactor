import gtk
import geany

class RefactorPlugin(geany.Plugin):
    __plugin_name__ = "Python refactoring"
    __plugin_description__ = "Python refactoring"
    __plugin_version__ = "0.0.1"
    __plugin_author__ = "Termvsrobo"

    def __init__(self):
        # Define menu and items
        self.rename_menu = gtk.Menu()
        self.rename_menu_item = gtk.MenuItem("Rename")
        self.refactor_menu_item = gtk.MenuItem("Refactoring")
        self.refactor_menu_item.set_submenu(self.rename_menu)
        self.rename_menu.append(self.rename_menu_item)
        # Show items
        self.rename_menu_item.show()
        self.refactor_menu_item.show()
        geany.main_widgets.editor_menu.append(self.refactor_menu_item)
        # define actions
        self.rename_menu_item.connect("activate", self.on_hello_item_clicked)

    def cleanup(self):
        self.refactor_menu_item.destroy()

    def on_hello_item_clicked(widget, data):
        widget.dialog = gtk.Dialog(title="Rename detail",
                            parent=geany.main_widgets.window,
                            )
        label_word = gtk.Label("word")
        widget.entry = gtk.Entry(max=0)
        hbox_word = gtk.HBox()
        hbox_word.pack_start(label_word, True, True, 0)
        hbox_word.pack_start(widget.entry, True, True, 0)
        widget.chbox_search_in_project = gtk.CheckButton()
        label_search_in_project = gtk.Label("Search in project")
        hbox_check = gtk.HBox()
        hbox_check.pack_start(widget.chbox_search_in_project, True, True, 0)
        hbox_check.pack_start(label_search_in_project, True, True, 0)
        widget.dialog.vbox.pack_start(hbox_word, True, True, 0)
        widget.dialog.vbox.pack_start(hbox_check, True, True, 0)
        button_ok = gtk.Button(stock=gtk.STOCK_OK)
        button_ok.connect("clicked", widget.on_ok_clicked)
        button_cancel = gtk.Button(stock=gtk.STOCK_CANCEL)
        button_cancel.connect("clicked", widget.on_cancel_clicked)
        widget.dialog.action_area.pack_start(button_ok, True, True, 0)
        widget.dialog.action_area.pack_start(button_cancel, True, True, 0)
        # show
        widget.entry.show()
        label_word.show()
        widget.chbox_search_in_project.show()
        label_search_in_project.show()
        hbox_word.show()
        hbox_check.show()
        button_ok.show()
        button_cancel.show()
        widget.dialog.show()

    def on_ok_clicked(widget, data):
        text = widget.entry.get_text()
        search_in_prj = widget.chbox_search_in_project.get_active()
        if search_in_prj:
            # search in project
            pass
        else:
            document = geany.document.get_current()
            print("document", document)
            print(dir(document))
            editor = document.editor
            print("editor", editor)
            print("editor", dir(editor))

    def on_cancel_clicked(widget, data):
        widget.dialog.destroy()

