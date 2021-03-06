import gaming_cycle
from general_functions import print_text
from menu_files.menu_page import MenuPage
from db_functions import *
import pygame as pg
from input_box import InputBox

pg.init()


class BeforeInfinityLevel(MenuPage):
    # CORDS INPUT BOX
    player_name_input = InputBox(20, 200, 140, 35)
    show_name_error = False
    top_score = select_top_score()

    def render_extra(self, screen):
        print_text(screen, TOP_PLAYER, x=10, y=50, font_size=FONT_FORTY_SIZE, font_color=WHITE_COLOR,
                   font_type=FONT_ROB_THIN)
        print_text(screen, f'{self.top_score[0]}  {self.top_score[1]}', x=350, y=50, font_size=FONT_FORTY_SIZE,
                   font_color=DEEP_GRAY, font_type=FONT_ROB_THIN)

        print_text(screen, MESSAGE_BEFORE_START_GAME, x=20, y=130, font_size=FONT_FORTY_SIZE, font_color=DEEP_GRAY,
                   font_type=FONT_ROB_THIN)
        self.player_name_input.update()
        self.player_name_input.draw(screen)

        if self.show_name_error:
            print_text(screen, ERROR_NAME_IS_EMPTY, 20, 250, FONT_THIRTY_SIZE, RED_COLOR,
                       font_type=FONT_ROB_THIN)

    def extra_event_handler(self, event):
        self.player_name_input.handle_event(event)

    def check_name(self):
        player_name = self.player_name_input.text.strip()
        if len(player_name) > 0:
            gaming_cycle.infinity_cycle(player_name)
        else:
            self.show_name_error = True

    def check_name(self):
        player_name = self.player_name_input.text.strip()
        if len(player_name) > 0:
            gaming_cycle.infinity_cycle(player_name)
        else:
            self.show_name_error = True
