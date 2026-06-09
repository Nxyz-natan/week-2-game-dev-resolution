
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
define protagonist = Character("[player_name]", color="#e8d5a3", image="protagonist")
define lyra     = Character("Lyra",           color="#a3d4e8", image="lyra")
define kael     = Character("Kael",           color="#c8a87a", image="kael")
define sera     = Character("Sera",           color="#e8a3c8", image="sera")
define tobias   = Character("Tobias",         color="#a3e8b4", image="tobias")
define maren    = Character("Elder Maren",    color="#d4c8e8", image="maren")
define oracle   = Character("The Oracle",     color="#e8e8a3", image="oracle")
define vex      = Character("Vex",            color="#e85a5a", image="vex")
define guard    = Character("Guard",          color="#aaaaaa")
define villager = Character("Villager",       color="#bbbbbb")

image bg_black      = "#000000"
image bg_white      = "#ffffff"
image bg_village    = "images/bg_village.png"
image bg_tavern     = "images/bg_tavern.png"
image bg_forest     = "images/bg_forest.png"
image bg_ruins      = "images/bg_ruins.png"
image bg_mountain   = "images/bg_mountain.png"
image bg_throne     = "images/bg_throne.png"
image bg_cliffside  = "images/bg_cliffside.png"
image bg_library    = "images/bg_library.png"
image bg_harbor     = "images/bg_harbor.png"
image bg_battlefield= "images/bg_battlefield.png"
image bg_oracle     = "images/bg_oracle.png"

image protagonist neutral   = "images/hero_neutral.png"
image protagonist happy     = "images/hero_happy.png"
image protagonist sad       = "images/hero_sad.png"
image protagonist angry     = "images/hero_angry.png"
image protagonist surprised = "images/hero_surprised.png"
image protagonist determined= "images/hero_determined.png"

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
image vex sad       = "images/vex_sad.png"
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
        "Before the road takes you further  what is your name?",
        default="",
        length=20
    )
    $ player_name = player_name.strip() or "Traveller"

    if persistent.runs > 1:
        "[player_name] again. The road remembers you."
        if persistent.ending_hero:
            "Last time, you gave the Crown back. Let's see if you're still that noble."
        elif persistent.ending_shadow:
            "Last time, you kept the power. Regrets?"
        elif persistent.ending_exile:
            "Last time, you burned it all down. Wiser now?"

    scene bg_village with dissolve
    show lyra neutral at left with dissolve

    lyra neutral "Hey! You with the pack  you a fighter?"

    show protagonist neutral at center

    protagonist neutral "Depends who's asking."

    lyra neutral "Lyra. Scout. The village behind me is about to stop being a village if someone doesn't help."

    protagonist neutral "What happened?"

    lyra worried "Something destroyed the eastern mill last night. Our elder went to investigate alone. She's gone."
    lyra worried "And I found tracks leading into the Thornwood. Big tracks. I'm good, but not {i}that{/i} good alone."

    menu:
        "\"I'll help. No strings.\""  :
            $ courage += 5
            $ rel_lyra += 10
            protagonist happy "Lead the way."
            lyra happy "Just like that? No negotiation?"
            protagonist happy "Sometimes things just need doing."

        "\"What's the pay?\""  :
            $ cunning += 5
            protagonist neutral "I appreciate the urgency. What's the compensation?"
            lyra neutral "Shelter, a hot meal, and  honestly  I think there's something weird going on that might interest someone like you."
            protagonist neutral "Weird how?"
            lyra worried "The tracks… they glow."
            protagonist surprised "I'll take the meal."

        "\"Tell me about this elder first.\""  :
            $ mercy += 5
            $ rel_maren += 5
            protagonist neutral "Elder Maren  what's she like? Will she have gone somewhere safe, or straight into danger?"
            lyra sad "Straight into danger. She's stubborn as stone and twice as hard."
            protagonist neutral "Sounds like someone worth finding. Let's go."

    scene bg_tavern with dissolve
    hide lyra

    lyra neutral "Before the Thornwood  I want to grab supplies from the tavern. Two minutes."

    show tobias happy at center with dissolve

    tobias happy "Lyra! And a stranger! Wonderful. I was just telling {i}no one{/i} about my latest invention."

    lyra neutral "Tobias is our local… inventor. Use that word loosely."

    tobias happy "I prefer {i}visionary engineer.{/i} But yes. Tobias Wren, at your service."
    tobias happy "[player_name], is it? Excellent name. I've built something that could help you in those woods."

    menu:
        "\"What kind of invention?\""  :
            $ tobias_joined = False
            $ rel_tobias += 10
            tobias happy "A compass  but instead of north, it points toward magical disturbances. I call it the Lodestar."
            protagonist surprised "That's… actually brilliant."
            tobias happy "I {i}know.{/i} It'll cost you nothing. Consider it field testing."
            "Tobias pressed a  small brass device into your hand. Its already twitching."

        "\"We don't have time for gadgets.\""  :
            $ cunning += 3
            tobias worried "Fair enough. But if you change your mind  I'll be here."
    hide tobias
    show sera nervous at center with dissolve

    sera nervous "Um. Excuse me."
    sera nervous "I… I heard you're going into the Thornwood. I need to go there too."
    sera nervous "My name is Sera. I owe a debt to someone in there. Please."

    lyra neutral "The Thornwood isn't a place for  no offence  someone who looks like they've never held a sword."

    sera sad "I know. But I have no choice."

    menu:
        "\"Come with us. We'll keep you safe.\""  :
            $ mercy += 10
            $ rel_sera += 15
            $ sera_joined = True
            protagonist neutral "Stay close and do what we say."
            sera happy "Thank you. Truly."

        "\"Tell us about this debt first.\""  :
            $ cunning += 5
            $ rel_sera += 5
            protagonist neutral "Who do you owe, and why does it involve the Thornwood?"
            sera nervous "A woman named Vex. She… she has my sister. She said if I bring her a shard of the Crown, she'll let her go."
            protagonist surprised "A shard of the Crown?"
            sera nervous "You know what those are?"
            protagonist neutral "Starting to. Come with us."
            $ sera_joined = True
            $ rel_sera += 10

        "\"It's too dangerous. Wait here.\""  :
            $ courage += 3
            protagonist neutral "We'll find out what's in the Thornwood and come back for you."
            sera sad "Please hurry. My sister doesn't have much time."

    hide tobias
    hide sera
    hide protagonist

