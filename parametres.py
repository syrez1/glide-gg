# GENERAL
UNDEFINED = None

# DATABASE
DB_PATH = 'data/glide_db.db'

# TITLE OF GAME
TITLE = 'Glide game'

# FONTS
FONT_DROID = 'font/DroidSansJapanese.ttf'
FONT_ROB_LIGHT = 'font/Roboto-Light.ttf'
FONT_ROB_THIN = 'Roboto-Thin.ttf'

# FONT_SIZE
FONT_TWENTY_SIZE = 20
FONT_THIRTY_SIZE = 30
FONT_FORTY_SIZE = 40
FONT_SIZE_FIFTY = 50
FONT_SIZE_ONE_H_TWENTY = 120
FONT_THIRTY_TWO = 32

# CONST (NAMES BALLS)
RED = 'red'
BLUE = 'blue'
GOL = 'gol'
IZUMRUD = 'izumrud'
# COLORS (RGB)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
BLUE_COLOR = (0, 0, 255)
DEEP_GRAY = (54, 54, 54)
WHITE_COLOR = (255, 255, 255)
RED_TRAIL_COLOR_1 = (255, 55, 0)
RED_TRAIL_COLOR_2 = (255, 85, 55)
RED_TRAIL_COLOR_3 = (255, 40, 40)
BLUE_TRAIL_COLOR_1 = (0, 170, 240)
BLUE_TRAIL_COLOR_2 = (15, 135, 255)
BLUE_TRAIL_COLOR_3 = (0, 190, 255)
DELETE_WALL_TRACE_COLOR = [30, 30, 30]
START_WALL_TRACE_COLOR = [90, 90, 90]
GREEN_COLOR = (0, 200, 100)
COL_STEP_WALL_TRACES = 15
COLOR_LIGHT_SKY = 'lightskyblue3'
COLOR_DODGER_BLUE = 'dodgerblue2'

TURQUOISE_COLOR = (143, 294, 201)
DARK_TURQUOISE_COLOR = (71, 129, 137)
DARK_GREEN = (40, 69, 71)

TURQUOISE_TRACE_COLOR1 = (120, 230, 190)
TURQUOISE_TRACE_COLOR2 = (100, 240, 230)
TURQUOISE_TRACE_COLOR3 = (150, 200, 220)

DARK_GREEN_TRACE_COLOR1 = (86, 157, 167)
DARK_GREEN_TRACE_COLOR2 = (104, 168, 170)
DARK_GREEN_TRACE_COLOR3 = (72, 132, 140)
# NAMES OF IMAGES
ITEM_SHOP = "Items/item_shop1.png"
ICON_IMG = 'icon.jpg'
RED_CIRCLE_IMG = 'circles_skins/red_circle.png'
BLUE_CIRCLE_IMG = 'circles_skins/blue_circle.png'
GOLUB_CIRCLE_IMG = 'circles_skins/goluboi_circle.png'
IZUMRUD_CIRCLE_IMG = 'circles_skins/izumrud_circle.png'
COINS_SHEET = "animation-coins.png"
MENU_IMG = "menu.png"
MOUSE_PNG = 'mouse.png'
PATH_GIF = 'gifs/top_gif_'
# IMAGES FORMATS
PNG = '.png'
GIF = '.gif'
RGBA = 'RGBA'
RGB = 'RGB'
# FOR BACKGROUND
KOSMO_BGD = 'Pictures/bg_kosmo/kosmo'
FIRST_FRAME = 1
LAST_FRAME = 40

# MUSIC LINKS
MENU_MUSIC = '1679007940657971.ogg'
SOUND_COLLUSION = 'Samples/3816133910831170.ogg'
SOUND_CLICK = 'Samples/zapsplat_multimedia_button_click_005_68777.mp3'
SAME_LINK_FOR_QUOTES = 'Quotes/quote'
PATH_FOR_CREATE_QUOTES = 'Music/Quotes/quote'
PATH_FOR_SOUND_IN_LEVELS = 'Music/Music for levels/'
SOUND_RESTART = 'Samples/8476647490550829.ogg'
PATH_MUSIC = 'Music/'

# MUSIC PARAMETRES
USING_VOLUME = 0.2
FORMAT_OGG = '.ogg'
INFINITY_PLAYBACK = -1

# PARSE LINKS
URL_FOR_QUOTE = 'https://api.quotable.io/random'
GET_QUOTE = 'content'

# LANGUAGE FOR TRANSLATE
RU = 'ru'
EN = 'en'

