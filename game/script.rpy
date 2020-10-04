# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Carson")
define j = Character("JSchlatt")
define ja = Character("Jawsh")
define ch = Character("Charlie")
define t = Character("Travis")
define co = Character("Cooper")
define cm = Character("Carson's Mom")
define p = Character("Mrs. Pokimaine")


define audio.traitors_requiem = "audio/music/traitors requiem.ogg"
define audio.gameover_gay_song = "audio/music/creepy wind song.ogg"
define audio.cave = "audio/music/cave.mp3"


# The game starts here.

label start:

    $ carsonAffection = 0
    stop music

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show carson happy at left

    #play music traitors_requiem

    # These display lines of dialogue.

    c "Oh hey how you doing?"

    show carson small at left

    c "Holy shit you grew!"

    show jschlatt happy at right

    j "Hey it's me Jschlatt, Dick and Balls!"

    c "OMG Jschlatt I'm talking to the new kid!"

    j "Whatever Carson I'll go talk to the big hot steamy men in the gym
    class."

    hide jschlatt happy

    c "Sorry about Jschlatt he is a goblin"

    c "Anyway how you doing?"

    $ player_name = renpy.input("So, What is your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Big Booby Girl"

    c "So your name is %(player_name)s? That's cool bruh."

    show jawsh disturbed at right

    ja "Hey Carson, can I borrow a pencil?"

    c "Ok, josh but make it quick!"

    show jawsh pencil at right

    ja "Thanks! OH! You must be the new kid!"

    ja "I'm Josh I play Super MArio 64."

    c "Ok nerd don't bore him with your baby rage stories."

    menu:

        "So you are all Gamers too!":
            jump gamers

        "Stupid nerd!":
            jump nerd

        "That's cool":
            jump thatsCool


label gamers:

    $ renpy.notify("Carson will remember that!")

    $ isGamer = 1
    $ carsonAffection += 10

    $ renpy.notify("Carson Affection increased")

    c "OMG that’s so cool!!!!! It’s hard being the most oppressed community"

    c "Anyway sport. I better be getting to class. Cya at recess!"

    jump recess

label nerd:

    c "HEy thats’ not nice i was just joking."

    c "Anyway sport. I better be getting to class. Cya at recess!"

    jump recess

label thatsCool:

    c "yea."

    c "ok cya around"

    jump recess


label recess:
    scene bg playground

    show carson happy at right

    c "Oh hey %(player_name)s, me and the Lunch Club like to play Minecraft IRL in recess"

    c "Care to join?"

    menu:
        "Yes":
            jump mcIRLYes

        "No":
            jump gameOver_MCIRL


label mcIRLYes:

    c "Awesome! Come on I’ll introduce you to the Lunch Club"

    c "Hey guys this is the new kid %(player_name)s."

    show charlie intro at left

    "???" "Hello!"

    c "This is Charlie!"

    ch "Nice to meet you!!!!"

    c "you already know Jschlatt and Jawsh."

    hide charlie intro

    show jawsh disturbed at left

    ja "sup"

    hide jawsh disturbed

    show jschlatt baby yuto at left

    j "I hung a baby yesterday on my Nintendo Wii!"

    c "cool. This is Travis he is not the sharpest tool in the shed."

    hide jschlatt baby yuto

    show traves stare at left

    t "He has the right to keep your sh*t, wait what"

    hide carson happy
    show cooper flip off at right

    co "OMG Travis swore!!!!!!!"

    hide traves stare
    show carson disappointed at left

    c "Good greif, Kids these days!"

    "After playing Minecraft, you and the Lunch Club decide to go to Carson’s house after school."
    jump carsonsHouse_one


label carsonsHouse_one:

    scene bg carson living room

    "You have arrived at Carson's House!"

    show carson happy at left

    c "Welcome %(player_name)s to my humble abode."

    show mom happy at right

    cm "Hi sweetie welcome home."

    c "Hey mom this is %(player_name)s They are new in town."

    cm "Hi I’m carson’s mom as he said can I get you anything to eat?"

    menu:

        "If you have any Wood fired pizza I’ll have that!":
            jump woodFiredPizza

        "Onion":
            jump onion

        "Fruit snacks":
            jump fruit_snacks

        "That’s fine I don’t want anything.":
            jump no_food


label woodFiredPizza:

    cm " EPIC!!!!!!! POG!!!!! I’ll go cook it up right away.
    Oh by the way Carson, don’t forget to take your pills for your erectile dysfunction."

    c "MOOOOOOOOMMMMMMM!!!!!!!!! THATS NOT COOL!!!"

    hide carsonMom epic

    show jschlatt laugh at right

    j "BWAAHAHAHAHAHAHAHAH YOU APE!!!!!!"

    c "Alright guys lets just go to my room."

    jump carsonsRoomOne

label onion:

    cm "k weird, but i’ll go get some and bring it up for you.
    Oh and also Carson dear. Make sure to wipe better i found skid marks all in your undies last week."

    c "OMG Mom I’m blushing that is not cool mom!!!!!"

    hide carsonMom epic

    show jschlatt laugh at right

    j "Does it get anymore embarrassing!?"

    c "Shut up dude."

    c "C’mon guys lets go up to my room"

    jump carsonsRoomOne


label fruit_snacks:

    cm "Intriguing… Anywho Carson You should clean up your (FEMALE STREAMER) shrine. You got cum all over the place!"

    c "C’MON MOM THAT”S SO INAPPROPRIATE WHAT IS WRONG WITH YOU!"

    hide carsonMom epic

    show jawsh disturbed at right

    ja "That’s fucking hilarious you incel!!!"

    c "Whatever man lets just go on up to my room."

    jump carsonsRoomOne

label no_food:

    $ renpy.notify("Carson's Mom will remember that!")

    cm "Oh Ok then have fun ya’ll."

    c "Let's go guys."

    jump carsonsRoomOne

label carsonsRoomOne:

    scene bg carson room

    "You and the Lunch Club have arrived in Carson's room"

    show carson happy

    c "Alright this is the Gamer Setup."

    c "so %(player_name)s what do you think?"

    menu:

        "It's truly epic!":
            jump epicSetup

        "Mines better!":
            jump my_better_setup

        "It's Gay!":
            jump gameOver_GAY


label epicSetup:

    $ renpy.notify("Carson Affection increased")

    $ carsonAffection += 10

    c "Thanks %(player_name)s, glad you like it!"

    jump carsonRoomTwo



label my_better_setup:

    $ renpy.notify("Carson will remember that!")

    c "Oh really? well I'll have to come see it someday."

    jump carsonRoomTwo


label carsonRoomTwo:

    show carson observe at right

    c "So what game does everyone want to play?"

    show traves stare at left

    t "Smash bros!"

    hide traves stare

    show jawsh disturbed at left

    ja "We always play smash bros."

    hide carson observe

    show cooper flip off at right

    co " let’s play minecraft!"

    hide cooper flip off

    show traves stare at right

    t "OK"

    hide jawsh disturbed

    show jschlatt baby yuto at left

    j "Eh whatever"

    hide traves stare

    show charlie hollow at right

    ch "No one asked what i wanted!"

    "we decide to play minecraft bedrock so we can have split screen."

    hide jschlatt baby yuto
    hide charlie hollow

    show carson happy

    c "What's your favorite minecraft mob short for mobiles?"

    menu:

        "Chicken":
            jump mob_chicken

        "Cave Spider":
            jump mob_caveSpider

        "Phantom":
            jump mob_phantom

        "mushroom chicken":
            jump mob_mushroomchicken


label mob_chicken:

    $ renpy.notify("Carson Affection increased")
    $ carsonAffection += 10

    c "That's pretty basic lame!"

    jump carsonRoomThree

label mob_caveSpider:

    c "interesting choice. not a very cash money mob if you ask me!"
    jump carsonRoomThree

label mob_phantom:

    $ carsonAffection -= 10
    $ renpy.notify("Carson Affection decreased")

    c "That's really weird champ if you ask me bruh."

    c "well ok then i guess what ever you like."

    jump carsonRoomThree


label mob_mushroomchicken:

    c "bruh thats not even real is it. quite pulling my leg!"

    "You tell him to look it up but he doesn't seem to feel like doing it."

    jump carsonRoomThree


label carsonRoomThree:

    show carson happy at right

    c "Oh goodnesss me oh my it's already 9 pm!!!!!"

    show jshlatt happy at left

    j "Oh man i better getting home!"

    "We all decided to go home."

    jump atHomeOne

label atHomeOne:

    scene bg home bedroom

    "You think to your self carson is a cool dude man i wonder what he is like in bed."

    "Welp time for bed!"

    "You have a crazy wacky dream about carson"

    "You awaken! you can the birds."

    $ renpy.notify("Objective: Date Carson!")

    "You think i need to get on carson's good side"

    jump classroomOne

label classroomOne:

    scene bg room

    show pokimaine happy at left

    p "Alright class time for a pop quiz!!"

    show carson disappointed at right

    c "BRUH MOMENT!!!!!"

    c "I didn't study for this"

    hide pokimaine happy

    "You tell carson that you will help him."

    $ renpy.notify("Carson Affection increased")

    $ carsonAffection += 10

    c "Really!? Thanks %(player_name)s!"








label gameOver_MCIRL:

    # this ends the game
    return

label gameOver_GAY:

    show carson deadstare

    play sound cave

    c "..."

    scene bg gameovergay

    play music gameover_gay_song

    "You have failed!"

    return





return
