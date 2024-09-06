import os
from baseball_scorecard.baseball_scorecard import Scorecard

# DET @ BOS, 2018-06-06
# https://www.baseball-reference.com/boxes/BOS/BOS201806060.shtml
# https://www.mlb.com/gameday/tigers-vs-red-sox/2018/06/06/530323/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-06 19:11-22:31",
        "at": "Fenway Park, Boston, MA",
        "att": "35,182",
        "temp": "59F, Partly Cloudy",
        "wind": "13mph, In From RF",
        "away": {
            "team": "Detroit Tigers",
            "starter": 36,
            "roster": {
                # Lineup
                28: "Niko Goodrum",
                9: "Nick Castellanos",
                24: "Miguel Cabrera",
                41: "Victor Martinez",
                34: "James McCann",
                12: "Leonys Martin",
                21: "JaCoby Jones",
                1: "Jose Iglesias",
                60: "Ronny Rodríguez",
                # Starting pitcher
                36: "Blaine Hardy",
                # Bench
                22: "Victor Reyes",
                46: "Jeimer Candelario",
                55: "John Hicks",
                49: "Dixon Machado",
                # Bullpen
                50: "Mike Fiers",
                19: "Louis Coleman",
                26: "Zac Reininger",
                53: "Warwick Saupold",
                57: "Artie Lewicki",
                48: "Matthew Boyd",
                61: "Shane Greene",
                54: "Drew VerHagen",
                45: "Buck Farmer",
                32: "Michael Fulmer",
                77: "Joe Jiménez",
            },
            "lefties": [36, 48],
            "lineup": [
                [28, "4"],
                [9, "9"],
                [24, "3"],
                [41, "0"],
                [34, "2"],
                [12, "8"],
                [21, "7"],
                [1, "6"],
                [60, "5"],
            ],
            "bench": [
                [22, "RF"],
                [46, "3B"],
                [55, "C"],
                [49, "SS"],
            ],
            "bullpen": [50, 19, 26, 53, 57, 48, 61, 54, 45, 32, 77],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                59: "Sam Travis",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                35: "Steven Wright",
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
                [16, "8"],
                [2, "6"],
                [28, "7"],
                [18, "3"],
                [36, "4"],
                [59, "0"],
                [11, "5"],
                [7, "2"],
                [19, "9"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [35, 44, 22, 41, 61, 66, 37, 24, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "Mike DiMuro",
            "1B": "Jeremie Rehak",
            "2B": "Mark Wegner",
            "3B": "John Tumpane",
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

# 1. DET #28 Niko Goodrum (X - X - X)
t1.new_ab()
t1.pitch_list("b c b s b f b")
t1.reach("BB")
t1.advance(2, "9 WP")

# 2. DET #9  Nick Castellanos (X - X - 28)
t1.new_ab()
t1.pitch_list("s s b b s")
t1.wp()
t1.out("K")

# 3. DET #24 Miguel Cabrera (X - 28 - X)
t1.new_ab()
t1.pitch_list("c f f c")
t1.out("!K")

# 4. DET #41 Victor Martinez (X - 28 - X)
t1.new_ab()
t1.pitch_list("b c b d")
t1.out("G5-3")


# Bot 1st
# Pitching: DET #36 Blaine Hardy
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c t b")
b1.out("G1-3")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("c c b s")
b1.out("K")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.hit(1)
b1.thrown_out(2, "7-4", 3, 36)


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 5. DET #34 James McCann (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("(F)P3")

# 6. DET #12 Leonys Martin (X - X - X)
t2.new_ab()
t2.pitch_list("b s s b f b f f")
t2.out("G4-3")

# 7. DET #21 JaCoby Jones (X - X - X)
t2.new_ab()
t2.hit(3)
t2.advance(4, "1 1B")

# 8. DET #1  Jose Iglesias (21 - X - X)
t2.new_ab()
t2.pitch_list("b b b c")
t2.hit(1, rbis=1)

# 9. DET #60 Ronny Rodríguez (X - X - 1)
t2.new_ab()
t2.pitch_list("c f s")
t2.out("K")


# Bot 2nd
# Pitching: DET #36 Blaine Hardy
b2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("c s b")
b2.out("G6-3")

# 5. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("c s b b t")
b2.out("KT")

# 6. BOS #59 Sam Travis (X - X - X)
b2.new_ab()
b2.out("P4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 1. DET #28 Niko Goodrum (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G5-3")

# 2. DET #9  Nick Castellanos (X - X - X)
t3.new_ab()
t3.pitch_list("b b s f s")
t3.pb()
t3.reach("K")

# 3. DET #24 Miguel Cabrera (X - X - 9)
t3.new_ab()
t3.pitch_list("b c b b s f f")
t3.out("L4")

# 4. DET #41 Victor Martinez (X - X - 9)
t3.new_ab()
t3.pitch_list("c b t b f")
t3.out("F8")


# Bot 3rd
# Pitching: DET #36 Blaine Hardy
b3 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(4, "7 2B")

# 8. BOS #7  Christian Vázquez (X - X - 11)
b3.new_ab()
b3.hit(2, rbis=1)
b3.advance(4, "16 2B")

# 9. BOS #19 Jackie Bradley Jr. (X - 7 - X)
b3.new_ab()
b3.pitch_list("c")
b3.reach("HBP")
b3.advance(3, "16 2B")
b3.advance(4, "2 2B")

# 1. BOS #16 Andrew Benintendi (X - 7 - 19)
b3.new_ab()
b3.pitch_list("s f f b f d")
b3.hit(2, rbis=1)
b3.advance(4, "2 2B")

# 2. BOS #2  Xander Bogaerts (19 - 16 - X)
b3.new_ab()
b3.pitch_list("b b b f f")
b3.hit(2, rbis=2)
b3.advance(3, "18 G4-3")

# 3. BOS #28 J.D. Martinez (X - 2 - X)
b3.new_ab()
b3.pitch_list("b s b c b")
b3.out("G5-3")

# 4. BOS #18 Mitch Moreland (X - 2 - X)
b3.new_ab()
b3.pitch_list("b f f d b")
b3.out("G4-3")

# 5. BOS #36 Eduardo Núñez (2 - X - X)
b3.new_ab()
b3.pitch_list("s")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 5. DET #34 James McCann (X - X - X)
t4.new_ab()
t4.pitch_list("c f b b b f")
t4.out("F9")

# 6. DET #12 Leonys Martin (X - X - X)
t4.new_ab()
t4.pitch_list("c b c")
t4.out("G3")

# 7. DET #21 JaCoby Jones (X - X - X)
t4.new_ab()
t4.pitch_list("c s b b b")
t4.hit(1)

# 8. DET #1  Jose Iglesias (X - X - 21)
t4.new_ab()
t4.pitch_list("c 1 b b f")
t4.out("G6-3")


# Bot 4th
# Pitching: DET #36 Blaine Hardy
b4 = game.new_inning()

# 6. BOS #59 Sam Travis (X - X - X)
b4.new_ab()
b4.pitch_list("c f b")
b4.out("G5-3")

# 7. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("P4")

# 8. BOS #7  Christian Vázquez (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 7)
b4.new_ab()
b4.pitch_list("c f b")
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #57 Eduardo Rodriguez
t5 = game.new_inning()

# 9. DET #60 Ronny Rodríguez (X - X - X)
t5.new_ab()
t5.pitch_list("l")
t5.out("G6-3")

# 1. DET #28 Niko Goodrum (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("G3")

# 2. DET #9  Nick Castellanos (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b")
t5.out("L7")


# Bot 5th
# Pitching: DET #36 Blaine Hardy
b5 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.hit(4, rbis=1)

# 2. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("c c b f b")
b5.hit(1)
b5.thrown_out(2, "28 DP1-4-3", 1, 36)

# 3. BOS #28 J.D. Martinez (X - X - 2)
b5.new_ab()
b5.pitch_list("1 f b b f 1")
b5.out("DP1-4-3")

# 4. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("s b")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #57 Eduardo Rodriguez
t6 = game.new_inning()

# 3. DET #24 Miguel Cabrera (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(1)
t6.advance(2, "12 1B")
t6.advance(3, "21 BB")

# 4. DET #41 Victor Martinez (X - X - 24)
t6.new_ab()
t6.out("(F)F9")

# 5. DET #34 James McCann (X - X - 24)
t6.new_ab()
t6.pitch_list("c b f s")
t6.out("K")

# 6. DET #12 Leonys Martin (X - X - 24)
t6.new_ab()
t6.pitch_list("b b c")
t6.hit(1)
t6.advance(2, "21 BB")

# Pitching change (BOS): #37 Heath Hembree replaces #57 Eduardo Rodriguez
t6.pitching_substitution(37)

# 7. DET #21 JaCoby Jones (X - 24 - 12)
t6.new_ab()
t6.pitch_list("b b d b")
t6.reach("BB")

# 8. DET #1  Jose Iglesias (24 - 12 - 21)
t6.new_ab()
t6.pitch_list("c c")
t6.out("L3")


# Bot 6th
# Pitching: DET #36 Blaine Hardy
b6 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("b f s b f")
b6.out("P4")

# 6. BOS #59 Sam Travis (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G1-3")

# 7. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("b f f b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Matt Barnes
t7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree
t7.pitching_substitution(32)

# 9. DET #60 Ronny Rodríguez (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("G6-3")

# 1. DET #28 Niko Goodrum (X - X - X)
t7.new_ab()
t7.pitch_list("s b s b c")
t7.out("!K")

# 2. DET #9  Nick Castellanos (X - X - X)
t7.new_ab()
t7.pitch_list("b b c b c")
t7.hit(1)
t7.advance(3, "24 E8")

# 3. DET #24 Miguel Cabrera (X - X - 9)
t7.new_ab()
t7.pitch_list("f d c f b f")
t7.hit(1)
t7.error(8)
t7.advance(2, "E8")

# 4. DET #41 Victor Martinez (9 - 24 - X)
t7.new_ab()
t7.pitch_list("s f d b f b f b")
t7.reach("BB")
t7.thrown_out(2, "34 FC6", 3, 32)

# 5. DET #34 James McCann (9 - 24 - 41)
t7.new_ab()
t7.pitch_list("f b f b f f")
t7.reach("FC6")


# Bot 7th
# Pitching: DET #45 Buck Farmer
b7 = game.new_inning()

# Pitching change (DET): #45 Buck Farmer replaces #36 Blaine Hardy
b7.pitching_substitution(45)

# 8. BOS #7  Christian Vázquez (X - X - X)
b7.new_ab()
b7.hit(4, rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.out("F7")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G1-3")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.hit(1)
b7.thrown_out(2, "28 FC6-4", 3, 45)

# 3. BOS #28 J.D. Martinez (X - X - 2)
b7.new_ab()
b7.pitch_list("b s s b")
b7.reach("FC6-4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #44 Brandon Workman
t8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #32 Matt Barnes
t8.pitching_substitution(44)

# 6. DET #12 Leonys Martin (X - X - X)
t8.new_ab()
t8.pitch_list("b c s")
t8.out("L7")

# 7. DET #21 JaCoby Jones (X - X - X)
t8.new_ab()
t8.pitch_list("c b b f b")
t8.out("F9")

# 8. DET #1  Jose Iglesias (X - X - X)
t8.new_ab()
t8.out("F7")


# Bot 8th
# Pitching: DET #19 Louis Coleman
b8 = game.new_inning()

# Pitching change (DET): #19 Louis Coleman replaces #45 Buck Farmer
b8.pitching_substitution(19)

# 4. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("s b b")
b8.error(9)
b8.reach("E9", end_base=2)
b8.advance("U", "59 1B")

# 5. BOS #36 Eduardo Núñez (X - 18 - X)
b8.new_ab()
b8.out("L1")

# 6. BOS #59 Sam Travis (X - 18 - X)
b8.new_ab()
b8.pitch_list("c s b")
b8.hit(1, rbis=1)
b8.advance(3, "11 2B")

# 7. BOS #11 Rafael Devers (X - X - 59)
b8.new_ab()
b8.pitch_list("f b b b f f f")
b8.hit(2)

# 8. BOS #7  Christian Vázquez (59 - 11 - X)
b8.new_ab()
b8.pitch_list("c f f b f c")
b8.out("!K")

# 9. BOS #19 Jackie Bradley Jr. (59 - 11 - X)
b8.new_ab()
b8.pitch_list("b f")
b8.reach("HBP")

# Pitching change (DET): #26 Zac Reininger replaces #19 Louis Coleman
b8.pitching_substitution(26)

# 1. BOS #16 Andrew Benintendi (59 - 11 - 19)
b8.new_ab()
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #66 Bobby Poyner
t9 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #44 Brandon Workman
t9.pitching_substitution(66)

# 9. DET #60 Ronny Rodríguez (X - X - X)
t9.new_ab()
t9.pitch_list("c f")
t9.out("G5-3")

# 1. DET #28 Niko Goodrum (X - X - X)
t9.new_ab()
t9.pitch_list("b t")
t9.out("G5-3")

# 2. DET #9  Nick Castellanos (X - X - X)
t9.new_ab()
t9.pitch_list("c b b f f f s")
t9.out("K")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57)

# Loser team: DET
# LP: DET #36 Blaine Hardy
game.losing_pitcher(36, is_away_team=True)

# print(game)
game.generate_scorecard()
