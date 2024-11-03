import os
from baseball_scorecard.baseball_scorecard import Scorecard

# SEA @ BOS, 2018-06-23
# https://www.baseball-reference.com/boxes/BOS/BOS201806230.shtml
# https://www.mlb.com/gameday/mariners-vs-red-sox/2018/06/23/530554/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-23 19:16-22:17",
        "at": "Fenway Park, Boston, MA",
        "att": "36,051",
        "temp": "60F, Cloudy",
        "wind": "10mph, In From CF",
        "away": {
            "team": "Seattle Mariners",
            "starter": 8,
            "roster": {
                # Lineup
                9: "Dee Strange-Gordon",
                17: "Mitch Haniger",
                23: "Nelson Cruz",
                15: "Kyle Seager",
                27: "Ryon Healy",
                16: "Ben Gamel",
                5: "Guillermo Heredia",
                26: "Chris Herrmann",
                7: "Andrew Romine",
                # Starting pitcher
                8: "Mike Leake",
                # Bench
                2: "Jean Segura",
                3: "Mike Zunino",
                4: "Denard Span",
                # Bullpen
                52: "Nick Rumbelow",
                48: "Alex Colomé",
                60: "Chasen Bradford",
                65: "James Paxton",
                47: "James Pazos",
                50: "Nick Vincent",
                12: "Juan Nicasio",
                49: "Wade LeBlanc",
                39: "Edwin Díaz",
                55: "Roenis Elías",
                32: "Marco Gonzales",
                34: "Félix Hernández",
            },
            "lefties": [65, 47, 49, 55, 32],
            "lineup": [
                [9, "4"],
                [17, "9"],
                [23, "0"],
                [15, "5"],
                [27, "3"],
                [16, "7"],
                [5, "8"],
                [26, "2"],
                [7, "6"],
            ],
            "bench": [
                [2, "2B"],
                [3, "C"],
                [4, "CF"],
            ],
            "bullpen": [52, 48, 60, 65, 47, 50, 12, 49, 39, 55, 32, 34],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                5: "Tzu-Wei Lin",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                12: "Brock Holt",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                23: "Blake Swihart",
                50: "Mookie Betts",
                2: "Xander Bogaerts",
                3: "Sandy León",
                # Bullpen
                24: "David Price",
                44: "Brandon Workman",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                22: "Rick Porcello",
                41: "Chris Sale",
                56: "Joe Kelly",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [57, 24, 41, 61],
            "lineup": [
                [5, "6"],
                [16, "7"],
                [28, "9"],
                [18, "3"],
                [12, "4"],
                [11, "5"],
                [36, "0"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [23, "C"],
                [50, "SS"],
                [2, "2B"],
                [3, "C"],
            ],
            "bullpen": [24, 44, 46, 76, 22, 41, 56, 61, 32, 37],
        },
        "umpires": {
            "HP": "Alfonso Márquez",
            "1B": "Bruce Dreckman",
            "2B": "Chad Fairchild",
            "3B": "Mike Estabrook",
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
# Pitching: BOS #57 Eduardo Rodriguez
t1 = game.new_inning()

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
t1.new_ab()
t1.pitch_list("c b c")
t1.hit(1)
t1.advance(4, "17 2B")

# 2. SEA #17 Mitch Haniger (X - X - 9)
t1.new_ab()
t1.pitch_list("b c")
t1.hit(2, rbis=1)
t1.advance(3, "23 G4-3")

# 3. SEA #23 Nelson Cruz (X - 17 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b f b f")
t1.out("G4-3")

# 4. SEA #15 Kyle Seager (17 - X - X)
t1.new_ab(is_risp=True)
t1.out("F7")

# 5. SEA #27 Ryon Healy (17 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b s b")
t1.out("F8")


# Bot 1st
# Pitching: SEA #8  Mike Leake
b1 = game.new_inning()

# 1. BOS #5  Tzu-Wei Lin (X - X - X)
b1.new_ab()
b1.pitch_list("c b c b s")
b1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("L3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.advance(3, "18 1B")

# 4. BOS #18 Mitch Moreland (X - X - 28)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(2, "12 BB")

# 5. BOS #12 Brock Holt (28 - X - 18)
b1.new_ab(is_risp=True)
b1.pitch_list("b b b b")
b1.reach("BB")

# 6. BOS #11 Rafael Devers (28 - 18 - 12)
b1.new_ab(is_risp=True)
b1.pitch_list("s")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 6. SEA #16 Ben Gamel (X - X - X)
t2.new_ab()
t2.pitch_list("b f")
t2.reach("HBP")
t2.advance(2, "26 1B")

# 7. SEA #5  Guillermo Heredia (X - X - 16)
t2.new_ab()
t2.pitch_list("b f b f f b s")
t2.out("K")

# 8. SEA #26 Chris Herrmann (X - X - 16)
t2.new_ab()
t2.pitch_list("b b s f")
t2.hit(1)

# 9. SEA #7  Andrew Romine (X - 16 - 26)
t2.new_ab(is_risp=True)
t2.pitch_list("f d")
t2.out("P3")

# 1. SEA #9  Dee Strange-Gordon (X - 16 - 26)
t2.new_ab(is_risp=True)
t2.pitch_list("b")
t2.out("L7")


# Bot 2nd
# Pitching: SEA #8  Mike Leake
b2 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b f")
b2.out("F9")

# 8. BOS #7  Christian Vázquez (X - X - X)
b2.new_ab()
b2.pitch_list("c b c")
b2.out("G5-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("b b c f")
b2.out("L1")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 2. SEA #17 Mitch Haniger (X - X - X)
t3.new_ab()
t3.pitch_list("b f b c b f t")
t3.out("KT")

# 3. SEA #23 Nelson Cruz (X - X - X)
t3.new_ab()
t3.hit(2)
t3.advance("U", "27 E6")

# 4. SEA #15 Kyle Seager (X - 23 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.out("F8")

# 5. SEA #27 Ryon Healy (X - 23 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("s b s")
t3.error(6)
t3.reach("E6")

# 6. SEA #16 Ben Gamel (X - X - 27)
t3.new_ab()
t3.pitch_list("b c b b f f")
t3.out("F8")


# Bot 3rd
# Pitching: SEA #8  Mike Leake
b3 = game.new_inning()

# 1. BOS #5  Tzu-Wei Lin (X - X - X)
b3.new_ab()
b3.pitch_list("c s b f s")
b3.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(1)
b3.thrown_out(2, "28 FC5-4", 2, 8)

# 3. BOS #28 J.D. Martinez (X - X - 16)
b3.new_ab()
b3.pitch_list("f")
b3.reach("FC5-4")
b3.thrown_out(2, "18 CS", 3, 8)

# 4. BOS #18 Mitch Moreland (X - X - 28)
b3.new_ab()
b3.pitch_list("b f b")
b3.no_ab("CS")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 7. SEA #5  Guillermo Heredia (X - X - X)
t4.new_ab()
t4.pitch_list("l b")
t4.out("B1-3")

# 8. SEA #26 Chris Herrmann (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c b")
t4.reach("BB")
t4.advance(2, "7 1B")
t4.advance(3, "9 G1-3")
t4.advance(4, "17 2B")

# 9. SEA #7  Andrew Romine (X - X - 26)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)
t4.advance(2, "9 G1-3")
t4.advance(4, "17 2B")

# 1. SEA #9  Dee Strange-Gordon (X - 26 - 7)
t4.new_ab(is_risp=True)
t4.pitch_list("f b")
t4.out("G1-3")

# 2. SEA #17 Mitch Haniger (26 - 7 - X)
t4.new_ab(is_risp=True)
t4.hit(2, rbis=2)
t4.advance(4, "15 1B")

# 3. SEA #23 Nelson Cruz (X - 17 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b v v")
t4.reach("IBB")
t4.advance(2, "15 1B")

# 4. SEA #15 Kyle Seager (X - 17 - 23)
t4.new_ab(is_risp=True)
t4.pitch_list("f f b b f b f f")
t4.hit(1, rbis=1)
t4.thrown_out(2, "27 FC6-4", 3, 57)

# 5. SEA #27 Ryon Healy (X - 23 - 15)
t4.new_ab(is_risp=True)
t4.reach("FC6-4")


# Bot 4th
# Pitching: SEA #8  Mike Leake
b4 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G4-3")

# 5. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("b c c f f")
b4.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("c c b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #76 Hector Velázquez
t5 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #57 Eduardo Rodriguez
t5.pitching_substitution(76)

# 6. SEA #16 Ben Gamel (X - X - X)
t5.new_ab()
t5.out("G6-3")

# 7. SEA #5  Guillermo Heredia (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b")
t5.hit(1)

# 8. SEA #26 Chris Herrmann (X - X - 5)
t5.new_ab()
t5.pitch_list("s 1 b f")
t5.out("F8")

# 9. SEA #7  Andrew Romine (X - X - 5)
t5.new_ab()
t5.pitch_list("1 b f s")
t5.out("L7")


# Bot 5th
# Pitching: SEA #8  Mike Leake
b5 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("F9")

# 8. BOS #7  Christian Vázquez (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G5-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("L8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #76 Hector Velázquez
t6 = game.new_inning()

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
t6.new_ab()
t6.out("F7")

# 2. SEA #17 Mitch Haniger (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G6-3")

# 3. SEA #23 Nelson Cruz (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b")
t6.hit(1)
t6.advance(3, "15 2B")
t6.advance(4, "27 1B")

# 4. SEA #15 Kyle Seager (X - X - 23)
t6.new_ab()
t6.pitch_list("b b c b s")
t6.hit(2)
t6.advance(3, "27 1B")

# 5. SEA #27 Ryon Healy (23 - 15 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c f")
t6.hit(1, rbis=1)
t6.thrown_out(2, "16 FC6", 3, 76)

# 6. SEA #16 Ben Gamel (15 - X - 27)
t6.new_ab(is_risp=True)
t6.pitch_list("b s")
t6.reach("FC6")


# Bot 6th
# Pitching: SEA #8  Mike Leake
b6 = game.new_inning()

# 1. BOS #5  Tzu-Wei Lin (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.error(3)
b6.reach("E3")
b6.advance(2, "16 G3")
b6.advance(3, "28 G4-3")

# 2. BOS #16 Andrew Benintendi (X - X - 5)
b6.new_ab()
b6.pitch_list("b d")
b6.out("G3")

# 3. BOS #28 J.D. Martinez (X - 5 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f")
b6.out("G4-3")

# 4. BOS #18 Mitch Moreland (5 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b f b")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #76 Hector Velázquez
t7 = game.new_inning()

# 7. SEA #5  Guillermo Heredia (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(1)
t7.advance(3, "26 1B")
t7.advance(4, "9 G4-3")

# 8. SEA #26 Chris Herrmann (X - X - 5)
t7.new_ab()
t7.pitch_list("f f")
t7.hit(1)
t7.advance(2, "9 G4-3")

# 9. SEA #7  Andrew Romine (5 - X - 26)
t7.new_ab(is_risp=True)
t7.pitch_list("b f f b f s")
t7.out("K")

# 1. SEA #9  Dee Strange-Gordon (5 - X - 26)
t7.new_ab(is_risp=True)
t7.pitch_list("c b")
t7.out("G4-3", rbis=1)

# 2. SEA #17 Mitch Haniger (X - 26 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.out("F7")


# Bot 7th
# Pitching: SEA #8  Mike Leake
b7 = game.new_inning()

# 5. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G3")

# 6. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("c f")
b7.out("G3-1")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")

# 8. BOS #7  Christian Vázquez (X - X - 36)
b7.new_ab()
b7.pitch_list("c b f c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #44 Brandon Workman
t8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #76 Hector Velázquez
t8.pitching_substitution(44)

# Defensive change (BOS): #23 Blake Swihart replaces #11 Rafael Devers (3B), playing 3B, batting 6th
t8.defensive_substitution(6, 23, "5")

# 3. SEA #23 Nelson Cruz (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b")
t8.hit(1)

# 4. SEA #15 Kyle Seager (X - X - 23)
t8.new_ab()
t8.pitch_list("c b c b c")
t8.out("!K")

# 5. SEA #27 Ryon Healy (X - X - 23)
t8.new_ab()
t8.pitch_list("f f f s")
t8.out("K")

# 6. SEA #16 Ben Gamel (X - X - 23)
t8.new_ab()
t8.pitch_list("b c")
t8.out("L7")


# Bot 8th
# Pitching: SEA #8  Mike Leake
b8 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("c b b f s")
b8.out("K")

# 1. BOS #5  Tzu-Wei Lin (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c")
b8.out("L9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #37 Heath Hembree
t9 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #44 Brandon Workman
t9.pitching_substitution(37)

# 7. SEA #5  Guillermo Heredia (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b c c")
t9.out("!K")

# 8. SEA #26 Chris Herrmann (X - X - X)
t9.new_ab()
t9.pitch_list("b s b b f f b")
t9.reach("BB")

# 9. SEA #7  Andrew Romine (X - X - 26)
t9.new_ab()
t9.pitch_list("f f")
t9.out("(F)P5")

# 1. SEA #9  Dee Strange-Gordon (X - X - 26)
t9.new_ab()
t9.pitch_list("b")
t9.out("L9")


# Bot 9th
# Pitching: SEA #39 Edwin Díaz
b9 = game.new_inning()

# Pitching change (SEA): #39 Edwin Díaz replaces #8  Mike Leake
b9.pitching_substitution(39)

# 3. BOS #28 J.D. Martinez (X - X - X)
b9.new_ab()
b9.hit(1)
b9.advance(4, "18 3B")

# 4. BOS #18 Mitch Moreland (X - X - 28)
b9.new_ab()
b9.hit(3, rbis=1)
b9.advance(4, "36 E9")

# 5. BOS #12 Brock Holt (18 - X - X)
b9.new_ab(is_risp=True)
b9.pitch_list("f f b s")
b9.out("K")

# 6. BOS #23 Blake Swihart (18 - X - X)
b9.new_ab(is_risp=True)
b9.pitch_list("s t s")
b9.out("K")

# 7. BOS #36 Eduardo Núñez (18 - X - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b b f f")
b9.hit(1, rbis=1)
b9.error(9)
b9.advance(2, "E9")

# 8. BOS #7  Christian Vázquez (X - 36 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b b c f")
b9.out("G5-3")

# Winning team: SEA
# WP: SEA #8 Mike Leake
game.winning_pitcher(8, is_away_team=True)

# Loser team: BOS
# LP: BOS #57 Eduardo Rodriguez
game.losing_pitcher(57)

# print(game)
game.generate_scorecard()
