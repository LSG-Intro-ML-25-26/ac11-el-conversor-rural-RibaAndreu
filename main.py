@namespace
class SpriteKind:
    trading = SpriteKind.create()
    menu_ui = SpriteKind.create()

def on_on_overlap(player2, house):
    global in_trading
    if joc_iniciat:
        in_trading = True
        steve.say("A: Botiga", 100)
sprites.on_overlap(SpriteKind.player, SpriteKind.trading, on_on_overlap)

def obrir_botiga():
    global i, opcio, idx, troncos
    steve.say("")
    llista = "BOTIGA (Preus):\n"
    while i < len(product_names):
        llista = "" + llista + "" + ("" + str((i + 1))) + ". " + product_names[i] + " (" + ("" + str(product_values[i])) + ")\n"
        i += 1
    game.show_long_text(llista, DialogLayout.CENTER)
    opcio = game.ask_for_number("Quin producte vols? (1-5)", 1)
    idx = opcio - 1
    if idx >= 0 and idx < len(product_names):
        quantitat = game.ask_for_number("Quantes unitats de " + product_names[idx] + "?", 1)
        if quantitat > 0:
            preu_total = product_values[idx] * quantitat
            if troncos >= preu_total:
                troncos += 0 - preu_total
                info.set_score(troncos)
                music.ba_ding.play()
                game.show_long_text("Has comprat " + ("" + str(quantitat)) + " " + product_names[idx],
                    DialogLayout.BOTTOM)
            else:
                game.show_long_text("No tens prou llenya! Falten " + ("" + str((preu_total - troncos))),
                    DialogLayout.BOTTOM)
    else:
        game.show_long_text("Opció no vàlida", DialogLayout.BOTTOM)
    steve.say("")

def on_down_pressed():
    if joc_iniciat:
        animation.run_image_animation(steve,
            assets.animation("""
                nena-animation-down
                """),
            500,
            False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_right_pressed():
    if joc_iniciat:
        animation.run_image_animation(steve,
            assets.animation("""
                nena-animation-right
                """),
            500,
            False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    if joc_iniciat:
        animation.run_image_animation(steve,
            assets.animation("""
                nena-animation-left
                """),
            500,
            False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_a_pressed():
    if not (joc_iniciat):
        iniciar_partida()
    elif in_trading:
        obrir_botiga()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def mostrar_menu_inicial():
    global fons_blanc, targeta_menu
    fons_blanc = image.create(140, 90)
    fons_blanc.fill(1)
    fons_blanc.print("LA GRANJA DE SORIA", 15, 15, 15)
    fons_blanc.print("-----------------", 15, 30, 15)
    fons_blanc.print("Mou-te amb fletxes", 15, 50, 15)
    fons_blanc.print("PREM A PER JUGAR", 20, 70, 15)
    targeta_menu = sprites.create(fons_blanc, SpriteKind.menu_ui)
    targeta_menu.set_position(80, 60)
    targeta_menu.z = 200
def iniciar_partida():
    global joc_iniciat, steve, trade, arbol, arbol2, arbol3, icono_llenya
    joc_iniciat = True
    targeta_menu.destroy()
    scene.set_background_image(assets.image("""
        fons
        """))
    steve = sprites.create(assets.image("""
        pers
        """), SpriteKind.player)
    steve.set_stay_in_screen(True)
    steve.z = 100
    controller.move_sprite(steve, 100, 100)
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
    arbol2.set_position(140, 90)
    arbol.set_position(80, 75)
    trade.set_position(25, 82)
    icono_llenya = sprites.create(assets.image("""
        llenya
        """), SpriteKind.food)
    icono_llenya.set_position(150, 10)
    icono_llenya.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    info.set_score(0)

def on_up_pressed():
    if joc_iniciat:
        animation.run_image_animation(steve,
            assets.animation("""
                nena-animation-up
                """),
            500,
            False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

temps_parat = 0
icono_llenya: Sprite = None
arbol3: Sprite = None
arbol2: Sprite = None
arbol: Sprite = None
trade: Sprite = None
targeta_menu: Sprite = None
troncos = 0
idx = 0
opcio = 0
i = 0
steve: Sprite = None
in_trading = False
joc_iniciat = False
product_values: List[number] = []
product_names: List[str] = []
fons_blanc: Image = None
product_names = ["Gallina", "Patates", "Cabra", "Ous", "Cavall"]
product_values = [6, 2, 5, 3, 12]
mostrar_menu_inicial()

def on_on_update():
    global temps_parat, troncos, in_trading
    if joc_iniciat and steve:
        if (steve.overlaps_with(arbol) or steve.overlaps_with(arbol2) or steve.overlaps_with(arbol3)) and steve.vx == 0 and steve.vy == 0:
            temps_parat += 1
            if temps_parat >= 120:
                troncos += 1
                info.set_score(troncos)
                temps_parat = 0
        else:
            temps_parat = 0
        if not (steve.overlaps_with(trade)):
            in_trading = False
            steve.say("")
game.on_update(on_on_update)
