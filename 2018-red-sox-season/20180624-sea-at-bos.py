import os
from baseball_scorecard.baseball_scorecard import Scorecard

# SEA @ BOS, 2018-06-24
# https://www.baseball-reference.com/boxes/BOS/BOS201806240.shtml
# https://www.mlb.com/gameday/mariners-vs-red-sox/2018/06/24/530569/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-24 13:08-15:37",
        "at": "Fenway Park, Boston, MA",
        "att": "36,274",
        "temp": "74F, Partly Cloudy",
        "wind": "5mph, Out To RF",
        "away": {
            "team": "Seattle Mariners",
            "starter": 32,
            "roster": {
                # Lineup
                9: "Dee Strange-Gordon",
                17: "Mitch Haniger",
                23: "Nelson Cruz",
                27: "Ryon Healy",
                15: "Kyle Seager",
                5: "Guillermo Heredia",
                3: "Mike Zunino",
                4: "Denard Span",
                7: "Andrew Romine",
                # Starting pitcher
                32: "Marco Gonzales",
                # Bench
                2: "Jean Segura",
                16: "Ben Gamel",
                26: "Chris Herrmann",
                # Bullpen
                52: "Nick Rumbelow",
                48: "Alex Colomé",
                8: "Mike Leake",
                60: "Chasen Bradford",
                65: "James Paxton",
                47: "James Pazos",
                50: "Nick Vincent",
                12: "Juan Nicasio",
                49: "Wade LeBlanc",
                39: "Edwin Díaz",
                55: "Roenis Elías",
                34: "Félix Hernández",
            },
            "lefties": [32, 65, 47, 49, 55],
            "lineup": [
                [9, "4"],
                [17, "9"],
                [23, "0"],
                [27, "3"],
                [15, "5"],
                [5, "8"],
                [3, "2"],
                [4, "7"],
                [7, "6"],
            ],
            "bench": [
                [2, "2B"],
                [16, "RF"],
                [26, "C"],
            ],
            "bullpen": [52, 48, 8, 60, 65, 47, 50, 12, 49, 39, 55, 34],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                5: "Tzu-Wei Lin",
                23: "Blake Swihart",
                12: "Brock Holt",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                24: "David Price",
                44: "Brandon Workman",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                22: "Rick Porcello",
                56: "Joe Kelly",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [41, 57, 24, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [36, "4"],
                [11, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [5, "OF"],
                [23, "C"],
                [12, "2B"],
                [7, "C"],
            ],
            "bullpen": [57, 24, 44, 46, 76, 22, 56, 61, 32, 37],
        },
        "umpires": {
            "HP": "Bruce Dreckman",
            "1B": "Chad Fairchild",
            "2B": "Mike Estabrook",
            "3B": "Alfonso Márquez",
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
# Pitching: BOS #41 Chris Sale
t1 = game.new_inning()

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
t1.new_ab()
t1.pitch_list("s b s")
t1.out("F9")

# 2. SEA #17 Mitch Haniger (X - X - X)
t1.new_ab()
t1.pitch_list("b s c c")
t1.out("!K")

# 3. SEA #23 Nelson Cruz (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.out("F9")


# Bot 1st
# Pitching: SEA #32 Marco Gonzales
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c f s")
b1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b f c")
b1.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c s b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 Chris Sale
t2 = game.new_inning()

# 4. SEA #27 Ryon Healy (X - X - X)
t2.new_ab()
t2.pitch_list("c b f")
t2.out("G4-3")

# 5. SEA #15 Kyle Seager (X - X - X)
t2.new_ab()
t2.pitch_list("c f b s")
t2.out("K")

# 6. SEA #5  Guillermo Heredia (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G5-3")


# Bot 2nd
# Pitching: SEA #32 Marco Gonzales
b2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b c b c b")
b2.out("F7")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("f f")
b2.out("P3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 Chris Sale
t3 = game.new_inning()

# 7. SEA #3  Mike Zunino (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f s")
t3.out("K")

# 8. SEA #4  Denard Span (X - X - X)
t3.new_ab()
t3.pitch_list("f s b")
t3.hit(1)
t3.thrown_out(2, "9 POCS", 3, 41)

# 9. SEA #7  Andrew Romine (X - X - 4)
t3.new_ab()
t3.pitch_list("c s f s")
t3.out("K")

# 1. SEA #9  Dee Strange-Gordon (X - X - 4)
t3.new_ab()
t3.pitch_list("b s 1")
t3.no_ab("POCS")


# Bot 3rd
# Pitching: SEA #32 Marco Gonzales
b3 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("f c f b f f")
b3.out("G4-3")

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c c b b")
b3.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 19)
b3.new_ab()
b3.pitch_list("c b b 1 b c f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 Chris Sale
t4 = game.new_inning()

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
t4.new_ab()
t4.pitch_list("f b f f s")
t4.out("K")

# 2. SEA #17 Mitch Haniger (X - X - X)
t4.new_ab()
t4.pitch_list("f s s")
t4.out("K")

# 3. SEA #23 Nelson Cruz (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(3)

# 4. SEA #27 Ryon Healy (23 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c s s")
t4.out("K")


# Bot 4th
# Pitching: SEA #32 Marco Gonzales
b4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.pitch_list("c f c")
b4.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("c b c b f f s")
b4.out("K")

# 4. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("f s b s")
b4.out("K2-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 Chris Sale
t5 = game.new_inning()

# 5. SEA #15 Kyle Seager (X - X - X)
t5.new_ab()
t5.pitch_list("c s s")
t5.out("K")

# 6. SEA #5  Guillermo Heredia (X - X - X)
t5.new_ab()
t5.pitch_list("f f s")
t5.out("K")

# 7. SEA #3  Mike Zunino (X - X - X)
t5.new_ab()
t5.pitch_list("f s b s")
t5.out("K")


# Bot 5th
# Pitching: SEA #32 Marco Gonzales
b5 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("b b s b c")
b5.hit(2)
b5.advance(3, "36 1B")
b5.advance(4, "11 2B")

# 6. BOS #36 Eduardo Núñez (X - 2 - X)
b5.new_ab(is_risp=True)
b5.hit(1)
b5.advance(3, "11 2B")
b5.advance(4, "3 SF8")

# 7. BOS #11 Rafael Devers (2 - X - 36)
b5.new_ab(is_risp=True)
b5.pitch_list("f")
b5.hit(2, rbis=1)
b5.advance(3, "19 1B")
b5.advance(4, "50 SF8")

# 8. BOS #3  Sandy León (36 - 11 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b s")
b5.out("SF8", rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (X - 11 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c f f")
b5.hit(1)

# 1. BOS #50 Mookie Betts (11 - X - 19)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.out("SF8", rbis=1)

# 2. BOS #16 Andrew Benintendi (X - X - 19)
b5.new_ab()
b5.pitch_list("1 1")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 Chris Sale
t6 = game.new_inning()

# 8. SEA #4  Denard Span (X - X - X)
t6.new_ab()
t6.pitch_list("c c b")
t6.out("G3")

# 9. SEA #7  Andrew Romine (X - X - X)
t6.new_ab()
t6.pitch_list("s")
t6.hit(1)
t6.thrown_out(2, "9 FC1-6", 2, 41)

# 1. SEA #9  Dee Strange-Gordon (X - X - 7)
t6.new_ab()
t6.pitch_list("b f f")
t6.reach("FC1-6")

# 2. SEA #17 Mitch Haniger (X - X - 9)
t6.new_ab()
t6.pitch_list("b b c")
t6.out("F9")


# Bot 6th
# Pitching: SEA #32 Marco Gonzales
b6 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.advance(4, "18 HR")

# 4. BOS #18 Mitch Moreland (X - X - 28)
b6.new_ab()
b6.pitch_list("b b")
b6.hit(4, rbis=2)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c b s")
b6.out("F8")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("(F)P5")

# 7. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("f f")
b6.out("P3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 Chris Sale
t7 = game.new_inning()

# 3. SEA #23 Nelson Cruz (X - X - X)
t7.new_ab()
t7.pitch_list("c c s")
t7.out("K")

# 4. SEA #27 Ryon Healy (X - X - X)
t7.new_ab()
t7.pitch_list("s b f")
t7.hit(1)
t7.advance(2, "5 BB")

# 5. SEA #15 Kyle Seager (X - X - 27)
t7.new_ab()
t7.pitch_list("c s s")
t7.out("K")

# 6. SEA #5  Guillermo Heredia (X - X - 27)
t7.new_ab()
t7.pitch_list("c b b b b")
t7.reach("BB")

# 7. SEA #3  Mike Zunino (X - 27 - 5)
t7.new_ab(is_risp=True)
t7.pitch_list("c b t s")
t7.out("K")


# Bot 7th
# Pitching: SEA #60 Chasen Bradford
b7 = game.new_inning()

# Pitching change (SEA): #60 Chasen Bradford replaces #32 Marco Gonzales
b7.pitching_substitution(60)

# 8. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("b s b f f f b s")
b7.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.hit(1)
b7.advance(2, "50 SB")

# 1. BOS #50 Mookie Betts (X - X - 19)
b7.new_ab(is_risp=True)
b7.pitch_list("c f f b f b s")
b7.out("K")

# 2. BOS #16 Andrew Benintendi (X - 19 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f f f f")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #41 Chris Sale
t8.pitching_substitution(56)

# 8. SEA #4  Denard Span (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b")
t8.out("L6")

# 9. SEA #7  Andrew Romine (X - X - X)
t8.new_ab()
t8.pitch_list("s b b b c")
t8.out("G6-3")

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("L7")


# Bot 8th
# Pitching: SEA #50 Nick Vincent
b8 = game.new_inning()

# Pitching change (SEA): #50 Nick Vincent replaces #60 Chasen Bradford
b8.pitching_substitution(50)

# 3. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.out("G5-3")

# 4. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("b f b")
b8.out("F7")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b f f")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #32 Matt Barnes
t9 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
t9.pitching_substitution(32)

# 2. SEA #17 Mitch Haniger (X - X - X)
t9.new_ab()
t9.pitch_list("b b f f")
t9.out("G6-3")

# 3. SEA #23 Nelson Cruz (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("L9")

# 4. SEA #27 Ryon Healy (X - X - X)
t9.new_ab()
t9.pitch_list("b s")
t9.out("G6-3")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41)

# Loser team: SEA
# LP: SEA #32 Marco Gonzales
game.losing_pitcher(32, is_away_team=True)

# print(game)
game.generate_scorecard()
