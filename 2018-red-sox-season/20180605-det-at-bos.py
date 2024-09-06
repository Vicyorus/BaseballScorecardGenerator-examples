import os
from baseball_scorecard.baseball_scorecard import Scorecard

# DET @ BOS, 2018-06-05
# https://www.baseball-reference.com/boxes/BOS/BOS201806050.shtml
# https://www.mlb.com/gameday/tigers-vs-red-sox/2018/06/05/530308/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-05 19:11-21:52",
        "at": "Fenway Park, Boston, MA",
        "att": "34,762",
        "temp": "58F, Partly Cloudy",
        "wind": "8mph, R To L",
        "away": {
            "team": "Detroit Tigers",
            "starter": 57,
            "roster": {
                # Lineup
                12: "Leonys Martin",
                9: "Nick Castellanos",
                24: "Miguel Cabrera",
                41: "Victor Martinez",
                46: "Jeimer Candelario",
                34: "James McCann",
                21: "JaCoby Jones",
                1: "Jose Iglesias",
                49: "Dixon Machado",
                # Starting pitcher
                57: "Artie Lewicki",
                # Bench
                28: "Niko Goodrum",
                22: "Victor Reyes",
                60: "Ronny Rodríguez",
                55: "John Hicks",
                # Bullpen
                50: "Mike Fiers",
                19: "Louis Coleman",
                26: "Zac Reininger",
                53: "Warwick Saupold",
                48: "Matthew Boyd",
                61: "Shane Greene",
                54: "Drew VerHagen",
                45: "Buck Farmer",
                32: "Michael Fulmer",
                77: "Joe Jiménez",
                36: "Blaine Hardy",
            },
            "lefties": [48, 36],
            "lineup": [
                [12, "8"],
                [9, "9"],
                [24, "3"],
                [41, "0"],
                [46, "5"],
                [34, "2"],
                [21, "7"],
                [1, "6"],
                [49, "4"],
            ],
            "bench": [
                [28, "3B"],
                [22, "RF"],
                [60, "SS"],
                [55, "C"],
            ],
            "bullpen": [50, 19, 26, 53, 48, 61, 54, 45, 32, 77, 36],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 35,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                35: "Steven Wright",
                # Bench
                59: "Sam Travis",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 66, 24],
            "lineup": [
                [16, "7"],
                [2, "6"],
                [28, "0"],
                [18, "3"],
                [36, "4"],
                [12, "9"],
                [11, "5"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [59, "1B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 44, 22, 41, 61, 66, 37, 24, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "John Tumpane",
            "1B": "Mike DiMuro",
            "2B": "Jeremie Rehak",
            "3B": "Mark Wegner",
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
# Pitching: BOS #35 Steven Wright
t1 = game.new_inning()

# 1. DET #12 Leonys Martin (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b b")
t1.reach("BB")
t1.thrown_out(4, "9 7-6-2", 1, 35)
t1.advance(3, "9 2B")

# 2. DET #9  Nick Castellanos (X - X - 12)
t1.new_ab()
t1.pitch_list("c b f")
t1.hit(2)

# 3. DET #24 Miguel Cabrera (X - 9 - X)
t1.new_ab()
t1.pitch_list("b c b s b b")
t1.reach("BB")

# 4. DET #41 Victor Martinez (X - 9 - 24)
t1.new_ab()
t1.pitch_list("c")
t1.out("P6")

# 5. DET #46 Jeimer Candelario (X - 9 - 24)
t1.new_ab()
t1.pitch_list("c s c")
t1.out("!K")


# Bot 1st
# Pitching: DET #57 Artie Lewicki
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("f")
b1.hit(1)
b1.advance(2, "2 SB")
b1.advance(4, "28 HR")

# 2. BOS #2  Xander Bogaerts (X - X - 16)
b1.new_ab()
b1.pitch_list("c b 1 f s")
b1.out("K")

# 3. BOS #28 J.D. Martinez (X - 16 - X)
b1.new_ab()
b1.pitch_list("b b f f b")
b1.hit(4, rbis=2)

# 4. BOS #18 Mitch Moreland (X - X - X)
b1.new_ab()
b1.pitch_list("f")
b1.out("G3-1")

# 5. BOS #36 Eduardo Núñez (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #35 Steven Wright
t2 = game.new_inning()

# 6. DET #34 James McCann (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")
t2.advance(2, "21 G5-3")

# 7. DET #21 JaCoby Jones (X - X - 34)
t2.new_ab()
t2.pitch_list("c f")
t2.out("G5-3")

# 8. DET #1  Jose Iglesias (X - 34 - X)
t2.new_ab()
t2.pitch_list("b b c d f")
t2.out("G5-3")

# 9. DET #49 Dixon Machado (X - 34 - X)
t2.new_ab()
t2.pitch_list("b b b c")
t2.out("G1-3")


# Bot 2nd
# Pitching: DET #57 Artie Lewicki
b2 = game.new_inning()

# 6. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.out("G6-3")

# 7. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.out("G4-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f b f")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #35 Steven Wright
t3 = game.new_inning()

# 1. DET #12 Leonys Martin (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c f")
t3.out("L8")

# 2. DET #9  Nick Castellanos (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)
t3.thrown_out(2, "24 DP6-4-3", 2, 35)

# 3. DET #24 Miguel Cabrera (X - X - 9)
t3.new_ab()
t3.pitch_list("f")
t3.out("DP6-4-3")


# Bot 3rd
# Pitching: DET #57 Artie Lewicki
b3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c f b b f b")
b3.hit(1)
b3.thrown_out(2, "16 PO", 1, 57)

# 1. BOS #16 Andrew Benintendi (X - X - 19)
b3.new_ab()
b3.pitch_list("f 1 1 f")
b3.out("G6-3")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("s c b b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #35 Steven Wright
t4 = game.new_inning()

# 4. DET #41 Victor Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.out("F7")

# 5. DET #46 Jeimer Candelario (X - X - X)
t4.new_ab()
t4.pitch_list("c f b b s")
t4.out("K")

# 6. DET #34 James McCann (X - X - X)
t4.new_ab()
t4.pitch_list("c c b f b b")
t4.out("G6-3")


# Bot 4th
# Pitching: DET #57 Artie Lewicki
b4 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("b s f")
b4.error(5)
b4.reach("E5", end_base=2)
b4.advance(3, "18 1B")
b4.advance("U", "36 1B")

# Defensive change (DET): #60 Ronny Rodríguez replaces #46 Jeimer Candelario (3B), playing 3B, batting 5th
b4.defensive_substitution(5, 60, "5")

# 4. BOS #18 Mitch Moreland (X - 28 - X)
b4.new_ab()
b4.pitch_list("b c b f")
b4.hit(1)
b4.advance(2, "36 1B")
b4.advance(3, "12 BB")
b4.advance("U", "11 DP6-3")

# 5. BOS #36 Eduardo Núñez (28 - X - 18)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1, rbis=1)
b4.advance(2, "12 BB")
b4.advance(3, "11 DP6-3")

# 6. BOS #12 Brock Holt (X - 18 - 36)
b4.new_ab()
b4.pitch_list("b b b c b")
b4.reach("BB")
b4.thrown_out(2, "11 DP6-3", 1, 57)

# 7. BOS #11 Rafael Devers (18 - 36 - 12)
b4.new_ab()
b4.pitch_list("c")
b4.out("DP6-3")

# 8. BOS #7  Christian Vázquez (36 - X - X)
b4.new_ab()
b4.pitch_list("b b b b")
b4.reach("BB")
b4.advance(2, "19 BB")

# 9. BOS #19 Jackie Bradley Jr. (36 - X - 7)
b4.new_ab()
b4.pitch_list("b c b b b")
b4.reach("BB")

# Pitching change (DET): #53 Warwick Saupold replaces #57 Artie Lewicki
b4.pitching_substitution(53)

# 1. BOS #16 Andrew Benintendi (36 - 7 - 19)
b4.new_ab()
b4.pitch_list("f")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #35 Steven Wright
t5 = game.new_inning()

# 7. DET #21 JaCoby Jones (X - X - X)
t5.new_ab()
t5.pitch_list("c s b b s")
t5.out("K")

# 8. DET #1  Jose Iglesias (X - X - X)
t5.new_ab()
t5.pitch_list("c b b c s")
t5.out("K2-3")

# 9. DET #49 Dixon Machado (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.out("G1-3")


# Bot 5th
# Pitching: DET #53 Warwick Saupold
b5 = game.new_inning()

# 2. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.hit(4, rbis=1)

# 3. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.hit(1)
b5.advance(2, "18 1B")
b5.advance(3, "36 1B")
b5.advance(4, "12 G4-3")

# 4. BOS #18 Mitch Moreland (X - X - 28)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(2, "36 1B")
b5.advance(3, "12 G4-3")

# 5. BOS #36 Eduardo Núñez (X - 28 - 18)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(2, "12 G4-3")

# 6. BOS #12 Brock Holt (28 - 18 - 36)
b5.new_ab()
b5.pitch_list("b b c")
b5.out("G4-3", rbis=1)

# 7. BOS #11 Rafael Devers (18 - 36 - X)
b5.new_ab()
b5.pitch_list("b b b v")
b5.reach("IBB")
b5.thrown_out(2, "7 DP4-6-3", 2, 53)

# 8. BOS #7  Christian Vázquez (18 - 36 - 11)
b5.new_ab()
b5.pitch_list("c d b f d")
b5.out("DP4-6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #35 Steven Wright
t6 = game.new_inning()

# 1. DET #12 Leonys Martin (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G3")

# 2. DET #9  Nick Castellanos (X - X - X)
t6.new_ab()
t6.pitch_list("b f s s")
t6.out("K")

# 3. DET #24 Miguel Cabrera (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G5-3")


# Bot 6th
# Pitching: DET #53 Warwick Saupold
b6 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("c b b c s")
b6.out("K")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G6-3")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b b")
b6.reach("BB")
b6.thrown_out(2, "28 FC4", 3, 53)

# 3. BOS #28 J.D. Martinez (X - X - 2)
b6.new_ab()
b6.pitch_list("s")
b6.reach("FC4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #35 Steven Wright
t7 = game.new_inning()

# 4. DET #41 Victor Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("b b c b f f c")
t7.out("!K")

# 5. DET #60 Ronny Rodríguez (X - X - X)
t7.new_ab()
t7.pitch_list("c b s b")
t7.out("G6-3")

# 6. DET #34 James McCann (X - X - X)
t7.new_ab()
t7.out("P4")


# Bot 7th
# Pitching: DET #45 Buck Farmer
b7 = game.new_inning()

# Pitching change (DET): #45 Buck Farmer replaces #53 Warwick Saupold
b7.pitching_substitution(45)

# 4. BOS #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.pitch_list("b f")
b7.out("L7")

# 5. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.out("G4-3")

# 6. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("c t b f c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #76 Hector Velázquez
t8 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #35 Steven Wright
t8.pitching_substitution(76)

# 7. DET #21 JaCoby Jones (X - X - X)
t8.new_ab()
t8.pitch_list("c b c b")
t8.out("G6-3")

# 8. DET #1  Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("c f f b b b f f f")
t8.out("L9")

# 9. DET #49 Dixon Machado (X - X - X)
t8.new_ab()
t8.hit(1)

# 1. DET #12 Leonys Martin (X - X - 49)
t8.new_ab()
t8.pitch_list("f b")
t8.out("G4-3")


# Bot 8th
# Pitching: DET #26 Zac Reininger
b8 = game.new_inning()

# Pitching change (DET): #26 Zac Reininger replaces #45 Buck Farmer
b8.pitching_substitution(26)

# 7. BOS #11 Rafael Devers (X - X - X)
b8.new_ab()
b8.pitch_list("s b b c t")
b8.out("KT")

# 8. BOS #7  Christian Vázquez (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1)

# 1. BOS #16 Andrew Benintendi (X - X - 19)
b8.new_ab()
b8.pitch_list("b c b f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #44 Brandon Workman
t9 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #76 Hector Velázquez
t9.pitching_substitution(44)

# 2. DET #9  Nick Castellanos (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("G5-3")

# 3. DET #24 Miguel Cabrera (X - X - X)
t9.new_ab()
t9.pitch_list("c b s")
t9.out("(F)P3")

# 4. DET #41 Victor Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.out("G5-3")

# Winning team: BOS
# WP: BOS #35 Steven Wright
game.winning_pitcher(35)

# Loser team: DET
# LP: DET #57 Artie Lewicki
game.losing_pitcher(57, is_away_team=True)

# print(game)
game.generate_scorecard()