label act_two:

    scene bg_forest with dissolve
    play music random.choice(bgm_tense) fadein 2.0 loop

    show lyra worried at right with dissolve
    show protagonist neutral at left with dissolve
    
    lyra worried "The tracks are fresher here. Whatever made them is big."

    if sera_joined:
        show sera nervous at center with dissolve
        sera nervous "I've never seen trees this dark."
        lyra worried "Stay between us, Sera."

    "The Lodestar  if Tobias gave it to you  pulses in your pocket."
    "Something ahead is radiating magic. Strong magic."
    hide sera
    show kael angry at center with dissolve

    kael angry "Far enough. This is your last warning."

    lyra neutral "Kael?!"

    kael angry "Don't. Don't say my name like we're old friends."

    lyra worried "We {i}were{/i} friends. Half the village thinks you're dead."

    kael angry "Half the village is right about most things. Leave."
    hide lyra
    show protagonist neutral at left

    menu:
        "Step forward. Don't let him bluff you.":
            $ courage += 10
            protagonist determined "You're outnumbered and your hand is shaking. Stand down."
            kael angry "You don't know what I've seen "
            protagonist determined "Then tell me. But lower the sword first."
            kael sad "..."
            $ rel_kael += 15
            kael sad "Fine. Fine. The elder is safe. I found her an hour ago."

        "Approach slowly. He's scared, not angry.":
            $ mercy += 10
            $ rel_kael += 20
            protagonist neutral "You're not trying to stop us. You're trying to protect something."
            kael sad "..."
            kael sad "The elder. She's in a hollow, half a mile north. She's hurt but alive."
            protagonist neutral "Thank you."

        "Let Lyra handle it  she knows him.":
            $ cunning += 5
            $ rel_lyra += 10
            lyra neutral "Kael. It's me. Whatever happened to you  I don't care. We need to find Maren."
            kael sad "Lyra…"
            kael sad "She's north. A hollow near the split oak. Go."

    menu:
        "\"Come with us, Kael.\""  :
            $ rel_kael += 10
            if rel_kael >= 30:
                kael sad "…I'm not the man you remember."
                protagonist neutral "Nobody is. Come anyway."
                kael sad "Alright. But I'm not making promises."
                $ kael_joined = True
            else:
                kael angry "No. You don't know me."
                protagonist neutral "Your call."

        "Leave him. Push on to Maren.":
            $ courage += 3
            protagonist neutral "We'll come back for him."

    hide kael
    hide protagonist 
    hide lyra         
    hide sera 

    scene bg_ruins with dissolve
    show maren neutral at center with dissolve
    show protagonist neutral at left with dissolve
    show lyra worried at right with dissolve

    lyra worried "Maren! Are you alright?"

    maren neutral "Bruised. Not broken. Help me up."

    protagonist neutral "What happened?"

    maren neutral "I heard something in the mill. Followed the tracks. Found... this."

    "She opens her hand. A jagged black shard sits in her palm, glowing faintly violet."
    $ shard_found = True

    maren neutral "It spoke to me. Not in words  in {i}feelings.{/i} It wanted to be found."

    protagonist surprised "A shard of the Shattered Crown."

    maren neutral "You know what it is."

    protagonist neutral "I've heard stories."

    maren neutral "Then you know what collecting them means. Whoever reunites the Crown… reshapes the world."
    maren neutral "The shard chose me first. But now it's pulling toward {i}you.{/i}"

    "She extends it. The moment [player_name]'s fingers close around it, the world goes silent."
    "Then  a voice. Ancient. Vast."
    "Oracle: {i}'Shard-bearer. Find the others. The choice will come.'{/i}"

    play sound "audio/sfx_rumble.ogg"

    maren neutral "That sound… it's not safe here. We need to move."

    if sera_joined:
        hide lyra
        show sera nervous at left with dissolve
        sera nervous "Vex will know you have it. She {i}always{/i} knows."
        maren neutral "Then we move fast."

