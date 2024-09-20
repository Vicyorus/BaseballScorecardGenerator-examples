import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TEX, 2018-05-03
# https://www.baseball-reference.com/boxes/TEX/TEX201805030.shtml
# https://www.mlb.com/gameday/red-sox-vs-rangers/2018/05/03/529873/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-03 20:14-23:34",
        "at": "Globe Life Park in Arlington, Arlington, TX",
        "att": "22,348",
        "temp": "77F, Partly Cloudy",
        "wind": "11mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                16: "Andrew Benintendi",
                3: "Sandy León",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 41, 31, 61],
            "lineup": [
                [50, "9"],
                [13, "3"],
                [28, "7"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [23, "0"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [5, "OF"],
                [18, "1B"],
                [16, "LF"],
                [3, "C"],
            ],
            "bullpen": [39, 22, 41, 31, 61, 37, 46, 76, 64, 56, 32],
        },
        "home": {
            "team": "Texas Rangers",
            "starter": 36,
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
                36: "Mike Minor",
                # Bench
                60: "Carlos Pérez",
                18: "Drew Robinson",
                # Bullpen
                41: "Jake Diekman",
                40: "Bartolo Colon",
                43: "Tony Barnette",
                53: "Jesse Chavez",
                55: "Matt Moore",
                65: "Yohander Méndez",
                32: "Kevin Jepsen",
                38: "Doug Fister",
                67: "Ronald Guzmán",
                58: "Alex Claudio",
                62: "José Leclerc",
                35: "Cole Hamels",
                50: "Keone Kela",
            },
            "lefties": [36, 41, 55, 65, 67, 58, 35],
            "lineup": [
                [3, "8"],
                [17, "0"],
                [9, "4"],
                [30, "9"],
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
            "bullpen": [41, 40, 43, 53, 55, 65, 32, 38, 67, 58, 62, 35, 50],
        },
        "umpires": {
            "HP": "Phil Cuzzi",
            "1B": "Adam Hamari",
            "2B": "Adrian Johnson",
            "3B": "Dan Bellino",
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
# Pitching: TEX #36 Mike Minor
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.out("F7")

# 2. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.out("G5-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.out("F9")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. TEX #3  Delino DeShields (X - X - X)
b1.new_ab()
b1.pitch_list("c c b b f s")
b1.out("K")

# 2. TEX #17 Shin-Soo Choo (X - X - X)
b1.new_ab()
b1.pitch_list("f b b c")
b1.out("G5-3")

# 3. TEX #9  Isiah Kiner-Falefa (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TEX #36 Mike Minor
t2 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c s")
t2.hit(2)

# 5. BOS #11 Rafael Devers (X - 2 - X)
t2.new_ab()
t2.pitch_list("b s b f f f b f c")
t2.out("!K")

# 6. BOS #36 Eduardo Núñez (X - 2 - X)
t2.new_ab()
t2.out("F8")

# 7. BOS #23 Blake Swihart (X - 2 - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 4. TEX #30 Nomar Mazara (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("L8")

# 5. TEX #13 Joey Gallo (X - X - X)
b2.new_ab()
b2.pitch_list("f b b b c f f")
b2.reach("HBP")
b2.advance(4, "19 3B")

# 6. TEX #19 Jurickson Profar (X - X - 13)
b2.new_ab()
b2.pitch_list("b")
b2.hit(3, rbis=1)
b2.advance(4, "20 SF7")

# 7. TEX #20 Renato Núñez (19 - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("SF7", rbis=1)

# 8. TEX #61 Robinson Chirinos (X - X - X)
b2.new_ab()
b2.pitch_list("b s f b f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TEX #36 Mike Minor
t3 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("c f b s")
t3.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("f b b f")
t3.out("(F)P2")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b b")
t3.hit(4)

# 2. BOS #13 Hanley Ramirez (X - X - X)
t3.new_ab()
t3.pitch_list("b f b b b")
t3.reach("BB")
t3.advance(2, "28 1B")

# 3. BOS #28 J.D. Martinez (X - X - 13)
t3.new_ab()
t3.pitch_list("s s b 1")
t3.hit(1)

# 4. BOS #2  Xander Bogaerts (X - 13 - 28)
t3.new_ab()
t3.pitch_list("c c b f b f")
t3.out("F8")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 9. TEX #16 Ryan Rua (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G5-3")

# 1. TEX #3  Delino DeShields (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.hit(1)
b3.advance(2, "17 E5")
b3.advance("U", "30 2B")

# 2. TEX #17 Shin-Soo Choo (X - X - 3)
b3.new_ab()
b3.pitch_list("f s b")
b3.error(5)
b3.reach("E5")
b3.advance(3, "30 2B")
b3.advance("U", "30 2B")

# 3. TEX #9  Isiah Kiner-Falefa (X - 3 - 17)
b3.new_ab()
b3.pitch_list("f")
b3.out("IF5")

# 4. TEX #30 Nomar Mazara (X - 3 - 17)
b3.new_ab()
b3.pitch_list("f f")
b3.hit(2, rbis=2)

# 5. TEX #13 Joey Gallo (X - 30 - X)
b3.new_ab()
b3.pitch_list("s f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TEX #36 Mike Minor
t4 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.error(8)
t4.advance(2, "36 1B")
t4.advance(3, "36 E8")
t4.advance(4, "7 1B")

# 6. BOS #36 Eduardo Núñez (X - X - 11)
t4.new_ab()
t4.pitch_list("1")
t4.hit(1)
t4.advance(2, "E8")
t4.advance(3, "7 1B")
t4.advance(4, "50 SF9")

# 7. BOS #23 Blake Swihart (11 - 36 - X)
t4.new_ab()
t4.pitch_list("c b b b t b")
t4.reach("BB")
t4.advance(2, "7 1B")
t4.advance(3, "50 SF9")

# 8. BOS #7  Christian Vázquez (11 - 36 - 23)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1, rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (36 - 23 - 7)
t4.new_ab()
t4.pitch_list("f f c")
t4.out("!K")

# 1. BOS #50 Mookie Betts (36 - 23 - 7)
t4.new_ab()
t4.pitch_list("b")
t4.out("SF9", rbis=1)

# 2. BOS #13 Hanley Ramirez (23 - X - 7)
t4.new_ab()
t4.pitch_list("b b")
t4.out("G1-3")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 6. TEX #19 Jurickson Profar (X - X - X)
b4.new_ab()
b4.pitch_list("b b f b b")
b4.reach("BB")
b4.advance(2, "61 1B")
b4.advance(4, "16 1B")

# 7. TEX #20 Renato Núñez (X - X - 19)
b4.new_ab()
b4.pitch_list("b c b 1 s b")
b4.out("(F)P3")

# 8. TEX #61 Robinson Chirinos (X - X - 19)
b4.new_ab()
b4.pitch_list("b c b f")
b4.hit(1)
b4.advance(2, "16 1B")
b4.advance(3, "3 1B")
b4.advance(4, "9 BB")

# 9. TEX #16 Ryan Rua (X - 19 - 61)
b4.new_ab()
b4.pitch_list("f")
b4.hit(1, rbis=1)
b4.advance(2, "3 1B")
b4.advance(3, "9 BB")
b4.advance(4, "30 WP")

# 1. TEX #3  Delino DeShields (X - 61 - 16)
b4.new_ab()
b4.pitch_list("f b b f")
b4.hit(1)
b4.advance(2, "9 BB")
b4.advance(3, "30 WP")
b4.advance(4, "30 HR")

# 2. TEX #17 Shin-Soo Choo (61 - 16 - 3)
b4.new_ab()
b4.pitch_list("b 3 s f b s")
b4.out("K")

# 3. TEX #9  Isiah Kiner-Falefa (61 - 16 - 3)
b4.new_ab()
b4.pitch_list("b f f b d b")
b4.reach("BB", rbis=1)
b4.advance(2, "30 WP")
b4.advance(4, "30 HR")

# Pitching change (BOS): #76 Hector Velázquez replaces #24 David Price
b4.pitching_substitution(76)

# 4. TEX #30 Nomar Mazara (16 - 3 - 9)
b4.new_ab()
b4.pitch_list("b f b b")
b4.wp()
b4.hit(4, rbis=3)

# 5. TEX #13 Joey Gallo (X - X - X)
b4.new_ab()
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TEX #36 Mike Minor
t5 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.pitch_list("c f b b b f")
t5.hit(1)
t5.advance(2, "2 BB")
t5.advance(3, "11 FC4-6")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
t5.new_ab()
t5.pitch_list("b c d b b")
t5.reach("BB")
t5.thrown_out(2, "11 FC4-6", 1, 36)

# 5. BOS #11 Rafael Devers (X - 28 - 2)
t5.new_ab()
t5.pitch_list("c b")
t5.reach("FC4-6")
t5.thrown_out(2, "23 FC6-4", 3, 36)

# 6. BOS #36 Eduardo Núñez (28 - X - 11)
t5.new_ab()
t5.pitch_list("s s s")
t5.out("K")

# 7. BOS #23 Blake Swihart (28 - X - 11)
t5.new_ab()
t5.pitch_list("c b c")
t5.reach("FC6-4")


# Bot 5th
# Pitching: BOS #76 Hector Velázquez
b5 = game.new_inning()

# 6. TEX #19 Jurickson Profar (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")
b5.error(6)
b5.advance(2, "61 FC6")
b5.advance(3, "61 E6")

# 7. TEX #20 Renato Núñez (X - X - 19)
b5.new_ab()
b5.pitch_list("c f s")
b5.out("K")

# 8. TEX #61 Robinson Chirinos (X - X - 19)
b5.new_ab()
b5.pitch_list("c d d b")
b5.reach("FC6")
b5.thrown_out(2, "3 FC6-4", 3, 64)

# Pitching change (BOS): #64 Marcus Walden replaces #76 Hector Velázquez
b5.pitching_substitution(64)

# 9. TEX #16 Ryan Rua (19 - X - 61)
b5.new_ab()
b5.pitch_list("c b s s")
b5.out("K")

# 1. TEX #3  Delino DeShields (19 - X - 61)
b5.new_ab()
b5.pitch_list("c b f f")
b5.reach("FC6-4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TEX #36 Mike Minor
t6 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.out("L4")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c f b")
t6.out("G3-1")


# Bot 6th
# Pitching: BOS #64 Marcus Walden
b6 = game.new_inning()

# 2. TEX #17 Shin-Soo Choo (X - X - X)
b6.new_ab()
b6.pitch_list("f b")
b6.hit(1)
b6.thrown_out(3, "9 9-5", 1, 64)
b6.advance(2, "9 1B")

# 3. TEX #9  Isiah Kiner-Falefa (X - X - 17)
b6.new_ab()
b6.pitch_list("b c")
b6.hit(1)
b6.advance(2, "30 G3")
b6.advance(3, "13 WP")

# 4. TEX #30 Nomar Mazara (X - X - 9)
b6.new_ab()
b6.pitch_list("b b")
b6.out("G3")

# 5. TEX #13 Joey Gallo (X - 9 - X)
b6.new_ab()
b6.pitch_list("f s b b b s")
b6.wp()
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TEX #62 José Leclerc
t7 = game.new_inning()

# Pitching change (TEX): #62 José Leclerc replaces #36 Mike Minor
t7.pitching_substitution(62)

# 2. BOS #13 Hanley Ramirez (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("G6-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("b b f b f s")
t7.out("K")

# 4. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.error(4)
t7.reach("E4")
t7.thrown_out(2, "11 FC6", 3, 62)

# 5. BOS #11 Rafael Devers (X - X - 2)
t7.new_ab()
t7.pitch_list("b f b b")
t7.reach("FC6")


# Bot 7th
# Pitching: BOS #64 Marcus Walden
b7 = game.new_inning()

# 6. TEX #19 Jurickson Profar (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b s")
b7.out("K")

# 7. TEX #20 Renato Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("c b c")
b7.error(6)
b7.reach("E6", end_base=2)
b7.advance(3, "61 2B")
b7.advance("U", "61 2B")

# 8. TEX #61 Robinson Chirinos (X - 20 - X)
b7.new_ab()
b7.pitch_list("c s")
b7.hit(2, rbis=1)

# 9. TEX #16 Ryan Rua (X - 61 - X)
b7.new_ab()
b7.pitch_list("b b s f")
b7.out("G1-3")

# 1. TEX #3  Delino DeShields (X - 61 - X)
b7.new_ab()
b7.out("L8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TEX #62 José Leclerc
t8 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("F9")

# 7. BOS #23 Blake Swihart (X - X - X)
t8.new_ab()
t8.pitch_list("b b c t b f b")
t8.reach("BB")
t8.advance(2, "7 1B")
t8.advance(4, "50 2B")

# 8. BOS #7  Christian Vázquez (X - X - 23)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.advance(4, "50 2B")

# 9. BOS #19 Jackie Bradley Jr. (X - 23 - 7)
t8.new_ab()
t8.pitch_list("b f b s s")
t8.out("K")

# 1. BOS #50 Mookie Betts (X - 23 - 7)
t8.new_ab()
t8.pitch_list("c c b")
t8.hit(2, rbis=2)

# Pitching change (TEX): #43 Tony Barnette replaces #62 José Leclerc
t8.pitching_substitution(43)

# 2. BOS #13 Hanley Ramirez (X - 50 - X)
t8.new_ab()
t8.pitch_list("d")
t8.out("G4-3")


# Bot 8th
# Pitching: BOS #64 Marcus Walden
b8 = game.new_inning()

# Pitching change (BOS): #64 Marcus Walden replaces #64 Marcus Walden, batting 8th
b8.pitching_substitution(64)
b8.defensive_substitution(8, 64, "1")

# Defensive switch (BOS): #23 Blake Swihart moves to C
b8.defensive_switch(23, "2")

# Defensive change (BOS): #5 Tzu-Wei Lin replaces #2 Xander Bogaerts (SS), playing SS, batting 4th
b8.defensive_substitution(4, 5, "6")

# 2. TEX #17 Shin-Soo Choo (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.hit(1)
b8.thrown_out(2, "9 DP6-4-3", 1, 64)

# 3. TEX #9  Isiah Kiner-Falefa (X - X - 17)
b8.new_ab()
b8.pitch_list("c")
b8.out("DP6-4-3")

# 4. TEX #30 Nomar Mazara (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TEX #43 Tony Barnette
t9 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("b c b f b f")
t9.out("G6-3")

# 4. BOS #5  Tzu-Wei Lin (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G4-3")

# 5. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("c s b f b")
t9.out("G6-3")

# Winning team: TEX
# WP: TEX #36 Mike Minor
game.winning_pitcher(36)

# Loser team: BOS
# LP: BOS #24 David Price
game.losing_pitcher(24, is_away_team=True)

# print(game)
game.generate_scorecard()
