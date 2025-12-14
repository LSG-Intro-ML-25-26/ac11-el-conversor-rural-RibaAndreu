@namespace
class SpriteKind:
    trading = SpriteKind.create()

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

def on_up_pressed():
    animation.run_image_animation(steve,
        assets.animation("""
            nena-animation-up
            """),
        500,
        False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

steve: Sprite = None
scene.set_background_image(assets.image("""
    background
    """))
steve = sprites.create(assets.image("""
    pers
    """), SpriteKind.player)
trade = sprites.create(assets.image("""
    trade
    """), SpriteKind.trading)
tiles.place_on_tile(trade, tiles.get_tile_location(-120, -15))
controller.move_sprite(steve)