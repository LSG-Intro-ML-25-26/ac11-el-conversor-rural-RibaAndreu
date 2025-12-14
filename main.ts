namespace SpriteKind {
    export const trading = SpriteKind.create()
}
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
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    steve,
    assets.animation`nena-animation-up`,
    500,
    false
    )
})
let steve: Sprite = null
scene.setBackgroundImage(assets.image`background`)
steve = sprites.create(assets.image`pers`, SpriteKind.Player)
let trade = sprites.create(assets.image`trade`, SpriteKind.trading)
tiles.placeOnTile(trade, tiles.getTileLocation(-120, -15))
controller.moveSprite(steve)
