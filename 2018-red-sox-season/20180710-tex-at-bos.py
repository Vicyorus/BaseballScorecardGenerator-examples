import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TEX @ BOS, 2018-07-10
# https://www.baseball-reference.com/boxes/BOS/BOS201807100.shtml
# https://www.mlb.com/gameday/rangers-vs-red-sox/2018/07/10/530784/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-10 19:11-22:07",
        "at": "Fenway Park, Boston, MA",
        "att": "36,883",
        "temp": "91F, Clear",
        "wind": "12mph, Out To RF",
        "away": {
            "team": "Texas Rangers",
            "starter": 49,
            "roster": {
                # Lineup
                17: "Shin-Soo Choo",
                1: "Elvis Andrus",
                30: "Nomar Mazara",
                29: "Adrian Beltré",
                12: "Rougned Odor",
                67: "Ronald Guzmán",
                9: "Isiah Kiner-Falefa",
                13: "Joey Gallo",
                3: "Delino DeShields",
                # Starting pitcher
                49: "Yovani Gallardo",
                # Bench
                61: "Robinson Chirinos",
                19: "Jurickson Profar",
                15: "Carlos Tocci",
                16: "Ryan Rua",
                # Bullpen
                41: "Jake Diekman",
                44: "Cory Gearrin",
                40: "Bartolo Colon",
                53: "Jesse Chavez",
                36: "Mike Minor",
                55: "Matt Moore",
                68: "Ricardo Rodríguez",
                58: "Alex Claudio",
                62: "José Leclerc",
                35: "Cole Hamels",
                50: "Keone Kela",
            },
            "lefties": [41, 36, 55, 58, 35],
            "lineup": [
                [17, "0"],
                [1, "6"],
                [30, "9"],
                [29, "5"],
                [12, "4"],
                [67, "3"],
                [9, "2"],
                [13, "7"],
                [3, "8"],
            ],
            "bench": [
                [61, "C"],
                [19, "LF"],
                [15, "OF"],
                [16, "LF"],
            ],
            "bullpen": [41, 44, 40, 53, 36, 55, 68, 58, 62, 35, 50],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 76,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                12: "Brock Holt",
                11: "Rafael Devers",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                76: "Hector Velázquez",
                # Bench
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                68: "Jalen Beeks",
                22: "Rick Porcello",
                41: "Chris Sale",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 68, 41, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [12, "4"],
                [11, "5"],
                [23, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [36, "SS"],
                [3, "C"],
            ],
            "bullpen": [47, 57, 44, 68, 22, 41, 37, 24, 46, 70, 56, 32],
        },
        "umpires": {
            "HP": "Alan Porter",
            "1B": "Marvin Hudson",
            "2B": "Bill Miller",
            "3B": "Todd Tichenor",
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
# Pitching: BOS #76 Hector Velázquez
t1 = game.new_inning()

# 1. TEX #17 Shin-Soo Choo (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G4-3")

# 2. TEX #1  Elvis Andrus (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G6-3")

# 3. TEX #30 Nomar Mazara (X - X - X)
t1.new_ab()
t1.pitch_list("c s b")
t1.out("G6-3")


# Bot 1st
# Pitching: TEX #49 Yovani Gallardo
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b c b c b f")
b1.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b s b b")
b1.reach("BB")
b1.thrown_out(2, "28 DP6-4-3", 2, 49)

# 3. BOS #28 J.D. Martinez (X - X - 16)
b1.new_ab()
b1.pitch_list("c 1 d 1")
b1.out("DP6-4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #76 Hector Velázquez
t2 = game.new_inning()

# 4. TEX #29 Adrian Beltré (X - X - X)
t2.new_ab()
t2.pitch_list("c c f f f s")
t2.out("K")

# 5. TEX #12 Rougned Odor (X - X - X)
t2.new_ab()
t2.hit(4)

# 6. TEX #67 Ronald Guzmán (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(2)

# 7. TEX #9  Isiah Kiner-Falefa (X - 67 - X)
t2.new_ab()
t2.pitch_list("c c")
t2.out("G5-3")

# 8. TEX #13 Joey Gallo (X - 67 - X)
t2.new_ab()
t2.pitch_list("b f f f b b d")
t2.reach("BB")

# 9. TEX #3  Delino DeShields (X - 67 - 13)
t2.new_ab()
t2.pitch_list("c b b")
t2.out("F9")


# Bot 2nd
# Pitching: TEX #49 Yovani Gallardo
b2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c")
b2.out("G3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G3")

# 6. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.pitch_list("c b b c f b c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #76 Hector Velázquez
t3 = game.new_inning()

# 1. TEX #17 Shin-Soo Choo (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b b")
t3.reach("BB")
t3.thrown_out(2, "30 FC4-6", 2, 76)

# 2. TEX #1  Elvis Andrus (X - X - 17)
t3.new_ab()
t3.pitch_list("b")
t3.out("P5")

# 3. TEX #30 Nomar Mazara (X - X - 17)
t3.new_ab()
t3.pitch_list("1 f s b b")
t3.reach("FC4-6")

# 4. TEX #29 Adrian Beltré (X - X - 30)
t3.new_ab()
t3.pitch_list("b f f d s")
t3.out("K")


# Bot 3rd
# Pitching: TEX #49 Yovani Gallardo
b3 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("c b b")
b3.out("L8")

# 8. BOS #23 Blake Swihart (X - X - X)
b3.new_ab()
b3.pitch_list("b c f f f")
b3.hit(2)
b3.advance(4, "19 2B")

# 9. BOS #19 Jackie Bradley Jr. (X - 23 - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(2, rbis=1)
b3.advance(4, "16 2B")

# 1. BOS #50 Mookie Betts (X - 19 - X)
b3.new_ab()
b3.pitch_list("c b b c t")
b3.out("KT")

# 2. BOS #16 Andrew Benintendi (X - 19 - X)
b3.new_ab()
b3.pitch_list("c d b")
b3.hit(2, rbis=1)
b3.advance(3, "28 1B")
b3.advance(4, "18 1B")

# 3. BOS #28 J.D. Martinez (X - 16 - X)
b3.new_ab()
b3.pitch_list("b b")
b3.hit(1)
b3.advance(3, "18 1B")
b3.advance(4, "2 3B")

# 4. BOS #18 Mitch Moreland (16 - X - 28)
b3.new_ab()
b3.hit(1, rbis=1)
b3.advance(4, "2 3B")

# 5. BOS #2  Xander Bogaerts (28 - X - 18)
b3.new_ab()
b3.pitch_list("c")
b3.hit(3, rbis=2)

# 6. BOS #12 Brock Holt (2 - X - X)
b3.new_ab()
b3.pitch_list("c d b b f")
b3.out("G3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #68 Jalen Beeks
t4 = game.new_inning()

# Pitching change (BOS): #68 Jalen Beeks replaces #76 Hector Velázquez
t4.pitching_substitution(68)

# 5. TEX #12 Rougned Odor (X - X - X)
t4.new_ab()
t4.pitch_list("c b c b f b")
t4.reach("HBP")
t4.advance(3, "67 1B")
t4.advance(4, "9 DP1-6-3")

# 6. TEX #67 Ronald Guzmán (X - X - 12)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.thrown_out(2, "9 DP1-6-3", 1, 68)

# 7. TEX #9  Isiah Kiner-Falefa (12 - X - 67)
t4.new_ab()
t4.pitch_list("d b c 1 f")
t4.out("DP1-6-3")

# 8. TEX #13 Joey Gallo (X - X - X)
t4.new_ab()
t4.pitch_list("b s b s b f f b")
t4.reach("BB")
t4.thrown_out(2, "3 FC5-4", 3, 68)

# 9. TEX #3  Delino DeShields (X - X - 13)
t4.new_ab()
t4.pitch_list("b")
t4.reach("FC5-4")


# Bot 4th
# Pitching: TEX #49 Yovani Gallardo
b4 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("f b b f b")
b4.out("G5-3")

# 8. BOS #23 Blake Swihart (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("F7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c c f")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #68 Jalen Beeks
t5 = game.new_inning()

# 1. TEX #17 Shin-Soo Choo (X - X - X)
t5.new_ab()
t5.pitch_list("b s b f c")
t5.out("!K")

# 2. TEX #1  Elvis Andrus (X - X - X)
t5.new_ab()
t5.pitch_list("b f s b")
t5.hit(1)
t5.thrown_out(2, "29 FC6-4", 3, 68)

# 3. TEX #30 Nomar Mazara (X - X - 1)
t5.new_ab()
t5.pitch_list("b")
t5.out("F9")

# 4. TEX #29 Adrian Beltré (X - X - 1)
t5.new_ab()
t5.pitch_list("d s")
t5.reach("FC6-4")


# Bot 5th
# Pitching: TEX #49 Yovani Gallardo
b5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("b b s")
b5.hit(2)
b5.advance(3, "16 G3-1")
b5.advance(4, "18 SF8")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b5.new_ab()
b5.pitch_list("s b b")
b5.out("G3-1")

# 3. BOS #28 J.D. Martinez (50 - X - X)
b5.new_ab()
b5.pitch_list("d d b b")
b5.reach("BB")
b5.thrown_out(2, "2 FC6-4", 3, 49)

# 4. BOS #18 Mitch Moreland (50 - X - 28)
b5.new_ab()
b5.pitch_list("1 b b")
b5.out("SF8", rbis=1)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b5.new_ab()
b5.pitch_list("d c 1 c b")
b5.reach("FC6-4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #68 Jalen Beeks
t6 = game.new_inning()

# 5. TEX #12 Rougned Odor (X - X - X)
t6.new_ab()
t6.pitch_list("f b b")
t6.hit(1)
t6.advance(3, "9 2B")
t6.advance(4, "13 2B")

# 6. TEX #67 Ronald Guzmán (X - X - 12)
t6.new_ab()
t6.pitch_list("b c f b")
t6.out("L8")

# 7. TEX #9  Isiah Kiner-Falefa (X - X - 12)
t6.new_ab()
t6.hit(2)
t6.advance(4, "13 2B")

# Pitching change (BOS): #44 Brandon Workman replaces #68 Jalen Beeks
t6.pitching_substitution(44)

# 8. TEX #13 Joey Gallo (12 - 9 - X)
t6.new_ab()
t6.pitch_list("b b s s")
t6.hit(2, rbis=2)

# 9. TEX #3  Delino DeShields (X - 13 - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F7")

# 1. TEX #17 Shin-Soo Choo (X - 13 - X)
t6.new_ab()
t6.pitch_list("c b f")
t6.out("G4-3")


# Bot 6th
# Pitching: TEX #68 Ricardo Rodríguez
b6 = game.new_inning()

# Pitching change (TEX): #68 Ricardo Rodríguez replaces #49 Yovani Gallardo
b6.pitching_substitution(68)

# 6. BOS #12 Brock Holt (X - X - X)
b6.new_ab()
b6.hit(1)
b6.thrown_out(2, "11 DP6-3", 1, 68)

# 7. BOS #11 Rafael Devers (X - X - 12)
b6.new_ab()
b6.pitch_list("c b 1")
b6.out("DP6-3")

# 8. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.hit(1)
b6.advance(4, "19 2B")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 23)
b6.new_ab()
b6.hit(2, rbis=1)
b6.thrown_out(3, "8-6-2-5", 3, 68)


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Matt Barnes
t7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #44 Brandon Workman
t7.pitching_substitution(32)

# 2. TEX #1  Elvis Andrus (X - X - X)
t7.new_ab()
t7.pitch_list("c b c s")
t7.out("K")

# 3. TEX #30 Nomar Mazara (X - X - X)
t7.new_ab()
t7.pitch_list("s b b b s f c")
t7.out("!K")

# 4. TEX #29 Adrian Beltré (X - X - X)
t7.new_ab()
t7.pitch_list("f c b s")
t7.out("K2-3")


# Bot 7th
# Pitching: TEX #68 Ricardo Rodríguez
b7 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.hit(1)
b7.advance(4, "16 2B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b7.new_ab()
b7.pitch_list("f 1 f")
b7.hit(2, rbis=1)
b7.advance(3, "12 SB")

# 3. BOS #28 J.D. Martinez (X - 16 - X)
b7.new_ab()
b7.pitch_list("b c c f d f f s")
b7.out("K")

# 4. BOS #18 Mitch Moreland (X - 16 - X)
b7.new_ab()
b7.pitch_list("v v v v")
b7.reach("IBB")
b7.error(2)
b7.advance(2, "12 E2")

# 5. BOS #2  Xander Bogaerts (X - 16 - 18)
b7.new_ab()
b7.pitch_list("b c b")
b7.out("F9")

# Pitching change (TEX): #58 Alex Claudio replaces #68 Ricardo Rodríguez
b7.pitching_substitution(58)

# 6. BOS #12 Brock Holt (X - 16 - 18)
b7.new_ab()
b7.pitch_list("c d f b b f")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
t8.pitching_substitution(56)

# 5. TEX #12 Rougned Odor (X - X - X)
t8.new_ab()
t8.out("F7")

# 6. TEX #67 Ronald Guzmán (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G6-3")

# 7. TEX #9  Isiah Kiner-Falefa (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b b")
t8.out("G4-3")


# Bot 8th
# Pitching: TEX #58 Alex Claudio
b8 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
b8.advance(2, "23 G1-3")
b8.advance(3, "19 G4-3")

# 8. BOS #23 Blake Swihart (X - X - 11)
b8.new_ab()
b8.pitch_list("c b s d f f")
b8.out("G1-3")

# 9. BOS #19 Jackie Bradley Jr. (X - 11 - X)
b8.new_ab()
b8.pitch_list("b b")
b8.out("G4-3")

# 1. BOS #50 Mookie Betts (11 - X - X)
b8.new_ab()
b8.pitch_list("v v v v")
b8.reach("IBB")

# 2. BOS #16 Andrew Benintendi (11 - X - 50)
b8.new_ab()
b8.pitch_list("c b t b 1")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #70 Ryan Brasier
t9 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #56 Joe Kelly
t9.pitching_substitution(70)

# 8. TEX #13 Joey Gallo (X - X - X)
t9.new_ab()
t9.pitch_list("b b c")
t9.out("F9")

# 9. TEX #3  Delino DeShields (X - X - X)
t9.new_ab()
t9.pitch_list("c b s s")
t9.out("K")

# 1. TEX #17 Shin-Soo Choo (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b d")
t9.reach("BB")

# 2. TEX #1  Elvis Andrus (X - X - 17)
t9.new_ab()
t9.pitch_list("c")
t9.out("G5-3")

# Winning team: BOS
# WP: BOS #32 Matt Barnes
game.winning_pitcher(32)

# Loser team: TEX
# LP: TEX #49 Yovani Gallardo
game.losing_pitcher(49, is_away_team=True)

# print(game)
game.generate_scorecard()
