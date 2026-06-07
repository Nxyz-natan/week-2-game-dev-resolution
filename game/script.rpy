
default persistent.ending_hero    = False
default persistent.ending_shadow  = False
default persistent.ending_exile   = False
default persistent.found_secret   = False   # secret 4th path hint
default persistent.runs           = 0

default player_name   = "Traveller"
default courage       = 0
default cunning       = 0
default mercy         = 0

default rel_lyra      = 30
default rel_kael      = 10
default rel_sera      = 0
default rel_tobias    = 0
default rel_maren     = 20

default sq_lyra_done   = False    # Lyra's lost brother
default sq_kael_done   = False    # Kael's redemption
default sq_sera_done   = False    # Sera's debt
default sq_tobias_done = False    # Tobias's invention

default shard_found    = False
default kael_joined    = False
default sera_joined    = False
default tobias_joined  = False
default maren_alive    = True
default crown_restored = False
default crown_broken   = False

init python:
    import random
    bgm_ambient = [
        "audio/ambient_a.ogg",
        "audio/ambient_b.ogg",
    ]
    bgm_tense = [
        "audio/tense_a.ogg",
        "audio/tense_b.ogg",
    ]
    bgm_peaceful = [
        "audio/peaceful_a.ogg",
    ]

define narrator = Character(None, kind=nvl)
define hero     = Character("[player_name]",  color="#e8d5a3")
define lyra     = Character("Lyra",           color="#a3d4e8")
define kael     = Character("Kael",           color="#c8a87a")
define sera     = Character("Sera",           color="#e8a3c8")
define tobias   = Character("Tobias",         color="#a3e8b4")
define maren    = Character("Elder Maren",    color="#d4c8e8")
define oracle   = Character("The Oracle",     color="#e8e8a3")
define vex      = Character("Vex",            color="#e85a5a")
define guard    = Character("Guard",          color="#aaaaaa")
define villager = Character("Villager",       color="#bbbbbb")

image bg_black      = "#000000"
image bg_white      = "#ffffff"
image bg_village    = "images/bg_village.png"
image bg_tavern     = "images/bg_tavern.png"
image bg_forest     = "images/bg_forest.png"
image bg_ruins      = "images/bg_ruins.png"
image bg_cave       = "images/bg_cave.png"
image bg_mountain   = "images/bg_mountain.png"
image bg_throne     = "images/bg_throne.png"
image bg_cliffside  = "images/bg_cliffside.png"
image bg_library    = "images/bg_library.png"
image bg_harbor     = "images/bg_harbor.png"
image bg_battlefield= "images/bg_battlefield.png"
image bg_oracle     = "images/bg_oracle.png"

image hero neutral   = "images/hero_neutral.png"
image hero happy     = "images/hero_happy.png"
image hero sad       = "images/hero_sad.png"
image hero angry     = "images/hero_angry.png"
image hero surprised = "images/hero_surprised.png"
image hero determined= "images/hero_determined.png"

image lyra neutral   = "images/lyra_neutral.png"
image lyra happy     = "images/lyra_happy.png"
image lyra sad       = "images/lyra_sad.png"
image lyra worried   = "images/lyra_worried.png"
image lyra angry     = "images/lyra_angry.png"

image kael neutral   = "images/kael_neutral.png"
image kael angry     = "images/kael_angry.png"
image kael sad       = "images/kael_sad.png"
image kael happy     = "images/kael_happy.png"

image sera neutral   = "images/sera_neutral.png"
image sera happy     = "images/sera_happy.png"
image sera sad       = "images/sera_sad.png"
image sera nervous   = "images/sera_nervous.png"

image tobias neutral = "images/tobias_neutral.png"
image tobias happy   = "images/tobias_happy.png"
image tobias worried = "images/tobias_worried.png"

image maren neutral  = "images/maren_neutral.png"
image maren sad      = "images/maren_sad.png"
image maren dying    = "images/maren_dying.png"

image oracle neutral = "images/oracle_neutral.png"
image oracle angry   = "images/oracle_angry.png"

