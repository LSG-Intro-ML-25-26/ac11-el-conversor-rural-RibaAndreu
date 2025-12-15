@namespace
class SpriteKind:
    trading = SpriteKind.create()
"""

---------- VARIABLES ----------

"""

def on_on_overlap(player2, house):
    global in_trading
    in_trading = True
    game.show_long_text("Prem A per comerciar", DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.player, SpriteKind.trading, on_on_overlap)


def on_down_pressed():
    animation.run_image_animation(steve,
        assets.animation("""
            nena-animation-down
            """),
        500,
        False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def abrir_inventario():
    global opcio2, quantitat2, resultat
    opcio2 = Math.floor(game.ask_for_number("""
        BOTIGA
        1 Gallina
        2 Patates
        3 Cabra
        4 Ous
        5 Cavall
        Escull opcio:
        """))
    quantitat2 = Math.floor(game.ask_for_number("Quantes unitats vols?"))
    resultat = calcular_arbres(opcio2, quantitat2)
    if resultat == -1:
        game.show_long_text("Opcio incorrecta", DialogLayout.BOTTOM)
    elif resultat == -2:
        game.show_long_text("""
                Quantitat incorrecta
                (Solo enters positius)
                """,
            DialogLayout.BOTTOM)
    else:
        producte = product_names[opcio2 - 1]
        game.show_long_text("" + str(quantitat2) + " " + producte + "\nnecessiten\n" + ("" + str(resultat)) + " arbres",
            DialogLayout.FULL)

def on_right_pressed():
    animation.run_image_animation(steve,
        assets.animation("""
            nena-animation-right
            """),
        500,
        False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    animation.run_image_animation(steve,
        assets.animation("""
            nena-animation-left
            """),
        500,
        False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)


def on_a_pressed():
    if in_trading:
        abrir_inventario()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_b_pressed():
    global in_trading
    in_trading = False
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def calcular_arbres(opcio: number, quantitat: number):
    global index, arbres
    index = opcio - 1
    if index < 0 or index >= len(product_values):
        return -1
    if quantitat <= 0 or quantitat != Math.floor(quantitat):
        return -2
    arbres = product_values[index] * quantitat
    return Math.round(arbres * 100) / 100

def on_up_pressed():
    animation.run_image_animation(steve,
        assets.animation("""
            nena-animation-up
            """),
        500,
        False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

arbres = 0
index = 0
resultat = 0
quantitat2 = 0
opcio2 = 0
in_trading = False
steve: Sprite = None
product_values: List[number] = []
product_names: List[str] = []
product_names = ["Gallina",
    "Patates (1.5 kg)",
    "Cabra",
    "Dotzena d'ous",
    "Cavall"]
product_values = [6, 2, 5, 3, 12]

scene.set_background_image(assets.image("""
    background
    """))
steve = sprites.create(assets.image("""
    pers
    """), SpriteKind.player)
trade = sprites.create(assets.image("""
    trade
    """), SpriteKind.trading)
arbol = sprites.create(assets.image("""
    arbol
    """), SpriteKind.enemy)
arbol2 = sprites.create(assets.image("""
    arbol
    """), SpriteKind.enemy)
arbol3 = sprites.create(assets.image("""
    arbol
    """), SpriteKind.enemy)
arbol3.set_position(144, 82)
arbol2.set_position(112, 82)
arbol.set_position(80, 82)
trade.set_position(25, 82)
controller.move_sprite(steve, 100, 100)