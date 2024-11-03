import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ LAA, 2018-04-19
# https://www.baseball-reference.com/boxes/ANA/ANA201804190.shtml
# https://www.mlb.com/gameday/red-sox-vs-angels/2018/04/19/529684/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-19 22:08-01:43 +1",
        "at": "Angel Stadium, Anaheim, CA",
        "att": "36,253",
        "temp": "62F, Clear",
        "wind": "7mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                7: "Christian Vázquez",
                12: "Brock Holt",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                5: "Tzu-Wei Lin",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "8"],
                [13, "0"],
                [28, "7"],
                [18, "3"],
                [11, "5"],
                [36, "4"],
                [7, "2"],
                [12, "6"],
            ],
            "bench": [
                [5, "OF"],
                [23, "C"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [39, 22, 41, 61, 37, 24, 46, 76, 64, 56, 32],
        },
        "home": {
            "team": "Los Angeles Angels",
            "starter": 35,
            "roster": {
                # Lineup
                3: "Ian Kinsler",
                27: "Mike Trout",
                8: "Justin Upton",
                5: "Albert Pujols",
                2: "Andrelton Simmons",
                17: "Shohei Ohtani",
                7: "Zack Cozart",
                24: "Chris Young",
                12: "Martín Maldonado",
                # Starting pitcher
                35: "Nick Tropeano",
                # Bench
                44: "René Rivera",
                18: "Luis Valbuena",
                56: "Kole Calhoun",
                19: "Jefry Marte",
                # Bullpen
                45: "Tyler Skaggs",
                48: "Jose Alvarez",
                65: "Luke Bard",
                32: "Cam Bedrosian",
                53: "Blake Parker",
                39: "Keynan Middleton",
                46: "Blake Wood",
                28: "Andrew Heaney",
                33: "Jim Johnson",
                25: "Noé Ramirez",
                43: "Garrett Richards",
            },
            "lefties": [45, 48, 28],
            "lineup": [
                [3, "4"],
                [27, "8"],
                [8, "7"],
                [5, "3"],
                [2, "6"],
                [17, "0"],
                [7, "5"],
                [24, "9"],
                [12, "2"],
            ],
            "bench": [
                [44, "C"],
                [18, "3B"],
                [56, "RF"],
                [19, "1B"],
            ],
            "bullpen": [45, 48, 65, 32, 53, 39, 46, 28, 33, 25, 43],
        },
        "umpires": {
            "HP": "Jerry Layne",
            "1B": "Greg Gibson",
            "2B": "Vic Carapazza",
            "3B": "Jordan Baker",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: LAA #35 Nick Tropeano
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("s")
t1.out("G6-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("f f b b b b")
t1.reach("BB")
t1.thrown_out(2, "28 DP6-4-3", 2, 35)

# 4. BOS #28 J.D. Martinez (X - X - 13)
t1.new_ab()
t1.pitch_list("c s")
t1.out("DP6-4-3")


# Bot 1st
# Pitching: BOS #57 Eduardo Rodriguez
b1 = game.new_inning()

# 1. LAA #3  Ian Kinsler (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("F8")

# 2. LAA #27 Mike Trout (X - X - X)
b1.new_ab()
b1.pitch_list("c f f b b s")
b1.out("K")

# 3. LAA #8  Justin Upton (X - X - X)
b1.new_ab()
b1.pitch_list("b c s f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: LAA #35 Nick Tropeano
t2 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("c s b c")
t2.out("!K")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.hit(1)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t2.new_ab()
t2.pitch_list("b 1 b f f")
t2.out("P2")

# 8. BOS #7  Christian Vázquez (X - X - 11)
t2.new_ab()
t2.pitch_list("f 1 s")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #57 Eduardo Rodriguez
b2 = game.new_inning()

# 4. LAA #5  Albert Pujols (X - X - X)
b2.new_ab()
b2.pitch_list("f b b s")
b2.out("G6-3")

# 5. LAA #2  Andrelton Simmons (X - X - X)
b2.new_ab()
b2.pitch_list("c b f b b b")
b2.reach("BB")
b2.advance(3, "17 G6-3")
b2.advance(4, "7 1B")

# 6. LAA #17 Shohei Ohtani (X - X - 2)
b2.new_ab()
b2.pitch_list("s d")
b2.out("G6-3")

# 7. LAA #7  Zack Cozart (2 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b f s f f b")
b2.hit(1, rbis=1)

# 8. LAA #24 Chris Young (X - X - 7)
b2.new_ab()
b2.pitch_list("c f")
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: LAA #35 Nick Tropeano
t3 = game.new_inning()

# 9. BOS #12 Brock Holt (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c c")
t3.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c c s")
t3.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("c s b b b t")
t3.out("KT")


# Bot 3rd
# Pitching: BOS #57 Eduardo Rodriguez
b3 = game.new_inning()

# 9. LAA #12 Martín Maldonado (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.out("G5-3")

# 1. LAA #3  Ian Kinsler (X - X - X)
b3.new_ab()
b3.pitch_list("s")
b3.hit(1)
b3.thrown_out(2, "27 FC5-4", 2, 57)

# 2. LAA #27 Mike Trout (X - X - 3)
b3.new_ab()
b3.pitch_list("c f b f b")
b3.reach("FC5-4")
b3.thrown_out(2, "8 FC5-4", 3, 57)

# 3. LAA #8  Justin Upton (X - X - 27)
b3.new_ab()
b3.pitch_list("f 1 b b")
b3.reach("FC5-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: LAA #35 Nick Tropeano
t4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("b f b b f b")
t4.reach("BB")
t4.advance(4, "28 2B")

# 4. BOS #28 J.D. Martinez (X - X - 13)
t4.new_ab()
t4.pitch_list("d b c c f")
t4.hit(2, rbis=1)
t4.advance(4, "11 1B")

# 5. BOS #18 Mitch Moreland (X - 28 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("s")
t4.out("G5-3")

# 6. BOS #11 Rafael Devers (X - 28 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("d d")
t4.hit(1, rbis=1)
t4.thrown_out(2, "9-3-6", 2, 35)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("c c")
t4.out("(F)P5")


# Bot 4th
# Pitching: BOS #57 Eduardo Rodriguez
b4 = game.new_inning()

# 4. LAA #5  Albert Pujols (X - X - X)
b4.new_ab()
b4.pitch_list("c s")
b4.out("P6")

# 5. LAA #2  Andrelton Simmons (X - X - X)
b4.new_ab()
b4.pitch_list("s b b b c b")
b4.reach("BB")

# 6. LAA #17 Shohei Ohtani (X - X - 2)
b4.new_ab()
b4.pitch_list("b c s s")
b4.out("K")

# 7. LAA #7  Zack Cozart (X - X - 2)
b4.new_ab()
b4.out("(F)P3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: LAA #35 Nick Tropeano
t5 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("G6-3")

# 9. BOS #12 Brock Holt (X - X - X)
t5.new_ab()
t5.hit(1)
t5.thrown_out(2, "50 DP4-6-3", 2, 35)

# 1. BOS #50 Mookie Betts (X - X - 12)
t5.new_ab()
t5.pitch_list("1 s d 1 1 d f 1")
t5.out("DP4-6-3")


# Bot 5th
# Pitching: BOS #57 Eduardo Rodriguez
b5 = game.new_inning()

# 8. LAA #24 Chris Young (X - X - X)
b5.new_ab()
b5.pitch_list("s b c b b")
b5.hit(4)

# 9. LAA #12 Martín Maldonado (X - X - X)
b5.new_ab()
b5.pitch_list("c s s")
b5.out("K")

# 1. LAA #3  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("F7")

# 2. LAA #27 Mike Trout (X - X - X)
b5.new_ab()
b5.pitch_list("c b b")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: LAA #35 Nick Tropeano
t6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("b c f b")
t6.hit(4)

# 3. BOS #13 Hanley Ramirez (X - X - X)
t6.new_ab()
t6.pitch_list("f b b")
t6.out("F8")

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("b s b c b f f")
t6.hit(1)
t6.advance(3, "18 2B")
t6.advance(4, "11 1B")

# Pitching change (LAA): #48 Jose Alvarez replaces #35 Nick Tropeano
t6.pitching_substitution(48)

# 5. BOS #18 Mitch Moreland (X - X - 28)
t6.new_ab()
t6.pitch_list("f")
t6.hit(2)
t6.advance(3, "11 1B")

# 6. BOS #11 Rafael Devers (28 - 18 - X)
t6.new_ab(is_risp=True)
t6.hit(1, rbis=1)
t6.thrown_out(2, "36 DP6-4-3", 2, 33)

# Pitching change (LAA): #33 Jim Johnson replaces #48 Jose Alvarez
t6.pitching_substitution(33)

# 7. BOS #36 Eduardo Núñez (18 - X - 11)
t6.new_ab(is_risp=True)
t6.pitch_list("f b f")
t6.out("DP6-4-3")


# Bot 6th
# Pitching: BOS #57 Eduardo Rodriguez
b6 = game.new_inning()

# 3. LAA #8  Justin Upton (X - X - X)
b6.new_ab()
b6.pitch_list("b s b s f b")
b6.out("F9")

# 4. LAA #5  Albert Pujols (X - X - X)
b6.new_ab()
b6.pitch_list("b b s")
b6.out("(F)P3")

# 5. LAA #2  Andrelton Simmons (X - X - X)
b6.new_ab()
b6.pitch_list("b c b f b b")
b6.reach("BB")

# 6. LAA #17 Shohei Ohtani (X - X - 2)
b6.new_ab()
b6.pitch_list("s s f f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: LAA #33 Jim Johnson
t7 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b")
t7.out("G5-3")

# 9. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(2)

# 1. BOS #50 Mookie Betts (X - 12 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c b f d b s")
t7.out("K")

# 2. BOS #16 Andrew Benintendi (X - 12 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b b")
t7.out("F7")


# Bot 7th
# Pitching: BOS #37 Heath Hembree
b7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #57 Eduardo Rodriguez
b7.pitching_substitution(37)

# 7. LAA #7  Zack Cozart (X - X - X)
b7.new_ab()
b7.pitch_list("b b c")
b7.error(5)
b7.reach("E5")
b7.advance(2, "56 WP")
b7.advance(3, "56 G4-3")

# Offensive change (LAA): Pinch-hitter #56 Kole Calhoun replaces #24 Chris Young, batting 8th
b7.offensive_substitution(8, 56, "PH")

# 8. LAA #56 Kole Calhoun (X - X - 7)
b7.new_ab(is_risp=True)
b7.pitch_list("b s")
b7.wp()
b7.out("G4-3")

# Offensive change (LAA): Pinch-hitter #18 Luis Valbuena replaces #12 Martín Maldonado, batting 9th
b7.offensive_substitution(9, 18, "PH")

# 9. LAA #18 Luis Valbuena (7 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f b s c")
b7.out("!K")

# 1. LAA #3  Ian Kinsler (7 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f b f f")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: LAA #46 Blake Wood
t8 = game.new_inning()

# Pitching change (LAA): #46 Blake Wood replaces #33 Jim Johnson
t8.pitching_substitution(46)

# Defensive switch (LAA): #56 Kole Calhoun moves to RF
t8.defensive_switch(56, "9")

# Defensive change (LAA): #44 René Rivera replaces #18 Luis Valbuena (PH), playing C, batting 9th
t8.defensive_substitution(9, 44, "2")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t8.new_ab()
t8.pitch_list("b c f f")
t8.hit(1)
t8.advance(3, "28 2B")
t8.advance(4, "18 SF7")

# 4. BOS #28 J.D. Martinez (X - X - 13)
t8.new_ab()
t8.hit(2)
# Offensive change (BOS): Pinch-runner #19 Jackie Bradley Jr. replaces #28 J.D. Martinez
t8.offensive_substitution(4, 19, "PR")
t8.atbase("PR")
t8.advance(3, "36 FC6")

# 5. BOS #18 Mitch Moreland (13 - 28 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b s")
t8.out("SF7", rbis=1)

# 6. BOS #11 Rafael Devers (X - 19 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("v v v v")
t8.reach("IBB")
t8.thrown_out(2, "36 FC6", 2, 46)

# 7. BOS #36 Eduardo Núñez (X - 19 - 11)
t8.new_ab(is_risp=True)
t8.pitch_list("b")
t8.reach("FC6")
t8.thrown_out(2, "7 FC6-4", 3, 46)

# 8. BOS #7  Christian Vázquez (19 - X - 36)
t8.new_ab(is_risp=True)
t8.pitch_list("d")
t8.reach("FC6-4")


# Bot 8th
# Pitching: BOS #39 Carson Smith
b8 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #37 Heath Hembree
b8.pitching_substitution(39)

# Defensive switch (BOS): #16 Andrew Benintendi moves to LF
b8.defensive_switch(16, "7")

# Defensive switch (BOS): #19 Jackie Bradley Jr. moves to CF
b8.defensive_switch(19, "8")

# 2. LAA #27 Mike Trout (X - X - X)
b8.new_ab()
b8.pitch_list("b b c f b")
b8.out("F8")

# 3. LAA #8  Justin Upton (X - X - X)
b8.new_ab()
b8.pitch_list("c s c")
b8.out("!K")

# 4. LAA #5  Albert Pujols (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("P5")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: LAA #25 Noé Ramirez
t9 = game.new_inning()

# Pitching change (LAA): #25 Noé Ramirez replaces #46 Blake Wood
t9.pitching_substitution(25)

# 9. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("b c b")
t9.error(5)
t9.reach("E5")
t9.advance(3, "50 2B")
t9.advance("U", "16 1B")

# 1. BOS #50 Mookie Betts (X - X - 12)
t9.new_ab()
t9.pitch_list("b 1")
t9.hit(2)
t9.advance(4, "16 1B")

# 2. BOS #16 Andrew Benintendi (12 - 50 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("d b")
t9.hit(1, rbis=2)
t9.advance(2, "T")
t9.advance(3, "13 F8")

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c f b b b")
t9.out("F8")

# 4. BOS #19 Jackie Bradley Jr. (16 - X - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.reach("HBP")

# Pitching change (LAA): #65 Luke Bard replaces #25 Noé Ramirez
t9.pitching_substitution(65)

# 5. BOS #18 Mitch Moreland (16 - X - 19)
t9.new_ab(is_risp=True)
t9.pitch_list("f f s")
t9.out("K")

# 6. BOS #11 Rafael Devers (16 - X - 19)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.out("F7")


# Bot 9th
# Pitching: BOS #56 Joe Kelly
b9 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #39 Carson Smith
b9.pitching_substitution(56)

# 5. LAA #2  Andrelton Simmons (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c c")
b9.hit(1)
b9.advance(2, "17 DI")

# 6. LAA #17 Shohei Ohtani (X - X - 2)
b9.new_ab(is_risp=True)
b9.pitch_list("b f b f f s")
b9.out("K")

# 7. LAA #7  Zack Cozart (X - 2 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c b b c b")
b9.out("L9")

# 8. LAA #56 Kole Calhoun (X - 2 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c f b s")
b9.out("K")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57, is_away_team=True)

# Loser team: LAA
# LP: LAA #35 Nick Tropeano
game.losing_pitcher(35)

# print(game)
game.generate_scorecard()
