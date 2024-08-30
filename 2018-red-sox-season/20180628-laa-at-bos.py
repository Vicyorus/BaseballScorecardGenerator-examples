import os
from baseball_scorecard.baseball_scorecard import Scorecard

# LAA @ BOS, 2018-06-28
# https://www.baseball-reference.com/boxes/BOS/BOS201806280.shtml
# https://www.mlb.com/gameday/angels-vs-red-sox/2018/06/28/530617/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-28 19:11-22:17",
        "at": "Fenway Park, Boston, MA",
        "att": "36,992",
        "temp": "74F, Cloudy",
        "wind": "13mph, Out To LF",
        "away": {
            "team": "Los Angeles Angels",
            "starter": 51,
            "roster": {
                # Lineup
                3: "Ian Kinsler",
                27: "Mike Trout",
                8: "Justin Upton",
                5: "Albert Pujols",
                2: "Andrelton Simmons",
                6: "David Fletcher",
                24: "Chris Young",
                10: "José Briceño",
                59: "Michael Hermosillo",
                # Starting pitcher
                51: "Jaime Barria",
                # Bench
                12: "Martín Maldonado",
                18: "Luis Valbuena",
                56: "Kole Calhoun",
                # Bullpen
                60: "Eduardo Paredes",
                68: "Deck McGuire",
                45: "Tyler Skaggs",
                48: "Jose Alvarez",
                64: "Félix Peña",
                32: "Cam Bedrosian",
                53: "Blake Parker",
                57: "Hansel Robles",
                67: "Taylor Cole",
                38: "Justin Anderson",
                28: "Andrew Heaney",
                25: "Noé Ramirez",
            },
            "lefties": [45, 48, 28],
            "lineup": [
                [3, "4"],
                [27, "0"],
                [8, "7"],
                [5, "3"],
                [2, "6"],
                [6, "5"],
                [24, "8"],
                [10, "2"],
                [59, "9"],
            ],
            "bench": [
                [12, "C"],
                [18, "3B"],
                [56, "RF"],
            ],
            "bullpen": [60, 68, 45, 48, 64, 32, 53, 57, 67, 38, 28, 25],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                12: "Brock Holt",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                5: "Tzu-Wei Lin",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [61, 57, 41, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [12, "4"],
                [11, "5"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [5, "OF"],
                [36, "SS"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 44, 22, 41, 37, 24, 46, 76, 65, 56, 32],
        },
        "umpires": {
            "HP": "Ed Hickox",
            "1B": "Jerry Meals",
            "2B": "Chris Segal",
            "3B": "Gabe Morales",
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
# Pitching: BOS #61 Brian Johnson
t1 = game.new_inning()

# 1. LAA #3  Ian Kinsler (X - X - X)
t1.new_ab()
t1.out("G6-3")

# 2. LAA #27 Mike Trout (X - X - X)
t1.new_ab()
t1.pitch_list("b b c t b")
t1.out("G5-3")

# 3. LAA #8  Justin Upton (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b")
t1.out("F8")


# Bot 1st
# Pitching: LAA #51 Jaime Barria
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b b c")
b1.out("P4")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("L9")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #61 Brian Johnson
t2 = game.new_inning()

# 4. LAA #5  Albert Pujols (X - X - X)
t2.new_ab()
t2.pitch_list("b b c b")
t2.out("G5-3")

# 5. LAA #2  Andrelton Simmons (X - X - X)
t2.new_ab()
t2.out("F7")

# 6. LAA #6  David Fletcher (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1)

# 7. LAA #24 Chris Young (X - X - 6)
t2.new_ab()
t2.pitch_list("b c f b 1 f s")
t2.out("K")


# Bot 2nd
# Pitching: LAA #51 Jaime Barria
b2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("c b s t")
b2.out("KT")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b b c")
b2.hit(2)
b2.advance(3, "12 G6-3")

# 6. BOS #12 Brock Holt (X - 2 - X)
b2.new_ab()
b2.pitch_list("c f d b b f f")
b2.out("G6-3")

# 7. BOS #11 Rafael Devers (2 - X - X)
b2.new_ab()
b2.pitch_list("d")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #61 Brian Johnson
t3 = game.new_inning()

# 8. LAA #10 José Briceño (X - X - X)
t3.new_ab()
t3.pitch_list("s f b f b f t")
t3.out("KT")

# 9. LAA #59 Michael Hermosillo (X - X - X)
t3.new_ab()
t3.pitch_list("c b b f")
t3.out("F8")

# 1. LAA #3  Ian Kinsler (X - X - X)
t3.new_ab()
t3.pitch_list("c s b")
t3.hit(1)
t3.advance(2, "27 BB")

# 2. LAA #27 Mike Trout (X - X - 3)
t3.new_ab()
t3.pitch_list("1 1 b b d b")
t3.reach("BB")

# 3. LAA #8  Justin Upton (X - 3 - 27)
t3.new_ab()
t3.pitch_list("b b f")
t3.out("G6-3")


# Bot 3rd
# Pitching: LAA #51 Jaime Barria
b3 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
b3.new_ab()
b3.pitch_list("b f c")
b3.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c s s")
b3.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c b b c f")
b3.hit(1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b3.new_ab()
b3.pitch_list("b f b c 1 f")
b3.out("L8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #61 Brian Johnson
t4 = game.new_inning()

# 4. LAA #5  Albert Pujols (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("L5")

# 5. LAA #2  Andrelton Simmons (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(4, rbis=1)

# 6. LAA #6  David Fletcher (X - X - X)
t4.new_ab()
t4.out("F7")

# 7. LAA #24 Chris Young (X - X - X)
t4.new_ab()
t4.pitch_list("b b c b")
t4.out("L7")


# Bot 4th
# Pitching: LAA #51 Jaime Barria
b4 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("c b s b b")
b4.out("F8")

# 4. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c c s")
b4.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b b")
b4.reach("BB")

# 6. BOS #12 Brock Holt (X - X - 2)
b4.new_ab()
b4.pitch_list("c b c b 1 f c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #76 Hector Velázquez
t5 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #61 Brian Johnson
t5.pitching_substitution(76)

# 8. LAA #10 José Briceño (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G5-3")

# 9. LAA #59 Michael Hermosillo (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c f")
t5.hit(1)
t5.advance(2, "3 G5-3")

# 1. LAA #3  Ian Kinsler (X - X - 59)
t5.new_ab()
t5.pitch_list("c 1 1 s b 1 d b")
t5.out("G5-3")

# 2. LAA #27 Mike Trout (X - 59 - X)
t5.new_ab()
t5.pitch_list("f")
t5.reach("HBP")

# 3. LAA #8  Justin Upton (X - 59 - 27)
t5.new_ab()
t5.pitch_list("c b b c c")
t5.out("!K")


# Bot 5th
# Pitching: LAA #51 Jaime Barria
b5 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(4, rbis=1)

# 8. BOS #7  Christian Vázquez (X - X - X)
b5.new_ab()
b5.pitch_list("f b")
b5.hit(1)
b5.thrown_out(2, "7-4", 1, 51)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b c s b f")
b5.out("P4")

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("b c c b b")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #76 Hector Velázquez
t6 = game.new_inning()

# 4. LAA #5  Albert Pujols (X - X - X)
t6.new_ab()
t6.pitch_list("b b c f f f f f")
t6.out("G6-3")

# 5. LAA #2  Andrelton Simmons (X - X - X)
t6.new_ab()
t6.pitch_list("c s f f b f s")
t6.out("K2-3")

# 6. LAA #6  David Fletcher (X - X - X)
t6.new_ab()
t6.pitch_list("b c c c")
t6.out("!K")


# Bot 6th
# Pitching: LAA #51 Jaime Barria
b6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("s")
b6.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("b b b s d")
b6.reach("BB")
b6.advance(3, "18 2B")
b6.advance(4, "12 BB")

# Pitching change (LAA): #48 Jose Alvarez replaces #51 Jaime Barria
b6.pitching_substitution(48)

# 4. BOS #18 Mitch Moreland (X - X - 28)
b6.new_ab()
b6.pitch_list("s d b")
b6.hit(2)
b6.advance(3, "12 BB")
b6.thrown_out(4, "11 DP1-2-3", 2, 48)

# 5. BOS #2  Xander Bogaerts (28 - 18 - X)
b6.new_ab()
b6.pitch_list("v v v v")
b6.reach("IBB")
b6.advance(2, "12 BB")

# 6. BOS #12 Brock Holt (28 - 18 - 2)
b6.new_ab()
b6.pitch_list("b d c b c f b")
b6.reach("BB", rbis=1)

# 7. BOS #11 Rafael Devers (18 - 2 - 12)
b6.new_ab()
b6.pitch_list("c f")
b6.out("DP1-2-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #44 Brandon Workman
t7 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #76 Hector Velázquez
t7.pitching_substitution(44)

# 7. LAA #24 Chris Young (X - X - X)
t7.new_ab()
t7.pitch_list("f c b b b s")
t7.out("K")

# 8. LAA #10 José Briceño (X - X - X)
t7.new_ab()
t7.pitch_list("s b s s")
t7.out("K")

# Offensive change (LAA): Pinch-hitter #56 Kole Calhoun replaces #59 Michael Hermosillo, batting 9th
t7.offensive_substitution(9, 56, "PH")

# 9. LAA #56 Kole Calhoun (X - X - X)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")

# 1. LAA #3  Ian Kinsler (X - X - 56)
t7.new_ab()
t7.out("F7")


# Bot 7th
# Pitching: LAA #25 Noé Ramirez
b7 = game.new_inning()

# Pitching change (LAA): #25 Noé Ramirez replaces #48 Jose Alvarez
b7.pitching_substitution(25)

# Defensive switch (LAA): #56 Kole Calhoun moves to RF
b7.defensive_switch(56, "9")

# 8. BOS #7  Christian Vázquez (X - X - X)
b7.new_ab()
b7.pitch_list("c c")
b7.hit(1)
b7.advance(4, "19 HR")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 7)
b7.new_ab()
b7.pitch_list("c f")
b7.hit(4, rbis=2)

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G6-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("f f b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #44 Brandon Workman
t8.pitching_substitution(56)

# 2. LAA #27 Mike Trout (X - X - X)
t8.new_ab()
t8.pitch_list("c c b b b b")
t8.reach("BB")
t8.advance(3, "8 1B")
t8.advance(4, "5 1B")

# 3. LAA #8  Justin Upton (X - X - 27)
t8.new_ab()
t8.pitch_list("c 1 f f b d b")
t8.hit(1)
t8.advance(2, "5 1B")

# 4. LAA #5  Albert Pujols (27 - X - 8)
t8.new_ab()
t8.pitch_list("f")
t8.hit(1, rbis=1)

# 5. LAA #2  Andrelton Simmons (X - 8 - 5)
t8.new_ab()
t8.pitch_list("b")
t8.out("L9")

# 6. LAA #6  David Fletcher (X - 8 - 5)
t8.new_ab()
t8.out("F7")

# Offensive change (LAA): Pinch-hitter #18 Luis Valbuena replaces #24 Chris Young, batting 7th
t8.offensive_substitution(7, 18, "PH")

# 7. LAA #18 Luis Valbuena (X - 8 - 5)
t8.new_ab()
t8.out("F8")


# Bot 8th
# Pitching: LAA #53 Blake Parker
b8 = game.new_inning()

# Pitching change (LAA): #53 Blake Parker replaces #25 Noé Ramirez
b8.pitching_substitution(53)

# Defensive switch (LAA): #6 David Fletcher moves to RF
b8.defensive_switch(6, "9")

# Defensive switch (LAA): #18 Luis Valbuena moves to 3B
b8.defensive_switch(18, "5")

# Defensive switch (LAA): #56 Kole Calhoun moves to CF
b8.defensive_switch(56, "8")

# 4. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("s c")
b8.out("G3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b b f f")
b8.out("G5-3")

# 6. BOS #12 Brock Holt (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
t9.pitching_substitution(46)

# Offensive change (LAA): Pinch-hitter #12 Martín Maldonado replaces #10 José Briceño, batting 8th
t9.offensive_substitution(8, 12, "PH")

# 8. LAA #12 Martín Maldonado (X - X - X)
t9.new_ab()
t9.pitch_list("c b c f b f s")
t9.out("K")

# 9. LAA #56 Kole Calhoun (X - X - X)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")

# 1. LAA #3  Ian Kinsler (X - X - 56)
t9.new_ab()
t9.pitch_list("c b c s")
t9.out("K")

# 2. LAA #27 Mike Trout (X - X - 56)
t9.new_ab()
t9.pitch_list("t b s s")
t9.out("K")

# Winning team: BOS
# WP: BOS #76 Hector Velázquez
game.winning_pitcher(76)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: LAA
# LP: LAA #51 Jaime Barria
game.losing_pitcher(51, is_away_team=True)

# print(game)
game.generate_scorecard()
