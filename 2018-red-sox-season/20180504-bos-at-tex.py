import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TEX, 2018-05-04
# https://www.baseball-reference.com/boxes/TEX/TEX201805040.shtml
# https://www.mlb.com/gameday/red-sox-vs-rangers/2018/05/04/529881/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-04 20:08-22:44",
        "at": "Globe Life Park in Arlington, Arlington, TX",
        "att": "31,404",
        "temp": "69F, Partly Cloudy",
        "wind": "5mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                39: "Carson Smith",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 31, 61, 66, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [3, "2"],
            ],
            "bench": [
                [5, "OF"],
                [18, "1B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [39, 41, 31, 61, 66, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Texas Rangers",
            "starter": 40,
            "roster": {
                # Lineup
                3: "Delino DeShields",
                17: "Shin-Soo Choo",
                19: "Jurickson Profar",
                30: "Nomar Mazara",
                13: "Joey Gallo",
                9: "Isiah Kiner-Falefa",
                67: "Ronald Guzmán",
                61: "Robinson Chirinos",
                18: "Drew Robinson",
                # Starting pitcher
                40: "Bartolo Colon",
                # Bench
                60: "Carlos Pérez",
                20: "Renato Núñez",
                16: "Ryan Rua",
                # Bullpen
                41: "Jake Diekman",
                43: "Tony Barnette",
                53: "Jesse Chavez",
                36: "Mike Minor",
                55: "Matt Moore",
                65: "Yohander Méndez",
                32: "Kevin Jepsen",
                38: "Doug Fister",
                58: "Alex Claudio",
                62: "José Leclerc",
                35: "Cole Hamels",
                50: "Keone Kela",
            },
            "lefties": [41, 36, 55, 65, 58, 35],
            "lineup": [
                [3, "8"],
                [17, "0"],
                [19, "6"],
                [30, "9"],
                [13, "7"],
                [9, "5"],
                [67, "3"],
                [61, "2"],
                [18, "4"],
            ],
            "bench": [
                [60, "C"],
                [20, "1B"],
                [16, "LF"],
            ],
            "bullpen": [41, 43, 53, 36, 55, 65, 32, 38, 58, 62, 35, 50],
        },
        "umpires": {
            "HP": "Adam Hamari",
            "1B": "Adrian Johnson",
            "2B": "Dan Bellino",
            "3B": "Phil Cuzzi",
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
# Pitching: TEX #40 Bartolo Colon
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("s b c f c")
t1.out("!K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("L9")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. TEX #3  Delino DeShields (X - X - X)
b1.new_ab()
b1.pitch_list("b f c b f")
b1.hit(1)
b1.thrown_out(2, "17 DP5-6-3", 1, 22)

# 2. TEX #17 Shin-Soo Choo (X - X - 3)
b1.new_ab()
b1.pitch_list("f f b f f")
b1.out("DP5-6-3")

# 3. TEX #19 Jurickson Profar (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("L7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TEX #40 Bartolo Colon
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("b f f b")
t2.hit(4)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c c b c")
t2.out("!K")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("c f f s")
t2.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("c b f f f")
t2.out("G5-3")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 4. TEX #30 Nomar Mazara (X - X - X)
b2.new_ab()
b2.pitch_list("f b c b f f f")
b2.hit(2)
b2.advance(3, "13 G4-3")

# 5. TEX #13 Joey Gallo (X - 30 - X)
b2.new_ab()
b2.out("G4-3")

# 6. TEX #9  Isiah Kiner-Falefa (30 - X - X)
b2.new_ab()
b2.pitch_list("b f")
b2.out("G5-3")

# 7. TEX #67 Ronald Guzmán (30 - X - X)
b2.new_ab()
b2.pitch_list("b f f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TEX #40 Bartolo Colon
t3 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b c b")
t3.hit(1)
t3.advance(2, "50 G5-3")

# 9. BOS #3  Sandy León (X - X - 19)
t3.new_ab()
t3.pitch_list("1")
t3.out("L9")

# 1. BOS #50 Mookie Betts (X - X - 19)
t3.new_ab()
t3.pitch_list("1")
t3.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - 19 - X)
t3.new_ab()
t3.pitch_list("f c")
t3.out("G3")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 8. TEX #61 Robinson Chirinos (X - X - X)
b3.new_ab()
b3.pitch_list("c b c s")
b3.out("K")

# 9. TEX #18 Drew Robinson (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b s s")
b3.out("K")

# 1. TEX #3  Delino DeShields (X - X - X)
b3.new_ab()
b3.pitch_list("b f f b")
b3.out("L8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TEX #40 Bartolo Colon
t4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("b f b f")
t4.out("G6-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.out("L6")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.out("F7")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 2. TEX #17 Shin-Soo Choo (X - X - X)
b4.new_ab()
b4.pitch_list("c f b f f b s")
b4.out("K")

# 3. TEX #19 Jurickson Profar (X - X - X)
b4.new_ab()
b4.pitch_list("c s s")
b4.out("K")

# 4. TEX #30 Nomar Mazara (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s b f")
b4.hit(4)

# 5. TEX #13 Joey Gallo (X - X - X)
b4.new_ab()
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TEX #40 Bartolo Colon
t5 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("s b f b")
t5.hit(4)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.out("G1-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.out("G3")

# 9. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("c f b b f f")
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 6. TEX #9  Isiah Kiner-Falefa (X - X - X)
b5.new_ab()
b5.pitch_list("c b f b")
b5.out("G5-3")

# 7. TEX #67 Ronald Guzmán (X - X - X)
b5.new_ab()
b5.pitch_list("c b f b b t")
b5.out("KT")

# 8. TEX #61 Robinson Chirinos (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("P6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TEX #40 Bartolo Colon
t6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c f f f f")
t6.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("b c b f f")
t6.out("G3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t6.new_ab()
t6.pitch_list("c f b b")
t6.out("G6-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("c f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 9. TEX #18 Drew Robinson (X - X - X)
b6.new_ab()
b6.pitch_list("b c b c b f c")
b6.out("!K")

# 1. TEX #3  Delino DeShields (X - X - X)
b6.new_ab()
b6.pitch_list("f f s")
b6.out("K")

# 2. TEX #17 Shin-Soo Choo (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")

# 3. TEX #19 Jurickson Profar (X - X - 17)
b6.new_ab()
b6.pitch_list("b b f")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TEX #40 Bartolo Colon
t7 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.out("F9")

# 6. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("b f")
t7.hit(4)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("L7")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.out("L7")


# Bot 7th
# Pitching: BOS #56 Joe Kelly
b7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #22 Rick Porcello
b7.pitching_substitution(56)

# 4. TEX #30 Nomar Mazara (X - X - X)
b7.new_ab()
b7.pitch_list("b c s b")
b7.out("L8")

# 5. TEX #13 Joey Gallo (X - X - X)
b7.new_ab()
b7.pitch_list("b b f f b s")
b7.out("K")

# 6. TEX #9  Isiah Kiner-Falefa (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b")
b7.out("L9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TEX #41 Jake Diekman
t8 = game.new_inning()

# Pitching change (TEX): #41 Jake Diekman replaces #40 Bartolo Colon
t8.pitching_substitution(41)

# 9. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.pitch_list("c b b c b b")
t8.reach("BB")
t8.advance(4, "13 2B")

# 1. BOS #50 Mookie Betts (X - X - 3)
t8.new_ab()
t8.pitch_list("c c b d")
t8.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - 3)
t8.new_ab()
t8.pitch_list("d")
t8.out("P3")

# 3. BOS #13 Hanley Ramirez (X - X - 3)
t8.new_ab()
t8.pitch_list("c b b f b")
t8.hit(2, rbis=1)

# 4. BOS #28 J.D. Martinez (X - 13 - X)
t8.new_ab()
t8.pitch_list("f c b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
b8.pitching_substitution(32)

# 7. TEX #67 Ronald Guzmán (X - X - X)
b8.new_ab()
b8.pitch_list("c b b f s")
b8.out("K")

# 8. TEX #61 Robinson Chirinos (X - X - X)
b8.new_ab()
b8.pitch_list("c f b t")
b8.out("KT")

# 9. TEX #18 Drew Robinson (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TEX #53 Jesse Chavez
t9 = game.new_inning()

# Pitching change (TEX): #53 Jesse Chavez replaces #41 Jake Diekman
t9.pitching_substitution(53)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G1-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.hit(1)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t9.new_ab()
t9.pitch_list("c f d s")
t9.out("K")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 11)
t9.new_ab()
t9.pitch_list("b s s 1 b d c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #66 Bobby Poyner
b9 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #32 Matt Barnes
b9.pitching_substitution(66)

# 1. TEX #3  Delino DeShields (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)

# 2. TEX #17 Shin-Soo Choo (X - X - 3)
b9.new_ab()
b9.pitch_list("c s b b f f f f")
b9.out("L7")

# 3. TEX #19 Jurickson Profar (X - X - 3)
b9.new_ab()
b9.pitch_list("c 1 c f f b b f")
b9.out("F9")

# 4. TEX #30 Nomar Mazara (X - X - 3)
b9.new_ab()
b9.pitch_list("c f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22, is_away_team=True)

# Loser team: TEX
# LP: TEX #40 Bartolo Colon
game.losing_pitcher(40)

# print(game)
game.generate_scorecard()
