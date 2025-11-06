#personajes Capitulo1
define R = Character("rata", color="#c582ff")
image rata neutral = "images/rata_neutral.png"
define Player = Character("Tu", color="#074eb8")
image bg habitacion = "images/habitacion.png"
define gui.text_font = "fonts/daydream.otf"


label start:
    scene bg habitacion
    with fade

    play music "liminalspace.mp3" loop
    "Un olor putrido pero familiar inunda tus cavidades nasales"
    "..."

    show rata neutral
    with dissolve
    R "soy pobre"
    R "..."
    R "Muy... pobre"




    return