# DELAY VAlUES
DELAY_THREE_OO = 300
# CONSTS FOR SCREEN
SIZE = WIDTH, HEIGHT = 600, 800
START_OF_SCREEN = (0, 0)
FPS_SIXTY = 60
FPS_FIFTEEN = 15
NOT_UPDATE_Y_CORD_1 = -400
NOT_UPDATE_Y_CORD_2 = 1000
DODGE_Y_CORD = 600
ONE_PIX = 1

# CONSTS FOR MAKE IMG TRANSPARENT
SPECIAL_VALUE = -1

# CONSTS FOR CIRCLE TRACES
ANGLE_PI = 180
START_TRACE_RADIUS = 5
QUANTITY_TRACE_CIRCLES = 50
RADIUS_FOR_DELETE_TRACE = 0
NUM_FOR_DECREASE_RADIUS = 50
DECREASE_TRACE_RADIUS = 1
CONNECT_CIRCLE_WTH_TRC = 10
IMPOSSIBLE_SPEED = 0
MAX_TRACE_SPEED_X = 2
MIN_TRACE_SPEED_X = -2
MAX_TRACE_SPEED_Y = 0
MIN_TRACE_SPEED_Y = -10
TER_VER_DECR_R_MIN = 0
TER_VER_FOR_DECR_MAX = 100

# CONSTS FOR MOVEMENT CIRCLES
SPEED_MOVEMENT_TRUE = 5
SPEED_MOVEMENT_FALSE = -5
CONVERT_ANGLE_TO_SIDE = 100

# CONSTS FOR GRAY CIRCLE (along which the circles rotate)
GRAY_CIRCLE_POSITION = (300, 600)
GRAY_CIRCLE_RADIUS = 100
GRAY_CIRCLE_WIDTH = 1

# CONSTS FOR RED CIRCLE
RED_CIRCLE_START_ANGLE = 0
RED_CIRCLE_START_X = 385
RED_CIRCLE_START_Y = 585

# CONSTS FOR BLUE CIRCLE
BLUE_CIRCLE_START_ANGLE = 180
BLUE_CIRCLE_START_X = 185
BLUE_CIRCLE_START_Y = 585

# SAME CONSTS FOR CIRCLES
CHANGE_X_COORD = HEIGHT // 2 - 115
CHANGE_Y_COORD = HEIGHT - 215

# INDEXES FOR ALL OBSTACLES
INX_IMG_NAME = 0
INX_X_POS = 1
INX_Y_POS = 2
INX_X_SPEED = 3
INX_Y_SPEED = 4

# INDEXES FOR SLOWER TWIST OBSTACLE
INX_STEP_ANG_TWIST = 5
INX_BASE_ANG_TWIST = 6

# INDEXES FOR SLIDE SIDE AND LF_DOWN OBSTACLE
INX_STATIC_ANGLE = 5
BASE_X_MOVE = 0
BASE_Y_MOVE = 0
BASE_ANGLE_MOVE = 0

# INDEXES FOR SLIDE SIDE OBSTACLE
INX_Y_START_SIDE = 6
INX_Y_END_SIDE = 7
INX_STEP_SPEED_SIDE = 8

# INDEXES FOR LEFT RIGHT AND DOWN MOVING OBSTACLE
INX_Y_START_DOWN = 6
INX_Y_END_DOWN = 7
INX_STEP_SPEED_DOWN = 8
INX_LEFT_BOARD_LF = 9
INX_RIGHT_BOARD_LF = 10
INX_STEP_SPEED_LF = 11

# ARGS OF FRAMES FOR LEFT RIGHT MOVING
SIXTY_FRAMES = 60
LIMIT_FRAME = 20
ZERO_FRAMES = 0
STEP_FRAME = 1

# CHECK LEVEL COMPLETE
MAX_RECT_Y_IN_LEVEL = 800

# VALUES FOR DATABASE
USERS = 'Users'
IMAGES = 'Images'
LEVELS = 'Levels'
LF_DOWN_OBSTACLES = 'LfDownObstacles'
SIDE_OBSTACLES = 'SideObstacles'
TWIST_OBSTACLES = 'TwistObstacles'
ITEM_SHOP_DB = 'ITEM_SHOP'
AVAILABILITY = 'availability'

# Speed multipliers for the Race level
INF_SPEED_MUL = 1.5

ID = 'id'
NAME = 'name'

ID_LEVEL = 'id_level'
ID_IMAGE = 'id_image'
X_POS = 'x_pos'
Y_POS = 'y_pos'
X_SPEED = 'x_speed'
Y_SPEED = 'y_speed'