label camp_night:

    scene bg_ruins with dissolve
    play music random.choice(bgm_peaceful) fadein 2.0 loop

    "The group makes camp in the ruins for the night."
    "The shard pulses quietly in [player_name]'s pack."
    "Before sleep takes you, there are conversations to be had."

    menu:
        "Talk to Lyra.":
            jump sq_lyra
        "Talk to Kael." if kael_joined:
            jump sq_kael
        "Talk to Sera." if sera_joined:
            jump sq_sera
        "Search the ruins alone.":
            jump sq_ruins
        "Sleep. Move on in the morning.":
            jump act_three

label sq_lyra:
    hide kael    
    hide sera   
    hide maren   
    show lyra sad at right with dissolve
    show protagonist neutral at left with dissolve

    lyra sad "Can't sleep either?"
    protagonist neutral "Too much on my mind. You?"
    lyra sad "My brother. He left the village two years ago. Said he was going to find work in the capital."
    lyra sad "He never wrote. Never came back."
    protagonist neutral "What was his name?"
    lyra sad "Finn. Finnian Aldric. He was seventeen."
    menu:
        "\"I'll help you find him.\"":
            $ rel_lyra += 20
            $ sq_lyra_done = True
            protagonist neutral "When this is over  we find Finn. I promise."
            lyra happy "You barely know me."
            protagonist neutral "Doesn't matter."
            lyra happy "...Thank you, [player_name]."

        "\"He might have just started a new life.\"":
            $ cunning += 3
            protagonist neutral "Sometimes people leave and… don't come back. Not because something happened. Just because they changed."
            lyra sad "I know. I just need to know {i}which{/i} it is."
            protagonist neutral "Then we'll find out."
            $ rel_lyra += 10

        "\"Tell me about him.\"":
            $ mercy += 5
            $ rel_lyra += 15
            lyra happy "He was annoying. Brilliant. Could fix anything mechanical  Tobias used to call him a prodigy."
            lyra sad "He wanted to see the world. I told him the village needed him."
            lyra sad "I think that's why he left without saying goodbye."
            protagonist neutral "He'll forgive you for that."
            lyra sad "How do you know?"
            protagonist neutral "Because you're still looking."

    jump camp_night

