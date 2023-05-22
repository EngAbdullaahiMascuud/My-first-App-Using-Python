from kivymd.app import MDApp
from kivy.core.window import  Window
from kivy.lang import  Builder
from kivymd.uix.screenmanager import  ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
Window.size=(380,580)




class Main(MDApp):


    def build(self):
        screen=ScreenManager()
        self.theme_cls.theme_style="Light"
        self.start=Builder.load_file("Dashboard_ui.kv.kv")

        screen.add_widget(self.start)
        return screen
    def Dialog(self,title,body):
        self.dialog=MDDialog(title=title,text=body,buttons=[MDFlatButton(text="ok",on_release=self.close),],)
        self.dialog.open()
    def close(self,inst):
        self.dialog.dismiss()

    def back(self):
        self.root.current = "just"
    def Login(self):
        user=self.start.ids.user.text
        ps=self.start.ids.passs.text


        if user==""and ps=="":
            self.Dialog("Notice","Please fill in blank splace")
        elif user!="c"and ps!="1":
            self.Dialog("Please Input ","User= CA202\nPassword=12345")
        elif user == "c" and ps == "1":
            self.root.current="Dash"




Main().run()