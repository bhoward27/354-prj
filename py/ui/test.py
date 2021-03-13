from tkinter import*
import tkinter.font
import random
class MyGUI:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry("960x600+480+100")
        self.main_window.title("Text Setter")
        
        self.sel_frame = Frame(self.main_window)
        self.tot_frame = Frame(self.main_window)
        
        self.sys_fonts = ('Noto Sans Gurmukhi', 'wasy10', 'Noto Sans Display', 'Noto Sans Arabic', 'Noto Serif Bengali', 'Noto Sans Bengali', 'Noto Sans Hebrew', 'Noto Sans Lepcha', 'Lato', 'Noto Serif Devanagari', 'Noto Sans Ogham', 'Lato', 'Piboto', 'DejaVu Math TeX Gyre', 'Noto Sans Buginese', 'OpenSymbol', 'Noto Sans Tai Le', 'Noto Sans Anatolian Hieroglyphs', 'Carlito', 'Noto Naskh Arabic', 'Noto Serif', 'Noto Sans Kayah Li', 'Noto Sans Tai Tham', 'msam10', 'Noto Sans Tifinagh', 'Noto Sans Psalter Pahlavi', 'Noto Serif Malayalam', 'Noto Sans Thaana', 'GentiumAlt', 'Quicksand', 'Linux Libertine Mono O', 'Noto Music', 'Gentium Book Basic', 'Noto Sans Mongolian', 'Noto Sans Sinhala', 'Noto Sans Old South Arabian', 'Quicksand Medium', 'Noto Serif Gurmukhi', 'Noto Sans Brahmi', 'Noto Sans Bengali UI', 'Noto Sans Adlam', 'Noto Sans Chakma', 'Noto Sans Tirhuta', 'Noto Sans Canadian Aboriginal', 'Noto Sans Cherokee', 'Lato', 'Linux Libertine Display O', 'Noto Sans Javanese', 'Noto Serif Thai', 'Noto Sans Lao UI', 'Noto Serif Lao', 'Noto Sans Multani', 'Noto Sans Myanmar UI', 'DejaVu Sans Mono', 'Noto Sans Shavian', 'esint10', 'Noto Sans Oriya UI', 'msbm10', 'Piboto', 'cmr10', 'Noto Sans Mandaic', 'Gentium', 'Noto Sans Kharoshthi', 'Noto Sans Old Persian', 'Noto Sans Tamil UI', 'Noto Sans Old Hungarian', 'PibotoLt', 'Noto Sans Cham', 'Noto Sans Arabic UI', 'Noto Sans Bhaiksuki', 'Noto Sans Thai UI', 'Noto Sans Deseret', 'Noto Sans Runic', 'Noto Serif Kannada', 'Noto Sans Gurmukhi UI', 'Noto Sans Buhid', 'Bitstream Vera Sans', 'Noto Sans Devanagari UI', 'Noto Sans Malayalam UI', 'Noto Serif Tamil Slanted', 'Noto Sans Tai Viet', 'Noto Sans Inscriptional Parthian', 'Lato', 'Bitstream Vera Sans Mono', 'Linux Libertine Initials O', 'FreeSerif', 'Noto Sans Hatran', 'Bitstream Vera Serif', 'Noto Sans Syriac Eastern', 'Noto Sans Telugu UI', 'Noto Sans Tagalog', 'Noto Sans Osage', 'DejaVu Sans', 'Noto Sans Batak', 'Noto Sans Glagolitic', 'stmary10', 'Noto Sans Malayalam', 'Noto Sans Old North Arabian', 'Noto Sans Oriya', 'Quicksand Light', 'Noto Sans Georgian', 'Noto Sans Mahajani', 'DejaVu Sans', 'Noto Sans Telugu', 'DejaVu Serif', 'Noto Sans Linear A', 'Noto Sans Linear B', 'Noto Sans Gothic', 'Noto Sans Lydian', 'Noto Serif Gujarati', 'Noto Sans Tibetan', 'Noto Sans Ol Chiki', 'rsfs10', 'Noto Sans Mono', 'Noto Sans Modi', 'Noto Serif Tibetan', 'Noto Sans Sora Sompeng', 'Noto Sans Meetei Mayek', 'Noto Sans Gujarati UI', 'Noto Sans Cypriot', 'Noto Sans Miao', 'DejaVu Sans', 'Noto Sans Pahawh Hmong', 'Noto Sans Ugaritic', 'Noto Sans Lao', 'cmmi10', 'Lato', 'Noto Sans Marchen', 'Liberation Sans Narrow', 'Liberation Mono', 'Noto Sans Mro', 'Noto Sans PhagsPa', 'Noto Sans Imperial Aramaic', 'Noto Sans Khmer UI', 'Caladea', 'Noto Sans Adlam Unjoined', 'Noto Sans Meroitic', 'Linux Biolinum O', 'Noto Sans Gujarati', 'Noto Sans Egyptian Hieroglyphs', 'Noto Sans Bassa Vah', 'Noto Serif Hebrew', 'Noto Sans Manichaean', 'Noto Sans', 'Droid Sans Fallback', 'Noto Sans Grantha', 'Noto Sans Armenian', 'Noto Serif Balinese', 'Noto Sans Duployan', 'Noto Serif Myanmar', 'Noto Sans Old Italic', 'Lato', 'Noto Sans Lisu', 'Noto Sans Thai', 'Noto Sans Khmer', 'Noto Sans Kaithi', 'Noto Naskh Arabic UI', 'Linux Biolinum Keyboard O', 'Noto Sans Tagbanwa', 'Noto Sans Myanmar', 'Noto Sans Vai', 'Liberation Serif', 'Noto Sans NKo', 'Noto Sans New Tai Lue', 'Noto Serif Georgian', 'Linux Libertine O', 'Noto Sans Syloti Nagri', 'Lato', 'Noto Sans Syriac Western', 'Noto Sans Sinhala UI', 'eufm10', 'Noto Sans Symbols', 'Piboto', 'Noto Sans Samaritan', 'Noto Sans Newa', 'Noto Serif Telugu', 'Noto Sans Carian', 'Liberation Sans', 'Noto Sans Bamum', 'Noto Sans Takri', 'Piboto Condensed', 'Noto Sans Nabataean', 'Noto Sans Avestan', 'Noto Sans Cuneiform', 'FreeSans', 'Noto Sans Kannada', 'cmex10', 'Noto Sans Elbasan', 'Noto Sans Old Turkic', 'Noto Sans Limbu', 'Noto Mono', 'Noto Sans Tamil', 'Noto Sans Sharada', 'Noto Sans Osmanya', 'Inconsolata', 'Noto Sans Palmyrene', 'Noto Serif Ahom', 'Gentium Basic', 'Noto Sans Lycian', 'Noto Sans Yi', 'Noto Kufi Arabic', 'Lato', 'Noto Sans Caucasian Albanian', 'Noto Sans Kannada UI', 'Noto Sans Pau Cin Hau', 'Noto Sans Saurashtra', 'Noto Sans Old Permic', 'Noto Serif Armenian', 'Noto Sans Warang Citi', 'Noto Sans Syriac', 'Noto Serif Sinhala', 'Noto Serif Ethiopic', 'Noto Sans Coptic', 'DejaVu Serif', 'Noto Sans Rejang', 'Noto Sans Devanagari', 'Noto Sans Symbols2', 'Noto Serif Khmer', 'Noto Serif Display', 'Noto Serif Tamil', 'Noto Nastaliq Urdu', 'Noto Sans Ethiopic', 'FreeMono', 'Noto Sans Syriac Estrangela', 'Noto Sans Hanunoo', 'Noto Sans Inscriptional Pahlavi', 'cmsy10', 'Noto Sans Phoenician', 'Noto Sans Sundanese', 'Noto Sans Khudawadi', 'Noto Sans Mende Kikakui')
        self.n_fonts = len(self.sys_fonts)
        self.weight_var = BooleanVar()
