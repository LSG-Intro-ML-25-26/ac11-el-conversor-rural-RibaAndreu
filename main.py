@namespace
class SpriteKind:
    trading = SpriteKind.create()
    menu_ui = SpriteKind.create()
"""
"""
#botiga
def obrir_botiga():
    global bucle_botiga, troncos
    steve.say("")
    scene.set_background_color(7)
    game.show_long_text("Hola veí! Vols fer un canvi?", DialogLayout.BOTTOM)
    bucle_botiga = True
    while bucle_botiga:
        llista = "MERCAT D'ALCUBILLA:" + "\n" + "1. Gallina (6)" + "\n" + "2. Patata 1.5kg (2)" + "\n" + "3. Cabra (5)" + "\n" + "4. Ous 12u (3)" + "\n" + "5. Cavall (12)" + "\n" + "6. SORTIR"
        game.show_long_text(llista, DialogLayout.CENTER)
        opcio = game.ask_for_number("Tria (1-6):", 1)
        if opcio == 6:
            bucle_botiga = False
        elif opcio >= 1 and opcio <= 5:
            idx = opcio - 1
            missatge_q = "Quantes unitats de " + product_names[idx] + "?"
            q = game.ask_for_number(missatge_q, 1)
            cost = calcular_conversi_llenya(idx, q)
            if cost == -1:
                game.show_long_text("Error: Quantitat no valida", DialogLayout.BOTTOM)
            elif cost == -2:
                game.show_long_text("Error: Només unitats senceres", DialogLayout.BOTTOM)
            else:
                game.show_long_text("Aixo et costara " + ("" + str(cost)) + " troncs",
                    DialogLayout.BOTTOM)
                if troncos >= cost:
                    troncos = troncos - cost
                    info.set_score(troncos)
                    music.ba_ding.play()
                    game.show_long_text("Fet!", DialogLayout.BOTTOM)
                else:
                    music.play(music.melody_playable(music.thump),
                        music.PlaybackMode.UNTIL_DONE)
                    game.show_long_text("No tens prou llenya!", DialogLayout.BOTTOM)
        else:
            game.show_long_text("Opció no vàlida", DialogLayout.BOTTOM)
    scene.set_background_image(assets.image("""
        fons
        """))
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


def on_on_overlap(sprite, other):
    global in_trading
    if joc_iniciat and not bucle_botiga:
        in_trading = True
        steve.say("A: Botiga", 100)
sprites.on_overlap(SpriteKind.player, SpriteKind.trading, on_on_overlap)


def on_a_pressed():
    if not (joc_iniciat):
        iniciar_partida()
    elif in_trading:
        obrir_botiga()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# menú inicial
def mostrar_menu_inicial():
    global img_menu, targeta_menu
    img_menu = image.create(160, 90)
    img_menu.fill(1)
    img_menu.print("EL CONVERSOR RURAL", 25, 15, 15)
    img_menu.print("--------------------------", 10, 30, 15)
    img_menu.print("Recull la llenya", 35, 55, 15)
    img_menu.print("PREM A PER JUGAR", 30, 75, 15)
    targeta_menu = sprites.create(img_menu, SpriteKind.menu_ui)
    targeta_menu.set_position(80, 60)
    targeta_menu.z = 200
def iniciar_partida():
    global joc_iniciat, steve, trade, arbol, arbol2, arbol3, pez, icono
    joc_iniciat = True
    targeta_menu.destroy()
    scene.set_background_image(assets.image("""
        fons
        """))
    steve = sprites.create(assets.image("""
        pers
        """), SpriteKind.player)
    steve.set_stay_in_screen(True)
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
    pez = sprites.create(assets.image("""
        mmcd
        """), SpriteKind.enemy)
    arbol3.set_position(116, 36)
    arbol2.set_position(140, 90)
    arbol.set_position(80, 75)
    trade.set_position(25, 82)
    pez.set_position(21, 14)
    icono = sprites.create(assets.image("""
        llenya
        """), SpriteKind.food)
    icono.set_position(150, 10)
    icono.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
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

# càlcul
def calcular_conversi_llenya(id_prod: number, unitats: number):
    global preu_unitari, resultat
    if unitats <= 0:
        return -1
    if unitats % 1 != 0:
        return -2
    preu_unitari = product_values[id_prod]
    resultat = preu_unitari * unitats
    return Math.round_with_precision(resultat, 2)
temps_parat = 0
preu_unitari = 0
icono: Sprite = None
pez: Sprite = None
arbol3: Sprite = None
arbol2: Sprite = None
arbol: Sprite = None
trade: Sprite = None
targeta_menu: Sprite = None
in_trading = False
joc_iniciat = False
troncos = 0
bucle_botiga = False
steve: Sprite = None
product_values: List[number] = []
product_names: List[str] = []
resultat = 0
img_menu: Image = None
product_names = ["Gallina",
    "Patata (Pack 1.5kg)",
    "Cabra",
    "Ous (12u)",
    "Cavall"]
product_values = [6, 2, 5, 3, 12]
mostrar_menu_inicial()

def on_on_update():
    global temps_parat, troncos, in_trading
    if joc_iniciat and steve:
        quiet = steve.vx == 0 and steve.vy == 0
        a_l_arbre = steve.overlaps_with(arbol) or steve.overlaps_with(arbol2) or steve.overlaps_with(arbol3)
        if quiet and a_l_arbre:
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