label sq_kael:
    hide lyra   
    hide sera   
    show kael sad at left with dissolve
    show protagonist neutral at right with dissolve

    kael sad "You're watching me."
    protagonist neutral "Hard not to. Former Iron guard knight, living alone in a haunted forest  it's a good story."
    kael sad "It's a shameful one."
    protagonist neutral "Tell me."

    kael sad "I was ordered to burn a village. Five years ago. Our general said they were hiding rebels."
    kael sad "They weren't. They were just… people."
    kael sad "I refused the order. My commander called it treason."
    kael sad "I ran. Let them think I died. Came here."

    menu:
        "\"Refusing was the right thing.\"":
            $ mercy += 10
            $ rel_kael += 20
            protagonist neutral "You didn't burn it. That matters."
            kael sad "People died anyway. Someone else carried out the order."
            protagonist neutral "That's not on you."
            kael angry "Isn't it? I trained those men. I led that unit."
            protagonist neutral "Then lead them better now. Come back."
            kael sad "...I'll think about it."
            $ sq_kael_done = True

        "\"You should have done more.\"":
            $ courage += 5
            protagonist neutral "Refusing isn't enough. You should have warned the village."
            kael angry "I was one man "
            protagonist neutral "One man can do a lot. You know that."
            kael sad "..."
            kael sad "You're right. I've been telling myself running was brave. It wasn't."
            $ rel_kael += 10
            $ sq_kael_done = True

        "\"What's done is done. What now?\"":
            $ cunning += 5
            $ rel_kael += 15
            protagonist neutral "You can't change the past. But you're here, aren't you? Protecting these woods."
            kael neutral "A poor substitute."
            protagonist neutral "It's a start."
            $ sq_kael_done = True

    jump camp_night

label sq_sera:
    hide lyra   
    hide kael    
    show sera nervous at left with dissolve
    show protagonist neutral at right with dissolve

    sera nervous "I owe you the truth."
    protagonist neutral "Take your time."
    sera sad "Vex isn't just a criminal. She was our mentor. Mine and my sister Mia's."
    sera sad "She taught us magic  real magic. The kind the kingdoms have tried to stamp out."
    sera sad "When Vex turned dark, Mia tried to leave. Vex took her as… insurance."
    sera sad "She knows about the shards. She's been hunting them for years."

    protagonist neutral "And she thinks if she threatens your sister, you'll bring one to her."

    sera sad "She's right. I would have."

    menu:
        "\"We won't let her have it.\"":
            $ courage += 10
            $ rel_sera += 20
            protagonist neutral "We'll get Mia out. Without giving Vex anything."
            sera sad "She's powerful, [player_name]."
            protagonist neutral "So are we."
            sera happy "...Okay. Okay, yes. Let's do this."
            $ sq_sera_done = True

        "\"Is there a way to negotiate?\"":
            $ cunning += 10
            $ rel_sera += 15
            protagonist neutral "Vex wants a shard. What if we give her a fake?"
            sera nervous "She'd know."
            protagonist neutral "Maybe not if the right person handed it over."
            sera nervous "What are you suggesting?"
            protagonist neutral "A con. Think you can act?"
            sera happy "I've been acting calm for three days. I think I qualify."
            $ sq_sera_done = True

        "\"What does Mia look like?\"":
            $ mercy += 5
            $ rel_sera += 10
            sera sad "Like me, but braver. Shorter hair. Laughs too loud."
            protagonist neutral "She sounds worth rescuing."
            sera happy "She really is."
            $ sq_sera_done = True

    jump camp_night

label sq_ruins:
    show protagonist neutral at center with dissolve

    "You explore the ruins alone."
    "Most of it is rubble  old stone, old ghosts."
    "But in the deepest chamber, behind a collapsed wall, you find a mural."
    "Five figures hold a crown between them. Beneath it, an inscription:"
    "{i}'The Crown was never meant to rule. It was meant to {b}bind{/b}.'{/i}"
    "{i}'Destroy the shards, and the binding ends. The kingdoms will be free  or fall.'{/i}"

    $ persistent.found_secret = True
    $ mercy += 5

    "You stare at it for a long time."
    "Then you go back to camp."

    jump camp_night

