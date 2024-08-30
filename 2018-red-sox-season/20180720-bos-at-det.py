import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ DET, 2018-07-20
# https://www.baseball-reference.com/boxes/DET/DET201807200.shtml
# https://www.mlb.com/gameday/red-sox-vs-tigers/2018/07/20/530860/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-20 19:11-22:42",
        "at": "Comerica Park, Detroit, MI",
        "att": "33,817",
        "temp": "78F, Partly Cloudy",
        "wind": "15mph, In From LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                25: "Steve Pearce",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                3: "Sandy León",
                # Starting pitcher
                24: "David Price",
                # Bench
                5: "Tzu-Wei Lin",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 41, 61, 66],
            "lineup": [
                [50, "8"],
                [16, "7"],
                [28, "9"],
                [25, "0"],
                [2, "6"],
                [18, "3"],
                [36, "5"],
                [12, "4"],
                [3, "2"],
            ],
            "bench": [
                [5, "OF"],
                [23, "C"],
                [19, "CF"],
            ],
            "bullpen": [47, 44, 22, 41, 61, 66, 37, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "Detroit Tigers",
            "starter": 48,
            "roster": {
                # Lineup
                28: "Niko Goodrum",
                46: "Jeimer Candelario",
                9: "Nick Castellanos",
                55: "John Hicks",
                34: "James McCann",
                41: "Victor Martinez",
                12: "Leonys Martin",
                1: "Jose Iglesias",
                21: "JaCoby Jones",
                # Starting pitcher
                48: "Matthew Boyd",
                # Bench
                37: "James Adduci",
                22: "Victor Reyes",
                60: "Ronny Rodríguez",
                # Bullpen
                38: "Francisco Liriano",
                30: "Alex Wilson",
                58: "Victor Alcántara",
                50: "Mike Fiers",
                19: "Louis Coleman",
                27: "Jordan Zimmermann",
                68: "Daniel Stumpf",
                61: "Shane Greene",
                54: "Drew VerHagen",
                45: "Buck Farmer",
                77: "Joe Jiménez",
                36: "Blaine Hardy",
            },
            "lefties": [48, 38, 68, 36],
            "lineup": [
                [28, "4"],
                [46, "5"],
                [9, "9"],
                [55, "3"],
                [34, "2"],
                [41, "0"],
                [12, "8"],
                [1, "6"],
                [21, "7"],
            ],
            "bench": [
                [37, "1B"],
                [22, "RF"],
                [60, "SS"],
            ],
            "bullpen": [38, 30, 58, 50, 19, 27, 68, 61, 54, 45, 77, 36],
        },
        "umpires": {
            "HP": "Gary Cederstrom",
            "1B": "Stu Scheurwater",
            "2B": "Eric Cooper",
            "3B": "Cory Blaser",
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
# Pitching: DET #48 Matthew Boyd
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G4-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("s f b")
t1.hit(1)
t1.advance(2, "28 BB")
t1.advance(4, "25 2B")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")
t1.advance(3, "25 2B")
t1.thrown_out(4, "2 FC5-2", 2, 48)

# 4. BOS #25 Steve Pearce (X - 16 - 28)
t1.new_ab()
t1.pitch_list("b c f d")
t1.hit(2, rbis=1)
t1.thrown_out(3, "18 FC5", 3, 48)

# 5. BOS #2  Xander Bogaerts (28 - 25 - X)
t1.new_ab()
t1.pitch_list("b b b c f f")
t1.reach("FC5-2")

# 6. BOS #18 Mitch Moreland (X - 25 - 2)
t1.new_ab()
t1.pitch_list("c s f")
t1.reach("FC5")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. DET #28 Niko Goodrum (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("G5-3")

# 2. DET #46 Jeimer Candelario (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.out("L6")

# 3. DET #9  Nick Castellanos (X - X - X)
b1.new_ab()
b1.pitch_list("c b s")
b1.out("L9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: DET #48 Matthew Boyd
t2 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("c b s")
t2.out("G4-3")

# 8. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("c f s")
t2.out("K")

# 9. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")

# 1. BOS #50 Mookie Betts (X - X - 3)
t2.new_ab()
t2.pitch_list("b b c c f b f f f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 4. DET #55 John Hicks (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G6-3")

# 5. DET #34 James McCann (X - X - X)
b2.new_ab()
b2.pitch_list("c f c")
b2.out("!K")

# 6. DET #41 Victor Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("s")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: DET #48 Matthew Boyd
t3 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("F9")

# 3. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("s c")
t3.out("G5-3")

# 4. BOS #25 Steve Pearce (X - X - X)
t3.new_ab()
t3.pitch_list("c b s f f b f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 7. DET #12 Leonys Martin (X - X - X)
b3.new_ab()
b3.pitch_list("s f f b f")
b3.out("F9")

# 8. DET #1  Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.out("F7")

# 9. DET #21 JaCoby Jones (X - X - X)
b3.new_ab()
b3.pitch_list("f b")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: DET #48 Matthew Boyd
t4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b f f")
t4.out("L8")

# 6. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b s c c")
t4.out("!K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.out("F7")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 1. DET #28 Niko Goodrum (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(2, "46 1B")
b4.advance(3, "9 1B")

# 2. DET #46 Jeimer Candelario (X - X - 28)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)
b4.advance(2, "9 1B")

# 3. DET #9  Nick Castellanos (X - 28 - 46)
b4.new_ab()
b4.pitch_list("f b")
b4.hit(1)

# 4. DET #55 John Hicks (28 - 46 - 9)
b4.new_ab()
b4.pitch_list("c f b f f")
b4.out("L7")

# Defensive change (BOS): #5 Tzu-Wei Lin replaces #12 Brock Holt (2B), playing 2B, batting 8th
b4.defensive_substitution(8, 5, "4")

# 5. DET #34 James McCann (28 - 46 - 9)
b4.new_ab()
b4.pitch_list("b b c s b s")
b4.out("K")

# 6. DET #41 Victor Martinez (28 - 46 - 9)
b4.new_ab()
b4.pitch_list("b c")
b4.out("L9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: DET #48 Matthew Boyd
t5 = game.new_inning()

# 8. BOS #5  Tzu-Wei Lin (X - X - X)
t5.new_ab()
t5.pitch_list("b b c s c")
t5.out("!K")

# 9. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("c f")
t5.out("G5-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("f c b b t")
t5.out("KT")


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# 7. DET #12 Leonys Martin (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b s")
b5.out("K")

# 8. DET #1  Jose Iglesias (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)
b5.advance(2, "21 BB")
b5.advance(3, "28 FC6-4")

# 9. DET #21 JaCoby Jones (X - X - 1)
b5.new_ab()
b5.pitch_list("b f b b f f b")
b5.reach("BB")
b5.thrown_out(2, "28 FC6-4", 2, 24)

# 1. DET #28 Niko Goodrum (X - 1 - 21)
b5.new_ab()
b5.pitch_list("c f b b f")
b5.reach("FC6-4")

# 2. DET #46 Jeimer Candelario (1 - X - 28)
b5.new_ab()
b5.pitch_list("c b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: DET #48 Matthew Boyd
t6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("b b c b f f")
t6.hit(1)
t6.error(1)
t6.advance(2, "28 E1")
t6.advance(3, "2 1B")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t6.new_ab()
t6.pitch_list("d 1 f 1 1 b f")
t6.reach("FC1")
t6.advance(2, "2 1B")

# Pitching change (DET): #19 Louis Coleman replaces #48 Matthew Boyd
t6.pitching_substitution(19)

# 4. BOS #25 Steve Pearce (X - 16 - 28)
t6.new_ab()
t6.pitch_list("b b f f c")
t6.out("!K")

# 5. BOS #2  Xander Bogaerts (X - 16 - 28)
t6.new_ab()
t6.pitch_list("c b b b c")
t6.hit(1)

# Pitching change (DET): #68 Daniel Stumpf replaces #19 Louis Coleman
t6.pitching_substitution(68)

# 6. BOS #18 Mitch Moreland (16 - 28 - 2)
t6.new_ab()
t6.pitch_list("f")
t6.out("(F)P5")

# Pitching change (DET): #45 Buck Farmer replaces #68 Daniel Stumpf
t6.pitching_substitution(45)

# 7. BOS #36 Eduardo Núñez (16 - 28 - 2)
t6.new_ab()
t6.pitch_list("b b b c c f")
t6.out("(F)F9")


# Bot 6th
# Pitching: BOS #24 David Price
b6 = game.new_inning()

# 3. DET #9  Nick Castellanos (X - X - X)
b6.new_ab()
b6.pitch_list("s f c")
b6.out("!K")

# 4. DET #55 John Hicks (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.out("F8")

# 5. DET #34 James McCann (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: DET #45 Buck Farmer
t7 = game.new_inning()

# 8. BOS #5  Tzu-Wei Lin (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.hit(1)
t7.thrown_out(2, "3 CS", 1, 45)

# 9. BOS #3  Sandy León (X - X - 5)
t7.new_ab()
t7.pitch_list("s b s f b s")
t7.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c f b b f f b b")
t7.reach("BB")
t7.advance(2, "16 BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t7.new_ab()
t7.pitch_list("1 1 b 1 b b b")
t7.reach("BB")

# Pitching change (DET): #58 Victor Alcántara replaces #45 Buck Farmer
t7.pitching_substitution(58)

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
t7.new_ab()
t7.pitch_list("f f b")
t7.out("G3")


# Bot 7th
# Pitching: BOS #24 David Price
b7 = game.new_inning()

# 6. DET #41 Victor Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("F8")

# 7. DET #12 Leonys Martin (X - X - X)
b7.new_ab()
b7.pitch_list("s f b f f b f")
b7.reach("HBP")

# Pitching change (BOS): #37 Heath Hembree replaces #24 David Price
b7.pitching_substitution(37)

# 8. DET #1  Jose Iglesias (X - X - 12)
b7.new_ab()
b7.pitch_list("1 c s s 1")
b7.out("K")

# 9. DET #21 JaCoby Jones (X - X - 12)
b7.new_ab()
b7.pitch_list("s 1 s b 1 s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: DET #58 Victor Alcántara
t8 = game.new_inning()

# 4. BOS #25 Steve Pearce (X - X - X)
t8.new_ab()
t8.pitch_list("c b f")
t8.hit(1)
t8.advance(2, "2 G5-3")
t8.advance(3, "18 G3-1")

# 5. BOS #2  Xander Bogaerts (X - X - 25)
t8.new_ab()
t8.pitch_list("b")
t8.out("G5-3")

# 6. BOS #18 Mitch Moreland (X - 25 - X)
t8.new_ab()
t8.pitch_list("f b")
t8.out("G3-1")

# 7. BOS #36 Eduardo Núñez (25 - X - X)
t8.new_ab()
t8.pitch_list("f f f f")
t8.out("G5-3")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree
b8.pitching_substitution(32)

# 1. DET #28 Niko Goodrum (X - X - X)
b8.new_ab()
b8.pitch_list("c s b s")
b8.wp()
b8.reach("K")
b8.advance(3, "46 WP")
b8.thrown_out(4, "9 FC5-2-5", 2, 32)

# 2. DET #46 Jeimer Candelario (X - X - 28)
b8.new_ab()
b8.pitch_list("c 1 f b s")
b8.wp()
b8.out("K")

# 3. DET #9  Nick Castellanos (28 - X - X)
b8.new_ab()
b8.pitch_list("f b")
b8.reach("FC5-2-5", end_base=2)

# 4. DET #55 John Hicks (X - 9 - X)
b8.new_ab()
b8.pitch_list("b s b s d b")
b8.reach("BB")

# 5. DET #34 James McCann (X - 9 - 55)
b8.new_ab()
b8.pitch_list("b c f f f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: DET #77 Joe Jiménez
t9 = game.new_inning()

# Pitching change (DET): #77 Joe Jiménez replaces #58 Victor Alcántara
t9.pitching_substitution(77)

# 8. BOS #5  Tzu-Wei Lin (X - X - X)
t9.new_ab()
t9.pitch_list("c b s b b s")
t9.out("K")

# 9. BOS #3  Sandy León (X - X - X)
t9.new_ab()
t9.pitch_list("f b s s")
t9.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F7")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
b9.pitching_substitution(46)

# 6. DET #41 Victor Martinez (X - X - X)
b9.new_ab()
b9.pitch_list("b c s f b f b")
b9.out("F8")

# 7. DET #12 Leonys Martin (X - X - X)
b9.new_ab()
b9.pitch_list("f c")
b9.hit(1)
# Offensive change (DET): Pinch-runner #22 Victor Reyes replaces #12 Leonys Martin
b9.offensive_substitution(7, 22, "PR")
b9.atbase("PR")
b9.thrown_out(2, "1 FC4-6", 2, 46)

# 8. DET #1  Jose Iglesias (X - X - 12)
b9.new_ab()
b9.pitch_list("1 1 b 1 s 1 s 1 f")
b9.reach("FC4-6")

# Offensive change (DET): Pinch-hitter #37 James Adduci replaces #21 JaCoby Jones, batting 9th
b9.offensive_substitution(9, 37, "PH")

# 9. DET #37 James Adduci (X - X - 1)
b9.new_ab()
b9.pitch_list("c b f b f f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: DET
# LP: DET #48 Matthew Boyd
game.losing_pitcher(48)

# print(game)
game.generate_scorecard()
