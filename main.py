from kivy.app import App
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class WindowManager(ScreenManager):

    class MainWindow(Screen):
        pass

    class Window_mEq(Screen):

        def mEq(self):
            n_meq = {
              'NaCl': 2, 'KCl': 2, 'CaCl2': 4, 'KI': 2, 'LiCl': 2,
              'glukoza': 0,  'atrop siar': 3,  'NaHCO3': 2}
            M_dict = { 'NaCl': 58.44, 'KCl': 74.55, 'CaCl2': 110.98, 'KI': 166, 'LiCl': 42.39,
              'glukoza': 180.156,  'atrop siar': 700,  'NaHCO3': 84}
            if float(self.ids.m.text) > 0:
                if self.ids.nazwa.text in M_dict:
                    n_meq = n_meq[self.ids.nazwa.text]
                    M = M_dict[self.ids.nazwa.text]
                    math = str(float(self.ids.m.text) * 1000 * n_meq / float(M))
                    return math
            invalidData()

        def mmol(self):
            n_mmol = { 'NaCl': 2, 'KCl': 2, 'CaCl2': 3, 'KI': 2, 'LiCl': 2,
              'glukoza': 1,  'atrop siar': 3,  'NaHCO3': 2}
            M_dict = { 'NaCl': 58.44, 'KCl': 74.55, 'CaCl2': 110.98, 'KI': 166, 'LiCl': 42.39,
              'glukoza': 180.156,  'atrop siar': 700,  'NaHCO3': 84}
            if float(self.ids.m.text) > 0:
                if self.ids.nazwa.text in M_dict:
                    n_mmol = n_mmol[self.ids.nazwa.text]
                    M = M_dict[self.ids.nazwa.text]
                    math = str(float(self.ids.m.text) * 1000 * n_mmol / float(M))
                    return math
            invalidData()

    class Window_tonic(Screen):

        def hiper(self):
            n_hiper = {
              'NaCl': 2, 'KCl': 2, 'CaCl2': 3, 'KI': 2, 'LiCl': 2,
              'glukoza': 1,  'atrop siar': 3,  'NaHCO3': 2}
            n_p = { 'NaCl': 2, 'KCl': 2, 'CaCl2': 3, 'KI': 2, 'LiCl': 2,
              'glukoza': 1,  'atrop siar': 3,  'NaHCO3': 2}
            M_dict = { 'NaCl': 58.44, 'KCl': 74.55, 'CaCl2': 110.98, 'KI': 166, 'LiCl': 42.39,
              'glukoza': 180.156,  'atrop siar': 700,  'NaHCO3': 84}
            if float(self.ids.m.text) > 0:
                if self.ids.nazwa.text in M_dict:
                    n_hiper = n_hiper[self.ids.nazwa.text]
                    M = M_dict[self.ids.nazwa.text]
                    L = M_dict[self.ids.nazwa_tonic.text]
                    p = n_p[self.ids.nazwa_tonic.text]
                    mOsm = float(self.ids.m.text) * 1000 * n_hiper / float(M)
                    x = 320 - mOsm
                    math = str(x * L / (1000 * p))
                    return math
            invalidData()

        def izo(self):
            n_izo = {
              'NaCl': 2, 'KCl': 2, 'CaCl2': 3, 'KI': 2, 'LiCl': 2,
              'glukoza': 1,  'atrop siar': 3,  'NaHCO3': 2}
            n_p = { 'NaCl': 2, 'KCl': 2, 'CaCl2': 3, 'KI': 2, 'LiCl': 2,
              'glukoza': 1,  'atrop siar': 3,  'NaHCO3': 2}
            M_dict = { 'NaCl': 58.44, 'KCl': 74.55, 'CaCl2': 110.98, 'KI': 166, 'LiCl': 42.39,
              'glukoza': 180.156,  'atrop siar': 700,  'NaHCO3': 84}
            if float(self.ids.m.text) > 0:
                if self.ids.nazwa.text in M_dict:
                    n_izo = n_izo[self.ids.nazwa.text]
                    M = M_dict[self.ids.nazwa.text]
                    L = M_dict[self.ids.nazwa_tonic.text]
                    p = n_p[self.ids.nazwa_tonic.text]
                    mOsm = float(self.ids.m.text) * 1000 * n_izo / float(M)
                    x = 300 - mOsm
                    math = str(x * L / (1000 * p))
                    return math
            invalidData()

        def hipo(self):
            n_hipo = {
              'NaCl': 2, 'KCl': 2, 'CaCl2': 3, 'KI': 2, 'LiCl': 2,
              'glukoza': 1,  'atrop siar': 3,  'NaHCO3': 2}
            n_p = { 'NaCl': 2, 'KCl': 2, 'CaCl2': 3, 'KI': 2, 'LiCl': 2,
              'glukoza': 1,  'atrop siar': 3,  'NaHCO3': 2}
            M_dict = { 'NaCl': 58.44, 'KCl': 74.55, 'CaCl2': 110.98, 'KI': 166, 'LiCl': 42.39,
              'glukoza': 180.156,  'atrop siar': 700,  'NaHCO3': 84}
            if float(self.ids.m.text) > 0:
                if self.ids.nazwa.text in M_dict:
                    n_hipo = n_hipo[self.ids.nazwa.text]
                    M = M_dict[self.ids.nazwa.text]
                    L = M_dict[self.ids.nazwa_tonic.text]
                    p = n_p[self.ids.nazwa_tonic.text]
                    mOsm = float(self.ids.m.text) * 1000 * n_hipo / float(M)
                    x = 150 - mOsm
                    math = str(x * L / (1000 * p))
                    return math
            invalidData()

    class Window_ion(Screen):

        def ion(self):
            n_meq = {
              'NaCl': 2, 'KCl': 2, 'CaCl2': 4, 'KI': 2, 'LiCl': 2,
              'glukoza': 0,  'atrop siar': 3,  'NaHCO3': 2}
            n_mmol = { 'NaCl': 2, 'KCl': 2, 'CaCl2': 3, 'KI': 2, 'LiCl': 2,
              'glukoza': 1,  'atrop siar': 3,  'NaHCO3': 2}
            M_dict = { 'NaCl': 58.44, 'KCl': 74.55, 'CaCl2': 110.98, 'KI': 166, 'LiCl': 42.39,
              'glukoza': 180.156,  'atrop siar': 700,  'NaHCO3': 84}
            if float(self.ids.mmol.text):
                if float(self.ids.Cp.text) > 0:
                    if self.ids.nazwa.text in n_meq:
                        n_meq = n_meq[self.ids.nazwa.text]
                        n_mmol = n_mmol[self.ids.nazwa.text]
                        M = M_dict[self.ids.nazwa.text]
                        mEq = float(self.ids.mmol.text) * n_meq
                        m = mEq * M / (1000 * n_mmol)
                        math = str(m * 100 / float(self.ids.Cp.text))
                        return math
            invalidData()


def invalidData():
    pop = Popup(title='Źle wpisane dane', content=Label(text='Źle wpisano dane.'),
      size_hint=(None, None),
      size=(400, 400))
    pop.open()


class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'LightGreen'


MyApp().run()