label act_three:

    scene bg_mountain with dissolve
    play music random.choice(bgm_tense) fadein 2.0 loop

    show protagonist neutral at center with dissolve

    "Morning. The group breaks camp and heads north toward the Oracle's Spire."
    "Two more shards need collecting. The Lodestar points the way."

    if kael_joined:
        show kael neutral at right with dissolve
        kael neutral "The second shard is in Halvenmoor  the old battlefield. I know it."
        protagonist neutral "How?"
        kael sad "Because I fought there. And I left something behind."
    hide protagonist scene bg_harbor
    hide kael        
    scene bg_battlefield with dissolve
    show protagonist neutral at left with dissolve

    "Halvenmoor. Ten thousand men died here five years ago."
    "The ground still doesn't grow grass."

    show vex smug at right with dissolve

    vex smug "Well. The shard-bearer. I was wondering when you'd show up."

    if sera_joined:
        show sera nervous at center with dissolve
        sera nervous "Vex."
        vex smug "Little Sera. Did you bring me my shard?"
        sera nervous "I brought something better."
        vex smug "Oh?"

    show protagonist neutral at left

    protagonist neutral "Where's Mia?"

    vex smug "Safe. Comfortable, even. I'm not a monster."
    vex smug "I just want what's mine. The Crown was supposed to go to the Order  not scatter across the countryside."
    vex smug "Give me the shard. I'll give you the girl. Everyone goes home."

    menu:
        "Refuse outright.":
            $ courage += 15
            protagonist determined "No. We're taking Mia and the shard."
            vex angry "Then we do this the hard way."
            play sound "audio/sfx_rumble.ogg"
            "The ground trembles. Vex raises her hands. This is going to be a fight."
            "... [player_name] and the group press forward through the assault."
            "It takes everything they have. But Vex retreats."
            $ rel_sera += 10
            $ courage += 5
            "Mia is found in a tent at the camp's edge  shaken but unhurt."

        "Negotiate  offer something else.":
            $ cunning += 15
            protagonist neutral "What do you actually want, Vex? Not the shard. The Crown whole? Power? Safety?"
            vex neutral "..."
            vex neutral "I want the Order restored. Magic recognised. Not hunted."
            protagonist neutral "Help us reunite the Crown the right way  and I'll advocate for the Order."
            vex angry "You'd say anything right now."
            protagonist neutral "Maybe. But you're smart enough to know a bad deal from a good one."
            vex neutral "...I'll release the girl. And I'll {i}watch{/i} what you do next."
            $ rel_sera += 15
            "Mia walks free. Vex disappears into the mist."

        "Let Sera speak for herself.":
            $ mercy += 10
            $ rel_sera += 20
            protagonist neutral "Sera. This is yours."
            sera nervous "Vex… you taught us that magic was a gift. Not a weapon."
            vex angry "The world made it a weapon "
            sera neutral "Then let's {i}unmake{/i} that. Help us. For Mia."
            "A long silence."
            vex sad "...The girl is in the tent."
            "Vex walks away without another word."

    hide vex
    "The second shard is recovered from the battlefield ruins."
    hide vex         
    hide sera        
    hide protagonist
    scene bg_harbor with dissolve
    play music random.choice(bgm_ambient) fadein 2.0 loop

    show protagonist neutral at left with dissolve

    "Veldport. A harbour city. The third and final shard is somewhere in the royal archives."

    show tobias happy at right with dissolve

    tobias happy "[player_name]! I got your message. And I brought the Lodestar upgrade."
    tobias happy "It now vibrates when a shard is within fifty feet. You're welcome."

    protagonist neutral "Tobias. I could kiss you."

    tobias happy "Please don't. But I {i}would{/i} appreciate being part of whatever this is."
    $ tobias_joined = True
    $ rel_tobias += 20
    $ sq_tobias_done = True

    scene bg_library with dissolve
    show protagonist neutral at left with dissolve

    "The royal archive. Massive. Guarded. The shard is {i}somewhere{/i} in here."

    

    guard "Halt. Authorised researchers only."

    menu:
        "Talk your way in.":
            $ cunning += 10
            protagonist neutral "Of course. We're here on behalf of the Maren Historical Society. Appointment under Aldric."
            guard "..."
            guard "I don't see it in the ledger."
            protagonist neutral "That's concerning. The Archivist will be very upset to hear about this administrative failure."
            guard "I  fine. Go through."
            

        "Find another way in.":
            $ cunning += 15
            "Tobias spots a delivery entrance."
            if tobias_joined:
                tobias happy "Loading dock. Shipment of books due this afternoon. We blend in, carry boxes."
                protagonist happy "Tobias, you beautiful genius."
            else:
                protagonist neutral "A loading dock. You slip in with the afternoon delivery."
            

        "Bribe the guard.":
            $ cunning += 5
            protagonist neutral "Look  we're not researchers. But we need to find something important. Name your price."
            guard "...Twenty gold."
            protagonist neutral "Ten."
            guard "Fifteen."
            protagonist neutral "Done."
            

    "The Lodestar leads you to a locked vault in the basement."
    "Inside  the third shard. Larger than the others. {i}Warmer.{/i}"

    if tobias_joined:
        tobias worried "It's reacting to the other two. [player_name]  if you hold all three together, I don't know what happens."
        protagonist neutral "One way to find out."