#         self.weight_var.set(0)
        self.slant_var = BooleanVar()
#         self.slant_var.set(0)
#         self.under_var = BooleanVar()
#         self.under_var.set(0)
#         self.tir_var = BooleanVar()
        self.tot_str = StringVar()
        self.rand_font = "Arial"
        
        self.font = tkinter.font.Font(family = "eufm10", size = 14)
        
        self.font_choice = IntVar()
        self.font_choice.set(0)
        
        self.textbox = Entry(self.sel_frame, width = 10, textvariable = self.tot_str).pack()
        
        self.type_title = Label(self.sel_frame, text = "Type", font = ("Arial", 14, "bold"))
        self.bold_cb = Checkbutton(self.sel_frame, text = "Bold", variable = self.weight_var, command = self.show_total)
        self.italic_cb = Checkbutton(self.sel_frame, text = "Italic", variable = self.slant_var, command = self.show_total)
        self.size_title = Label(self.sel_frame, text = "Size", font = ("Arial", 14, "bold"))
#         self.under_cb = Checkbutton(self.sel_frame, text = "Underline", variable = self.under_var, command = self.show_total)
        #self.tir_cb = Checkbutton(self.sel_frame, text = "Tire rotation --- $20.00", variable = self.tir_var, command = self.show_total)
        
        self.font_title = Label(self.sel_frame, text = "Font", font = ("Arial", 14, "bold"))
        self.font1_rb = Radiobutton(self.sel_frame, text = "eufm10", variable = self.font_choice, value = 0, command = self.show_total)
        self.font2_rb = Radiobutton(self.sel_frame, text = "msam10", variable = self.font_choice, value = 1, command = self.show_total)
        self.font3_rb = Radiobutton(self.sel_frame, text = "Gentium Basic", variable = self.font_choice, value = 2, command = self.show_total)
        self.rand_rb = Radiobutton(self.sel_frame, text = "Random", variable = self.font_choice, value = 3, command = self.show_total)
        
        self.rand_but = Button(self.sel_frame, text = "Randomize", command = self.randomize)
        
        self.font_title.pack()
        self.font1_rb.pack()
        self.font2_rb.pack()
        self.font3_rb.pack()
        self.rand_rb.pack()
        self.rand_but.pack()
        