image vex neutral    = "images/vex_neutral.png"
image vex angry      = "images/vex_angry.png"
image vex smug       = "images/vex_smug.png"

label start:

    $ persistent.runs += 1

    play music random.choice(bgm_ambient) fadein 2.0 loop

    scene bg_black with fade
    nvl clear
    narrator "Once, a crown held the world together."
    narrator "Five kingdoms. Five shards. One promise of peace."
    narrator ""
    narrator "Then a king grew greedy."
    narrator "Then a queen grew afraid."
    narrator "Then a general grew ambitious."
    narrator ""
    narrator "And the Crown shattered."
    narrator ""
    narrator "That was five years ago."
    narrator "The kingdoms have been bleeding ever since."
    narrator ""
    narrator "{i}You have been walking for three days.{/i}"
    narrator "{i}You are tired. You are hungry.{/i}"
    narrator "{i}And something in your pack has been glowing since dawn.{/i}"
    nvl clear

    scene bg_village with dissolve

    $ player_name = renpy.input(
        "Before the road takes you further — what is your name?",
        default="",
        length=20
    )
    $ player_name = player_name.strip() or "Traveller"
    $ hero = Character(player_name, color="#e8d5a3")

    if persistent.runs > 1:
        "[player_name] again. The road remembers you."
        if persistent.ending_hero:
            "Last time, you gave the Crown back. Let's see if you're still that noble."
        elif persistent.ending_shadow:
            "Last time, you kept the power. Regrets?"
        elif persistent.ending_exile:
            "Last time, you burned it all down. Wiser now?"

    scene bg_village with dissolve
    show lyra neutral at center with dissolve

    lyra neutral "Hey! You with the pack — you a fighter?"

    show hero neutral at center

    hero neutral "Depends who's asking."

    lyra neutral "Lyra. Scout. The village behind me is about to stop being a village if someone doesn't help."

    hero neutral "What happened?"

    lyra worried "Something destroyed the eastern mill last night. Our elder went to investigate alone. She's gone."
    lyra worried "And I found tracks leading into the Thornwood. Big tracks. I'm good, but not {i}that{/i} good alone."

    menu:
        "\"I'll help. No strings.\""  :
            $ courage += 5
            $ rel_lyra += 10
            hero happy "Lead the way."
            lyra happy "Just like that? No negotiation?"
            hero happy "Sometimes things just need doing."

        "\"What's the pay?\""  :
            $ cunning += 5
            hero neutral "I appreciate the urgency. What's the compensation?"
            lyra neutral "Shelter, a hot meal, and — honestly — I think there's something weird going on that might interest someone like you."
            hero neutral "Weird how?"
            lyra worried "The tracks… they glow."
            hero surprised "I'll take the meal."

        "\"Tell me about this elder first.\""  :
            $ mercy += 5
            $ rel_maren += 5
            hero neutral "Elder Maren — what's she like? Will she have gone somewhere safe, or straight into danger?"
            lyra sad "Straight into danger. She's stubborn as stone and twice as hard."
            hero neutral "Sounds like someone worth finding. Let's go."

    scene bg_tavern with dissolve
    hide lyra

    lyra neutral "Before the Thornwood — I want to grab supplies from the tavern. Two minutes."

    show tobias happy at center with dissolve

    tobias happy "Lyra! And a stranger! Wonderful. I was just telling {i}no one{/i} about my latest invention."

    lyra neutral "Tobias is our local… inventor. Use that word loosely."

    tobias happy "I prefer {i}visionary engineer.{/i} But yes. Tobias Wren, at your service."
    tobias happy "[player_name], is it? Excellent name. I've built something that could help you in those woods."

    menu:
        "\"What kind of invention?\""  :
            $ tobias_joined = False
            $ rel_tobias += 10
            tobias happy "A compass — but instead of north, it points toward magical disturbances. I call it the Lodestar."
            hero surprised "That's… actually brilliant."
            tobias happy "I {i}know.{/i} It'll cost you nothing. Consider it field testing."
            Tobias pressed a  small brass device into your hand. Its already twitching.

        ""

