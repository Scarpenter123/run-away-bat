controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    mySprite.vy = -200
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    game.over(false)
})
let projectile : Sprite = null
let mySprite : Sprite = null
tiles.setTilemap(tiles.createTilemap(hex`
            0a0008000101010101010101010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001010101010101010101
        `, img`
            2 2 2 2 2 2 2 2 2 2
            . . . . . . . . . .
            . . . . . . . . . .
            . . . . . . . . . .
            . . . . . . . . . .
            . . . . . . . . . .
            . . . . . . . . . .
            2 2 2 2 2 2 2 2 2 2
        `, [myTiles.transparency16, sprites.builtin.forestTiles6], TileScale.Sixteen))
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
tiles.placeOnTile(mySprite, tiles.getTileLocation(1, 5))
mySprite.ay = 500
game.onUpdateInterval(2000, function on_update_interval() {
    
    projectile = sprites.createProjectileFromSide(img`
        . . . . . . . .
        . . . . . . . .
        e e 5 5 5 5 5 4
        e 5 5 5 5 5 5 4
        e 5 5 5 5 5 5 4
        e e 5 5 5 5 5 4
        . . . . . . . .
        . . . . . . . .
    `, randint(-100, -80), 0)
    tiles.placeOnTile(projectile, tiles.getTileLocation(9, 5))
    info.changeScoreBy(1)
})
