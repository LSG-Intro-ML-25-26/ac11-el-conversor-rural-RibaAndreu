namespace SpriteKind {
    export const trading = SpriteKind.create()
    export const menu_ui = SpriteKind.create()
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.trading, function on_on_overlap(player2: Sprite, house: Sprite) {
    
    if (joc_iniciat) {
        in_trading = true
        steve.say("A: Botiga", 100)
    }
    
})
function obrir_botiga() {
    let quantitat: number;
    let preu_total: number;
    
    steve.say("")
    let llista = "BOTIGA (Preus):\n"
    while (i < product_names.length) {
        llista = "" + llista + "" + ("" + ("" + (i + 1))) + ". " + product_names[i] + " (" + ("" + ("" + product_values[i])) + ")\n"
        i += 1
    }
    game.showLongText(llista, DialogLayout.Center)
    opcio = game.askForNumber("Quin producte vols? (1-5)", 1)
    idx = opcio - 1
    if (idx >= 0 && idx < product_names.length) {
        quantitat = game.askForNumber("Quantes unitats de " + product_names[idx] + "?", 1)
        if (quantitat > 0) {
            preu_total = product_values[idx] * quantitat
            if (troncos >= preu_total) {
                troncos += 0 - preu_total
                info.setScore(troncos)
                music.baDing.play()
                game.showLongText("Has comprat " + ("" + ("" + quantitat)) + " " + product_names[idx], DialogLayout.Bottom)
            } else {
                game.showLongText("No tens prou llenya! Falten " + ("" + ("" + (preu_total - troncos))), DialogLayout.Bottom)
            }
            
        }
        
    } else {
        game.showLongText("Opció no vàlida", DialogLayout.Bottom)
    }
    
    steve.say("")
}

controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    if (joc_iniciat) {
        animation.runImageAnimation(steve, assets.animation`
                nena-animation-down
                `, 500, false)
    }
    
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    if (joc_iniciat) {
        animation.runImageAnimation(steve, assets.animation`
                nena-animation-right
                `, 500, false)
    }
    
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    if (joc_iniciat) {
        animation.runImageAnimation(steve, assets.animation`
                nena-animation-left
                `, 500, false)
    }
    
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    if (!joc_iniciat) {
        iniciar_partida()
    } else if (in_trading) {
        obrir_botiga()
    }
    
})
function mostrar_menu_inicial() {
    
    fons_blanc = image.create(140, 90)
    fons_blanc.fill(1)
    fons_blanc.print("LA GRANJA DE SORIA", 15, 15, 15)
    fons_blanc.print("-----------------", 15, 30, 15)
    fons_blanc.print("Mou-te amb fletxes", 15, 50, 15)
    fons_blanc.print("PREM A PER JUGAR", 20, 70, 15)
    targeta_menu = sprites.create(fons_blanc, SpriteKind.menu_ui)
    targeta_menu.setPosition(80, 60)
    targeta_menu.z = 200
}

function iniciar_partida() {
    
    joc_iniciat = true
    targeta_menu.destroy()
    scene.setBackgroundImage(assets.image`
        fons
        `)
    steve = sprites.create(assets.image`
        pers
        `, SpriteKind.Player)
    steve.setStayInScreen(true)
    steve.z = 100
    controller.moveSprite(steve, 100, 100)
    trade = sprites.create(assets.image`
        trade
        `, SpriteKind.trading)
    arbol = sprites.create(assets.image`
        arbol
        `, SpriteKind.Enemy)
    arbol2 = sprites.create(assets.image`
        arbol
        `, SpriteKind.Enemy)
    arbol3 = sprites.create(assets.image`
        arbol
        `, SpriteKind.Enemy)
    arbol3.setPosition(116, 36)
    arbol2.setPosition(140, 90)
    arbol.setPosition(80, 75)
    trade.setPosition(25, 82)
    icono_llenya = sprites.create(assets.image`
        llenya
        `, SpriteKind.Food)
    icono_llenya.setPosition(150, 10)
    icono_llenya.setFlag(SpriteFlag.StayInScreen, true)
    info.setScore(0)
}

controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    if (joc_iniciat) {
        animation.runImageAnimation(steve, assets.animation`
                nena-animation-up
                `, 500, false)
    }
    
})
let temps_parat = 0
let icono_llenya : Sprite = null
let arbol3 : Sprite = null
let arbol2 : Sprite = null
let arbol : Sprite = null
let trade : Sprite = null
let targeta_menu : Sprite = null
let troncos = 0
let idx = 0
let opcio = 0
let i = 0
let steve : Sprite = null
let in_trading = false
let joc_iniciat = false
let product_values : number[] = []
let product_names : string[] = []
let fons_blanc : Image = null
product_names = ["Gallina", "Patates", "Cabra", "Ous", "Cavall"]
product_values = [6, 2, 5, 3, 12]
mostrar_menu_inicial()
game.onUpdate(function on_on_update() {
    
    if (joc_iniciat && steve) {
        if ((steve.overlapsWith(arbol) || steve.overlapsWith(arbol2) || steve.overlapsWith(arbol3)) && steve.vx == 0 && steve.vy == 0) {
            temps_parat += 1
            if (temps_parat >= 120) {
                troncos += 1
                info.setScore(troncos)
                temps_parat = 0
            }
            
        } else {
            temps_parat = 0
        }
        
        if (!steve.overlapsWith(trade)) {
            in_trading = false
            steve.say("")
        }
        
    }
    
})