#         self.tot_label = Label(self.tot_frame, text = "Total charges = $")
        self.tot_title = Label(self.tot_frame, text = "Output", font = ("Arial", 14, "bold"))
        self.tot_var = Label(self.tot_frame, textvariable = self.tot_str, font = self.font)
        
        self.pos = IntVar()
        self.pos.set(14)
        
        self.slide_frame = Frame(self.main_window)
        self.small = Label(self.slide_frame, text = "small").pack(side = "left")
        
        self.slider = Scale(self.slide_frame, orient = HORIZONTAL, length = 500, from_ = 8, to = 100, variable = self.pos,
                            command = self.do_this).pack(side = "left")
        self.big = Label(self.slide_frame, text = "big").pack(side = "left")
#         self.get_slide = Button(self.tot_frame, text = "Show Slider Value", command = self.do_this)
#         self.get_slide.pack()
        
        self.type_title.pack()
        self.bold_cb.pack()
        self.italic_cb.pack()
        self.size_title.pack()
#         self.under_cb.pack()
        #self.tir_cb.pack()
#         self.tot_label.pack(side = "left")
        self.tot_title.pack()
        self.tot_var.pack()
        
        self.sel_frame.pack()
        self.slide_frame.pack()
        self.tot_frame.pack()
        
        mainloop()
    
    def show_total(self):
