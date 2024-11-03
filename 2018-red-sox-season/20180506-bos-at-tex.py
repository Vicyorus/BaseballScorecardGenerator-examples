import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TEX, 2018-05-06
# https://www.baseball-reference.com/boxes/TEX/TEX201805060.shtml
# https://www.mlb.com/gameday/red-sox-vs-rangers/2018/05/06/529912/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-06 15:08-17:41",
        "at": "Globe Life Park in Arlington, Arlington, TX",
        "att": "28,360",
        "temp": "84F, Sunny",
        "wind": "4mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                5: "Tzu-Wei Lin",
                23: "Blake Swihart",
                13: "Hanley Ramirez",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [3, "2"],
            ],
            "bench": [
                [5, "OF"],
                [23, "C"],
                [13, "SS"],
                [7, "C"],
            ],
            "bullpen": [57, 39, 22, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Texas Rangers",
            "starter": 38,
            "roster": {
                # Lineup
                3: "Delino DeShields",
                17: "Shin-Soo Choo",
                9: "Isiah Kiner-Falefa",
                30: "Nomar Mazara",
                19: "Jurickson Profar",
                20: "Renato Núñez",
                16: "Ryan Rua",
                67: "Ronald Guzmán",
                60: "Carlos Pérez",
                # Starting pitcher
                38: "Doug Fister",
                # Bench
                61: "Robinson Chirinos",
                18: "Drew Robinson",
                13: "Joey Gallo",
                # Bullpen
                41: "Jake Diekman",
                40: "Bartolo Colon",
                43: "Tony Barnette",
                53: "Jesse Chavez",
                36: "Mike Minor",
                55: "Matt Moore",
                65: "Yohander Méndez",
                32: "Kevin Jepsen",
                58: "Alex Claudio",
                62: "José Leclerc",
                35: "Cole Hamels",
                50: "Keone Kela",
            },
            "lefties": [41, 36, 55, 65, 58, 35],
            "lineup": [
                [3, "8"],
                [17, "0"],
                [9, "4"],
                [30, "9"],
                [19, "6"],
                [20, "5"],
                [16, "7"],
                [67, "3"],
                [60, "2"],
            ],
            "bench": [
                [61, "C"],
                [18, "CF"],
                [13, "1B"],
            ],
            "bullpen": [41, 40, 43, 53, 36, 55, 65, 32, 58, 62, 35, 50],
        },
        "umpires": {
            "HP": "Dan Bellino",
            "1B": "Phil Cuzzi",
            "2B": "Adam Hamari",
            "3B": "Adrian Johnson",
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
# Pitching: TEX #38 Doug Fister
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b f b b")
t1.hit(1)
t1.advance(2, "16 G3")
t1.advance(4, "18 2B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.pitch_list("b 1 b 1 f 1")
t1.out("G3")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b f d b")
t1.reach("BB")
t1.advance(3, "18 2B")
t1.thrown_out(4, "2 FC5-2", 2, 38)

# 4. BOS #18 Mitch Moreland (X - 50 - 28)
t1.new_ab(is_risp=True)
t1.pitch_list("b c")
t1.hit(2, rbis=1)

# 5. BOS #2  Xander Bogaerts (28 - 18 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b")
t1.reach("FC5-2")

# 6. BOS #11 Rafael Devers (X - 18 - 2)
t1.new_ab(is_risp=True)
t1.out("G4-3")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. TEX #3  Delino DeShields (X - X - X)
b1.new_ab()
b1.pitch_list("b c f s")
b1.out("K")

# 2. TEX #17 Shin-Soo Choo (X - X - X)
b1.new_ab()
b1.pitch_list("c b s s")
b1.out("K")

# 3. TEX #9  Isiah Kiner-Falefa (X - X - X)
b1.new_ab()
b1.pitch_list("c f b b f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TEX #38 Doug Fister
t2 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G5-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("f b b s c")
t2.out("!K")

# 9. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 3)
t2.new_ab()
t2.pitch_list("c c")
t2.out("L8")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# Defensive change (BOS): #23 Blake Swihart replaces #50 Mookie Betts (RF), playing LF, batting 1st
b2.defensive_substitution(1, 23, "7")

# Defensive switch (BOS): #16 Andrew Benintendi moves to CF
b2.defensive_switch(16, "8")

# Defensive switch (BOS): #19 Jackie Bradley Jr. moves to RF
b2.defensive_switch(19, "9")

# 4. TEX #30 Nomar Mazara (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.reach("HBP")
b2.advance(2, "19 1B")
b2.advance(3, "67 E5")

# 5. TEX #19 Jurickson Profar (X - X - 30)
b2.new_ab()
b2.pitch_list("c f f")
b2.hit(1)
b2.advance(2, "67 E5")

# 6. TEX #20 Renato Núñez (X - 30 - 19)
b2.new_ab(is_risp=True)
b2.pitch_list("c c b s")
b2.out("K")

# 7. TEX #16 Ryan Rua (X - 30 - 19)
b2.new_ab(is_risp=True)
b2.pitch_list("b s s f s")
b2.out("K")

# 8. TEX #67 Ronald Guzmán (X - 30 - 19)
b2.new_ab(is_risp=True)
b2.pitch_list("b f b s")
b2.error(5)
b2.reach("E5")

# 9. TEX #60 Carlos Pérez (30 - 19 - 67)
b2.new_ab(is_risp=True)
b2.pitch_list("c b")
b2.out("L1")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TEX #38 Doug Fister
t3 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("f f c")
t3.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c")
t3.hit(2)
t3.advance(4, "2 1B")

# 4. BOS #18 Mitch Moreland (X - 28 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f b c")
t3.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.hit(1, rbis=1)
t3.advance(2, "T")

# 6. BOS #11 Rafael Devers (X - 2 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b c f f")
t3.out("F8")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 1. TEX #3  Delino DeShields (X - X - X)
b3.new_ab()
b3.pitch_list("c b s b b")
b3.hit(1)
b3.advance(2, "9 SB")

# 2. TEX #17 Shin-Soo Choo (X - X - 3)
b3.new_ab()
b3.pitch_list("c c s")
b3.out("K")

# 3. TEX #9  Isiah Kiner-Falefa (X - X - 3)
b3.new_ab(is_risp=True)
b3.pitch_list("b f b n b b")
b3.reach("BB")

# 4. TEX #30 Nomar Mazara (X - 3 - 9)
b3.new_ab(is_risp=True)
b3.pitch_list("f s s")
b3.out("K")

# 5. TEX #19 Jurickson Profar (X - 3 - 9)
b3.new_ab(is_risp=True)
b3.pitch_list("b b")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TEX #38 Doug Fister
t4 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("b s")
t4.out("L7")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("c b b")
t4.out("G6-3")

# 9. BOS #3  Sandy León (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b b")
t4.reach("BB")
t4.advance(2, "23 1B")
t4.thrown_out(3, "23 9-5", 3, 38)

# 1. BOS #23 Blake Swihart (X - X - 3)
t4.new_ab()
t4.pitch_list("c b b f 1")
t4.hit(1)


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 6. TEX #20 Renato Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("s")
b4.hit(1)
b4.thrown_out(2, "16 DP1-6-3", 1, 41)

# 7. TEX #16 Ryan Rua (X - X - 20)
b4.new_ab()
b4.out("DP1-6-3")

# 8. TEX #67 Ronald Guzmán (X - X - X)
b4.new_ab()
b4.pitch_list("c s b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TEX #38 Doug Fister
t5 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("L8")

# 4. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.out("G1-3")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 9. TEX #60 Carlos Pérez (X - X - X)
b5.new_ab()
b5.pitch_list("s f f f s")
b5.out("K")

# 1. TEX #3  Delino DeShields (X - X - X)
b5.new_ab()
b5.pitch_list("f f")
b5.reach("HBP")
b5.advance(2, "9 SB")

# 2. TEX #17 Shin-Soo Choo (X - X - 3)
b5.new_ab()
b5.pitch_list("c f")
b5.out("F8")

# 3. TEX #9  Isiah Kiner-Falefa (X - X - 3)
b5.new_ab(is_risp=True)
b5.pitch_list("s b b s b")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TEX #38 Doug Fister
t6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("c f b s")
t6.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("c f c")
t6.out("!K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("c b b c")
t6.hit(1)
t6.advance(2, "19 HBP")
t6.advance(4, "3 HR")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 36)
t6.new_ab()
t6.pitch_list("d 1 f s")
t6.reach("HBP")
t6.advance(4, "3 HR")

# 9. BOS #3  Sandy León (X - 36 - 19)
t6.new_ab(is_risp=True)
t6.pitch_list("b b")
t6.hit(4, rbis=3)

# 1. BOS #23 Blake Swihart (X - X - X)
t6.new_ab()
t6.pitch_list("b c s")
t6.out("G1-4-3")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 4. TEX #30 Nomar Mazara (X - X - X)
b6.new_ab()
b6.pitch_list("b c c s")
b6.out("K")

# 5. TEX #19 Jurickson Profar (X - X - X)
b6.new_ab()
b6.out("G4-3")

# 6. TEX #20 Renato Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("s c b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TEX #38 Doug Fister
t7 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("c f b f c")
t7.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(4)

# Pitching change (TEX): #53 Jesse Chavez replaces #38 Doug Fister
t7.pitching_substitution(53)

# 4. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("b c s f")
t7.hit(1)

# 5. BOS #2  Xander Bogaerts (X - X - 18)
t7.new_ab()
t7.pitch_list("b f f f f f f d f")
t7.out("F7")

# 6. BOS #11 Rafael Devers (X - X - 18)
t7.new_ab()
t7.pitch_list("c")
t7.out("G3")


# Bot 7th
# Pitching: BOS #41 Chris Sale
b7 = game.new_inning()

# 7. TEX #16 Ryan Rua (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c")
b7.hit(4)

# 8. TEX #67 Ronald Guzmán (X - X - X)
b7.new_ab()
b7.pitch_list("c f s")
b7.out("K")

# 9. TEX #60 Carlos Pérez (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F9")

# 1. TEX #3  Delino DeShields (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TEX #53 Jesse Chavez
t8 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("G1-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("s s f f b f s")
t8.out("K")

# 9. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.pitch_list("c c b b b")
t8.out("G3")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #41 Chris Sale
b8.pitching_substitution(32)

# 2. TEX #17 Shin-Soo Choo (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G5-3")

# 3. TEX #9  Isiah Kiner-Falefa (X - X - X)
b8.new_ab()
b8.pitch_list("b b c")
b8.out("G6-3")

# 4. TEX #30 Nomar Mazara (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TEX #43 Tony Barnette
t9 = game.new_inning()

# Pitching change (TEX): #43 Tony Barnette replaces #53 Jesse Chavez
t9.pitching_substitution(43)

# 1. BOS #23 Blake Swihart (X - X - X)
t9.new_ab()
t9.out("G3-1")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.out("F9")

# 3. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("c b s c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #39 Carson Smith
b9 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #32 Matt Barnes
b9.pitching_substitution(39)

# 5. TEX #19 Jurickson Profar (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("G6-3")

# 6. TEX #20 Renato Núñez (X - X - X)
b9.new_ab()
b9.pitch_list("c s")
b9.hit(1)
b9.advance(2, "67 DI")
b9.advance(3, "67 DI")

# 7. TEX #16 Ryan Rua (X - X - 20)
b9.new_ab()
b9.pitch_list("b f s s")
b9.out("K")

# 8. TEX #67 Ronald Guzmán (X - X - 20)
b9.new_ab(is_risp=True)
b9.pitch_list("s b s b s")
b9.out("K")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41, is_away_team=True)

# Loser team: TEX
# LP: TEX #38 Doug Fister
game.losing_pitcher(38)

# print(game)
game.generate_scorecard()
