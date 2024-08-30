import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TEX, 2018-05-05
# https://www.baseball-reference.com/boxes/TEX/TEX201805050.shtml
# https://www.mlb.com/gameday/red-sox-vs-rangers/2018/05/05/529896/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-05 20:07-23:25",
        "at": "Globe Life Park in Arlington, Arlington, TX",
        "att": "35,728",
        "temp": "81F, Clear",
        "wind": "8mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                7: "Christian Vázquez",
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
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "8"],
                [13, "0"],
                [28, "7"],
                [2, "6"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [7, "2"],
            ],
            "bench": [
                [5, "OF"],
                [23, "C"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [39, 22, 41, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Texas Rangers",
            "starter": 35,
            "roster": {
                # Lineup
                3: "Delino DeShields",
                17: "Shin-Soo Choo",
                9: "Isiah Kiner-Falefa",
                30: "Nomar Mazara",
                13: "Joey Gallo",
                19: "Jurickson Profar",
                20: "Renato Núñez",
                61: "Robinson Chirinos",
                16: "Ryan Rua",
                # Starting pitcher
                35: "Cole Hamels",
                # Bench
                60: "Carlos Pérez",
                18: "Drew Robinson",
                # Bullpen
                41: "Jake Diekman",
                40: "Bartolo Colon",
                43: "Tony Barnette",
                53: "Jesse Chavez",
                36: "Mike Minor",
                55: "Matt Moore",
                65: "Yohander Méndez",
                32: "Kevin Jepsen",
                38: "Doug Fister",
                67: "Ronald Guzmán",
                58: "Alex Claudio",
                62: "José Leclerc",
                50: "Keone Kela",
            },
            "lefties": [35, 41, 36, 55, 65, 67, 58],
            "lineup": [
                [3, "8"],
                [17, "9"],
                [9, "4"],
                [30, "0"],
                [13, "3"],
                [19, "6"],
                [20, "5"],
                [61, "2"],
                [16, "7"],
            ],
            "bench": [
                [60, "C"],
                [18, "CF"],
            ],
            "bullpen": [41, 40, 43, 53, 36, 55, 65, 32, 38, 67, 58, 62, 50],
        },
        "umpires": {
            "HP": "Adrian Johnson",
            "1B": "Dan Bellino",
            "2B": "Phil Cuzzi",
            "3B": "Adam Hamari",
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
# Pitching: TEX #35 Cole Hamels
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("F7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("b b s c s")
t1.out("K")


# Bot 1st
# Pitching: BOS #57 Eduardo Rodriguez
b1 = game.new_inning()

# 1. TEX #3  Delino DeShields (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F9")

# 2. TEX #17 Shin-Soo Choo (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b b c")
b1.out("!K")

# 3. TEX #9  Isiah Kiner-Falefa (X - X - X)
b1.new_ab()
b1.pitch_list("c f f")
b1.out("G1-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TEX #35 Cole Hamels
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("c f")
t2.out("F9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c b f")
t2.hit(2)
t2.error(1)
t2.advance(3, "36 E1")

# 6. BOS #18 Mitch Moreland (X - 2 - X)
t2.new_ab()
t2.pitch_list("b d c f f d b")
t2.reach("BB")
t2.advance(2, "36 E1")

# 7. BOS #36 Eduardo Núñez (X - 2 - 18)
t2.new_ab()
t2.reach("FC1")

# 8. BOS #11 Rafael Devers (2 - 18 - 36)
t2.new_ab()
t2.pitch_list("f f b b s")
t2.out("K")

# 9. BOS #7  Christian Vázquez (2 - 18 - 36)
t2.new_ab()
t2.pitch_list("c c f d b f")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #57 Eduardo Rodriguez
b2 = game.new_inning()

# 4. TEX #30 Nomar Mazara (X - X - X)
b2.new_ab()
b2.pitch_list("c s b b f f f f b t")
b2.out("KT")

# 5. TEX #13 Joey Gallo (X - X - X)
b2.new_ab()
b2.pitch_list("s f b b")
b2.hit(4, rbis=1)

# 6. TEX #19 Jurickson Profar (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f")
b2.out("G4-3")

# 7. TEX #20 Renato Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")

# 8. TEX #61 Robinson Chirinos (X - X - 20)
b2.new_ab()
b2.pitch_list("f b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TEX #35 Cole Hamels
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b b c")
t3.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("F7")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b")
t3.hit(1)

# 4. BOS #28 J.D. Martinez (X - X - 13)
t3.new_ab()
t3.pitch_list("s b d s 1 d f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #57 Eduardo Rodriguez
b3 = game.new_inning()

# 9. TEX #16 Ryan Rua (X - X - X)
b3.new_ab()
b3.pitch_list("b b s c c")
b3.out("!K")

# 1. TEX #3  Delino DeShields (X - X - X)
b3.new_ab()
b3.out("F9")

# 2. TEX #17 Shin-Soo Choo (X - X - X)
b3.new_ab()
b3.pitch_list("b c s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TEX #35 Cole Hamels
t4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("c s b b s")
t4.out("K")

# 6. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b b f t")
t4.out("G3-1")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G5-3")


# Bot 4th
# Pitching: BOS #57 Eduardo Rodriguez
b4 = game.new_inning()

# 3. TEX #9  Isiah Kiner-Falefa (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("F9")

# 4. TEX #30 Nomar Mazara (X - X - X)
b4.new_ab()
b4.pitch_list("b f c")
b4.out("L5")

# 5. TEX #13 Joey Gallo (X - X - X)
b4.new_ab()
b4.pitch_list("b b c f b c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TEX #35 Cole Hamels
t5 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("b s")
t5.out("(F)F7")

# 9. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("f b b s b d")
t5.reach("BB")
t5.advance(3, "50 E5")
t5.advance("U", "16 1B")

# 1. BOS #50 Mookie Betts (X - X - 7)
t5.new_ab()
t5.pitch_list("b b")
t5.error(5)
t5.reach("E5", 2)

# 2. BOS #16 Andrew Benintendi (7 - 50 - X)
t5.new_ab()
t5.pitch_list("d")
t5.hit(1, rbis=1)
t5.thrown_out(2, "13 DP1-4-3", 2, 35)

# 3. BOS #13 Hanley Ramirez (X - 50 - 16)
t5.new_ab()
t5.pitch_list("b c f b b")
t5.out("DP1-4-3")


# Bot 5th
# Pitching: BOS #57 Eduardo Rodriguez
b5 = game.new_inning()

# 6. TEX #19 Jurickson Profar (X - X - X)
b5.new_ab()
b5.pitch_list("b c c s")
b5.out("K")

# 7. TEX #20 Renato Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("f b s f c")
b5.out("!K")

# 8. TEX #61 Robinson Chirinos (X - X - X)
b5.new_ab()
b5.pitch_list("f b b b s")
b5.hit(1)
b5.advance(2, "16 BB")
b5.advance(4, "3 HR")

# 9. TEX #16 Ryan Rua (X - X - 61)
b5.new_ab()
b5.pitch_list("f c b b b f f f b")
b5.reach("BB")
b5.advance(4, "3 HR")

# 1. TEX #3  Delino DeShields (X - 61 - 16)
b5.new_ab()
b5.hit(4, rbis=3)

# 2. TEX #17 Shin-Soo Choo (X - X - X)
b5.new_ab()
b5.pitch_list("c b f b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TEX #35 Cole Hamels
t6 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("s b f b b")
t6.hit(1)
t6.advance(4, "18 HR")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t6.new_ab()
t6.pitch_list("c b f s")
t6.out("K")

# 6. BOS #18 Mitch Moreland (X - X - 28)
t6.new_ab()
t6.pitch_list("b s")
t6.hit(4, rbis=2)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("L8")

# 8. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G4-3")


# Bot 6th
# Pitching: BOS #57 Eduardo Rodriguez
b6 = game.new_inning()

# 3. TEX #9  Isiah Kiner-Falefa (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G6-3")

# 4. TEX #30 Nomar Mazara (X - X - X)
b6.new_ab()
b6.pitch_list("b b s c f s")
b6.out("K")

# 5. TEX #13 Joey Gallo (X - X - X)
b6.new_ab()
b6.pitch_list("s b")
b6.hit(4, rbis=1)

# 6. TEX #19 Jurickson Profar (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TEX #62 José Leclerc
t7 = game.new_inning()

# Pitching change (TEX): #62 José Leclerc replaces #35 Cole Hamels
t7.pitching_substitution(62)

# 9. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.out("P3")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c c b b b b")
t7.reach("BB")
t7.advance(4, "16 2B")

# Pitching change (TEX): #58 Alex Claudio replaces #62 José Leclerc
t7.pitching_substitution(58)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t7.new_ab()
t7.pitch_list("c b 1 1")
t7.hit(2)
t7.advance(3, "13 G1-3")
t7.advance(4, "28 1B")

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
t7.new_ab()
t7.pitch_list("s c b")
t7.out("G1-3")

# 4. BOS #28 J.D. Martinez (16 - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(1, rbis=1)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t7.new_ab()
t7.pitch_list("b c f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #37 Heath Hembree
b7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #57 Eduardo Rodriguez
b7.pitching_substitution(37)

# 7. TEX #20 Renato Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("c c s")
b7.out("K")

# 8. TEX #61 Robinson Chirinos (X - X - X)
b7.new_ab()
b7.pitch_list("s b s t")
b7.out("KT")

# 9. TEX #16 Ryan Rua (X - X - X)
b7.new_ab()
b7.pitch_list("s b b c f b c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TEX #58 Alex Claudio
t8 = game.new_inning()

# 6. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("c s b f b")
t8.hit(1)
t8.advance(2, "36 SAC1-3")
t8.thrown_out(3, "11 FC1-5", 2, 58)

# 7. BOS #36 Eduardo Núñez (X - X - 18)
t8.new_ab()
t8.pitch_list("1 l")
t8.out("SAC1-3")

# 8. BOS #11 Rafael Devers (X - 18 - X)
t8.new_ab()
t8.pitch_list("b f")
t8.reach("FC1-5")

# Pitching change (TEX): #32 Kevin Jepsen replaces #58 Alex Claudio
t8.pitching_substitution(32)

# 9. BOS #7  Christian Vázquez (X - X - 11)
t8.new_ab()
t8.pitch_list("b c")
t8.out("G1-4-3")


# Bot 8th
# Pitching: BOS #37 Heath Hembree
b8 = game.new_inning()

# 1. TEX #3  Delino DeShields (X - X - X)
b8.new_ab()
b8.pitch_list("c b f f b")
b8.hit(1)
b8.advance(3, "17 2B")

# 2. TEX #17 Shin-Soo Choo (X - X - 3)
b8.new_ab()
b8.pitch_list("b f")
b8.hit(2)

# 3. TEX #9  Isiah Kiner-Falefa (3 - 17 - X)
b8.new_ab()
b8.pitch_list("s f")
b8.out("G6-3")

# 4. TEX #30 Nomar Mazara (3 - 17 - X)
b8.new_ab()
b8.pitch_list("v v v v")
b8.reach("IBB")

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
b8.pitching_substitution(56)

# 5. TEX #13 Joey Gallo (3 - 17 - 30)
b8.new_ab()
b8.pitch_list("b f b f s")
b8.out("K")

# 6. TEX #19 Jurickson Profar (3 - 17 - 30)
b8.new_ab()
b8.pitch_list("f b f b f f d f f f c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TEX #50 Keone Kela
t9 = game.new_inning()

# Pitching change (TEX): #50 Keone Kela replaces #32 Kevin Jepsen
t9.pitching_substitution(50)

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("b b c c")
t9.out("(F)P3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("b b s c")
t9.hit(3)
t9.advance(4, "13 SF8")

# 3. BOS #13 Hanley Ramirez (16 - X - X)
t9.new_ab()
t9.pitch_list("s b b")
t9.out("SF8", rbis=1)

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.out("G3")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
b9.pitching_substitution(46)

# Defensive switch (BOS): #16 Andrew Benintendi moves to LF
b9.defensive_switch(16, "7")

# Defensive change (BOS): #19 Jackie Bradley Jr. replaces #28 J.D. Martinez (LF), playing CF, batting 4th
b9.defensive_substitution(4, 19, "8")

# 7. TEX #20 Renato Núñez (X - X - X)
b9.new_ab()
b9.out("(F)P3")

# 8. TEX #61 Robinson Chirinos (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c f s")
b9.out("K")

# Offensive change (TEX): Pinch-hitter #67 Ronald Guzmán replaces #16 Ryan Rua, batting 9th
b9.offensive_substitution(9, 67, "PH")

# 9. TEX #67 Ronald Guzmán (X - X - X)
b9.new_ab()
b9.pitch_list("b c f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #56 Joe Kelly
game.winning_pitcher(56, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: TEX
# LP: TEX #50 Keone Kela
game.losing_pitcher(50)

# print(game)
game.generate_scorecard()
