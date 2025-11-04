#Personajes Capitulo1
define q = Character("Quency", color="#5b029c")
define Player = Character("Investigador", color="#ed5f00")
#Personajes Capitulo2
define ti = Character("Tiki", color="#5b029c")
define ta = Character("Taka", color="#5b029c")
#Karma Settings
default karma = 0
screen kamra_bar:
    text "Karma Total: [karma]"



label start:

     play music "camaróncaramelo.mp3" loop
     show screen karma_bar
     scene fondo
     
     show quency_neutro with dissolve
     play sound "womp.mp3"
     q "ola chambaleshhhh, como stais?"
     hide quency_neutro
     show quency_thinking

     q "siento la fragilidad de mi existencia chocando con la realización de mi proposito acercandose y llegando a mi inevitable y patetico fin"

     hide quency_thinking
     show gato with dissolve

     "puff"

     Player "como?" 
     jump Capitulo2

     

    
label Capitulo2:
     scene fondo

     show tiki with dissolve
     show taka with dissolve
     play sound "womp.mp3"

     ti "ola"
     ta "demonio"
       
#Final Malo
label final_tiki: