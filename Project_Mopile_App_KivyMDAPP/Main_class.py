






from kivy.lang import Builder
from kivymd.app import MDApp
import webbrowser,Data
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import  Window
obj=Data.data()

Window.size=(380,580)



class Dash(MDApp):

    def build(self):
        screen=ScreenManager()
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette="DeepPurple"
        self.just=Builder.load_file("Just.kv")
        self.Dash1=Builder.load_file("Dashboard_ui.kv")
        self.dash=Builder.load_file("registrato.kv")
        screen.add_widget(self.dash)
        screen.add_widget(self.just)
        screen.add_widget(self.Dash1)


        return screen
    def Dialog(self,title,body):
        self.dialog=MDDialog(title=title,text=body,buttons=[MDFlatButton(text="OK",on_release=self.close),],)
        self.dialog.open()
    def close(self,inst):
        self.dialog.dismiss()

    def SigUp(self):
        User=self.dash.ids.user.text
        Pin=self.dash.ids.pin.text
        Con=self.dash.ids.con.text
        if User=="" and Pin=="":
            self.Dialog("Notice","Please fill in blank splace")
        elif (User!="" or Pin!="") and Pin!=Con:
            self.Dialog("Notice", "Inccrrect inputs user or pin or conform pin ")

        if Pin==Con:
            check=self.checker(User,Pin)

            if check==True:
                obj.insert_table(User,Pin)
                self.root.current="just"
    def checker(self,user,pin):
        if user=="" and str(pin)=="":
            return False
        elif str(user[-11:]).upper()=="@JUST.CA202" and len(str(pin))==4:
            return True

    def Login(self):
        user=self.just.ids.user.text
        ps=self.just.ids.passs.text
        User,Pin=obj.get_user(user)
        if user == User and ps == Pin:
            self.root.current="Dash"
        elif user==""and ps=="":
            self.Dialog("Notice","Please fill in blank ")
        elif user!=User or ps!=Pin:
            self.Dialog("Notice", "Inccrrect inputs user or pin ")


    def show_and_hide(self):
        if self.dash.ids.pin.password==True:
            self.dash.ids.pin.password=False
            self.dash.ids.con.password = False
        else:
            self.dash.ids.pin.password = True
            self.dash.ids.con.password = True

    def SignInPage(self):
        self.root.current="just"
    def gellry(self):
        webbrowser.open('https://just.edu.so/just-gallary/')

    def faculty(self):
        webbrowser.open('https://just.edu.so/jobs/')

    def gradu(self):
        webbrowser.open('https://www.just.edu.so')

    def welco(self):
        webbrowser.open('https://just.edu.so/welcome/')

    def news(self):
        webbrowser.open('https://just.edu.so/news/')

    def stud(self):
        webbrowser.open('https://www.just.edu.so')

    def face(self):
        webbrowser.open('Jamhuriya University of Science and Technology')
    def email(self):
        webbrowser.open("info@just.edu.so")
    def web(self):
        webbrowser.open("www.just.edu.so")
    def myist(self):
        webbrowser.open("https://instagram.com/yarkaloosarakacay?igshid=YmMyMTA2M2Y=")
    def fcebo(self):
        webbrowser.open("https://www.facebook.com/Cabdullaahi.mascuudjr?mibextid=ZbWKwL")

    def what(self):
        webbrowser.open("http://Wa.me//252615268691")
    def back(self):
        print("Ma timid")
        self.root.current="just"














Dash().run()
# x=Dash()
# x.checker("Liiyow@just.ca202",8088)
#