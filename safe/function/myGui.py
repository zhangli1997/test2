'''
  界面函数
'''
import wx

global step
global vehname
global guijudge
global vehnum
vehnum = '1'
guijudge = False
step = "123"
vehname = ""

global deletevehname  # delete
global deletejudge
deletejudge = False
deletevehname = ""


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '车辆调度台', size=(400, 400), pos=(1000, 50))
        panel = wx.Panel(self)

        self.bt_confirm = wx.Button(panel, label='确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)

        self.bt_confirm1 = wx.Button(panel, label='确定')  # delete
        self.bt_confirm1.Bind(wx.EVT_BUTTON, self.OnclickSubmit1)
        self.bt_cancel1 = wx.Button(panel, label='取消')
        self.bt_cancel1.Bind(wx.EVT_BUTTON, self.OnclickCancel1)

        self.title = wx.StaticText(panel, label='请输入调度时间和车辆ID')
        self.label_user = wx.StaticText(panel, label='调度时间:')
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label='车  辆 ID:')
        self.text_password = wx.TextCtrl(panel, style=wx.TE_LEFT)
        self.label_num = wx.StaticText(panel, label='车辆数量:')
        self.text_num = wx.TextCtrl(panel, style=wx.TE_LEFT)

        self.title1 = wx.StaticText(panel, label='请输入删除车辆ID')  # delete
        self.label_pwd1 = wx.StaticText(panel, label='车  辆 ID:')
        self.text_password1 = wx.TextCtrl(panel, style=wx.TE_LEFT)

        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd.Add(self.text_password, proportion=1, flag=wx.ALL, border=5)
        hsizer_num = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_num.Add(self.label_num, proportion=0, flag=wx.ALL, border=5)
        hsizer_num.Add(self.text_num, proportion=1, flag=wx.ALL, border=5)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALL, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=0, flag=wx.ALL, border=5)

        hsizer_pwd1 = wx.BoxSizer(wx.HORIZONTAL)  # delete
        hsizer_pwd1.Add(self.label_pwd1, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd1.Add(self.text_password1, proportion=1, flag=wx.ALL, border=5)
        hsizer_button1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button1.Add(self.bt_confirm1, proportion=0, flag=wx.ALL, border=5)
        hsizer_button1.Add(self.bt_cancel1, proportion=0, flag=wx.ALL, border=5)

        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, border=15)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_num, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)

        vsizer_all.Add(self.title1, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, border=15)  # delete
        vsizer_all.Add(hsizer_pwd1, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button1, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)
        panel.SetSizer(vsizer_all)

        panel.SetSizer(vsizer_all)

    def OnclickSubmit(self, event):
        global step
        global vehname
        global guijudge
        global vehnum
        message = ""
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        num = self.text_num.GetValue()
        if username == "" or password == "" or num == "":
            message = "调度时间和车辆ID不能为空"
        else:
            step = int(username)
            vehname = password
            vehnum = int(num)
            message = "增加成功"
            guijudge = True
        wx.MessageBox(message)

    def OnclickCancel(self, event):
        self.text_user.SetValue("")
        self.text_password.SetValue("")

    def OnclickSubmit1(self, event):
        global deletevehname
        global deletejudge
        message = ""
        password = self.text_password1.GetValue()
        if password == "":
            message = "删除车辆ID不能为空"
        else:
            deletevehname = password
            message = "删除成功"
            deletejudge = True
        wx.MessageBox(message)

    def OnclickCancel1(self, event):
        self.text_password1.SetValue("")


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
