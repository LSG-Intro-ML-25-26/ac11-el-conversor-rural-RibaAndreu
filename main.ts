namespace SpriteKind {
    export const trading = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.trading, function (player2, house) {
    in_trading = true
    game.showLongText("Prem A per comerciar", DialogLayout.Bottom)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    steve,
    assets.animation`nena-animation-down`,
    500,
    false
    )
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    steve,
    assets.animation`nena-animation-right`,
    500,
    false
    )
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    steve,
    assets.animation`nena-animation-left`,
    500,
    false
    )
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (in_trading) {
    	
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    in_trading = false
})
function calcular_arbres (opcio: number, quantitat: number) {
    index = opcio - 1
    if (index < 0 || index >= product_values.length) {
        return -1
    }
    if (quantitat <= 0 || quantitat != Math.floor(quantitat)) {
        return -2
    }
    arbres = product_values[index] * quantitat
    return Math.round(arbres * 100) / 100
}
function jugador_quieto () {
    return steve.vx == 0 && steve.vy == 0
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    steve,
    assets.animation`nena-animation-up`,
    500,
    false
    )
})
function esta_sobre_arbol () {
    return steve.overlapsWith(arbol) || steve.overlapsWith(arbol2) || steve.overlapsWith(arbol3)
}
let troncos = 0
let temps_parat = 0
let arbres = 0
let index = 0
let in_trading = false
let arbol3: Sprite = null
let arbol2: Sprite = null
let arbol: Sprite = null
let steve: Sprite = null
let product_values: number[] = []
let product_names = [
"Gallina",
"Patates (1.5 kg)",
"Cabra",
"Dotzena d'ous",
"Cavall"
]
product_values = [
6,
2,
5,
3,
12
]
scene.setBackgroundImage(assets.image`fons`)
steve = sprites.create(assets.image`pers`, SpriteKind.Player)
let trade = sprites.create(assets.image`trade`, SpriteKind.trading)
arbol = sprites.create(assets.image`arbol`, SpriteKind.Enemy)
arbol2 = sprites.create(assets.image`arbol`, SpriteKind.Enemy)
arbol3 = sprites.create(assets.image`arbol`, SpriteKind.Enemy)
arbol3.setPosition(116, 36)
arbol2.setPosition(144, 90)
arbol.setPosition(80, 75)
trade.setPosition(25, 82)
controller.moveSprite(steve, 100, 100)
let icono_llenya = sprites.create(assets.image`llenya`, SpriteKind.Food)
icono_llenya.setPosition(150, 10)
icono_llenya.setFlag(SpriteFlag.StayInScreen, true)
info.setScore(0)
game.onUpdate(function () {
    if (esta_sobre_arbol() && jugador_quieto()) {
        temps_parat += 1
        if (temps_parat >= 120) {
            // ~3 segons parat al costat de l'arbre
            troncos += 1
            info.setScore(troncos)
            temps_parat = 0
        }
    } else {
        temps_parat = 0
    }
})
