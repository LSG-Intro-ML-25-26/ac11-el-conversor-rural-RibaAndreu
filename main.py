@namespace
class SpriteKind:
    trading = SpriteKind.create()
    menu_ui = SpriteKind.create()

# --- VARIABLES GLOBALS ---
joc_iniciat = False
in_trading = False
troncos = 0
temps_parat = 0
bucle_botiga = False

# Noms dels productes
product_names = ["Gallina", "Patata (Pack 1.5kg)", "Cabra", "Ous (12u)", "Cavall"]
# Valors en TRONCOS: La patata ara val 2 troncos per cada unitat (que són 1.5kg)
product_values = [6, 2, 5, 3, 12]

# --- SPRITES ---
steve: Sprite = None
trade: Sprite = None
arbol: Sprite = None
arbol2: Sprite = None
arbol3: Sprite = None
targeta_menu: Sprite = None

# --- MÈTODE DE CÀLCUL (Encapsulat) ---
def calcular_conversi_llenya(id_prod: number, unitats: number):
    if unitats <= 0:
        return -1
    
    # Validació d'animals i packs sencers (No venem mig cavall ni mig pack de patates)
    if unitats % 1 != 0:
        return -2
            
    preu_unitari = product_values[id_prod]
    resultat = preu_unitari * unitats
    return Math.round_with_precision(resultat, 2)

# --- BOTIGA ---
def obrir_botiga():
    global troncos, bucle_botiga
    steve.say("")
    game.show_long_text("Hola veí! Vols fer un canvi?", DialogLayout.BOTTOM)
    bucle_botiga = True
    
    while bucle_botiga:
        # Menú on s'explica que la patata va a 2 troncos el pack
        llista = "MERCAT D'ALCUBILLA:" + "\n" + "1. Gallina (6)" + "\n" + "2. Patata 1.5kg (2)" + "\n" + "3. Cabra (5)" + "\n" + "4. Ous 12u (3)" + "\n" + "5. Cavall (12)" + "\n" + "6. SORTIR"
        
        game.show_long_text(llista, DialogLayout.CENTER)
        opcio = game.ask_for_number("Tria (1-6):", 1)
        
        if opcio == 6:
            bucle_botiga = False
        elif opcio >= 1 and opcio <= 5:
            idx = opcio - 1
            # Preguntem quantes unitats o packs vol
            missatge_q = "Quantes unitats de " + product_names[idx] + "?"
            q = game.ask_for_number(missatge_q, 1)
            
            cost = calcular_conversi_llenya(idx, q)
            
            if cost == -1:
                game.show_long_text("Error: Quantitat no vàlida", DialogLayout.BOTTOM)
            elif cost == -2:
                game.show_long_text("Error: Només unitats senceres", DialogLayout.BOTTOM)
            else:
                game.show_long_text("Això et costarà " + str(cost) + " kg de llenya", DialogLayout.BOTTOM)
                
                if troncos >= cost:
                    troncos = troncos - cost
                    info.set_score(troncos)
                    music.ba_ding.play()
                    game.show_long_text("Gràcies! Aquí tens el teu producte.", DialogLayout.BOTTOM)
                else:
                    music.play(music.melody_playable(music.thump), music.PlaybackMode.UNTIL_DONE)
                    game.show_long_text("No tens prou llenya!", DialogLayout.BOTTOM)
        else:
            game.show_long_text("Opció no vàlida", DialogLayout.BOTTOM)
    steve.say("")

# --- PANTALLA INICIAL ---
def mostrar_menu_inicial():
    global targeta_menu
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
    global joc_iniciat, steve, trade, arbol, arbol2, arbol3
    joc_iniciat = True
    targeta_menu.destroy()
    scene.set_background_image(assets.image("fons"))
    
    steve = sprites.create(assets.image("pers"), SpriteKind.player)
    steve.set_stay_in_screen(True)
    controller.move_sprite(steve, 100, 100)
    
    trade = sprites.create(assets.image("trade"), SpriteKind.trading)
    arbol = sprites.create(assets.image("arbol"), SpriteKind.enemy)
    arbol2 = sprites.create(assets.image("arbol"), SpriteKind.enemy)
    arbol3 = sprites.create(assets.image("arbol"), SpriteKind.enemy)
    
    arbol3.set_position(116, 36)
    arbol2.set_position(140, 90)
    arbol.set_position(80, 75)
    trade.set_position(25, 82)
    
    icono = sprites.create(assets.image("llenya"), SpriteKind.food)
    icono.set_position(150, 10)
    icono.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    info.set_score(0)

# --- CONTROLS ---
def on_a_pressed():
    if joc_iniciat == False:
        iniciar_partida()
    elif in_trading == True:
        obrir_botiga()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# Animacions de moviment
def on_up():
    if joc_iniciat:
        animation.run_image_animation(steve, assets.animation("nena-animation-up"), 500, False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up)
def on_down():
    if joc_iniciat:
        animation.run_image_animation(steve, assets.animation("nena-animation-down"), 500, False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down)
def on_left():
    if joc_iniciat:
        animation.run_image_animation(steve, assets.animation("nena-animation-left"), 500, False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left)
def on_right():
    if joc_iniciat:
        animation.run_image_animation(steve, assets.animation("nena-animation-right"), 500, False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right)

# --- UPDATES I OVERLAPS ---
def on_overlap(sprite, other):
    global in_trading
    if joc_iniciat:
        in_trading = True
        steve.say("A: Botiga", 100)
sprites.on_overlap(SpriteKind.player, SpriteKind.trading, on_overlap)

def on_update():
    global temps_parat, troncos, in_trading
    if joc_iniciat:
        if steve:
            # Recollida de llenya
            quiet = steve.vx == 0 and steve.vy == 0
            a_l_arbre = steve.overlaps_with(arbol) or steve.overlaps_with(arbol2) or steve.overlaps_with(arbol3)
            
            if quiet and a_l_arbre:
                temps_parat = temps_parat + 1
                if temps_parat >= 120:
                    troncos = troncos + 1
                    info.set_score(troncos)
                    temps_parat = 0
            else:
                temps_parat = 0
            
            # Gestió del text de botiga
            if not steve.overlaps_with(trade):
                in_trading = False
                steve.say("")
game.on_update(on_update)

mostrar_menu_inicial()