#         if self.oil_var.get():
#             oil = 35.0
#         else:
#             oil = 0.0
#             
#         if self.ins_var.get():
#             ins = 50.0
#         else:
#             ins = 0.0
#             
#         if self.muf_var.get():
#             muf = 100.0
#         else:
#             muf = 0.0
#             
#         if self.tir_var.get():
#             tir = 20.0
#         else:
#             tir = 0.0
#             
        
        if self.font_choice.get() == 0:
            if self.weight_var.get() == 0:
                if self.slant_var.get() == 0:
                    self.tot_var.config(font = ("eufm10", self.pos.get(), "normal", "roman"))
                else:
                    self.tot_var.config(font = ("eufm10", self.pos.get(), "normal", "italic"))
            else:
                if self.slant_var.get() == 0:
                    self.tot_var.config(font = ("eufm10", self.pos.get(), "bold", "roman"))
                else:
                    self.tot_var.config(font = ("eufm10", self.pos.get(), "bold", "italic"))
        elif self.font_choice.get() == 1:            
            if self.weight_var.get() == 0:
                if self.slant_var.get() == 0:
                    self.tot_var.config(font = ("masm10", self.pos.get(), "normal", "roman"))
                else:
                    self.tot_var.config(font = ("masm10", self.pos.get(), "normal", "italic"))
            else:
                if self.slant_var.get() == 0:
                    self.tot_var.config(font = ("masm10", self.pos.get(), "bold", "roman"))
                else:
                    self.tot_var.config(font = ("masm10", self.pos.get(), "bold", "italic"))
        elif self.font_choice.get() == 2:
            if self.weight_var.get() == 0:
                if self.slant_var.get() == 0:
                    self.tot_var.config(font = ("Gentium Basic", self.pos.get(), "normal", "roman"))
                else:
                    self.tot_var.config(font = ("Gentium Basic", self.pos.get(), "normal", "italic"))
            else:
                if self.slant_var.get() == 0:
                    self.tot_var.config(font = ("Gentium Basic", self.pos.get(), "bold", "roman"))
                else:
                    self.tot_var.config(font = ("Gentium Basic", self.pos.get(), "bold", "italic"))
        else:
            if self.weight_var.get() == 0:
                if self.slant_var.get() == 0:
                    self.tot_var.config(font = (self.rand_font, self.pos.get(), "normal", "roman"))
                else:
                    self.tot_var.config(font = (self.rand_font, self.pos.get(), "normal", "italic"))
            else:
                if self.slant_var.get() == 0:
                    self.tot_var.config(font = (self.rand_font, self.pos.get(), "bold", "roman"))
                else:
                    self.tot_var.config(font = (self.rand_font, self.pos.get(), "bold", "italic"))
            
#         self.tot_str.set(format(oil + ins + muf + tir, ".2f"))
    
    def do_this(self, val):
        self.show_total()
#         
#         if self.font_choice.get() == 0:
#             self.tot_var.config(font = ("masm10", val))
#         elif self.font_choice.get() == 1:
#             self.tot_var.config(font = ("masm10", val, "bold"))
#         else:
#             self.tot_var.config(font = ("Gentium Basic", val, "italic"))
            
        ##self.tot_str.set(self.textbox.get())

    def randomize(self):
        again = True
        while again:
            rand_font = self.sys_fonts[random.randint(0, self.n_fonts - 1)]
            if " " not in rand_font:
                again = False
# #         self.tot_var.config(font = (rand_font, self.pos.get()))
        if self.weight_var.get() == 0:
            if self.slant_var.get() == 0:
                self.tot_var.config(font = (rand_font, self.pos.get(), "normal", "roman"))
            else:
                self.tot_var.config(font = (rand_font, self.pos.get(), "normal", "italic"))
        else:
            if self.slant_var.get() == 0:
                self.tot_var.config(font = (rand_font, self.pos.get(), "bold", "roman"))
            else:
                self.tot_var.config(font = (rand_font, self.pos.get(), "bold", "italic"))
        self.rand_font = rand_font
        
my_gui = MyGUI()