Y_START_DOWN = 'y_start_down'
Y_END_DOWN = 'y_end_down'
SPEED_STEP_DOWN = 'speed_step_down'
LEFT_BOARD_LF = 'left_board_lf'
RIGHT_BOARD_LF = 'right_board_lf'
SPEED_STEP_LF = 'speed_step_lf'

ANGLE_STATIC = 'angle_static'
Y_START_SIDE = 'y_start_side'
Y_END_SIDE = 'y_end_side'
SPEED_STEP_SIDE = 'speed_step_side'

ANGLE_STEP = 'angle_step'
ANGLE_MOVE = 'angle_move'

MUS_LEVEL = 'music level'
SPEED = 'speed'
COINS = 'coins'
COINS_AMOUNT = 'coins_amount'

SETTINGS = 'settings'
EFFECTS = 'effects'
MUSIC = 'music'
MUSIC_LEVEL = 'music_level'
VOICE = 'voice'
SOUND_EFFECTS = 'sound_effects'
PICTURES = 'pictures/'
INF_LEVELS = 'Infinity_level_scores'
SCORE = 'score'
NAME_PLAYER = 'name_player'
LOCKERS_DB = 'LOCKER'

TABLES = {
    IMAGES: [ID,
             NAME],
    USERS: [ID, COINS_AMOUNT],
    LEVELS: [ID, MUS_LEVEL, SPEED, COINS],

    LF_DOWN_OBSTACLES: [ID_LEVEL, ID_IMAGE,
                        X_POS, Y_POS,
                        X_SPEED, Y_SPEED, ANGLE_STATIC,
                        Y_START_DOWN,
                        Y_END_DOWN,
                        SPEED_STEP_DOWN,
                        LEFT_BOARD_LF,
                        RIGHT_BOARD_LF,
                        SPEED_STEP_LF],

    SIDE_OBSTACLES: [ID_LEVEL, ID_IMAGE,
                     X_POS, Y_POS,
                     X_SPEED, Y_SPEED,
                     ANGLE_STATIC,
                     Y_START_SIDE,
                     Y_END_SIDE,
                     SPEED_STEP_SIDE],

    TWIST_OBSTACLES: [ID_LEVEL, ID_IMAGE,
                      X_POS, Y_POS,
                      X_SPEED, Y_SPEED,
                      ANGLE_STEP,
                      ANGLE_MOVE]

}

SELECT_ALL = '*'

# INDEXES FOR GET LEVEL'S OBSTACLES
INX_ID_LEVEL = 0
HIDDEN_OBSTACLE = True
INX_IMG_ID = 1

# INDEXES FOR CREATING WALLS
INX_INVIZ = 0
INX_INFO_ARRAY = 1
BASE_STATIC_ANGLE = 0

# LEVELS
ZERO_COINS = 0

ALL_LEVELS = []
for i in range(1, 7):
    for j in range(1, 7):
        ALL_LEVELS.append(int(str(i) + str(j)))

MAX_LEVEL = 60
INCREASE_LEVELS = 1
# MESSAGES
LEVEL_COMPLITED = '?????????????? ??????????????!'
PAUSE_ACTIONS = '??????????, ?????????????? Enter, ??????????'
BANK_MESSAGE = '???? ??????????????????:'
COIN_MESSAGE = '??????????'
DODGED_MESS = 'Dodged:'
TITLE = 'GLIDE'
PLOT_TITLE = '??????????'
IGNORANCE_TITLE = '????????????????'
DENIAL_TITLE = '??????????????????'
ANGER_TITLE = '????????'
CONVERSATION_TITLE = '????????????????????'
HOPE_TITLE = '??????????????'
ACCEPTANCE_TITLE = '????????????????'
LEFT_KEY_NAME = 'LEFT'
RIGHT_KEY_NAME = 'RIGHT'
MANAGEMENT_TITLE = '????????????????????'
EFFECTS_TITLE = '??????????????'
RIGHT_TITLE = '????????????'
LEFT_TITLE = '??????????'
ITEM_SHOP_TITLE = '?????????????? ????????????'
MUSIC_SETTINGS = '???????????? - '
VOICE_SETTINGS = '???????? - '
SOUND_EFF_SETTINGS = '???????????????? ?????????????? - '
MESSAGE_BEFORE_START_GAME = f'?????????????? ???????? ??????, ?????????? ???????????? ????????'
ERROR_NAME_IS_EMPTY = '?????? ???? ????????????'
TOP_PLAYER = '?????? ??????????(??????????????????): '
BALANCE_TEXT = '????????????: '
LOCKER_TEXT = '??????????????'
ITEM_SHOP_TEXT = '?????????????? ????????????'
LEVEL_TEXT = '??????????????: '
PLOT_TEXT = '??????????: '
ITEM_NAME_TEXT = '???????????????? ????????????????????:'
ITEM_PRICE_TEXT = '??????????????????:'
LIVES_TEXT = 'Lives:'
SPEED_TEXT = 'Speed:'
CHANGE_EQUIP_TEXT = '???????????????????? ???????????????????? ?????????? ???????????????????? ?? ????????'
# BUTTONS SIZE
BTN_RESUME_X = 150
BTN_RESUME_Y = 50
BTN_LEAVE_HUB_X = 150
BTN_LEAVE_HUB_Y = 50
BTN_LEVELS_X = 50
BTN_LEVELS_Y = 50
BTN_PAUSE_RECT = 30

