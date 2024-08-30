import os
from baseball_scorecard.baseball_scorecard import Scorecard

# PHI @ BOS, 2018-07-31
# https://www.baseball-reference.com/boxes/BOS/BOS201807310.shtml
# https://www.mlb.com/gameday/phillies-vs-red-sox/2018/07/31/531021/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-31 19:12-22:25",
        "at": "Fenway Park, Boston, MA",
        "att": "37,816",
        "temp": "77F, Clear",
        "wind": "10mph, In From RF",
        "away": {
            "team": "Philadelphia Phillies",
            "starter": 49,
            "roster": {
                # Lineup
                16: "César Hernández",
                17: "Rhys Hoskins",
                41: "Carlos Santana",
                13: "Asdrúbal Cabrera",
                5: "Nick Williams",
                7: "Maikel Franco",
                24: "Roman Quinn",
                38: "Jorge Alfaro",
                4: "Scott Kingery",
                # Starting pitcher
                49: "Jake Arrieta",
                # Bench
                25: "Dylan Cozens",
                15: "Andrew Knapp",
                37: "Odúbel Herrera",
                # Bullpen
                21: "Vince Velasquez",
                40: "Tommy Hunter",
                58: "Seranthony Domínguez",
                43: "Nick Pivetta",
                56: "Zach Eflin",
                93: "Pat Neshek",
                44: "Jake Thompson",
                64: "Víctor Arano",
                54: "Austin Davis",
                53: "Yacksel Ríos",
                27: "Aaron Nola",
                57: "Luis García",
            },
            "lefties": [54],
            "lineup": [
                [16, "4"],
                [17, "7"],
                [41, "3"],
                [13, "0"],
                [5, "9"],
                [7, "5"],
                [24, "8"],
                [38, "2"],
                [4, "6"],
            ],
            "bench": [
                [25, "LF"],
                [15, "C"],
                [37, "CF"],
            ],
            "bullpen": [21, 40, 58, 43, 56, 93, 44, 64, 54, 53, 27, 57],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                23: "Blake Swihart",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                5: "Ian Kinsler",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                31: "Drew Pomeranz",
                # Bench
                25: "Steve Pearce",
                50: "Mookie Betts",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [16, "7"],
                [23, "2"],
                [18, "3"],
                [28, "9"],
                [2, "6"],
                [5, "4"],
                [36, "5"],
                [12, "0"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [50, "SS"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 22, 61, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Jeff Nelson",
            "1B": "Chad Whitson",
            "2B": "Manny Gonzalez",
            "3B": "Andy Fletcher",
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
# Pitching: BOS #31 Drew Pomeranz
t1 = game.new_inning()

# 1. PHI #16 César Hernández (X - X - X)
t1.new_ab()
t1.pitch_list("b c c b b f")
t1.out("G6-3")

# 2. PHI #17 Rhys Hoskins (X - X - X)
t1.new_ab()
t1.pitch_list("b c c b b b")
t1.reach("BB")
t1.advance(3, "41 1B")

# 3. PHI #41 Carlos Santana (X - X - 17)
t1.new_ab()
t1.pitch_list("b b c")
t1.hit(1)
t1.thrown_out(2, "7-4", 2, 31)

# 4. PHI #13 Asdrúbal Cabrera (17 - X - X)
t1.new_ab()
t1.pitch_list("d")
t1.out("G6-3")


# Bot 1st
# Pitching: PHI #49 Jake Arrieta
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c c")
b1.hit(1)
b1.advance(2, "18 SB")
b1.advance(3, "28 WP")
b1.thrown_out(4, "2 CS", 3, 49)

# 2. BOS #23 Blake Swihart (X - X - 16)
b1.new_ab()
b1.pitch_list("b b b c 1")
b1.out("F7")

# 3. BOS #18 Mitch Moreland (X - X - 16)
b1.new_ab()
b1.pitch_list("1 c c s")
b1.out("K")

# 4. BOS #28 J.D. Martinez (X - 16 - X)
b1.new_ab()
b1.pitch_list("d b c b f")
b1.wp()
b1.reach("HBP")

# 5. BOS #2  Xander Bogaerts (16 - X - 28)
b1.new_ab()
b1.pitch_list("b b f f b")
b1.no_ab("CS")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Drew Pomeranz
t2 = game.new_inning()

# 5. PHI #5  Nick Williams (X - X - X)
t2.new_ab()
t2.pitch_list("c b b f")
t2.out("F8")

# 6. PHI #7  Maikel Franco (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")
t2.advance(4, "38 2B")

# 7. PHI #24 Roman Quinn (X - X - 7)
t2.new_ab()
t2.out("(F)P3")

# 8. PHI #38 Jorge Alfaro (X - X - 7)
t2.new_ab()
t2.hit(2, rbis=1)

# 9. PHI #4  Scott Kingery (X - 38 - X)
t2.new_ab()
t2.pitch_list("c f b f f b f s")
t2.out("K")


# Bot 2nd
# Pitching: PHI #49 Jake Arrieta
b2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.hit(2)

# 6. BOS #5  Ian Kinsler (X - 2 - X)
b2.new_ab()
b2.pitch_list("c b l s")
b2.out("K")

# 7. BOS #36 Eduardo Núñez (X - 2 - X)
b2.new_ab()
b2.pitch_list("b s c c")
b2.out("!K")

# 8. BOS #12 Brock Holt (X - 2 - X)
b2.new_ab()
b2.pitch_list("d b c c")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Drew Pomeranz
t3 = game.new_inning()

# 1. PHI #16 César Hernández (X - X - X)
t3.new_ab()
t3.pitch_list("b f f b b")
t3.out("G6-3")

# 2. PHI #17 Rhys Hoskins (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b b")
t3.reach("BB")

# 3. PHI #41 Carlos Santana (X - X - 17)
t3.new_ab()
t3.pitch_list("s c b s")
t3.out("K")

# 4. PHI #13 Asdrúbal Cabrera (X - X - 17)
t3.new_ab()
t3.pitch_list("b b")
t3.out("P3")


# Bot 3rd
# Pitching: PHI #49 Jake Arrieta
b3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.hit(2)
b3.advance(3, "23 G4-3")

# 1. BOS #16 Andrew Benintendi (X - 19 - X)
b3.new_ab()
b3.pitch_list("s b b f")
b3.out("L6")

# 2. BOS #23 Blake Swihart (X - 19 - X)
b3.new_ab()
b3.pitch_list("d s c d")
b3.out("G4-3")

# 3. BOS #18 Mitch Moreland (19 - X - X)
b3.new_ab()
b3.pitch_list("b s")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Drew Pomeranz
t4 = game.new_inning()

# 5. PHI #5  Nick Williams (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G3-1")

# 6. PHI #7  Maikel Franco (X - X - X)
t4.new_ab()
t4.pitch_list("b b b b")
t4.reach("BB")
t4.advance(3, "24 2B")
t4.advance(4, "4 SF8")

# 7. PHI #24 Roman Quinn (X - X - 7)
t4.new_ab()
t4.hit(2)

# 8. PHI #38 Jorge Alfaro (7 - 24 - X)
t4.new_ab()
t4.pitch_list("f")
t4.reach("HBP")

# 9. PHI #4  Scott Kingery (7 - 24 - 38)
t4.new_ab()
t4.pitch_list("b s b")
t4.out("SF8", rbis=1)

# 1. PHI #16 César Hernández (X - 24 - 38)
t4.new_ab()
t4.pitch_list("b f b")
t4.out("F8")


# Bot 4th
# Pitching: PHI #49 Jake Arrieta
b4 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("c f c")
b4.out("!K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("P4")

# 6. BOS #5  Ian Kinsler (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.error(1)
b4.advance(3, "36 POE1")

# 7. BOS #36 Eduardo Núñez (X - X - 5)
b4.new_ab()
b4.pitch_list("f 1")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Drew Pomeranz
t5 = game.new_inning()

# 2. PHI #17 Rhys Hoskins (X - X - X)
t5.new_ab()
t5.pitch_list("c f")
t5.out("G5-3")

# 3. PHI #41 Carlos Santana (X - X - X)
t5.new_ab()
t5.pitch_list("b f c")
t5.out("F8")

# 4. PHI #13 Asdrúbal Cabrera (X - X - X)
t5.new_ab()
t5.pitch_list("c b b c")
t5.hit(1)
t5.advance(2, "5 HBP")

# 5. PHI #5  Nick Williams (X - X - 13)
t5.new_ab()
t5.pitch_list("c b")
t5.reach("HBP")

# 6. PHI #7  Maikel Franco (X - 13 - 5)
t5.new_ab()
t5.pitch_list("d b c s d f s")
t5.out("K")


# Bot 5th
# Pitching: PHI #49 Jake Arrieta
b5 = game.new_inning()

# 8. BOS #12 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("(F)P5")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b f s f s")
b5.out("K")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("c b f b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #56 Joe Kelly
t6 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #31 Drew Pomeranz
t6.pitching_substitution(56)

# 7. PHI #24 Roman Quinn (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(1)
t6.thrown_out(2, "38 CS", 1, 56)

# 8. PHI #38 Jorge Alfaro (X - X - 24)
t6.new_ab()
t6.pitch_list("d 1 1 f s f f b f")
t6.out("F8")

# 9. PHI #4  Scott Kingery (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("F9")


# Bot 6th
# Pitching: PHI #49 Jake Arrieta
b6 = game.new_inning()

# 2. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.advance(3, "28 2B")
b6.advance(4, "2 G5-3")

# 3. BOS #18 Mitch Moreland (X - X - 23)
b6.new_ab()
b6.pitch_list("b")
b6.out("L9")

# 4. BOS #28 J.D. Martinez (X - X - 23)
b6.new_ab()
b6.hit(2)
b6.advance(3, "2 G5-3")

# 5. BOS #2  Xander Bogaerts (23 - 28 - X)
b6.new_ab()
b6.pitch_list("b f")
b6.out("G5-3", rbis=1)

# 6. BOS #5  Ian Kinsler (28 - X - X)
b6.new_ab()
b6.pitch_list("d f f")
b6.out("L9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #56 Joe Kelly
t7.pitching_substitution(37)

# 1. PHI #16 César Hernández (X - X - X)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")

# 2. PHI #17 Rhys Hoskins (X - X - 16)
t7.new_ab()
t7.pitch_list("b 1 c c d s")
t7.out("K")

# 3. PHI #41 Carlos Santana (X - X - 16)
t7.new_ab()
t7.out("L8")

# 4. PHI #13 Asdrúbal Cabrera (X - X - 16)
t7.new_ab()
t7.pitch_list("c 1 f b 1 s")
t7.out("K")


# Bot 7th
# Pitching: PHI #49 Jake Arrieta
b7 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.out("F8")

# 8. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("c f")
b7.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("f c s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree
t8.pitching_substitution(32)

# 5. PHI #5  Nick Williams (X - X - X)
t8.new_ab()
t8.pitch_list("c b s b c")
t8.out("!K")

# 6. PHI #7  Maikel Franco (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(2, "24 1B")
t8.advance(3, "4 BB")

# 7. PHI #24 Roman Quinn (X - X - 7)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(1)
t8.advance(2, "4 BB")

# 8. PHI #38 Jorge Alfaro (X - 7 - 24)
t8.new_ab()
t8.pitch_list("c s b s")
t8.out("K")

# 9. PHI #4  Scott Kingery (X - 7 - 24)
t8.new_ab()
t8.pitch_list("f b s b f d f d")
t8.reach("BB")

# 1. PHI #16 César Hernández (7 - 24 - 4)
t8.new_ab()
t8.pitch_list("s f s")
t8.out("K")


# Bot 8th
# Pitching: PHI #40 Tommy Hunter
b8 = game.new_inning()

# Pitching change (PHI): #40 Tommy Hunter replaces #49 Jake Arrieta
b8.pitching_substitution(40)

# 1. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G6-3")

# 2. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.out("L8")

# 3. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("c s f")
b8.out("G3-1")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #76 Hector Velázquez
t9 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #32 Matt Barnes
t9.pitching_substitution(76)

# 2. PHI #17 Rhys Hoskins (X - X - X)
t9.new_ab()
t9.pitch_list("b c b f")
t9.hit(2)
t9.advance(4, "41 1B")

# 3. PHI #41 Carlos Santana (X - 17 - X)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(1, rbis=1)
t9.thrown_out(2, "5 FC3-6", 2, 76)

# 4. PHI #13 Asdrúbal Cabrera (X - X - 41)
t9.new_ab()
t9.pitch_list("b f b")
t9.out("L4")

# 5. PHI #5  Nick Williams (X - X - 41)
t9.new_ab()
t9.pitch_list("1 b b b c")
t9.reach("FC3-6")
t9.advance(2, "7 1B")

# 6. PHI #7  Maikel Franco (X - X - 5)
t9.new_ab()
t9.hit(1)

# 7. PHI #24 Roman Quinn (X - 5 - 7)
t9.new_ab()
t9.pitch_list("c")
t9.out("G1-3")


# Bot 9th
# Pitching: PHI #58 Seranthony Domínguez
b9 = game.new_inning()

# Pitching change (PHI): #58 Seranthony Domínguez replaces #40 Tommy Hunter
b9.pitching_substitution(58)

# 4. BOS #28 J.D. Martinez (X - X - X)
b9.new_ab()
b9.pitch_list("b f s b b d")
b9.reach("BB")
b9.advance(2, "2 HBP")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b9.new_ab()
b9.pitch_list("f f")
b9.reach("HBP")

# 6. BOS #5  Ian Kinsler (X - 28 - 2)
b9.new_ab()
b9.pitch_list("b f c t")
b9.out("KT")

# Offensive change (BOS): Pinch-hitter #50 Mookie Betts replaces #36 Eduardo Núñez, batting 7th
b9.offensive_substitution(7, 50, "PH")

# 7. BOS #50 Mookie Betts (X - 28 - 2)
b9.new_ab()
b9.pitch_list("d")
b9.out("IF5")

# 8. BOS #12 Brock Holt (X - 28 - 2)
b9.new_ab()
b9.pitch_list("c b b f c")
b9.out("!K")

# Winning team: PHI
# WP: PHI #49 Jake Arrieta
game.winning_pitcher(49, is_away_team=True)
# SV: PHI #58 Seranthony Domínguez
game.save_pitcher(58, is_away_team=True)

# Loser team: BOS
# LP: BOS #31 Drew Pomeranz
game.losing_pitcher(31)

# print(game)
game.generate_scorecard()