label act_four:

    scene bg_oracle with dissolve
    play music random.choice(bgm_tense) fadein 2.0 loop

    show oracle neutral at center with dissolve
    show protagonist neutral at left with dissolve

    oracle neutral "You found them all. I am… surprised. And impressed."

    protagonist neutral "You've been watching."

    oracle neutral "Always. Shard-bearer, I must tell you something before you choose."
    oracle neutral "The Crown was not made to rule. It was made to {i}bind{/i}  to seal an old wound between the kingdoms."
    oracle neutral "Restoring it will bring peace. Destroying it will bring freedom  and chaos."
    oracle neutral "Claiming it will bring order  under your hand, and your hand alone."

    if persistent.found_secret:
        oracle neutral "You found the mural. Then you already know all of this."
        protagonist neutral "I wanted to hear you say it."
        oracle neutral "Wise."

    if kael_joined:
        show kael neutral at right with dissolve
        kael neutral "[player_name]. Whatever you decide  I'll back you."
        if sq_kael_done:
            kael neutral "I've spent five years running from choices. You've reminded me that's not living."

    if rel_lyra >= 10:
        show lyra neutral at right with dissolve
        lyra neutral "I trust you. That's all I've got."

    if sera_joined:
        show sera neutral at right with dissolve
        if sq_sera_done:
            sera neutral "Whatever you choose  choose it honestly. That's all anyone can ask."

    hide kael
    hide lyra
    hide sera

    show maren neutral at right with dissolve

    maren neutral "I have one last thing to tell you, child."
    maren neutral "I'm dying. Slow. The shard's energy... it doesn't like old blood."
    maren neutral "I have weeks, maybe less."
    maren neutral "Don't mourn me. Just  choose well."

    $ maren_alive = False

    protagonist sad "Maren…"

    maren sad "I've had a long life. And I got to see something remarkable at the end of it."
    maren sad "You."

    hide maren

    oracle neutral "It is time, [player_name]. Three paths."
    oracle neutral "{b}Restore{/b}  return the Crown to the world. Bind the kingdoms in peace."
    oracle neutral "{b}Claim{/b}  take the Crown for yourself. Rule with power no one can challenge."
    oracle neutral "{b}Destroy{/b}  shatter the shards beyond repair. End the power forever."

    "Your journey has shaped you."
    "Courage: [courage] | Cunning: [cunning] | Mercy: [mercy]"
    menu:
        "Restore the Crown  give it back to the world." :
            jump act_five_hero

        "Claim the Crown  take what you've earned." :
            jump act_five_shadow

        "Destroy the shards  end this forever." :
            jump act_five_exile

label act_five_hero:

    scene bg_throne with dissolve
    play music random.choice(bgm_peaceful) fadein 3.0 loop

    show protagonist happy at left with dissolve

    "Restoring the Crown is not a moment. It is a {i}campaign.{/i}"
    "Three months of riding. Of convincing. Of arguing."
    "Of Kael standing at your back while you spoke to kings who'd rather fight."
    "Of Lyra scouting ahead so you never walked into an ambush."
    "Of Tobias quietly improving the Lodestar until it could detect hostile magic at a hundred yards."
    "Of Sera finding out  finally  that her sister Mia had a gift for diplomacy no one had noticed."

    if sq_lyra_done:
        show lyra happy at right with dissolve
        lyra happy "We found him."
        protagonist happy "Finn?"
        lyra happy "He's a cartographer in the capital. He's {i}fine.{/i} He's been writing letters  they just never got through."
        protagonist happy "Good."
        lyra happy "I'm going to kill him and then hug him for an hour."
        hide lyra

    show oracle neutral at center with dissolve

    oracle neutral "The five kings have agreed. They will accept the Crown's return."

    protagonist happy "And the conditions? No single king holds it?"

    oracle neutral "Jointly held. Jointly governed. As it was before."

    "You place all three shards in the Oracle's flame."
    play sound "audio/sfx_magic.ogg"
    "They {i}sing.{/i} They pull toward each other."
    "Then, slowly, the Crown reforms  whole and radiant and lighter than you expected."

    oracle neutral "You could take it. Even now."

    protagonist happy "I know."

    protagonist happy "That's why I won't."

    jump ending_hero

