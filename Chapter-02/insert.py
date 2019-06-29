#!/usr/bin/env python

import wx

class InsertFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button',
                size=(800,600))
        panel = wx.Panel(self)
        self.button = wx.Button(panel, label="Close", pos=(125, 10),
                size=(50, 75))
        self.button1 = wx.Button(panel, label="Again\nToClose", pos=(250, 10),
                size=(50, 75))
        self.button1.Show(False)

        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, self.button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Bind(wx.EVT_BUTTON, self.OnCloseMeAgain, self.button1)

    def OnCloseMe(self, event):
        self.button1.Show()
        self.button.Show(False)

    def OnCloseMeAgain(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App()  #SimpleApp is deprecated
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

