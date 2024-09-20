import os
from baseball_scorecard.baseball_scorecard import Scorecard

# LAA @ BOS, 2018-06-26
# https://www.baseball-reference.com/boxes/BOS/BOS201806260.shtml
# https://www.mlb.com/gameday/angels-vs-red-sox/2018/06/26/530590/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-26 19:12-22:06",
        "at": "Fenway Park, Boston, MA",
        "att": "37,366",
        "temp": "76F, Clear",
        "wind": "18mph, Out To LF",
        "away": {
            "team": "Los Angeles Angels",
            "starter": 46,
            "roster": {
                # Lineup
                3: "Ian Kinsler",
                27: "Mike Trout",
                8: "Justin Upton",
                5: "Albert Pujols",
                2: "Andrelton Simmons",
                12: "Martín Maldonado",
                6: "David Fletcher",
                24: "Chris Young",
                59: "Michael Hermosillo",
                # Starting pitcher
                46: "John Lamb",
                # Bench
                18: "Luis Valbuena",
                56: "Kole Calhoun",
                10: "José Briceño",
                # Bullpen
                68: "Deck McGuire",
                58: "Akeel Morris",
                45: "Tyler Skaggs",
                48: "Jose Alvarez",
                64: "Félix Peña",
                32: "Cam Bedrosian",
                51: "Jaime Barria",
                53: "Blake Parker",
                57: "Hansel Robles",
                38: "Justin Anderson",
                28: "Andrew Heaney",
                25: "Noé Ramirez",
            },
            "lefties": [46, 45, 48, 28],
            "lineup": [
                [3, "4"],
                [27, "0"],
                [8, "7"],
                [5, "3"],
                [2, "6"],
                [12, "2"],
                [6, "5"],
                [24, "8"],
                [59, "9"],
            ],
            "bench": [
                [18, "3B"],
                [56, "RF"],
                [10, "C"],
            ],
            "bullpen": [68, 58, 45, 48, 64, 32, 51, 53, 57, 38, 28, 25],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                5: "Tzu-Wei Lin",
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [5, "OF"],
                [12, "2B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 44, 22, 41, 61, 37, 46, 76, 65, 56, 32],
        },
        "umpires": {
            "HP": "Chris Segal",
            "1B": "Gabe Morales",
            "2B": "Ed Hickox",
            "3B": "Jerry Meals",
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
# Pitching: BOS #24 David Price
t1 = game.new_inning()

# 1. LAA #3  Ian Kinsler (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.out("P4")

# 2. LAA #27 Mike Trout (X - X - X)
t1.new_ab()
t1.pitch_list("c s")
t1.out("F8")

# 3. LAA #8  Justin Upton (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.out("F9")


# Bot 1st
# Pitching: LAA #46 John Lamb
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("L9")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.hit(2)

# 4. BOS #2  Xander Bogaerts (X - 28 - X)
b1.new_ab()
b1.pitch_list("b c")
b1.out("F9")

# 5. BOS #18 Mitch Moreland (X - 28 - X)
b1.new_ab()
b1.pitch_list("c b s s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 4. LAA #5  Albert Pujols (X - X - X)
t2.new_ab()
t2.pitch_list("c s b s")
t2.out("K")

# 5. LAA #2  Andrelton Simmons (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("L9")

# 6. LAA #12 Martín Maldonado (X - X - X)
t2.new_ab()
t2.pitch_list("b b s f t")
t2.out("KT")


# Bot 2nd
# Pitching: LAA #46 John Lamb
b2 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.hit(1)
b2.error(4)
b2.advance(2, "11 E4")
b2.advance(3, "7 G6-3")
b2.advance("U", "19 2B")

# 7. BOS #11 Rafael Devers (X - X - 36)
b2.new_ab()
b2.pitch_list("1 f b c")
b2.reach("FC4")
b2.advance(2, "7 G6-3")
b2.advance(4, "19 2B")

# 8. BOS #7  Christian Vázquez (X - 36 - 11)
b2.new_ab()
b2.pitch_list("c")
b2.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (36 - 11 - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(2, rbis=2)
b2.advance(4, "16 2B")

# 1. BOS #50 Mookie Betts (X - 19 - X)
b2.new_ab()
b2.pitch_list("c b b b d")
b2.reach("BB")
b2.advance(3, "16 2B")
b2.advance("U", "18 1B")

# 2. BOS #16 Andrew Benintendi (X - 19 - 50)
b2.new_ab()
b2.pitch_list("t b b b 2 f")
b2.hit(2, rbis=1)
b2.advance(3, "18 1B")

# 3. BOS #28 J.D. Martinez (50 - 16 - X)
b2.new_ab()
b2.pitch_list("f b f f c")
b2.out("!K")

# 4. BOS #2  Xander Bogaerts (50 - 16 - X)
b2.new_ab()
b2.pitch_list("v v v v")
b2.reach("IBB")
b2.advance(2, "18 1B")

# 5. BOS #18 Mitch Moreland (50 - 16 - 2)
b2.new_ab()
b2.hit(1, rbis=1)

# Pitching change (LAA): #68 Deck McGuire replaces #46 John Lamb
b2.pitching_substitution(68)

# 6. BOS #36 Eduardo Núñez (16 - 2 - 18)
b2.new_ab()
b2.out("P2")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 7. LAA #6  David Fletcher (X - X - X)
t3.new_ab()
t3.pitch_list("b f b b")
t3.out("G6-3")

# 8. LAA #24 Chris Young (X - X - X)
t3.new_ab()
t3.pitch_list("b f b")
t3.hit(4)

# 9. LAA #59 Michael Hermosillo (X - X - X)
t3.new_ab()
t3.pitch_list("c s f b f c")
t3.out("!K")

# 1. LAA #3  Ian Kinsler (X - X - X)
t3.new_ab()
t3.pitch_list("b b")
t3.hit(1)
t3.advance(3, "27 1B")

# 2. LAA #27 Mike Trout (X - X - 3)
t3.new_ab()
t3.pitch_list("c b f b b 1")
t3.hit(1)
t3.advance(2, "8 WP")

# 3. LAA #8  Justin Upton (3 - X - 27)
t3.new_ab()
t3.pitch_list("c b b b b")
t3.wp()
t3.reach("BB")

# 4. LAA #5  Albert Pujols (3 - 27 - 8)
t3.new_ab()
t3.pitch_list("c b b f")
t3.out("G5-3")


# Bot 3rd
# Pitching: LAA #68 Deck McGuire
b3 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F9")

# 8. BOS #7  Christian Vázquez (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.out("G1-6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c")
b3.hit(4)

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("b c b b b")
b3.reach("BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b3.new_ab()
b3.pitch_list("1 1 b s b")
b3.out("L3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 5. LAA #2  Andrelton Simmons (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b c")
t4.out("G6-3")

# 6. LAA #12 Martín Maldonado (X - X - X)
t4.new_ab()
t4.out("G5-3")

# 7. LAA #6  David Fletcher (X - X - X)
t4.new_ab()
t4.pitch_list("b b b b")
t4.reach("BB")

# 8. LAA #24 Chris Young (X - X - 6)
t4.new_ab()
t4.pitch_list("b f f c")
t4.out("!K")


# Bot 4th
# Pitching: LAA #68 Deck McGuire
b4 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G6-3")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.out("F8")

# 5. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G3-1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 9. LAA #59 Michael Hermosillo (X - X - X)
t5.new_ab()
t5.pitch_list("l c c")
t5.out("!K")

# 1. LAA #3  Ian Kinsler (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.hit(1)
t5.thrown_out(2, "27 FC5-4", 2, 24)

# 2. LAA #27 Mike Trout (X - X - 3)
t5.new_ab()
t5.pitch_list("b")
t5.reach("FC5-4")

# 3. LAA #8  Justin Upton (X - X - 27)
t5.new_ab()
t5.pitch_list("b b f c c")
t5.out("!K")


# Bot 5th
# Pitching: LAA #68 Deck McGuire
b5 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("b f b c c")
b5.out("!K")

# 7. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.out("F9")

# 8. BOS #7  Christian Vázquez (X - X - X)
b5.new_ab()
b5.hit(4)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 4. LAA #5  Albert Pujols (X - X - X)
t6.new_ab()
t6.pitch_list("c b f c")
t6.out("!K")

# 5. LAA #2  Andrelton Simmons (X - X - X)
t6.new_ab()
t6.pitch_list("b f b c")
t6.hit(1)

# 6. LAA #12 Martín Maldonado (X - X - 2)
t6.new_ab()
t6.pitch_list("b b c b s")
t6.out("(F)P3")

# 7. LAA #6  David Fletcher (X - X - 2)
t6.new_ab()
t6.pitch_list("c b")
t6.out("F7")


# Bot 6th
# Pitching: LAA #68 Deck McGuire
b6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("b c b c")
b6.out("L7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b f f")
b6.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(4)

# 4. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c f b f b b f")
b6.hit(2)

# Pitching change (LAA): #58 Akeel Morris replaces #68 Deck McGuire
b6.pitching_substitution(58)

# 5. BOS #18 Mitch Moreland (X - 2 - X)
b6.new_ab()
b6.pitch_list("b s b b c")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #24 David Price
t7.pitching_substitution(37)

# 8. LAA #24 Chris Young (X - X - X)
t7.new_ab()
t7.pitch_list("f b b c s")
t7.out("K")

# 9. LAA #59 Michael Hermosillo (X - X - X)
t7.new_ab()
t7.pitch_list("f c b f")
t7.out("P4")

# 1. LAA #3  Ian Kinsler (X - X - X)
t7.new_ab()
t7.pitch_list("c b b f s")
t7.out("K")


# Bot 7th
# Pitching: LAA #58 Akeel Morris
b7 = game.new_inning()

# Defensive change (LAA): #56 Kole Calhoun replaces #8 Justin Upton (LF), playing RF, batting 3rd
b7.defensive_substitution(3, 56, "9")

# Defensive change (LAA): #18 Luis Valbuena replaces #2 Andrelton Simmons (SS), playing 3B, batting 5th
b7.defensive_substitution(5, 18, "5")

# Defensive switch (LAA): #6 David Fletcher moves to SS
b7.defensive_switch(6, "6")

# Defensive switch (LAA): #59 Michael Hermosillo moves to LF
b7.defensive_switch(59, "7")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #36 Eduardo Núñez, batting 6th
b7.offensive_substitution(6, 23, "PH")

# 6. BOS #23 Blake Swihart (X - X - X)
b7.new_ab()
b7.pitch_list("s b s b b")
b7.hit(1)
b7.advance(3, "7 2B")
b7.advance(4, "19 1B")

# 7. BOS #11 Rafael Devers (X - X - 23)
b7.new_ab()
b7.pitch_list("b b s s f s")
b7.out("K")

# 8. BOS #7  Christian Vázquez (X - X - 23)
b7.new_ab()
b7.pitch_list("d")
b7.hit(2)
b7.advance(3, "19 1B")

# 9. BOS #19 Jackie Bradley Jr. (23 - 7 - X)
b7.new_ab()
b7.hit(1, rbis=1)

# 1. BOS #50 Mookie Betts (7 - X - 19)
b7.new_ab()
b7.pitch_list("b")
b7.out("F7")

# Offensive change (BOS): Pinch-hitter #5 Tzu-Wei Lin replaces #16 Andrew Benintendi, batting 2nd
b7.offensive_substitution(2, 5, "PH")

# 2. BOS #5  Tzu-Wei Lin (7 - X - 19)
b7.new_ab()
b7.pitch_list("b b c c f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #44 Brandon Workman
t8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #37 Heath Hembree
t8.pitching_substitution(44)

# Defensive switch (BOS): #5 Tzu-Wei Lin moves to 2B
t8.defensive_switch(5, "4")

# Defensive change (BOS): #12 Brock Holt replaces #18 Mitch Moreland (1B), playing 1B, batting 5th
t8.defensive_substitution(5, 12, "3")

# Defensive switch (BOS): #23 Blake Swihart moves to LF
t8.defensive_switch(23, "7")

# 2. LAA #27 Mike Trout (X - X - X)
t8.new_ab()
t8.pitch_list("b f f b f t")
t8.out("KT")

# 3. LAA #56 Kole Calhoun (X - X - X)
t8.new_ab()
t8.pitch_list("c b c f b b")
t8.out("L8")

# 4. LAA #5  Albert Pujols (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("F8")


# Bot 8th
# Pitching: LAA #58 Akeel Morris
b8 = game.new_inning()

# Defensive change (LAA): #10 José Briceño replaces #5 Albert Pujols (1B), playing 1B, batting 4th
b8.defensive_substitution(4, 10, "3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.out("F8")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b c b f b b")
b8.reach("BB")
b8.advance(3, "12 2B")
b8.thrown_out(4, "23 2", 2, 58)

# 5. BOS #12 Brock Holt (X - X - 2)
b8.new_ab()
b8.hit(2)
b8.advance(3, "23 2")

# 6. BOS #23 Blake Swihart (2 - 12 - X)
b8.new_ab()
b8.pitch_list("c d")
b8.out("L9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #65 Justin Haley
t9 = game.new_inning()

# Pitching change (BOS): #65 Justin Haley replaces #44 Brandon Workman
t9.pitching_substitution(65)

# 5. LAA #18 Luis Valbuena (X - X - X)
t9.new_ab()
t9.pitch_list("c b s f f f")
t9.out("F9")

# 6. LAA #12 Martín Maldonado (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G2-3")

# 7. LAA #6  David Fletcher (X - X - X)
t9.new_ab()
t9.pitch_list("b b f b")
t9.out("P4")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24)

# Loser team: LAA
# LP: LAA #46 John Lamb
game.losing_pitcher(46, is_away_team=True)

# print(game)
game.generate_scorecard()
