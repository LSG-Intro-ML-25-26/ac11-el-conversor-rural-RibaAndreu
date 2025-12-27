@namespace
class SpriteKind:
    trading = SpriteKind.create()

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
        pass
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
def jugador_quieto():
    return steve.vx == 0 and steve.vy == 0

def on_up_pressed():
    animation.run_image_animation(steve,
        assets.animation("""
            nena-animation-up
            """),
        500,
        False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def esta_sobre_arbol():
    return steve.overlaps_with(arbol) or steve.overlaps_with(arbol2) or steve.overlaps_with(arbol3)
troncos = 0
temps_parat = 0
arbres = 0
index = 0
in_trading = False
arbol3: Sprite = None
arbol2: Sprite = None
arbol: Sprite = None
steve: Sprite = None
product_values: List[number] = []
product_names = ["Gallina",
    "Patates (1.5 kg)",
    "Cabra",
    "Dotzena d'ous",
    "Cavall"]
product_values = [6, 2, 5, 3, 12]
scene.set_background_image(assets.image("""
    fons
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
arbol3.set_position(116, 36)
arbol2.set_position(144, 90)
arbol.set_position(80, 75)
trade.set_position(25, 82)
controller.move_sprite(steve, 100, 100)
icono_llenya = sprites.create(assets.image("""
    llenya
    """), SpriteKind.food)
icono_llenya.set_position(150, 10)
icono_llenya.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_score(0)

def on_on_update():
    global temps_parat, troncos
    if esta_sobre_arbol() and jugador_quieto():
        temps_parat += 1
        if temps_parat >= 120:
            # ~3 segons parat al costat de l'arbre
            troncos += 1
            info.set_score(troncos)
            temps_parat = 0
    else:
        temps_parat = 0
game.on_update(on_on_update)
