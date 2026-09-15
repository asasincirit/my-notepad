import os
from pathlib import Path

from kivy.app import App
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.clock import Clock


# =========================================================
# تنظیمات اولیه
# =========================================================

Window.clearcolor = (0.035, 0.04, 0.055, 1)


# =========================================================
# دکمه حرفه‌ای
# =========================================================

class ModernButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)

        self.color = (0.92, 0.94, 0.98, 1)
        self.font_size = dp(14)

        with self.canvas.before:
            self.bg_color = Color(
                0.10, 0.12, 0.17, 1
            )

            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(8)]
            )

        self.bind(
            pos=self.update_bg,
            size=self.update_bg
        )

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


# =========================================================
# ویرایشگر متن
# =========================================================

class Editor(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.multiline = True

        self.font_size = dp(18)

        self.padding = [
            dp(20),
            dp(18),
            dp(20),
            dp(18)
        ]

        self.background_normal = ""
        self.background_active = ""

        self.background_color = (
            0.055,
            0.065,
            0.09,
            1
        )

        self.foreground_color = (
            0.92,
            0.94,
            0.98,
            1
        )

        self.cursor_color = (
            0.35,
            0.65,
            1,
            1
        )

        self.selection_color = (
            0.20,
            0.40,
            0.75,
            0.45
        )

        self.write_tab = False


# =========================================================
# برنامه اصلی
# =========================================================

class Notepad(FloatLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.current_file = None

        self.dark_mode = True

        # -------------------------------------------------
        # پس‌زمینه
        # -------------------------------------------------

        with self.canvas.before:

            self.background_color = Color(
                0.035,
                0.04,
                0.055,
                1
            )

            self.background = Rectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.update_background,
            size=self.update_background
        )

        # -------------------------------------------------
        # لایه اصلی
        # -------------------------------------------------

        main = BoxLayout(
            orientation="vertical",
            padding=dp(8),
            spacing=dp(7)
        )

        # =================================================
        # نوار بالایی
        # =================================================

        top = BoxLayout(
            size_hint_y=None,
            height=dp(52),
            spacing=dp(6)
        )

        title = Label(
            text="  ✦  My Notepad",
            font_size=dp(19),
            bold=True,
            color=(0.8, 0.88, 1, 1),
            halign="left",
            valign="middle"
        )

        title.bind(
            size=lambda obj, value:
            setattr(obj, "text_size", value)
        )

        top.add_widget(title)

        new_btn = ModernButton(
            text="＋",
            size_hint_x=None,
            width=dp(48)
        )

        new_btn.bind(
            on_press=self.new_file
        )

        open_btn = ModernButton(
            text="📂",
            size_hint_x=None,
            width=dp(48)
        )

        open_btn.bind(
            on_press=self.open_file
        )

        save_btn = ModernButton(
            text="💾",
            size_hint_x=None,
            width=dp(48)
        )

        save_btn.bind(
            on_press=self.save_file
        )

        menu_btn = ModernButton(
            text="☰",
            size_hint_x=None,
            width=dp(48)
        )

        menu_btn.bind(
            on_press=self.show_menu
        )

        top.add_widget(new_btn)
        top.add_widget(open_btn)
        top.add_widget(save_btn)
        top.add_widget(menu_btn)

        main.add_widget(top)

        # =================================================
        # نوار ابزار ویرایش
        # =================================================

        tools_scroll = ScrollView(
            size_hint_y=None,
            height=dp(48),
            do_scroll_y=False
        )

        tools = BoxLayout(
            size_hint_x=None,
            spacing=dp(5)
        )

        tools.bind(
            minimum_width=tools.setter("width")
        )

        undo_btn = ModernButton(
            text="↶",
            size_hint_x=None,
            width=dp(52)
        )

        undo_btn.bind(
            on_press=self.undo
        )

        redo_btn = ModernButton(
            text="↷",
            size_hint_x=None,
            width=dp(52)
        )

        redo_btn.bind(
            on_press=self.redo
        )

        cut_btn = ModernButton(
            text="✂",
            size_hint_x=None,
            width=dp(52)
        )

        cut_btn.bind(
            on_press=self.cut_text
        )

        copy_btn = ModernButton(
            text="کپی",
            size_hint_x=None,
            width=dp(65)
        )

        copy_btn.bind(
            on_press=self.copy_text
        )

        paste_btn = ModernButton(
            text="پیست",
            size_hint_x=None,
            width=dp(70)
        )

        paste_btn.bind(
            on_press=self.paste_text
        )

        select_btn = ModernButton(
            text="انتخاب همه",
            size_hint_x=None,
            width=dp(105)
        )

        select_btn.bind(
            on_press=self.select_all
        )

        find_btn = ModernButton(
            text="🔎 جستجو",
            size_hint_x=None,
            width=dp(100)
        )

        find_btn.bind(
            on_press=self.find_text
        )

        tools.add_widget(undo_btn)
        tools.add_widget(redo_btn)
        tools.add_widget(cut_btn)
        tools.add_widget(copy_btn)
        tools.add_widget(paste_btn)
        tools.add_widget(select_btn)
        tools.add_widget(find_btn)

        tools_scroll.add_widget(tools)

        main.add_widget(tools_scroll)

        # =================================================
        # نوار تنظیمات فونت
        # =================================================

        font_bar = BoxLayout(
            size_hint_y=None,
            height=dp(43),
            spacing=dp(6)
        )

        font_label = Label(
            text="فونت:",
            size_hint_x=None,
            width=dp(45),
            color=(0.75, 0.78, 0.85, 1)
        )

        self.font_spinner = Spinner(
            text="Default",
            values=[
                "Default",
                "Roboto",
                "Sans",
                "Serif"
            ],
            size_hint_x=None,
            width=dp(105)
        )

        self.font_spinner.bind(
            text=self.change_font
        )

        size_label = Label(
            text="اندازه:",
            size_hint_x=None,
            width=dp(55),
            color=(0.75, 0.78, 0.85, 1)
        )

        self.size_spinner = Spinner(
            text="18",
            values=[
                "12",
                "14",
                "16",
                "18",
                "20",
                "22",
                "24",
                "28",
                "32",
                "36",
                "42"
            ],
            size_hint_x=None,
            width=dp(65)
        )

        self.size_spinner.bind(
            text=self.change_font_size
        )

        font_bar.add_widget(font_label)
        font_bar.add_widget(self.font_spinner)
        font_bar.add_widget(size_label)
        font_bar.add_widget(self.size_spinner)

        # فضای خالی
        font_bar.add_widget(Widget())

        main.add_widget(font_bar)

        # =================================================
        # ویرایشگر
        # =================================================

        self.editor = Editor()

        self.editor.bind(
            text=self.update_status
        )

        main.add_widget(self.editor)

        # =================================================
        # نوار وضعیت
        # =================================================

        status = BoxLayout(
            size_hint_y=None,
            height=dp(32)
        )

        self.status = Label(
            text="آماده",
            color=(0.55, 0.62, 0.72, 1),
            halign="left",
            valign="middle"
        )

        self.status.bind(
            size=lambda obj, value:
            setattr(obj, "text_size", value)
        )

        status.add_widget(self.status)

        main.add_widget(status)

        self.add_widget(main)

    # =====================================================
    # پس زمینه
    # =====================================================

    def update_background(self, *args):

        self.background.pos = self.pos
        self.background.size = self.size

    # =====================================================
    # فایل جدید
    # =====================================================

    def new_file(self, *args):

        if self.editor.text.strip():

            self.confirm_new()

        else:

            self.editor.text = ""
            self.current_file = None

    def confirm_new(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        label = Label(
            text="متن فعلی پاک شود و فایل جدید ساخته شود؟"
        )

        buttons = BoxLayout(
            size_hint_y=None,
            height=dp(45),
            spacing=dp(8)
        )

        yes = ModernButton(text="بله")
        no = ModernButton(text="لغو")

        buttons.add_widget(yes)
        buttons.add_widget(no)

        layout.add_widget(label)
        layout.add_widget(buttons)

        popup = Popup(
            title="فایل جدید",
            content=layout,
            size_hint=(0.85, 0.3)
        )

        yes.bind(
            on_press=lambda x: self.create_new(popup)
        )

        no.bind(
            on_press=popup.dismiss
        )

        popup.open()

    def create_new(self, popup):

        self.editor.text = ""
        self.current_file = None
        self.status.text = "فایل جدید"

        popup.dismiss()

    # =====================================================
    # ذخیره
    # =====================================================

    def save_file(self, *args):

        if self.current_file:

            self.write_file(self.current_file)

        else:

            self.save_as()

    def save_as(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        filename = TextInput(
            hint_text="نام فایل",
            multiline=False,
            size_hint_y=None,
            height=dp(45)
        )

        save = ModernButton(
            text="ذخیره"
        )

        layout.add_widget(filename)
        layout.add_widget(save)

        popup = Popup(
            title="ذخیره فایل",
            content=layout,
            size_hint=(0.85, 0.35)
        )

        def do_save(*args):

            name = filename.text.strip()

            if not name:
                return

            if not name.endswith(".txt"):
                name += ".txt"

            path = os.path.join(
                os.path.expanduser("~"),
                name
            )

            self.write_file(path)

            popup.dismiss()

        save.bind(
            on_press=do_save
        )

        popup.open()

    def write_file(self, path):

        try:

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(self.editor.text)

            self.current_file = path

            self.status.text = (
                f"ذخیره شد: {os.path.basename(path)}"
            )

        except Exception as e:

            self.status.text = "خطا در ذخیره فایل"

    # =====================================================
    # باز کردن
    # =====================================================

    def open_file(self, *args):

        from kivy.uix.filechooser import FileChooserListView

        chooser = FileChooserListView(
            path=os.path.expanduser("~"),
            filters=["*.txt"]
        )

        layout = BoxLayout(
            orientation="vertical"
        )

        buttons = BoxLayout(
            size_hint_y=None,
            height=dp(48)
        )

        open_btn = ModernButton(
            text="باز کردن"
        )

        cancel_btn = ModernButton(
            text="لغو"
        )

        buttons.add_widget(open_btn)
        buttons.add_widget(cancel_btn)

        layout.add_widget(chooser)
        layout.add_widget(buttons)

        popup = Popup(
            title="باز کردن فایل",
            content=layout,
            size_hint=(0.95, 0.9)
        )

        def load_file(*args):

            if not chooser.selection:
                return

            path = chooser.selection[0]

            try:

                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    self.editor.text = f.read()

                self.current_file = path

                self.status.text = (
                    f"باز شد: {os.path.basename(path)}"
                )

                popup.dismiss()

            except:

                self.status.text = "خطا در باز کردن فایل"

        open_btn.bind(
            on_press=load_file
        )

        cancel_btn.bind(
            on_press=popup.dismiss
        )

        popup.open()

    # =====================================================
    # ویرایش
    # =====================================================

    def undo(self, *args):

        try:
            self.editor.do_undo()
            self.status.text = "Undo"
        except:
            pass

    def redo(self, *args):

        try:
            self.editor.do_redo()
            self.status.text = "Redo"
        except:
            pass

    def cut_text(self, *args):

        self.editor.cut()
        self.status.text = "متن برش خورد"

    def copy_text(self, *args):

        self.editor.copy()
        self.status.text = "متن کپی شد"

    def paste_text(self, *args):

        self.editor.paste()
        self.status.text = "متن پیست شد"

    def select_all(self, *args):

        self.editor.select_all()
        self.status.text = "همه متن انتخاب شد"

    # =====================================================
    # فونت
    # =====================================================

    def change_font(self, spinner, value):

        if value == "Default":

            self.editor.font_name = "Roboto"

        else:

            self.editor.font_name = value

    def change_font_size(self, spinner, value):

        try:

            self.editor.font_size = dp(
                int(value)
            )

        except:

            pass

    # =====================================================
    # جستجو
    # =====================================================

    def find_text(self, *args):

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        search = TextInput(
            hint_text="عبارت موردنظر...",
            multiline=False,
            size_hint_y=None,
            height=dp(45)
        )

        result = Label(
            text="عبارت را وارد کنید"
        )

        button = ModernButton(
            text="جستجو",
            size_hint_y=None,
            height=dp(45)
        )

        layout.add_widget(search)
        layout.add_widget(result)
        layout.add_widget(button)

        popup = Popup(
            title="جستجو در متن",
            content=layout,
            size_hint=(0.85, 0.4)
        )

        def search_now(*args):

            word = search.text

            if not word:
                return

            text = self.editor.text

            count = text.lower().count(
                word.lower()
            )

            result.text = (
                f"تعداد پیدا شده: {count}"
            )

        button.bind(
            on_press=search_now
        )

        popup.open()

    # =====================================================
    # منو
    # =====================================================

    def show_menu(self, *args):

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(7)
        )

        theme_btn = ModernButton(
            text="🌙 تغییر حالت روشن / تاریک"
        )

        info_btn = ModernButton(
            text="ℹ درباره برنامه"
        )

        exit_btn = ModernButton(
            text="خروج"
        )

        layout.add_widget(theme_btn)
        layout.add_widget(info_btn)
        layout.add_widget(exit_btn)

        popup = Popup(
            title="منو",
            content=layout,
            size_hint=(0.85, 0.45)
        )

        theme_btn.bind(
            on_press=lambda x: (
                self.toggle_theme(),
                popup.dismiss()
            )
        )

        info_btn.bind(
            on_press=lambda x: self.show_about()
        )

        exit_btn.bind(
            on_press=lambda x: App.get_running_app().stop()
        )

        popup.open()

    # =====================================================
    # تم
    # =====================================================

    def toggle_theme(self):

        self.dark_mode = not self.dark_mode

        if self.dark_mode:

            self.background_color.rgb = (
                0.035,
                0.04,
                0.055
            )

            self.editor.background_color = (
                0.055,
                0.065,
                0.09,
                1
            )

            self.editor.foreground_color = (
                0.92,
                0.94,
                0.98,
                1
            )

            self.status.text = "حالت تاریک فعال شد"

        else:

            self.background_color.rgb = (
                0.90,
                0.91,
                0.94
            )

            self.editor.background_color = (
                0.97,
                0.97,
                0.98,
                1
            )

            self.editor.foreground_color = (
                0.08,
                0.08,
                0.10,
                1
            )

            self.status.text = "حالت روشن فعال شد"

    # =====================================================
    # درباره
    # =====================================================

    def show_about(self):

        popup = Popup(
            title="درباره My Notepad",
            content=Label(
                text=(
                    "My Notepad\n\n"
                    "یک ویرایشگر متن ساده و مدرن\n"
                    "ساخته شده با Python + Kivy"
                ),
                halign="center"
            ),
            size_hint=(0.8, 0.4)
        )

        popup.open()

    # =====================================================
    # وضعیت متن
    # =====================================================

    def update_status(self, *args):

        text = self.editor.text

        characters = len(text)

        words = len(
            text.split()
        )

        lines = (
            text.count("\n") + 1
            if text
            else 1
        )

        self.status.text = (
            f"خطوط: {lines}   |   "
            f"کلمات: {words}   |   "
            f"حروف: {characters}"
        )


# =========================================================
# اجرای برنامه
# =========================================================

class MyNotepadApp(App):

    title = "My Notepad"

    def build(self):

        return Notepad()


if __name__ == "__main__":

    MyNotepadApp().run()
