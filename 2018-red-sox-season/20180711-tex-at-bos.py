import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TEX @ BOS, 2018-07-11
# https://www.baseball-reference.com/boxes/BOS/BOS201807110.shtml
# https://www.mlb.com/gameday/rangers-vs-red-sox/2018/07/11/530799/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-11 19:11-22:09",
        "at": "Fenway Park, Boston, MA",
        "att": "36,920",
        "temp": "69F, Clear",
        "wind": "9mph, Out To RF",
        "away": {
            "team": "Texas Rangers",
            "starter": 40,
            "roster": {
                # Lineup
                3: "Delino DeShields",
                1: "Elvis Andrus",
                30: "Nomar Mazara",
                29: "Adrian Beltré",
                12: "Rougned Odor",
                19: "Jurickson Profar",
                61: "Robinson Chirinos",
                13: "Joey Gallo",
                16: "Ryan Rua",
                # Starting pitcher
                40: "Bartolo Colon",
                # Bench
                15: "Carlos Tocci",
                9: "Isiah Kiner-Falefa",
                17: "Shin-Soo Choo",
                # Bullpen
                41: "Jake Diekman",
                44: "Cory Gearrin",
                68: "Ricardo Rodríguez",
                49: "Yovani Gallardo",
                53: "Jesse Chavez",
                67: "Ronald Guzmán",
                36: "Mike Minor",
                55: "Matt Moore",
                62: "José Leclerc",
                35: "Cole Hamels",
                50: "Keone Kela",
            },
            "lefties": [41, 67, 36, 55, 35],
            "lineup": [
                [3, "8"],
                [1, "6"],
                [30, "9"],
                [29, "0"],
                [12, "4"],
                [19, "5"],
                [61, "2"],
                [13, "7"],
                [16, "3"],
            ],
            "bench": [
                [15, "OF"],
                [9, "3B"],
                [17, "RF"],
            ],
            "bullpen": [41, 44, 68, 49, 53, 67, 36, 55, 62, 35, 50],
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
                12: "Brock Holt",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                25: "Steve Pearce",
                23: "Blake Swihart",
                # Bullpen
                63: "Robby Scott",
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                24: "David Price",
                44: "Brandon Workman",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                22: "Rick Porcello",
                56: "Joe Kelly",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [41, 63, 57, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [12, "4"],
                [36, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [23, "C"],
            ],
            "bullpen": [63, 47, 57, 24, 44, 46, 76, 70, 22, 56, 32, 37],
        },
        "umpires": {
            "HP": "Marvin Hudson",
            "1B": "Bill Miller",
            "2B": "Todd Tichenor",
            "3B": "Alan Porter",
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

# 1. TEX #3  Delino DeShields (X - X - X)
t1.new_ab()
t1.pitch_list("c b b c b f c")
t1.out("!K")

# 2. TEX #1  Elvis Andrus (X - X - X)
t1.new_ab()
t1.pitch_list("s s b b f f")
t1.hit(2)

# 3. TEX #30 Nomar Mazara (X - 1 - X)
t1.new_ab()
t1.pitch_list("f b f s")
t1.out("K")

# 4. TEX #29 Adrian Beltré (X - 1 - X)
t1.new_ab()
t1.pitch_list("b c s b")
t1.out("G5-3")


# Bot 1st
# Pitching: TEX #40 Bartolo Colon
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b c b b")
b1.hit(1)
b1.advance(2, "16 G1-5-3")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("1 l 1 1")
b1.out("G1-5-3")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
b1.new_ab()
b1.pitch_list("b b c f b c")
b1.out("!K")

# 4. BOS #18 Mitch Moreland (X - 50 - X)
b1.new_ab()
b1.pitch_list("b b b c")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 Chris Sale
t2 = game.new_inning()

# 5. TEX #12 Rougned Odor (X - X - X)
t2.new_ab()
t2.pitch_list("s")
t2.out("F7")

# 6. TEX #19 Jurickson Profar (X - X - X)
t2.new_ab()
t2.pitch_list("c f b")
t2.out("G3")

# 7. TEX #61 Robinson Chirinos (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)

# 8. TEX #13 Joey Gallo (X - X - 61)
t2.new_ab()
t2.pitch_list("b b c s b c")
t2.out("!K")


# Bot 2nd
# Pitching: TEX #40 Bartolo Colon
b2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("c c f")
b2.hit(1)
b2.error(1)
b2.advance(2, "12 POE1")
b2.advance(3, "12 G4-3")
b2.advance("U", "36 E4")

# 6. BOS #12 Brock Holt (X - X - 2)
b2.new_ab()
b2.pitch_list("b 1 b s")
b2.out("G4-3")

# 7. BOS #36 Eduardo Núñez (2 - X - X)
b2.new_ab()
b2.pitch_list("f b d b")
b2.error(4)
b2.reach("E4", 2)

# 8. BOS #3  Sandy León (X - 36 - X)
b2.new_ab()
b2.pitch_list("c f")
b2.out("P6")

# 9. BOS #19 Jackie Bradley Jr. (X - 36 - X)
b2.new_ab()
b2.pitch_list("b f b")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 Chris Sale
t3 = game.new_inning()

# 9. TEX #16 Ryan Rua (X - X - X)
t3.new_ab()
t3.pitch_list("c c s")
t3.out("K")

# 1. TEX #3  Delino DeShields (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b")
t3.out("(F)P3")

# 2. TEX #1  Elvis Andrus (X - X - X)
t3.new_ab()
t3.pitch_list("b f b c f f")
t3.out("F8")


# Bot 3rd
# Pitching: TEX #40 Bartolo Colon
b3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("b c b f b b")
b3.reach("BB")
b3.advance(2, "16 1B")
b3.advance(3, "28 DP6-4-3")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.thrown_out(2, "28 DP6-4-3", 1, 40)

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
b3.new_ab()
b3.pitch_list("b")
b3.out("DP6-4-3")

# 4. BOS #18 Mitch Moreland (50 - X - X)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")

# 5. BOS #2  Xander Bogaerts (50 - X - 18)
b3.new_ab()
b3.pitch_list("b c b")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 Chris Sale
t4 = game.new_inning()

# 3. TEX #30 Nomar Mazara (X - X - X)
t4.new_ab()
t4.pitch_list("f f b f")
t4.out("G4-3")

# 4. TEX #29 Adrian Beltré (X - X - X)
t4.new_ab()
t4.pitch_list("c b f")
t4.hit(1)
t4.thrown_out(2, "19 FC6-4", 3, 41)

# 5. TEX #12 Rougned Odor (X - X - 29)
t4.new_ab()
t4.pitch_list("s s c")
t4.out("!K")

# 6. TEX #19 Jurickson Profar (X - X - 29)
t4.new_ab()
t4.reach("FC6-4")


# Bot 4th
# Pitching: TEX #40 Bartolo Colon
b4 = game.new_inning()

# 6. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.out("G6-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G6-3")

# 8. BOS #3  Sandy León (X - X - X)
b4.new_ab()
b4.pitch_list("c b c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 Chris Sale
t5 = game.new_inning()

# 7. TEX #61 Robinson Chirinos (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b b")
t5.reach("BB")

# 8. TEX #13 Joey Gallo (X - X - 61)
t5.new_ab()
t5.pitch_list("b b f s c")
t5.out("!K")

# 9. TEX #16 Ryan Rua (X - X - 61)
t5.new_ab()
t5.pitch_list("c s b c")
t5.out("!K")

# 1. TEX #3  Delino DeShields (X - X - 61)
t5.new_ab()
t5.pitch_list("f c f f s")
t5.out("K")


# Bot 5th
# Pitching: TEX #40 Bartolo Colon
b5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.out("L9")

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("c b c b")
b5.hit(1)
b5.advance(2, "16 1B")
b5.advance(4, "28 2B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b5.new_ab()
b5.hit(1)
b5.advance(4, "28 2B")

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
b5.new_ab()
b5.pitch_list("b d")
b5.hit(2, rbis=2)
b5.advance(4, "2 3B")

# 4. BOS #18 Mitch Moreland (X - 28 - X)
b5.new_ab()
b5.pitch_list("f c c")
b5.out("!K")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
b5.new_ab()
b5.pitch_list("c d b f")
b5.hit(3, rbis=1)

# 6. BOS #12 Brock Holt (2 - X - X)
b5.new_ab()
b5.pitch_list("c c b")
b5.out("(F)P5")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 Chris Sale
t6 = game.new_inning()

# 2. TEX #1  Elvis Andrus (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(2)
t6.advance(3, "30 1B")

# 3. TEX #30 Nomar Mazara (X - 1 - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.thrown_out(2, "12 DP1-6-3", 2, 41)

# 4. TEX #29 Adrian Beltré (1 - X - 30)
t6.new_ab()
t6.pitch_list("b c s f s")
t6.out("K")

# 5. TEX #12 Rougned Odor (1 - X - 30)
t6.new_ab()
t6.out("DP1-6-3")


# Bot 6th
# Pitching: TEX #40 Bartolo Colon
b6 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.thrown_out(2, "9-6", 1, 40)

# Defensive change (TEX): #67 Ronald Guzmán replaces #3 Delino DeShields (CF), playing 1B, batting 1st
b6.defensive_substitution(1, 67, "3")

# Defensive switch (TEX): #16 Ryan Rua moves to CF
b6.defensive_switch(16, "8")

# 8. BOS #3  Sandy León (X - X - X)
b6.new_ab()
b6.hit(1)
b6.thrown_out(2, "50 FC6-4", 3, 40)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")

# 1. BOS #50 Mookie Betts (X - X - 3)
b6.new_ab()
b6.pitch_list("b b")
b6.reach("FC6-4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 Chris Sale
t7 = game.new_inning()

# 6. TEX #19 Jurickson Profar (X - X - X)
t7.new_ab()
t7.pitch_list("c f f")
t7.hit(1)
t7.advance(2, "16 PB")

# 7. TEX #61 Robinson Chirinos (X - X - 19)
t7.new_ab()
t7.pitch_list("f c s")
t7.out("K")

# 8. TEX #13 Joey Gallo (X - X - 19)
t7.new_ab()
t7.pitch_list("s s b s")
t7.out("K")

# 9. TEX #16 Ryan Rua (X - X - 19)
t7.new_ab()
t7.pitch_list("f b s b s")
t7.pb()
t7.out("K")


# Bot 7th
# Pitching: TEX #41 Jake Diekman
b7 = game.new_inning()

# Pitching change (TEX): #41 Jake Diekman replaces #40 Bartolo Colon
b7.pitching_substitution(41)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("b c b f c")
b7.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("c s s")
b7.out("K")

# 4. BOS #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.pitch_list("b s c s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #37 Heath Hembree
t8 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #41 Chris Sale
t8.pitching_substitution(37)

# 1. TEX #67 Ronald Guzmán (X - X - X)
t8.new_ab()
t8.pitch_list("s f f b s")
t8.out("K")

# 2. TEX #1  Elvis Andrus (X - X - X)
t8.new_ab()
t8.pitch_list("c f f f")
t8.hit(1)
t8.advance(2, "30 SB")
t8.advance(3, "30 WP")
t8.advance(4, "30 1B")

# 3. TEX #30 Nomar Mazara (X - X - 1)
t8.new_ab()
t8.pitch_list("b s f b b")
t8.wp()
t8.hit(1, rbis=1)
t8.advance(3, "12 2B")
t8.advance(4, "61 BB")

# 4. TEX #29 Adrian Beltré (X - X - 30)
t8.new_ab()
t8.pitch_list("c s t")
t8.out("KT")

# 5. TEX #12 Rougned Odor (X - X - 30)
t8.new_ab()
t8.hit(2)
t8.advance(3, "61 BB")

# 6. TEX #19 Jurickson Profar (30 - 12 - X)
t8.new_ab()
t8.pitch_list("d b c b b")
t8.reach("BB")
t8.advance(2, "61 BB")

# Pitching change (BOS): #46 Craig Kimbrel replaces #37 Heath Hembree
t8.pitching_substitution(46)

# 7. TEX #61 Robinson Chirinos (30 - 12 - 19)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB", rbis=1)

# 8. TEX #13 Joey Gallo (12 - 19 - 61)
t8.new_ab()
t8.pitch_list("b c s f b s")
t8.out("K")


# Bot 8th
# Pitching: TEX #53 Jesse Chavez
b8 = game.new_inning()

# Pitching change (TEX): #53 Jesse Chavez replaces #41 Jake Diekman
b8.pitching_substitution(53)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("f b")
b8.hit(1)
b8.thrown_out(2, "12 DP4-6-3", 1, 53)

# 6. BOS #12 Brock Holt (X - X - 2)
b8.new_ab()
b8.out("DP4-6-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.hit(1)

# 8. BOS #3  Sandy León (X - X - 36)
b8.new_ab()
b8.pitch_list("f c")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# 9. TEX #16 Ryan Rua (X - X - X)
t9.new_ab()
t9.pitch_list("c c b b c")
t9.out("!K")

# 1. TEX #67 Ronald Guzmán (X - X - X)
t9.new_ab()
t9.pitch_list("c f b s")
t9.out("K")

# 2. TEX #1  Elvis Andrus (X - X - X)
t9.new_ab()
t9.pitch_list("c c b s")
t9.out("K")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: TEX
# LP: TEX #40 Bartolo Colon
game.losing_pitcher(40, is_away_team=True)

# print(game)
game.generate_scorecard()