# BUTTONS TEXT
BTN_CONTINUE_TEXT = '????????????????????'
BTN_LEAVE_TEXT = '??????????'
PAUSE_BTN_TEXT = 'II'
BTN_SOUND_TEXT = '????????'
BTN_BACK_TEXT = '??????????'
BTN_ON_TEXT = '??????'
BTN_OFF_TEXT = '????????'
BTN_NEXT_PAGE_TEXT = '?????????????????? ????????????????'
BTN_SETTINGS_TEXT = '??????????????????'
BTN_PLAY_TEXT = '????????????'
BTN_ITEM_SHOP_TEXT = '?????????????? ????????????'
BTN_RACE_TEXT = '??????????'
BTN_PLOT_TEXT = '??????????'
BTN_START_RACE = '???????????? ??????????'
BTN_LOCKER_TEXT = '??????????????'
BTN_BUY_EQUIPMENT = '???????????? ????????????????????'
BTN_PURCHASED_TEXT = '??????????????'
SELECT_ITEM = '??????????????'
SELECTED_ITEM = '??????????????'
BTN_MAIN_MENU_TEXT = '?????????????? ????????'

# BUTTONS LEVELS
BTN_FIRST_LEVEL = ' I '
BTN_SECOND_LEVEL = 'II'
BTN_THIRD_LEVEL = 'III'
BTN_FOURTH_LEVEL = 'IV'
BTN_FIFTH_LEVEL = 'V'
BTN_SIXTH_LEVEL = 'VI'

# CONSTS FOR RENDER BORDERS
PADDING_DIST = 20
BORDER_WIDTH = 4
BORDER_LENGTH = 8

INFINITY_LEVEL_ID = 1
INFINITY_LEVEL_LIVES = 3

# CONSTS FOR BUTTONS
CLICK_TRUE = 1
INCREASE_FOR_BUTTONS = 10

# CONSTS FOR GET VALUES
GET_ZERO_VALUES = 0
GET_FIRST_VALUES = 1
GET_SEC_VALUE = 2
GET_THIRD_VALUE = 3
GET_FOURTH_VALUE = 4
# CONSTS FOR COIN ANIMATION
INCREASE_FRAME = 1
FRAME_X = 0
FRAME_Y = 0

# CONST FOR COLORS BALLS
AVAILABILITY_TRUE = 1
ID_ITEM_FIRST = 1
ID_ITEM_SEC = 2

# FOR WALLS
MAX_WALLS_Y = -350
SPEED_CHANGING = 1.5
NUM_TO_DEL_TRACE = 1

# FOR GIFS
CHANGE_FRAME_GIF = 1
MIN_RANDOM_GIF = 1
MAX_RANDOM_GIF = 5
ZEROING_FRAMES = 0
COUNT_FRAMES = 4
CUT_LAST_FRAME = -1
CUT_FIRST_FRAME = 1
# CONSTS FOR QUOTES
PLAY_EVERY_TEN_TIMES = 10
CHECK_PLAY_QUOTE = 0
ZEROING_QUOTES = 0

# CONSTS FOR INPUT_BOX
MAX_LEN_INPUT = 200
INCREASE_BOX = 10
INCREASE_BOX_X = 5
INCREASE_BOX_Y = 5

# CONST_FOR_EQUIP
FIRST_ITEM = 1
SEC_ITEM = 2

# CHECK BALANCE
BALANCE_MIN = 0

# CONSTS FOR MENU

INCREASE_ITEMS_X1 = 200
INCREASE_ITEMS_Y1 = 200
INCREASE_ITEMS_X2 = 300
INCREASE_ITEMS_Y2 = 300
GAP = 50

CLICK_SIZE = [10, 12, 16, 20, 28, 34, 40, 45, 48, 54, 58]