label ending_hero:
    $ persistent.ending_hero = True

    scene bg_white with fade
    nvl clear
    narrator "{b} THE HERO'S ENDING {/b}"
    narrator "{i}The Crown Restored{/i}"
    narrator ""
    narrator "The Shattered Crown was made whole."
    narrator "No single hand held it."
    narrator "No single voice commanded it."
    narrator ""
    narrator "The five kingdoms did not become friends overnight."
    narrator "Peace is never that simple."
    narrator "But the wars stopped."
    narrator "And in the stopping, people had space to try."
    narrator ""
    narrator "[player_name] asked for nothing."
    narrator "Which is, of course, exactly what made history remember them."
    narrator ""
    if kael_joined and sq_kael_done:
        narrator "Kael returned to the Ironguard. As its new commander."
        narrator "His first act was to formally apologise to the village of Halvenmoor."
        narrator "His second was to rebuild it."
        narrator ""
    if sq_lyra_done:
        narrator "Lyra and Finn travelled the world together."
        narrator "He made the maps. She made sure they survived long enough to use them."
        narrator ""
    if sera_joined and sq_sera_done:
        narrator "Sera and Mia founded the first open school of magic in four generations."
        narrator "They named it after Maren."
        narrator ""
    narrator "And [player_name]?"
    narrator "The road, again. Always the road."
    narrator "But lighter, this time."
    nvl clear
    jump epilogue

label act_five_shadow:

    scene bg_throne with dissolve
    play music random.choice(bgm_tense) fadein 2.0 loop

    show protagonist neutral at left with dissolve

    "You don't announce it. You don't declare yourself."
    "You simply… keep the Crown."
    "And the world, slowly, notices."

    if kael_joined:
        show kael angry at right with dissolve
        kael angry "This isn't what I signed up for."
        protagonist neutral "I know."
        kael angry "The kings won't accept this."
        protagonist neutral "They won't have a choice."
        kael sad "..."
        kael sad "Is that who you are now?"

        menu:
            "\"I'm who the world made me.\"":
                $ cunning += 5
                protagonist neutral "I didn't ask for the shard. But I have it. And someone has to decide."
                kael sad "Someone. Not anyone. You."
                kael sad "Fine. I'll stay. God help me."

            "\"Maybe. I don't know yet.\"":
                $ mercy += 5
                protagonist sad "I'm trying to do right, Kael. I'm just not sure what right looks like from here."
                kael sad "That's the most honest thing you've said."
                kael sad "I'll stay. But I'm watching."

        hide kael

    show oracle angry at center with dissolve
    oracle angry "You claim the Crown. I cannot stop you."
    protagonist neutral "No."
    oracle angry "But know this  power held alone corrodes. Always."
    protagonist neutral "Then I'll have to be careful."
    oracle neutral "They all say that."
    hide oracle

    jump ending_shadow

label ending_shadow:
    $ persistent.ending_shadow = True

    scene bg_black with fade
    nvl clear
    narrator "{b} THE SHADOW ENDING {/b}"
    narrator "{i}The Crown Claimed{/i}"
    narrator ""
    narrator "No war was declared without [player_name]'s word."
    narrator "No treaty was signed without their seal."
    narrator ""
    narrator "Crime fell. Famine fell. Three border conflicts ended in months."
    narrator "The numbers were, by any measure, good."
    narrator ""
    narrator "The people were not sure what to call what they lived in."
    narrator "Not a kingdom. Not an empire."
    narrator "Something new. Something with no name yet."
    narrator ""
    narrator "Kael remained. Watchful."
    narrator "Lyra left. She sent letters."
    narrator "Sera stayed, and kept the school of magic alive  under careful conditions."
    narrator ""
    narrator "Whether [player_name] became a tyrant or a guardian,"
    narrator "history would argue about for centuries."
    narrator ""
    narrator "That argument, at least, meant they remembered."
    nvl clear
    jump epilogue

