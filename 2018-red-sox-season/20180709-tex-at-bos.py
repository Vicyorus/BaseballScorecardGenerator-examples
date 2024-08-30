import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TEX @ BOS, 2018-07-09
# https://www.baseball-reference.com/boxes/BOS/BOS201807090.shtml
# https://www.mlb.com/gameday/rangers-vs-red-sox/2018/07/09/530770/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-09 19:11-22:03",
        "at": "Fenway Park, Boston, MA",
        "att": "36,754",
        "temp": "88F, Clear",
        "wind": "15mph, Out To CF",
        "away": {
            "team": "Texas Rangers",
            "starter": 36,
            "roster": {
                # Lineup
                3: "Delino DeShields",
                1: "Elvis Andrus",
                30: "Nomar Mazara",
                29: "Adrian Beltré",
                12: "Rougned Odor",
                19: "Jurickson Profar",
                9: "Isiah Kiner-Falefa",
                61: "Robinson Chirinos",
                16: "Ryan Rua",
                # Starting pitcher
                36: "Mike Minor",
                # Bench
                17: "Shin-Soo Choo",
                15: "Carlos Tocci",
                13: "Joey Gallo",
                # Bullpen
                41: "Jake Diekman",
                44: "Cory Gearrin",
                49: "Yovani Gallardo",
                40: "Bartolo Colon",
                53: "Jesse Chavez",
                55: "Matt Moore",
                68: "Ricardo Rodríguez",
                67: "Ronald Guzmán",
                58: "Alex Claudio",
                62: "José Leclerc",
                35: "Cole Hamels",
                50: "Keone Kela",
            },
            "lefties": [36, 41, 55, 67, 58, 35],
            "lineup": [
                [3, "8"],
                [1, "6"],
                [30, "9"],
                [29, "0"],
                [12, "4"],
                [19, "3"],
                [9, "5"],
                [61, "2"],
                [16, "7"],
            ],
            "bench": [
                [17, "RF"],
                [15, "OF"],
                [13, "1B"],
            ],
            "bullpen": [41, 44, 49, 40, 53, 55, 68, 67, 58, 62, 35, 50],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                25: "Steve Pearce",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                3: "Sandy León",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                41: "Chris Sale",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 24],
            "lineup": [
                [50, "8"],
                [16, "7"],
                [28, "9"],
                [25, "0"],
                [2, "6"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [3, "2"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [19, "CF"],
            ],
            "bullpen": [47, 44, 67, 22, 41, 37, 24, 46, 76, 70, 56, 32],
        },
        "umpires": {
            "HP": "Todd Tichenor",
            "1B": "Alan Porter",
            "2B": "Marvin Hudson",
            "3B": "Bill Miller",
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

# 1. TEX #3  Delino DeShields (X - X - X)
t1.new_ab()
t1.pitch_list("c b b c b s")
t1.out("K")

# 2. TEX #1  Elvis Andrus (X - X - X)
t1.new_ab()
t1.pitch_list("s b b s")
t1.out("G6-3")

# 3. TEX #30 Nomar Mazara (X - X - X)
t1.new_ab()
t1.pitch_list("c b b c f b b")
t1.reach("BB")

# 4. TEX #29 Adrian Beltré (X - X - 30)
t1.new_ab()
t1.pitch_list("c b b s")
t1.out("L9")


# Bot 1st
# Pitching: TEX #36 Mike Minor
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c")
b1.out("L7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b c c b b c")
b1.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("b s b")
b1.hit(1)
b1.advance(4, "25 HR")

# 4. BOS #25 Steve Pearce (X - X - 28)
b1.new_ab()
b1.pitch_list("b b b c f f")
b1.hit(4, rbis=2)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("L7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 5. TEX #12 Rougned Odor (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b c")
t2.out("!K")

# 6. TEX #19 Jurickson Profar (X - X - X)
t2.new_ab()
t2.pitch_list("c c c")
t2.out("!K")

# 7. TEX #9  Isiah Kiner-Falefa (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b b b")
t2.reach("BB")

# 8. TEX #61 Robinson Chirinos (X - X - 9)
t2.new_ab()
t2.pitch_list("s b b c b")
t2.out("G5-3")


# Bot 2nd
# Pitching: TEX #36 Mike Minor
b2 = game.new_inning()

# 6. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("b f")
b2.out("G4-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("P4")

# 8. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("c f b f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 9. TEX #16 Ryan Rua (X - X - X)
t3.new_ab()
t3.pitch_list("c f")
t3.out("F7")

# 1. TEX #3  Delino DeShields (X - X - X)
t3.new_ab()
t3.pitch_list("f b f")
t3.out("L4")

# 2. TEX #1  Elvis Andrus (X - X - X)
t3.new_ab()
t3.pitch_list("b c s")
t3.out("G4-3")


# Bot 3rd
# Pitching: TEX #36 Mike Minor
b3 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.advance(3, "16 2B")

# 1. BOS #50 Mookie Betts (X - X - 3)
b3.new_ab()
b3.pitch_list("d f s")
b3.out("P3")

# 2. BOS #16 Andrew Benintendi (X - X - 3)
b3.new_ab()
b3.pitch_list("b b s c")
b3.hit(2)

# 3. BOS #28 J.D. Martinez (3 - 16 - X)
b3.new_ab()
b3.out("F8")

# 4. BOS #25 Steve Pearce (3 - 16 - X)
b3.new_ab()
b3.pitch_list("c f b")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 3. TEX #30 Nomar Mazara (X - X - X)
t4.new_ab()
t4.pitch_list("b f f b f c")
t4.out("!K")

# 4. TEX #29 Adrian Beltré (X - X - X)
t4.new_ab()
t4.pitch_list("b s b f")
t4.hit(1)
t4.advance(2, "19 1B")

# 5. TEX #12 Rougned Odor (X - X - 29)
t4.new_ab()
t4.pitch_list("f c c")
t4.out("!K")

# 6. TEX #19 Jurickson Profar (X - X - 29)
t4.new_ab()
t4.pitch_list("s b b b f")
t4.hit(1)

# 7. TEX #9  Isiah Kiner-Falefa (X - 29 - 19)
t4.new_ab()
t4.pitch_list("f f f f f b b")
t4.out("F7")


# Bot 4th
# Pitching: TEX #36 Mike Minor
b4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c s f f")
b4.out("L8")

# 6. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("f c b b")
b4.out("L8")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b f f f f")
b4.out("P6")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #57 Eduardo Rodriguez
t5 = game.new_inning()

# 8. TEX #61 Robinson Chirinos (X - X - X)
t5.new_ab()
t5.pitch_list("c b b")
t5.error(5)
t5.reach("E5")
t5.thrown_out(2, "16 FC5-4", 1, 57)

# 9. TEX #16 Ryan Rua (X - X - 61)
t5.new_ab()
t5.pitch_list("f s")
t5.reach("FC5-4")

# 1. TEX #3  Delino DeShields (X - X - 16)
t5.new_ab()
t5.pitch_list("c f")
t5.out("L6")

# 2. TEX #1  Elvis Andrus (X - X - 16)
t5.new_ab()
t5.pitch_list("t f")
t5.out("F8")


# Bot 5th
# Pitching: TEX #36 Mike Minor
b5 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("b f f s")
b5.out("K")

# 9. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G5-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.hit(2)

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b5.new_ab()
b5.pitch_list("b f c b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #57 Eduardo Rodriguez
t6 = game.new_inning()

# 3. TEX #30 Nomar Mazara (X - X - X)
t6.new_ab()
t6.out("G6-3")

# 4. TEX #29 Adrian Beltré (X - X - X)
t6.new_ab()
t6.pitch_list("c f")
t6.out("G1-3")

# 5. TEX #12 Rougned Odor (X - X - X)
t6.new_ab()
t6.hit(1)
t6.advance(2, "19 BB")

# 6. TEX #19 Jurickson Profar (X - X - 12)
t6.new_ab()
t6.pitch_list("d b b c b")
t6.reach("BB")

# Pitching change (BOS): #37 Heath Hembree replaces #57 Eduardo Rodriguez
t6.pitching_substitution(37)

# 7. TEX #9  Isiah Kiner-Falefa (X - 12 - 19)
t6.new_ab()
t6.pitch_list("c f f d s")
t6.out("K")


# Bot 6th
# Pitching: TEX #36 Mike Minor
b6 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("b s b s")
b6.out("G5-3")

# 4. BOS #25 Steve Pearce (X - X - X)
b6.new_ab()
b6.pitch_list("b c f")
b6.hit(1)

# Pitching change (TEX): #44 Cory Gearrin replaces #36 Mike Minor
b6.pitching_substitution(44)

# 5. BOS #2  Xander Bogaerts (X - X - 25)
b6.new_ab()
b6.pitch_list("c s s")
b6.out("K")

# 6. BOS #18 Mitch Moreland (X - X - 25)
b6.new_ab()
b6.pitch_list("b b s 1 b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #44 Brandon Workman
t7 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #37 Heath Hembree
t7.pitching_substitution(44)

# 8. TEX #61 Robinson Chirinos (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b")
t7.hit(3)

# Offensive change (TEX): Pinch-hitter #13 Joey Gallo replaces #16 Ryan Rua, batting 9th
t7.offensive_substitution(9, 13, "PH")

# 9. TEX #13 Joey Gallo (61 - X - X)
t7.new_ab()
t7.pitch_list("c b b s s")
t7.out("K")

# 1. TEX #3  Delino DeShields (61 - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G5-3")

# 2. TEX #1  Elvis Andrus (61 - X - X)
t7.new_ab()
t7.pitch_list("b f")
t7.out("G4-3")


# Bot 7th
# Pitching: TEX #44 Cory Gearrin
b7 = game.new_inning()

# Defensive switch (TEX): #13 Joey Gallo moves to LF
b7.defensive_switch(13, "7")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("f c f f f")
b7.out("G3")

# 8. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G4-3")

# 9. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("b b f b f")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #44 Brandon Workman
t8.pitching_substitution(56)

# 3. TEX #30 Nomar Mazara (X - X - X)
t8.new_ab()
t8.hit(1)
t8.thrown_out(2, "19 FC6", 3, 56)

# 4. TEX #29 Adrian Beltré (X - X - 30)
t8.new_ab()
t8.pitch_list("s f s")
t8.out("K")

# 5. TEX #12 Rougned Odor (X - X - 30)
t8.new_ab()
t8.pitch_list("b d b c f c")
t8.out("!K")

# 6. TEX #19 Jurickson Profar (X - X - 30)
t8.new_ab()
t8.pitch_list("b s d 1")
t8.reach("FC6")


# Bot 8th
# Pitching: TEX #53 Jesse Chavez
b8 = game.new_inning()

# Pitching change (TEX): #53 Jesse Chavez replaces #44 Cory Gearrin
b8.pitching_substitution(53)

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.hit(1)
b8.advance(2, "16 1B")
b8.advance(4, "28 HR")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b8.new_ab()
b8.pitch_list("b b")
b8.hit(1)
b8.advance(4, "28 HR")

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
b8.new_ab()
b8.pitch_list("s b s f b")
b8.hit(4, rbis=3)

# 4. BOS #25 Steve Pearce (X - X - X)
b8.new_ab()
b8.pitch_list("c b f")
b8.out("G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("c s b f f f s")
b8.out("K")

# 6. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #70 Ryan Brasier
t9 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #56 Joe Kelly
t9.pitching_substitution(70)

# 7. TEX #9  Isiah Kiner-Falefa (X - X - X)
t9.new_ab()
t9.pitch_list("c s")
t9.out("L9")

# 8. TEX #61 Robinson Chirinos (X - X - X)
t9.new_ab()
t9.pitch_list("c s b f b")
t9.out("P3")

# 9. TEX #13 Joey Gallo (X - X - X)
t9.new_ab()
t9.pitch_list("c b f f")
t9.out("L6")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57)

# Loser team: TEX
# LP: TEX #36 Mike Minor
game.losing_pitcher(36, is_away_team=True)

# print(game)
game.generate_scorecard()
