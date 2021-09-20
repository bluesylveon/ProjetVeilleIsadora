import tkinter as tk
from tkinter.constants import *
from tkinter import ttk
import wx

from note import Note
from priorite import Priorite

# Ceci sera sujet à beaucoup de changements puisque que ce ne sont que des esssais


class Application(wx.Frame):
    def __init__(self, *args, **kw):
        super(Application, self).__init__(*args, **kw)
        self.pnl = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.pnl.SetSizer(self.sizer)

        # st = wx.StaticText(self.pnl, label="Hello World!")

        # self.sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        # self.master = master
        # self.pack()
        self.create_widgets()

    def create_widgets(self):
        print("test")

        self.checkbox = wx.CheckListBox(self.pnl)
        self.sizer.Add(self.checkbox)
        self.checkbox.Bind(wx.EVT_LISTBOX, self.on_item_selected)
        self.checkbox.Bind(wx.EVT_CHECKLISTBOX, self.on_item_checked)

        self.list_item(note=None)

        sizer_button = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(sizer_button)

        self.create_button = wx.Button(self.pnl, label="Créer une note")
        self.create_button.Bind(wx.EVT_BUTTON, self.create_note)
        sizer_button.Add(self.create_button)

        self.modify_button = wx.Button(self.pnl, label="Modifier note")
        self.modify_button.Disable()
        sizer_button.Add(self.modify_button)

        self.erase = wx.Button(self.pnl, label="Effacer")
        self.erase.Bind(wx.EVT_BUTTON, self.on_erased_clicked)
        sizer_button.Add(self.erase)

    def on_erased_clicked(self, event):
        print("Erase")

    def on_exit(self, event):
        self.Close(True)

    def create_note(self, event):
        # self.create_note_page()

        dial = CreateNotePage(self)

        print("you will create a note!")

    def create_note_page(self):
        self.create_page = wx.Dialog(self)
        create_pnl = wx.Panel(self.create_page)
        sizer_create = wx.BoxSizer(wx.VERTICAL)
        create_pnl.SetSizer(sizer_create)

        sizer_title = wx.BoxSizer(wx.HORIZONTAL)
        sizer_create.Add(sizer_title)

        title_label = wx.StaticText(create_pnl, label="Titre")
        sizer_title.Add(title_label, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        title_ctrl = wx.TextCtrl(create_pnl, name="title_ctrl")
        sizer_title.Add(title_ctrl, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        # self.create_page = wx.PopupWindow(self.pnl)
        # self.create_page = tk.Toplevel(self)
        # self.create_page.pack_propagate()
        # self.create_page.title("Créer une note")

        # titre_label = ttk.Label(self.create_page, text="Titre")
        # titre_label.pack(side= LEFT)

        # titre = ttk.Entry(self.create_page)
        # titre.pack(side= RIGHT)

        note = Note(id=0, titre="test", contenu="", priorite=Priorite.Faible)
        # self.list.insert(END, note.get_titre())

        # combo = ttk.Combobox(self.create_page, values=["Faible", "Moyenne", "Urgent"], ).pack(side=RIGHT)
        self.create_page.Show()

    def list_item(self, note=None):
        self.checkbox.Append("item 0")
        self.checkbox.Append("item 1")
        self.checkbox.Append("item 2")
        self.checkbox.Append("item 3")
        self.checkbox.Append("item 4")

        # item_panel = wx.Panel(self.pnl)
        # sizer = wx.BoxSizer(wx.VERTICAL)

        # item_title = wx.StaticText(self.pnl, label="hewwo")
        # self.sizer.Add(item_title)
        # delete_btn = wx.Button(item_panel, label="delete")
        # sizer.Add(item_title ,wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        # sizer.Add(delete_btn, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        # item_panel.SetSizer(sizer)
        # self.sizer.Add(item_title, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        # self.sizer.Add(delete_btn, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        # self.pnl.SetSizer(self.sizer)
        # item_title2 = wx.StaticText(self, label="hewwo")
        # item_title3 = wx.StaticText(self, label="hewwo")
        # item_title4 = wx.StaticText(self, label="hewwo")

        # list_items = wx.ListCtrl(self)
        # list_items.Append( "hewwo")

    def on_item_selected(self, event):
        self.modify_button.Enable()
        print(event.GetSelection())

    def on_item_checked(self, event):
        # print(event.GetInt())
        print(event.GetString())


class CreateNotePage(wx.Dialog):
    def __init__(self, parent):
        super(CreateNotePage, self).__init__(parent)

        self.pnl = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.pnl.SetSizer(self.sizer)
        self.create_widgets()

        self.Show()

    def create_widgets(self):
        sizer_title = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(sizer_title)

        title_label = wx.StaticText(self.pnl, label="Titre")
        sizer_title.Add(title_label, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        title_ctrl = wx.TextCtrl(self.pnl, name="title_ctrl")
        sizer_title.Add(title_ctrl, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)


        sizer_content = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(sizer_content)

        content_label = wx.StaticText(self.pnl, label="Contenu")
        sizer_content.Add(content_label, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        content_ctrl = wx.TextCtrl(self.pnl, name="content_ctrl", style=wx.TE_MULTILINE)
        sizer_content.Add(content_ctrl, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        sizer_button = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(sizer_button)

        self.create_button = wx.Button(self.pnl, label="Créer")
        self.create_button.Bind(wx.EVT_BUTTON, self.on_create_clicked)
        sizer_button.Add(self.create_button)

        self.cancel_button = wx.Button(self.pnl, label="Annuler")
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel_clicked)

        sizer_button.Add(self.cancel_button)

    def on_create_clicked(self, event):
        print("create clicked")
        confirm = wx.MessageBox("Enregistrer cette note et toutes ses modification?", "Confirm", wx.YES_NO, self.pnl)

        if confirm == wx.YES:
            # TODO: ADD les trucs pour sauvegarder la note
            self.Close(True)


    def on_cancel_clicked(self, event):
        # TODO: CHANGER wx.YES_NO POUR FR
        print("cancel clicked")
        confirm = wx.MessageBox("Annuler cette note et toutes ses modification?", "Confirm", wx.YES_NO, self.pnl)

        if confirm == wx.YES:
            self.Close(True)

        
        

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = Application(None, title='TODO Liste')
    frm.Show()
    app.MainLoop()
