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

        self.create_widgets()

    def create_widgets(self):
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

        # TODO: REMOVE
        self.create_note(None)

    def on_erased_clicked(self, event):
        print("Erase")

    def on_exit(self, event):
        self.Close(True)

    def create_note(self, event):
        dial = CreateNotePage(self)

    def list_item(self, note=None):
        self.checkbox.Append("item 0")
        self.checkbox.Append("item 1")
        self.checkbox.Append("item 2")
        self.checkbox.Append("item 3")
        self.checkbox.Append("item 4")

    def on_item_selected(self, event):
        # TODO
        self.modify_button.Enable()
        print(event.GetSelection())

    def on_item_checked(self, event):
        # TODO
        # print(event.GetInt())
        print(event.GetString())


class CreateNotePage(wx.Dialog):
    def __init__(self, parent):
        super(CreateNotePage, self).__init__(parent)
        self.WindowStyle = wx.CAPTION
        self.Title = "Créer une note"

        self.pnl = wx.Panel(self)
        self.sizer = wx.GridSizer(2, gap=wx.Size(0,0))
        self.pnl.SetSizer(self.sizer)
        self.create_widgets()
        self.note = Note()

        self.Show()

    def create_widgets(self):
        title_label = wx.StaticText(self.pnl, label="Titre")
        self.sizer.Add(title_label, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        title_ctrl = wx.TextCtrl(self.pnl, name="title_ctrl")
        self.sizer.Add(title_ctrl, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        content_label = wx.StaticText(self.pnl, label="Contenu")
        self.sizer.Add(content_label, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        content_ctrl = wx.TextCtrl(self.pnl, name="content_ctrl", style=wx.TE_MULTILINE)
        self.sizer.Add(content_ctrl, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        priority_label = wx.StaticText(self.pnl, label="Priorité")
        self.sizer.Add(priority_label, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        priority_combobox = wx.ComboBox(self.pnl,1 , choices=[Priorite.Faible.name, Priorite.Moyenne.name, Priorite.Urgent.name], style=wx.CB_DROPDOWN)
        priority_combobox.SetValue(Priorite.Faible.name)
        self.sizer.Add(priority_combobox, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.create_button = wx.Button(self.pnl, label="Sauvegarder")
        self.create_button.Bind(wx.EVT_BUTTON, self.on_create_clicked)
        self.sizer.Add(self.create_button, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cancel_button = wx.Button(self.pnl, label="Annuler")
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel_clicked)

        self.sizer.Add(self.cancel_button, 1, wx.ALIGN_CENTER | wx.ALL, 5)

    def on_create_clicked(self, event):
        confirm_create_dialog = wx.MessageDialog(self.pnl, "Enregistrer cette note et toutes ses modification?", "Sauvegarde", style= wx.YES_NO )
        confirm_create_dialog.SetYesNoLabels("&Oui", "&Non")
        confirm_value = confirm_create_dialog.ShowModal()

        if confirm_value == wx.ID_YES:
            # TODO: ADD les trucs pour sauvegarder la note
            self.Close(True)


    def on_cancel_clicked(self, event):
        confirm_cancel_dialog = wx.MessageDialog(self.pnl, "Jeter cette note et toutes ses modification?", "Annuler", style= wx.YES_NO )
        confirm_cancel_dialog.SetYesNoLabels("&Oui", "&Non")
        confirm_value = confirm_cancel_dialog.ShowModal()

        if confirm_value == wx.ID_YES:
            self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    frm = Application(None, title='TODO Liste')
    frm.Show()
    app.MainLoop()
