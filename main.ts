namespace SpriteKind {
    export const trading = SpriteKind.create()
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.trading, function on_on_overlap(player2: Sprite, house: Sprite) {
    
    in_trading = true
    steve.say("A: Botiga", 200)
})
function obrir_botiga() {
    let quantitat: number;
    let preu_total: number;
    
    let llista = "BOTIGA (Preus):\n"
    while (i <= product_names.length - 1) {
        llista = "" + llista + ("" + ("" + (i + 1))) + ". " + product_names[i] + " (" + ("" + ("" + product_values[i])) + ")\n"
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
    
}

controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    animation.runImageAnimation(steve, assets.animation`
            nena-animation-down
            `, 500, false)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    animation.runImageAnimation(steve, assets.animation`
            nena-animation-right
            `, 500, false)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    animation.runImageAnimation(steve, assets.animation`
            nena-animation-left
            `, 500, false)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    if (in_trading) {
        obrir_botiga()
    }
    
})
function jugador_quieto() {
    return steve.vx == 0 && steve.vy == 0
}

controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    animation.runImageAnimation(steve, assets.animation`
            nena-animation-up
            `, 500, false)
})
function esta_sobre_arbol() {
    return steve.overlapsWith(arbol) || steve.overlapsWith(arbol2) || steve.overlapsWith(arbol3)
}

let temps_parat = 0
let troncos = 0
let idx = 0
let opcio = 0
let i = 0
let in_trading = false
let arbol3 : Sprite = null
let arbol2 : Sprite = null
let arbol : Sprite = null
let steve : Sprite = null
let product_values : number[] = []
let product_names : string[] = []
product_names = ["Gallina", "Patates", "Cabra", "Ous", "Cavall"]
product_values = [6, 2, 5, 3, 12]
scene.setBackgroundImage(assets.image`
    fons
    `)
steve = sprites.create(assets.image`
    pers
    `, SpriteKind.Player)
steve.setStayInScreen(true)
steve.z = 100
let trade = sprites.create(assets.image`
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
controller.moveSprite(steve, 100, 100)
let icono_llenya = sprites.create(assets.image`
    llenya
    `, SpriteKind.Food)
icono_llenya.setPosition(150, 10)
icono_llenya.setFlag(SpriteFlag.StayInScreen, true)
info.setScore(0)
game.onUpdate(function on_on_update() {
    
    if (!steve.overlapsWith(trade)) {
        in_trading = false
    }
    
})
game.onUpdate(function on_on_update2() {
    
    if (esta_sobre_arbol() && jugador_quieto()) {
        temps_parat += 1
        if (temps_parat >= 120) {
            troncos += 1
            info.setScore(troncos)
            temps_parat = 0
        }
        
    } else {
        temps_parat = 0
    }
    
})
