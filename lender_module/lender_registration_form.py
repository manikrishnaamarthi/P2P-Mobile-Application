from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivy.metrics import dp
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup




#Window.size = (300, 500)
KV = """
BoxLayout:
    orientation: 'vertical'

    ScreenManager:
        id: screen_manager

        Screen:
            name: 'lender_reg_form1'

            Image:
                source: 'C:\\kivymd\\images\\kotak.png'
                size_hint: None, None  # This line ensures that size is not hinted
                size: 200, 80  # Adjust the size as per your requirement
                pos_hint: {'x': 0, 'top': 1}

            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Lender Registration Form1'
                        font_size: 25
                        halign: 'center'
                        bold: True

                    MDTextField:
                        id: username
                        hint_text: 'Enter full name'
                        multiline: False
                        helper_text: 'Enter valid name'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: gender_field
                        multiline: False
                        hint_text: "Select gender"
                        on_focus: if self.focus: app.show_gender_menu()
                        height: self.minimum_height
                        readonly: True
                        width: 300
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        hint_text_color: (0, 0, 0, 1)  # Black hint text color
                        text_color: (0, 0, 0, 1)  # Black text color
                        helper_text: "Select gender"
                        size_hint_x: None
                        size_hint_y: None
                        helper_text_mode: "on_focus"
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: date_textfield
                        hint_text: "Select Date"
                        icon_right: "calendar"
                        readonly: True
                        width: 300
                        size_hint_x: None
                        size_hint_y: None
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_focus: if self.focus: app.show_date_picker()
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: mobile_number
                        hint_text: "Enter mobile number"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                        size_hint_x: None
                        width: 300
                        theme_text_color: "Custom"
                        hint_text_color: (0, 0, 0, 1)  # Black hint text color
                        text_color: (0, 0, 0, 1)  # Black text color
                        helper_text: "Enter valid number"
                        helper_text_mode: "on_focus"
                        font_name: "Roboto-Bold"
                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form2'

        Screen:
            name: 'lender_reg_form2'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Lender Registration Form2'
                        font_size: 25
                        halign: 'center'
                        bold: True

                    MDTextField:
                        id: mobile_number
                        hint_text: "Enter mobile number"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                        size_hint_x: None
                        width: 300
                        theme_text_color: "Custom"
                        hint_text_color: (0, 0, 0, 1)  # Black hint text color
                        text_color: (0, 0, 0, 1)  # Black text color
                        helper_text: "Enter valid number"
                        helper_text_mode: "on_focus"
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: alternate_email
                        hint_text: 'Enter alternate email'
                        multiline: False
                        helper_text: 'Enter valid email'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300

                    MDRectangleFlatButton:
                        text: 'Upload your Image'
                        text_color: 0, 0, 0, 1  # Black text color
                        pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        on_release: app.file_manager_open()
                        size_hint: (0.1, 0.01)
                        font_size: "12sp"
                        size_hint_y: None
                        size_hint_x: None

                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form1'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form3'
        Screen:
            name: 'lender_reg_form3'

            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Lender Registration Form3'
                        font_size: 25
                        halign: 'center'
                        bold: True
                    MDTextField:
                        id: aadhar_number
                        hint_text: 'Enter aadhar number '
                        multiline: False
                        helper_text: 'Enter valid number'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300

                    MDRectangleFlatButton:
                        text: 'Upload aadharcard '
                        text_color: 0, 0, 0, 1  # Black text color
                        pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        on_release: app.file_manager_open()
                        size_hint: (0.1, 0.01)
                        font_size: "12sp"
                        size_hint_y: None
                        size_hint_x: None

                    MDTextField:
                        id: pan_number
                        hint_text: 'Enter pan number '
                        multiline: False
                        helper_text: 'Enter valid number'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300

                    MDRectangleFlatButton:
                        text: 'Upload pancard '
                        text_color: 0, 0, 0, 1  # Black text color
                        pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        on_release: app.file_manager_open()
                        size_hint: (0.1, 0.01)
                        font_size: "12sp"
                        size_hint_y: None
                        size_hint_x: None


                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form2'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form4'

        Screen:
            name: 'lender_reg_form4'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Lender Registration Form4'
                        font_size: 25
                        halign: 'center'
                        bold: True
                    MDLabel:
                        text: 'Address'
                        font_size: 25
                        halign: 'center'
                        bold: True

                    MDTextField:
                        id: street_address
                        hint_text: 'Enter street address '
                        multiline: False
                        helper_text: 'Enter valid address'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300


                    MDTextField:
                        id: city
                        hint_text: 'Enter city here'
                        multiline: False

                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:
                        id: Zip_code
                        hint_text: 'Enter postal/zipcode '
                        multiline: False

                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:
                        id: state
                        hint_text: 'Enter state here'
                        multiline: False

                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:
                        id: country
                        hint_text: 'Enter country here'
                        multiline: False

                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300


                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form3'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form5'   

        Screen:
            name: 'lender_reg_form5'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Lender Registration Form6'
                        font_size: 25
                        halign: 'center'
                        bold: True

                    MDTextField:
                        id: lending_type_field
                        multiline: False
                        hint_text: "Select one"
                        on_focus: if self.focus: app.show_lending_type_menu()
                        height: self.minimum_height
                        readonly: True
                        width: 300
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        hint_text_color: (0, 0, 0, 1)  # Black hint text color
                        text_color: (0, 0, 0, 1)  # Black text color
                        size_hint_x: None
                        size_hint_y: None
                        helper_text_mode: "on_focus"
                        font_name: "Roboto-Bold"



                    MDTextField:
                        id: investment
                        hint_text: 'Enter investment '
                        multiline: False
                        helper_text: 'Enter above 10000'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300

                    MDTextField:
                        id: lending_period_field
                        multiline: False
                        hint_text: "Select one"
                        on_focus: if self.focus: app.show_lending_period_menu()
                        height: self.minimum_height
                        readonly: True
                        width: 300
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        hint_text_color: (0, 0, 0, 1)  # Black hint text color
                        text_color: (0, 0, 0, 1)  # Black text color
                        helper_text: "Select gender"
                        size_hint_x: None
                        size_hint_y: None
                        helper_text_mode: "on_focus"
                        font_name: "Roboto-Bold"

                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form5'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.on_next_button_click()     
        Screen:
            name: 'len_reg_institutional_form1'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Institutional Type'
                        font_size: 25
                        halign: 'center'
                        bold: True
                    MDLabel:
                        text: 'Step-1'
                        font_size: 25
                        halign: 'center'
                        bold: True

                    MDTextField:
                        id: business_name
                        hint_text: 'Enter business name '
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300


                    MDTextField:
                        id: business_location
                        hint_text: 'Enter business_location'
                        multiline: False                   
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:
                        id:  business_address
                        hint_text: 'Enter business address'
                        multiline: False

                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:
                        id:branch_name
                        hint_text: 'Enter branch_name'
                        multiline: False                        
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300

                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form5'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_institutional_form2' 
        Screen:
            name: 'len_reg_institutional_form2'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Institutional Type'
                        font_size: 25
                        halign: 'center'
                        bold: True
                    MDLabel:
                        text: 'Step-2'
                        font_size: 25
                        halign: 'center'
                        bold: True

                    MDTextField:
                        id: nearest_location
                        hint_text: 'Enter nearest location '
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300


                    MDTextField:
                        id: business_type
                        hint_text: 'Enter business type'
                        multiline: False                   
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:
                        id:  no_of_employee_working
                        hint_text: 'Enter no of employees working'
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:
                        id:year_of_estd
                        hint_text: 'Enter year of estd'
                        multiline: False                        
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300

                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_institutional_form1'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_institutional_form3'
        Screen:
            name: 'len_reg_institutional_form3'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Institutional Type'
                        font_size: 25
                        halign: 'center'
                        bold: True
                    MDLabel:
                        text: 'Step-3'
                        font_size: 25
                        halign: 'center'
                        bold: True

                    MDTextField:
                        id: industry_type
                        hint_text: 'Enter industry type '
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300


                    MDTextField:
                        id: last_six_months_turnover
                        hint_text: 'Enter last 6 months turnover'
                        multiline: False                   
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDLabel:
                        text: "Last 6 months bank statements"
                        font_size: 22
                        halign: 'center'


                    MDRectangleFlatButton:
                        text: 'Upload here'
                        text_color: 0, 0, 0, 1  # Black text color
                        pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        on_release: app.file_manager_open()
                        size_hint: (0.1, 0.01)
                        font_size: "12sp"
                        size_hint_y: None
                        size_hint_x: None

                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_institutional_form2'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_institutional_form4' 
        Screen:
            name: 'len_reg_institutional_form4'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Institutional Type'
                        font_size: 25
                        halign: 'center'
                        bold: True
                    MDLabel:
                        text: 'Step-4'
                        font_size: 25
                        halign: 'center'
                        bold: True

                    MDTextField:
                        id: director_name
                        hint_text: 'Enter director name '
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300


                    MDTextField:
                        id: director_mobile_number
                        hint_text: 'Enter director mobile number'
                        multiline: False                   
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:
                        id:  din
                        hint_text: 'Enter DIN here'
                        multiline: False

                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:
                        id:cin
                        hint_text: 'Enter CIN here'
                        multiline: False                        
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300

                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_institutional_form3'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_institutional_form5'
        Screen:
            name: 'len_reg_institutional_form5'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Institutional Type'
                        font_size: 25
                        halign: 'center'
                        bold: True
                    MDLabel:
                        text: 'Step-5'
                        font_size: 25
                        halign: 'center'
                        bold: True

                    MDTextField:
                        id: reg_office_address
                        hint_text: 'Enter registered office address '
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300


                    MDTextField:
                        id: office_address_proof
                        hint_text: 'Enter office address proof'
                        multiline: False                   
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDLabel:
                        text: "Proof of verification"
                        font_size: 22
                        halign: 'center'


                    MDRectangleFlatButton:
                        text: 'Upload here'
                        text_color: 0, 0, 0, 1  # Black text color
                        pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        on_release: app.file_manager_open()
                        size_hint: (0.1, 0.01)
                        font_size: "12sp"
                        size_hint_y: None
                        size_hint_x: None
                    MDTextField:
                        id:branch_name
                        hint_text: 'Enter branch_name'
                        multiline: False                        
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300

                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_institutional_form4'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_institutional_form4'

        Screen:
            name: 'len_reg_individual_form1'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Individual Type'
                        font_size: 25
                        halign: 'center'
                        bold: True
                    MDLabel:
                        text: 'Employment Details'
                        font_size: 25
                        halign: 'center'
                        bold: True   
                    MDTextField:
                        id: employment_type_field
                        hint_text: "Select employment type"
                        on_focus: if self.focus: app.show_employment_type_menu()
                        size_hint: (None, None)
                        readonly: True
                        width: 300
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        hint_text_color: (0, 0, 0, 1)  # Black hint text color
                        text_color: (0, 0, 0, 1)  # Black text color   
                        helper_text_mode: "on_focus"
                        font_name: "Roboto-Bold"
                    MDTextField:
                        id: organization_type_field
                        hint_text: "Select organization type"
                        on_focus: if self.focus: app.show_organization_type_menu()
                        size_hint: (None, None)
                        readonly: True
                        width: 300
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        hint_text_color: (0, 0, 0, 1)  # Black hint text color
                        text_color: (0, 0, 0, 1)  # Black text color   
                        helper_text_mode: "on_focus"
                        font_name: "Roboto-Bold"
                    MDTextField:              
                        id:company_name
                        hint_text: 'Enter company_name'
                        multiline: False                        
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300


                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form5'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_individual_form2'        

        Screen:
            name: 'len_reg_individual_form2'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Individual Type'
                        font_size: 25
                        halign: 'center'
                        bold: True
                    MDLabel:
                        text: 'Employment Details'
                        font_size: 25
                        halign: 'center'
                        bold: True   
                    MDTextField:              
                        id:company_address
                        hint_text: 'Enter company address'
                        multiline: False                        
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:              
                        id:landmark
                        hint_text: 'Enter landmark'
                        multiline: False                        
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:              
                        id:business_phone_number
                        hint_text: 'Enter business phone number'
                        multiline: False                        
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300


                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_individual_form1'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'len_reg_individual_form3'       
        Screen:
            name: 'len_reg_individual_form3'
            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Individual Type'
                        font_size: 25
                        halign: 'center'
                        bold: True
                    MDLabel:
                        text: 'Employment Details'
                        font_size: 25
                        halign: 'center'
                        bold: True   
                    MDTextField:              
                        id:annual_salary
                        hint_text: 'Enter annual salary'
                        multiline: False                        
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDTextField:              
                        id:designation
                        hint_text: 'Enter designation'
                        multiline: False                        
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                    MDLabel:
                        text: "Upload Employee ID"
                        font_size: 18
                        halign: 'center'


                    MDRectangleFlatButton:
                        text: 'Upload here'
                        text_color: 0, 0, 0, 1  # Black text color
                        pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        on_release: app.file_manager_open()
                        size_hint: (0.1, 0.01)
                        font_size: "10sp"
                        size_hint_y: None
                        size_hint_x: None

                    MDLabel:
                        text: "Upload last 6 months bank statements"
                        font_size: 18
                        halign: 'center'


                    MDRectangleFlatButton:
                        text: 'Upload here'
                        text_color: 0, 0, 0, 1  # Black text color
                        pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        on_release: app.file_manager_open()
                        size_hint: (0.1, 0.01)
                        font_size: "10sp"
                        size_hint_y: None
                        size_hint_x: None


                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form6'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'lender_reg_form5'        

"""


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
        return Builder.load_string(KV)

    def show_gender_menu(self):
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Male",
                "on_release": lambda x="Male": self.set_selected_gender(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Female",
                "on_release": lambda x="Female": self.set_selected_gender(x),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.gender_field,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def set_selected_gender(self, gender):
        self.root.ids.gender_field.text = gender
        # Close the dropdown menu
        self.menu.dismiss()

    def show_lending_type_menu(self):
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Institutional",
                "on_release": lambda x="Institutional": self.set_selected_lending_type(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Individual",
                "on_release": lambda x="Individual": self.set_selected_lending_type(x),
            },
            # Add more lending types as needed
        ]
        self.lending_type_menu = MDDropdownMenu(
            caller=self.root.ids.lending_type_field,
            items=menu_items,
            width_mult=4,
        )
        self.lending_type_menu.open()

    def set_selected_lending_type(self, lending_type):
        self.root.ids.lending_type_field.text = lending_type
        # Close the dropdown menu
        self.lending_type_menu.dismiss()

    def show_lending_period_menu(self):
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "1 year",
                "on_release": lambda x="1 year": self.set_selected_lending_period(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "2-3 years",
                "on_release": lambda x="2-3 years": self.set_selected_lending_period(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "4-5 years",
                "on_release": lambda x="4-5 years": self.set_selected_lending_period(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Above 5 years",
                "on_release": lambda x="Above 5 years": self.set_selected_lending_period(x),
            },
            # Add more lending periods as needed
        ]
        self.lending_period_menu = MDDropdownMenu(
            caller=self.root.ids.lending_period_field,
            items=menu_items,
            width_mult=4,
        )
        self.lending_period_menu.open()

    def set_selected_lending_period(self, lending_period):
        self.root.ids.lending_period_field.text = lending_period
        # Close the dropdown menu
        self.lending_period_menu.dismiss()

    def on_save(self, instance, value, date_range):
        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)

        # Set the size_hint and width to control the size of the date picker
        date_dialog.size_hint = (None, None)
        date_dialog.width = dp(800)  # Adjust the width as needed

        date_dialog.open()


    def go_home(self):
        pass

    def set_text_color(self, text_field, color):
        text_field.text_color = color

    def file_manager_open(self):
        self.file_manager.show("/")

    def exit_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        # You can use the selected image path here
        print("Selected Path:", path)
        self.exit_manager()

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        selected_date = value.strftime('%Y-%m-%d')
        self.root.ids.date_textfield.text = selected_date

    def on_cancel(self, instance, value):
     pass

    def on_next_button_click(self):
        selected_lending_type = self.root.ids.lending_type_field.text
        if selected_lending_type == "Individual":
            self.root.ids.screen_manager.current = 'len_reg_individual_form1'
        elif selected_lending_type == "Institutional":
            self.root.ids.screen_manager.current = 'len_reg_institutional_form1'

    def show_employment_type_menu(self):
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Business",
                "on_release": lambda x="Business": self.set_selected_employment_type(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Student",
                "on_release": lambda x="Student": self.set_selected_employment_type(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Employee",
                "on_release": lambda x="Employment": self.set_selected_employment_type(x),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.employment_type_field,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def set_selected_employment_type(self, employment_type):
        self.root.ids.employment_type_field.text =employment_type
        # Close the dropdown menu
        self.menu.dismiss()


    def show_organization_type_menu(self):
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Public",
                "on_release": lambda x="Public": self.set_selected_organization_type(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Private",
                "on_release": lambda x="Private": self.set_selected_organization_type(x),
            },

        ]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.organization_type_field,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def set_selected_organization_type(self, organization_type):
        self.root.ids.organization_type_field.text =organization_type
        # Close the dropdown menu
        self.menu.dismiss()
DemoApp().run()