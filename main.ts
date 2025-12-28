namespace SpriteKind {
    export const trading = SpriteKind.create()
    export const menu_ui = SpriteKind.create()
}

let joc_iniciat = false
let in_trading = false
let troncos = 0
let temps_parat = 0
let bucle_botiga = false
//  Noms dels productes
let product_names = ["Gallina", "Patata (Pack 1.5kg)", "Cabra", "Ous (12u)", "Cavall"]
let product_values = [6, 2, 5, 3, 12]
//  Sprites del joc
let steve : Sprite = null
let trade : Sprite = null
let arbol : Sprite = null
let arbol2 : Sprite = null
let arbol3 : Sprite = null
let targeta_menu : Sprite = null
//  Càlcul comerç
function calcular_conversi_llenya(id_prod: number, unitats: number): number {
    if (unitats <= 0) {
        return -1
    }
    
    if (unitats % 1 != 0) {
        return -2
    }
    
    let preu_unitari = product_values[id_prod]
    let resultat = preu_unitari * unitats
    return Math.roundWithPrecision(resultat, 2)
}

//  Botiga joc
function obrir_botiga() {
    let llista: any;
    let opcio: number;
    let idx: number;
    let missatge_q: any;
    let q: number;
    let cost: number;
    
    steve.say("")
    game.showLongText("Hola veí! Vols fer un canvi?", DialogLayout.Bottom)
    bucle_botiga = true
    while (bucle_botiga) {
        llista = "MERCAT D'ALCUBILLA:" + "\n" + "1. Gallina (6)" + "\n" + "2. Patata 1.5kg (2)" + "\n" + "3. Cabra (5)" + "\n" + "4. Ous 12u (3)" + "\n" + "5. Cavall (12)" + "\n" + "6. SORTIR"
        game.showLongText(llista, DialogLayout.Center)
        opcio = game.askForNumber("Tria (1-6):", 1)
        if (opcio == 6) {
            bucle_botiga = false
        } else if (opcio >= 1 && opcio <= 5) {
            idx = opcio - 1
            //  Preguntem quantes unitats o packs vol
            missatge_q = "Quantes unitats de " + product_names[idx] + "?"
            q = game.askForNumber(missatge_q, 1)
            cost = calcular_conversi_llenya(idx, q)
            if (cost == -1) {
                game.showLongText("Error: Quantitat no vàlida", DialogLayout.Bottom)
            } else if (cost == -2) {
                game.showLongText("Error: Només unitats senceres", DialogLayout.Bottom)
            } else {
                game.showLongText("Això et costarà " + ("" + cost) + " kg de llenya", DialogLayout.Bottom)
                if (troncos >= cost) {
                    troncos = troncos - cost
                    info.setScore(troncos)
                    music.baDing.play()
                    game.showLongText("Gràcies! Aquí tens el teu producte.", DialogLayout.Bottom)
                } else {
                    music.play(music.melodyPlayable(music.thump), music.PlaybackMode.UntilDone)
                    game.showLongText("No tens prou llenya!", DialogLayout.Bottom)
                }
                
            }
            
        } else {
            game.showLongText("Opció no vàlida", DialogLayout.Bottom)
        }
        
    }
    steve.say("")
}

//  Menú inical
function mostrar_menu_inicial() {
    
    let img_menu = image.create(160, 90)
    img_menu.fill(1)
    img_menu.print("EL CONVERSOR RURAL", 25, 15, 15)
    img_menu.print("--------------------------", 10, 30, 15)
    img_menu.print("Recull la llenya", 35, 55, 15)
    img_menu.print("PREM A PER JUGAR", 30, 75, 15)
    targeta_menu = sprites.create(img_menu, SpriteKind.menu_ui)
    targeta_menu.setPosition(80, 60)
    targeta_menu.z = 200
}

function iniciar_partida() {
    
    joc_iniciat = true
    targeta_menu.destroy()
    scene.setBackgroundImage(assets.image`fons`)
    steve = sprites.create(assets.image`pers`, SpriteKind.Player)
    steve.setStayInScreen(true)
    controller.moveSprite(steve, 100, 100)
    trade = sprites.create(assets.image`trade`, SpriteKind.trading)
    arbol = sprites.create(assets.image`arbol`, SpriteKind.Enemy)
    arbol2 = sprites.create(assets.image`arbol`, SpriteKind.Enemy)
    arbol3 = sprites.create(assets.image`arbol`, SpriteKind.Enemy)
    arbol3.setPosition(116, 36)
    arbol2.setPosition(140, 90)
    arbol.setPosition(80, 75)
    trade.setPosition(25, 82)
    let icono = sprites.create(assets.image`llenya`, SpriteKind.Food)
    icono.setPosition(150, 10)
    icono.setFlag(SpriteFlag.StayInScreen, true)
    info.setScore(0)
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    if (joc_iniciat == false) {
        iniciar_partida()
    } else if (in_trading == true) {
        obrir_botiga()
    }
    
})
//  Animacions personatje
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up() {
    if (joc_iniciat) {
        animation.runImageAnimation(steve, assets.animation`nena-animation-up`, 500, false)
    }
    
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down() {
    if (joc_iniciat) {
        animation.runImageAnimation(steve, assets.animation`nena-animation-down`, 500, false)
    }
    
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left() {
    if (joc_iniciat) {
        animation.runImageAnimation(steve, assets.animation`nena-animation-left`, 500, false)
    }
    
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right() {
    if (joc_iniciat) {
        animation.runImageAnimation(steve, assets.animation`nena-animation-right`, 500, false)
    }
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.trading, function on_overlap(sprite: Sprite, other: Sprite) {
    
    if (joc_iniciat) {
        in_trading = true
        steve.say("A: Botiga", 100)
    }
    
})
game.onUpdate(function on_update() {
    let quiet: any;
    let a_l_arbre: any;
    
    if (joc_iniciat) {
        if (steve) {
            //  Recollida de llenya
            quiet = steve.vx == 0 && steve.vy == 0
            a_l_arbre = steve.overlapsWith(arbol) || steve.overlapsWith(arbol2) || steve.overlapsWith(arbol3)
            if (quiet && a_l_arbre) {
                temps_parat = temps_parat + 1
                if (temps_parat >= 120) {
                    troncos = troncos + 1
                    info.setScore(troncos)
                    temps_parat = 0
                }
                
            } else {
                temps_parat = 0
            }
            
            //  Gestió del text de botiga
            if (!steve.overlapsWith(trade)) {
                in_trading = false
                steve.say("")
            }
            
        }
        
    }
    
})
mostrar_menu_inicial()
