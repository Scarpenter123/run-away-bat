def on_a_pressed():
    mySprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

projectile: Sprite = None
mySprite: Sprite = None
tiles.set_tilemap(tiles.create_tilemap(hex("""
            0a0008000101010101010101010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001010101010101010101
        """),
        img("""
            2 2 2 2 2 2 2 2 2 2
            . . . . . . . . . .
            . . . . . . . . . .
            . . . . . . . . . .
            . . . . . . . . . .
            . . . . . . . . . .
            . . . . . . . . . .
            2 2 2 2 2 2 2 2 2 2
        """),
        [myTiles.transparency16, sprites.builtin.forest_tiles6],
        TileScale.SIXTEEN))
mySprite = sprites.create(img("""
        . f f f . . . . . . . . f f f . 
            f f c . . . . . . . f c b b c . 
            f c c . . . . . . f c b b c . . 
            c f . . . . . . . f b c c c . . 
            c f f . . . . . f f b b c c . . 
            f f f c c . c c f b c b b c . . 
            f f f c c c c c f b c c b c . . 
            . f c 3 c c 3 b c b c c c . . . 
            . c b 3 b c 3 b b c c c c . . . 
            c c b b b b b b b b c c . . . . 
            c 1 1 b b b 1 1 b b b f c . . . 
            f b b b b b b b b b b f c c . . 
            f b c b b b c b b b b f . . . . 
            . f 1 f f f 1 b b b c f . . . . 
            . . f b b b b b b c f . . . . . 
            . . . f f f f f f f . . . . . .
    """),
    SpriteKind.player)
tiles.place_on_tile(mySprite, tiles.get_tile_location(1, 5))
mySprite.ay = 500

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile_from_side(img("""
        . . . . . . . .
        . . . . . . . .
        e e 5 5 5 5 5 4
        e 5 5 5 5 5 5 4
        e 5 5 5 5 5 5 4
        e e 5 5 5 5 5 4
        . . . . . . . .
        . . . . . . . .
    """),
        randint(-100, -80),
        0)
    tiles.place_on_tile(projectile, tiles.get_tile_location(9, 5))
    info.change_score_by(1)
game.on_update_interval(2000, on_update_interval)
