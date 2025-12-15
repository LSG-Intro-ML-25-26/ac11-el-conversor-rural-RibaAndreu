namespace SpriteKind {
    export const trading = SpriteKind.create()
}
// ---------- VARIABLES ----------
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
function abrir_inventario () {
    let producte: string;
opcio2 = Math.floor(game.askForNumber(`
        BOTIGA
        1 Gallina
        2 Patates
        3 Cabra
        4 Ous
        5 Cavall
        Escull opcio:
        `))
    quantitat2 = Math.floor(game.askForNumber("Quantes unitats vols?"))
    resultat = calcular_arbres(opcio2, quantitat2)
    if (resultat == -1) {
        game.showLongText("Opcio incorrecta", DialogLayout.Bottom)
    } else if (resultat == -2) {
        game.showLongText(`
                Quantitat incorrecta
                (Solo enters positius)
                `, DialogLayout.Bottom)
    } else {
        producte = product_names[opcio2 - 1]
        game.showLongText("" + quantitat2 + " " + producte + "\nnecessiten\n" + ("" + resultat) + " arbres", DialogLayout.Full)
    }
}
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
        abrir_inventario()
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
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    steve,
    assets.animation`nena-animation-up`,
    500,
    false
    )
})
let arbres = 0
let index = 0
let resultat = 0
let quantitat2 = 0
let opcio2 = 0
let in_trading = false
let steve: Sprite = null
let product_values: number[] = []
let product_names: string[] = []
product_names = [
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
scene.setBackgroundImage(assets.image`background`)
steve = sprites.create(assets.image`pers`, SpriteKind.Player)
let trade = sprites.create(assets.image`trade`, SpriteKind.trading)
let arbol = sprites.create(assets.image`arbol`, SpriteKind.Enemy)
let arbol2 = sprites.create(assets.image`arbol`, SpriteKind.Enemy)
let arbol3 = sprites.create(assets.image`arbol`, SpriteKind.Enemy)
arbol3.setPosition(144, 82)
arbol2.setPosition(112, 82)
arbol.setPosition(80, 82)
trade.setPosition(25, 82)
controller.moveSprite(steve, 100, 100)