label act_five_exile:

    scene bg_cliffside with dissolve
    play music random.choice(bgm_peaceful) fadein 3.0 loop

    show protagonist sad at left with dissolve

    "You take the shards to the highest point of the Spire."
    "The wind is cold. The view is endless."

    if kael_joined:
        show kael neutral at right with dissolve
        kael neutral "You're sure?"
        protagonist sad "The mural said it best. Some power shouldn't exist."
        kael neutral "The kingdoms will fall without the binding."
        protagonist sad "Or they'll learn to stand on their own."
        kael neutral "That's optimistic."
        protagonist sad "Someone has to be."
        hide kael

    if rel_lyra >= 10:
        show lyra sad at right with dissolve
        lyra sad "No Crown. No power. Just… people."
        protagonist sad "Just people."
        lyra sad "God, I hope you're right."
        hide lyra

    "You hold all three shards over the edge."
    "They pull toward each other  wanting to be whole."
    "You let them pull."
    "Then you open your hands."

    play sound "audio/sfx_shatter.ogg"

    "The shards fall."
    "They don't hit the ground. They dissolve. They become light. Then nothing."

    "The Oracle appears beside you."
    oracle neutral "It is done."
    protagonist sad "Is it? Will it hold?"
    oracle neutral "The binding is broken. What the kingdoms do now is their own doing."
    protagonist sad "Good. It should have been all along."
    oracle neutral "You are a strange person, [player_name]."
    protagonist sad "I get that a lot."

    jump ending_exile

label ending_exile:
    $ persistent.ending_exile = True

    scene bg_cliffside with fade
    nvl clear
    narrator "{b} THE EXILE'S ENDING {/b}"
    narrator "{i}The Crown Destroyed{/i}"
    narrator ""
    narrator "The first year was hard."
    narrator "Old grievances resurfaced. Two minor wars sparked and sputtered."
    narrator "People mourned the loss of something they hadn't known they relied on."
    narrator ""
    narrator "The second year was harder."
    narrator "But different-harder. Building-harder."
    narrator "The kingdoms negotiated. Slowly. Badly. But they did."
    narrator ""
    narrator "By the fifth year, three of the five had a working alliance."
    narrator "Not because of magic. Because they had to."
    narrator ""
    narrator "[player_name] watched it from a distance."
    narrator "Lyra came with them  of course she did."
    if sq_lyra_done:
        narrator "Finn joined them eventually. He made maps of places no one had named yet."
    narrator ""
    narrator "Kael went home. Finally."
    if sq_kael_done:
        narrator "The village forgave him. It took time. It happened."
    narrator ""
    narrator "Sera built her school. No conditions this time."
    narrator ""
    narrator "[player_name] never stopped walking."
    narrator "Some people are just like that."
    nvl clear
    jump epilogue

label epilogue:

    scene bg_village with dissolve
    play music random.choice(bgm_peaceful) fadein 3.0 loop

    nvl clear
    narrator " {b}EPILOGUE{/b} "
    narrator ""

    if persistent.ending_hero and persistent.ending_shadow and persistent.ending_exile:
        narrator "You have walked every road."
        narrator "Seen every face of the Crown."
        narrator ""
        narrator "Hero. Shadow. Exile."
        narrator ""
        narrator "None of them were wrong. None of them were right."
        narrator "They were just {i}yours.{/i}"
        narrator ""
        narrator "That's all any story can be."
    else:
        narrator "Endings unlocked:"
        if persistent.ending_hero:
            narrator "  ✦  The Crown Restored  (Hero's Ending)"
        else:
            narrator "  ◌  The Crown Restored   not yet seen"
        if persistent.ending_shadow:
            narrator "  ✦  The Crown Claimed   (Shadow Ending)"
        else:
            narrator "  ◌  The Crown Claimed    not yet seen"
        if persistent.ending_exile:
            narrator "  ✦  The Crown Destroyed (Exile's Ending)"
        else:
            narrator "  ◌  The Crown Destroyed  not yet seen"
        narrator ""
        if persistent.found_secret:
            narrator "  ✦  Secret: The Mural  found"
        else:
            narrator "  ◌  Secret: The Mural  not yet found"

    nvl clear
    narrator "Side quests completed this run:"
    if sq_lyra_done:
        narrator "  ✦  Lyra's Brother  resolved"
    if sq_kael_done:
        narrator "  ✦  Kael's Redemption  resolved"
    if sq_sera_done:
        narrator "  ✦  Sera's Debt  resolved"
    if sq_tobias_done:
        narrator "  ✦  Tobias's Invention  used"

    nvl clear
    narrator "Playthrough [persistent.runs] complete."
    narrator ""
    narrator "{i}Thank you for playing The Shattered Crown.{/i}"
    nvl clear

    return