import os
from baseball_scorecard.baseball_scorecard import Scorecard

# PHI @ BOS, 2018-07-30
# https://www.baseball-reference.com/boxes/BOS/BOS201807300.shtml
# https://www.mlb.com/gameday/phillies-vs-red-sox/2018/07/30/531006/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-30 19:12-23:15",
        "at": "Fenway Park, Boston, MA",
        "att": "37,722",
        "temp": "80F, Partly Cloudy",
        "wind": "14mph, R To L",
        "away": {
            "team": "Philadelphia Phillies",
            "starter": 27,
            "roster": {
                # Lineup
                16: "César Hernández",
                17: "Rhys Hoskins",
                37: "Odúbel Herrera",
                41: "Carlos Santana",
                13: "Asdrúbal Cabrera",
                7: "Maikel Franco",
                38: "Jorge Alfaro",
                24: "Roman Quinn",
                4: "Scott Kingery",
                # Starting pitcher
                27: "Aaron Nola",
                # Bench
                5: "Nick Williams",
                10: "Trevor Plouffe",
                15: "Andrew Knapp",
                # Bullpen
                21: "Vince Velasquez",
                40: "Tommy Hunter",
                58: "Seranthony Domínguez",
                43: "Nick Pivetta",
                56: "Zach Eflin",
                93: "Pat Neshek",
                49: "Jake Arrieta",
                44: "Jake Thompson",
                64: "Víctor Arano",
                54: "Austin Davis",
                53: "Yacksel Ríos",
                57: "Luis García",
            },
            "lefties": [54],
            "lineup": [
                [16, "4"],
                [17, "7"],
                [37, "8"],
                [41, "3"],
                [13, "0"],
                [7, "5"],
                [38, "2"],
                [24, "9"],
                [4, "6"],
            ],
            "bench": [
                [5, "OF"],
                [10, "3B"],
                [15, "C"],
            ],
            "bullpen": [21, 40, 58, 43, 56, 93, 49, 44, 64, 54, 53, 57],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                19: "Jackie Bradley Jr.",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                3: "Sandy León",
                # Starting pitcher
                24: "David Price",
                # Bench
                5: "Tzu-Wei Lin",
                25: "Steve Pearce",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                22: "Rick Porcello",
                56: "Joe Kelly",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [24, 31, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [19, "8"],
                [36, "5"],
                [12, "4"],
                [3, "2"],
            ],
            "bench": [
                [5, "OF"],
                [25, "1B"],
                [23, "C"],
            ],
            "bullpen": [47, 46, 76, 70, 22, 56, 31, 61, 17, 32, 37],
        },
        "umpires": {
            "HP": "Andy Fletcher",
            "1B": "Jeff Nelson",
            "2B": "Chad Whitson",
            "3B": "Manny Gonzalez",
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
# Pitching: BOS #24 David Price
t1 = game.new_inning()

# 1. PHI #16 César Hernández (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G6-3")

# 2. PHI #17 Rhys Hoskins (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.hit(2)

# 3. PHI #37 Odúbel Herrera (X - 17 - X)
t1.new_ab()
t1.pitch_list("f b f")
t1.out("F8")

# 4. PHI #41 Carlos Santana (X - 17 - X)
t1.new_ab()
t1.out("P6")


# Bot 1st
# Pitching: PHI #27 Aaron Nola
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("f c")
b1.out("L9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("f c")
b1.out("F7")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c s f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 5. PHI #13 Asdrúbal Cabrera (X - X - X)
t2.new_ab()
t2.hit(2)
t2.advance(4, "7 1B")

# 6. PHI #7  Maikel Franco (X - 13 - X)
t2.new_ab()
t2.hit(1, rbis=1)

# 7. PHI #38 Jorge Alfaro (X - X - 7)
t2.new_ab()
t2.pitch_list("f")
t2.out("L8")

# 8. PHI #24 Roman Quinn (X - X - 7)
t2.new_ab()
t2.pitch_list("b c b b f f f s")
t2.out("K")

# 9. PHI #4  Scott Kingery (X - X - 7)
t2.new_ab()
t2.pitch_list("s b f f s")
t2.out("K")


# Bot 2nd
# Pitching: PHI #27 Aaron Nola
b2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("b c s")
b2.out("F8")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.out("G4-3")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("c b f b")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 1. PHI #16 César Hernández (X - X - X)
t3.new_ab()
t3.pitch_list("c b f f b b s")
t3.out("K")

# 2. PHI #17 Rhys Hoskins (X - X - X)
t3.new_ab()
t3.hit(2)
t3.advance(3, "37 1B")
t3.thrown_out(4, "41 DP5-2-6-5", 3, 24)

# 3. PHI #37 Odúbel Herrera (X - 17 - X)
t3.new_ab()
t3.pitch_list("f b f")
t3.hit(1)
t3.thrown_out(3, "41 DP5-2-6-5", 2, 24)

# 4. PHI #41 Carlos Santana (17 - X - 37)
t3.new_ab()
t3.pitch_list("b")
t3.reach("DP5-2-6-5")


# Bot 3rd
# Pitching: PHI #27 Aaron Nola
b3 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("c b s")
b3.out("G4-3")

# 8. BOS #12 Brock Holt (X - X - X)
b3.new_ab()
b3.pitch_list("c b f")
b3.out("L8")

# 9. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("c b f b")
b3.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 3)
b3.new_ab()
b3.pitch_list("c c b t")
b3.out("KT")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 5. PHI #13 Asdrúbal Cabrera (X - X - X)
t4.new_ab()
t4.out("G6-3")

# 6. PHI #7  Maikel Franco (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G1-3")

# 7. PHI #38 Jorge Alfaro (X - X - X)
t4.new_ab()
t4.out("G5-3")


# Bot 4th
# Pitching: PHI #27 Aaron Nola
b4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.pitch_list("b s b c")
b4.out("G1-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("b s s")
b4.out("G1-3")

# 4. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("b b c s b f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 8. PHI #24 Roman Quinn (X - X - X)
t5.new_ab()
t5.pitch_list("l b f")
t5.out("P3")

# 9. PHI #4  Scott Kingery (X - X - X)
t5.new_ab()
t5.pitch_list("c s")
t5.out("F9")

# 1. PHI #16 César Hernández (X - X - X)
t5.new_ab()
t5.pitch_list("c b b")
t5.out("G5-3")


# Bot 5th
# Pitching: PHI #27 Aaron Nola
b5 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("c f s")
b5.out("K")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("c b b s f")
b5.hit(1)
b5.advance(4, "36 3B")

# 7. BOS #36 Eduardo Núñez (X - X - 19)
b5.new_ab()
b5.pitch_list("1")
b5.hit(3, rbis=1)

# 8. BOS #12 Brock Holt (36 - X - X)
b5.new_ab()
b5.pitch_list("c b b b b")
b5.reach("BB")
b5.thrown_out(1, "3 DP4-3", 3, 27)

# 9. BOS #3  Sandy León (36 - X - 12)
b5.new_ab()
b5.out("DP4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 2. PHI #17 Rhys Hoskins (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("F9")

# 3. PHI #37 Odúbel Herrera (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G6-3")

# 4. PHI #41 Carlos Santana (X - X - X)
t6.new_ab()
t6.pitch_list("b c b")
t6.hit(1)
t6.advance(2, "13 1B")

# 5. PHI #13 Asdrúbal Cabrera (X - X - 41)
t6.new_ab()
t6.pitch_list("c c f b")
t6.hit(1)

# 6. PHI #7  Maikel Franco (X - 41 - 13)
t6.new_ab()
t6.pitch_list("s c c")
t6.out("!K")


# Bot 6th
# Pitching: PHI #27 Aaron Nola
b6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("c f b")
b6.out("G1-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b s t")
b6.out("KT")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #24 David Price
t7 = game.new_inning()

# 7. PHI #38 Jorge Alfaro (X - X - X)
t7.new_ab()
t7.pitch_list("s")
t7.out("F9")

# 8. PHI #24 Roman Quinn (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("G6-3")

# 9. PHI #4  Scott Kingery (X - X - X)
t7.new_ab()
t7.out("F7")


# Bot 7th
# Pitching: PHI #27 Aaron Nola
b7 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.out("B2-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("b c f")
b7.out("G1-4-3")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b")
b7.error(3)
b7.reach("E3")
b7.thrown_out(2, "36 FC4", 3, 27)

# 7. BOS #36 Eduardo Núñez (X - X - 19)
b7.new_ab()
b7.pitch_list("1 1 1 c 1 b")
b7.reach("FC4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #24 David Price
t8 = game.new_inning()

# 1. PHI #16 César Hernández (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("B2-3")

# 2. PHI #17 Rhys Hoskins (X - X - X)
t8.new_ab()
t8.pitch_list("b b c c c")
t8.out("!K")

# 3. PHI #37 Odúbel Herrera (X - X - X)
t8.new_ab()
t8.pitch_list("s b")
t8.hit(2)

# 4. PHI #41 Carlos Santana (X - 37 - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")

# 5. PHI #13 Asdrúbal Cabrera (X - 37 - 41)
t8.new_ab()
t8.out("L9")


# Bot 8th
# Pitching: PHI #27 Aaron Nola
b8 = game.new_inning()

# 8. BOS #12 Brock Holt (X - X - X)
b8.new_ab()
b8.pitch_list("c f")
b8.hit(2)

# 9. BOS #3  Sandy León (X - 12 - X)
b8.new_ab()
b8.pitch_list("b b c")
b8.out("P5")

# 1. BOS #50 Mookie Betts (X - 12 - X)
b8.new_ab()
b8.pitch_list("c b f t")
b8.out("KT")

# 2. BOS #16 Andrew Benintendi (X - 12 - X)
b8.new_ab()
b8.out("L8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #47 Tyler Thornburg
t9 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #24 David Price
t9.pitching_substitution(47)

# 6. PHI #7  Maikel Franco (X - X - X)
t9.new_ab()
t9.out("P4")

# Offensive change (PHI): Pinch-hitter #15 Andrew Knapp replaces #38 Jorge Alfaro, batting 7th
t9.offensive_substitution(7, 15, "PH")

# 7. PHI #15 Andrew Knapp (X - X - X)
t9.new_ab()
t9.pitch_list("b s b c s")
t9.out("K")

# 8. PHI #24 Roman Quinn (X - X - X)
t9.new_ab()
t9.pitch_list("b s")
t9.hit(1)
t9.thrown_out(2, "4 CS", 3, 47)

# 9. PHI #4  Scott Kingery (X - X - 24)
t9.new_ab()
t9.pitch_list("b 1 c")
t9.no_ab("CS")


# Bot 9th
# Pitching: PHI #58 Seranthony Domínguez
b9 = game.new_inning()

# Pitching change (PHI): #58 Seranthony Domínguez replaces #27 Aaron Nola
b9.pitching_substitution(58)

# Defensive switch (PHI): #15 Andrew Knapp moves to C
b9.defensive_switch(15, "2")

# 3. BOS #28 J.D. Martinez (X - X - X)
b9.new_ab()
b9.pitch_list("c b b b s f b")
b9.reach("BB")
b9.thrown_out(2, "18 DP4-6-3", 1, 58)

# 4. BOS #18 Mitch Moreland (X - X - 28)
b9.new_ab()
b9.pitch_list("b")
b9.out("DP4-6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("G5-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #70 Ryan Brasier
t10 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #47 Tyler Thornburg
t10.pitching_substitution(70)

# 9. PHI #4  Scott Kingery (X - X - X)
t10.new_ab()
t10.pitch_list("c s")
t10.out("G5-3")

# 1. PHI #16 César Hernández (X - X - X)
t10.new_ab()
t10.pitch_list("b s")
t10.out("L1")

# 2. PHI #17 Rhys Hoskins (X - X - X)
t10.new_ab()
t10.pitch_list("f b b s b f b")
t10.reach("BB")
t10.advance(2, "37 BB")

# 3. PHI #37 Odúbel Herrera (X - X - 17)
t10.new_ab()
t10.pitch_list("b b b b")
t10.reach("BB")

# 4. PHI #41 Carlos Santana (X - 17 - 37)
t10.new_ab()
t10.pitch_list("f b s b")
t10.out("G4-3")


# Bot 10th
# Pitching: PHI #93 Pat Neshek
b10 = game.new_inning()

# Pitching change (PHI): #93 Pat Neshek replaces #58 Seranthony Domínguez
b10.pitching_substitution(93)

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
b10.new_ab()
b10.pitch_list("s b c")
b10.out("F7")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b10.new_ab()
b10.out("(F)F9")

# 8. BOS #12 Brock Holt (X - X - X)
b10.new_ab()
b10.pitch_list("c c b b b")
b10.hit(2)
b10.advance(3, "23 SB")

# Pitching change (PHI): #40 Tommy Hunter replaces #93 Pat Neshek
b10.pitching_substitution(40)

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #3 Sandy León, batting 9th
b10.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Blake Swihart (X - 12 - X)
b10.new_ab()
b10.pitch_list("b c s")
b10.out("F7")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: BOS #37 Heath Hembree
t11 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #70 Ryan Brasier
t11.pitching_substitution(37)

# Defensive switch (BOS): #23 Blake Swihart moves to C
t11.defensive_switch(23, "2")

# 5. PHI #13 Asdrúbal Cabrera (X - X - X)
t11.new_ab()
t11.pitch_list("t s b f b b f f f f s")
t11.out("K")

# 6. PHI #7  Maikel Franco (X - X - X)
t11.new_ab()
t11.pitch_list("b b c")
t11.out("G6-3")

# 7. PHI #15 Andrew Knapp (X - X - X)
t11.new_ab()
t11.pitch_list("c t s")
t11.out("K")


# Bot 11th
# Pitching: PHI #40 Tommy Hunter
b11 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b11.new_ab()
b11.pitch_list("b")
b11.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b11.new_ab()
b11.pitch_list("b b s b f")
b11.out("G3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b11.new_ab()
b11.pitch_list("b")
b11.out("G1-3")


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: BOS #56 Joe Kelly
t12 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
t12.pitching_substitution(56)

# 8. PHI #24 Roman Quinn (X - X - X)
t12.new_ab()
t12.out("B5-3")

# 9. PHI #4  Scott Kingery (X - X - X)
t12.new_ab()
t12.pitch_list("c b b")
t12.out("L8")

# 1. PHI #16 César Hernández (X - X - X)
t12.new_ab()
t12.pitch_list("b b c f b b")
t12.reach("BB")
t12.thrown_out(2, "17 FC5-4", 3, 56)

# 2. PHI #17 Rhys Hoskins (X - X - 16)
t12.new_ab()
t12.pitch_list("1 c f f")
t12.reach("FC5-4")


# Bot 12th
# Pitching: PHI #54 Austin Davis
b12 = game.new_inning()

# Pitching change (PHI): #54 Austin Davis replaces #40 Tommy Hunter
b12.pitching_substitution(54)

# Offensive change (BOS): Pinch-hitter #25 Steve Pearce replaces #18 Mitch Moreland, batting 4th
b12.offensive_substitution(4, 25, "PH")

# 4. BOS #25 Steve Pearce (X - X - X)
b12.new_ab()
b12.pitch_list("c b c b s")
b12.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b12.new_ab()
b12.pitch_list("c b b")
b12.out("G6-3")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
b12.new_ab()
b12.pitch_list("c b")
b12.out("L3")


##########################################################
# 13th Inning
##########################################################
# Top 13th
# Pitching: BOS #76 Hector Velázquez
t13 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #56 Joe Kelly
t13.pitching_substitution(76)

# Defensive switch (BOS): #25 Steve Pearce moves to 1B
t13.defensive_switch(25, "3")

# 3. PHI #37 Odúbel Herrera (X - X - X)
t13.new_ab()
t13.pitch_list("b f b s b b")
t13.reach("BB")
t13.advance(2, "7 1B")

# 4. PHI #41 Carlos Santana (X - X - 37)
t13.new_ab()
t13.pitch_list("c b f b f 1 s")
t13.out("K")

# 5. PHI #13 Asdrúbal Cabrera (X - X - 37)
t13.new_ab()
t13.pitch_list("1 b s b c f s")
t13.out("K")

# 6. PHI #7  Maikel Franco (X - X - 37)
t13.new_ab()
t13.pitch_list("b")
t13.hit(1)

# 7. PHI #15 Andrew Knapp (X - 37 - 7)
t13.new_ab()
t13.pitch_list("b")
t13.out("F7")


# Bot 13th
# Pitching: PHI #54 Austin Davis
b13 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b13.new_ab()
b13.pitch_list("b b f f b")
b13.hit(1)
b13.advance(2, "12 SB")
b13.advance(4, "23 2B")

# Pitching change (PHI): #57 Luis García replaces #54 Austin Davis
b13.pitching_substitution(57)

# 8. BOS #12 Brock Holt (X - X - 36)
b13.new_ab()
b13.pitch_list("1 c f b f s")
b13.out("K")

# 9. BOS #23 Blake Swihart (X - 36 - X)
b13.new_ab()
b13.hit(2, rbis=1)

# Winning team: BOS
# WP: BOS #76 Hector Velázquez
game.winning_pitcher(76)

# Loser team: PHI
# LP: PHI #54 Austin Davis
game.losing_pitcher(54, is_away_team=True)

# print(game)
game.generate_scorecard()
