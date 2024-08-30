import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ PHI, 2018-08-15
# https://www.baseball-reference.com/boxes/PHI/PHI201808150.shtml
# https://www.mlb.com/gameday/red-sox-vs-phillies/2018/08/15/531211/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-15 19:11-22:38",
        "at": "Citizens Bank Park, Philadelphia, PA",
        "att": "35,266",
        "temp": "88F, Clear",
        "wind": "9mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                12: "Brock Holt",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                19: "Jackie Bradley Jr.",
                11: "Rafael Devers",
                3: "Sandy León",
                17: "Nathan Eovaldi",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                50: "Mookie Betts",
                # Bullpen
                47: "Tyler Thornburg",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                22: "Rick Porcello",
                56: "Joe Kelly",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [24, 31, 61],
            "lineup": [
                [16, "7"],
                [12, "4"],
                [18, "3"],
                [28, "9"],
                [2, "6"],
                [19, "8"],
                [11, "5"],
                [3, "2"],
                [17, "1"],
            ],
            "bench": [
                [25, "1B"],
                [36, "SS"],
                [23, "C"],
                [50, "SS"],
            ],
            "bullpen": [47, 24, 46, 76, 70, 22, 56, 31, 61, 32, 37],
        },
        "home": {
            "team": "Philadelphia Phillies",
            "starter": 21,
            "roster": {
                # Lineup
                16: "César Hernández",
                33: "Justin Bour",
                13: "Asdrúbal Cabrera",
                17: "Rhys Hoskins",
                5: "Nick Williams",
                40: "Wilson Ramos",
                37: "Odúbel Herrera",
                7: "Maikel Franco",
                21: "Vince Velasquez",
                # Starting pitcher
                21: "Vince Velasquez",
                # Bench
                4: "Scott Kingery",
                24: "Roman Quinn",
                38: "Jorge Alfaro",
                41: "Carlos Santana",
                # Bullpen
                50: "Héctor Neris",
                47: "Aaron Loup",
                96: "Tommy Hunter",
                58: "Seranthony Domínguez",
                43: "Nick Pivetta",
                93: "Pat Neshek",
                49: "Jake Arrieta",
                64: "Víctor Arano",
                54: "Austin Davis",
                46: "Adam Morgan",
                27: "Aaron Nola",
                57: "Luis García",
            },
            "lefties": [47, 54, 46],
            "lineup": [
                [16, "4"],
                [33, "3"],
                [13, "6"],
                [17, "7"],
                [5, "9"],
                [40, "2"],
                [37, "8"],
                [7, "5"],
                [21, "1"],
            ],
            "bench": [
                [4, "SS"],
                [24, "CF"],
                [38, "C"],
                [41, "1B"],
            ],
            "bullpen": [50, 47, 96, 58, 43, 93, 49, 64, 54, 46, 27, 57],
        },
        "umpires": {
            "HP": "Kerwin Danley",
            "1B": "Ben May",
            "2B": "Ted Barrett",
            "3B": "Will Little",
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
# Pitching: PHI #21 Vince Velasquez
t1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c f b t")
t1.out("KT")

# 2. BOS #12 Brock Holt (X - X - X)
t1.new_ab()
t1.hit(1)
t1.thrown_out(2, "28 CS", 3, 21)

# 3. BOS #18 Mitch Moreland (X - X - 12)
t1.new_ab()
t1.pitch_list("c f 1 b 1 b b s")
t1.out("K")

# 4. BOS #28 J.D. Martinez (X - X - 12)
t1.new_ab()
t1.pitch_list("b d f f b")
t1.no_ab("CS")


# Bot 1st
# Pitching: BOS #17 Nathan Eovaldi
b1 = game.new_inning()

# 1. PHI #16 César Hernández (X - X - X)
b1.new_ab()
b1.pitch_list("f b f b f")
b1.out("L6")

# 2. PHI #33 Justin Bour (X - X - X)
b1.new_ab()
b1.pitch_list("c b b c b s")
b1.out("K")

# 3. PHI #13 Asdrúbal Cabrera (X - X - X)
b1.new_ab()
b1.hit(1)
b1.thrown_out(2, "17 FC6-4", 3, 17)

# 4. PHI #17 Rhys Hoskins (X - X - 13)
b1.new_ab()
b1.pitch_list("c b f f f")
b1.reach("FC6-4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: PHI #21 Vince Velasquez
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b s b")
t2.reach("BB")
t2.thrown_out(2, "2 DP6-4-3", 1, 21)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t2.new_ab()
t2.pitch_list("b")
t2.out("DP6-4-3")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("f s f b b")
t2.hit(1)
t2.error(2)
t2.advance(3, "11 POE2")

# 7. BOS #11 Rafael Devers (X - X - 19)
t2.new_ab()
t2.pitch_list("s 1 1 b 1 s 1 b f")
t2.out("P6")


# Bot 2nd
# Pitching: BOS #17 Nathan Eovaldi
b2 = game.new_inning()

# 5. PHI #5  Nick Williams (X - X - X)
b2.new_ab()
b2.pitch_list("c c f f b f")
b2.hit(1)
b2.thrown_out(2, "7 FC1-4-6", 3, 17)

# 6. PHI #40 Wilson Ramos (X - X - 5)
b2.new_ab()
b2.pitch_list("f b b f s")
b2.out("K")

# 7. PHI #37 Odúbel Herrera (X - X - 5)
b2.new_ab()
b2.pitch_list("1 b f f")
b2.out("F8")

# 8. PHI #7  Maikel Franco (X - X - 5)
b2.new_ab()
b2.pitch_list("c")
b2.reach("FC1-4-6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: PHI #21 Vince Velasquez
t3 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G5-3")

# 9. BOS #17 Nathan Eovaldi (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c c b")
t3.reach("BB")
t3.advance(2, "16 HBP")
t3.advance(3, "12 1B")
t3.advance(4, "18 2B")

# 1. BOS #16 Andrew Benintendi (X - X - 17)
t3.new_ab()
t3.pitch_list("c s")
t3.reach("HBP")
t3.advance(2, "12 1B")
t3.advance(4, "18 2B")

# 2. BOS #12 Brock Holt (X - 17 - 16)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)
t3.advance(4, "18 2B")

# 3. BOS #18 Mitch Moreland (17 - 16 - 12)
t3.new_ab()
t3.pitch_list("f b")
t3.hit(2, rbis=3)
t3.advance(3, "2 BB")

# 4. BOS #28 J.D. Martinez (X - 18 - X)
t3.new_ab()
t3.pitch_list("b d b c b")
t3.reach("BB")
t3.advance(2, "2 BB")

# 5. BOS #2  Xander Bogaerts (X - 18 - 28)
t3.new_ab()
t3.pitch_list("b c d b c b")
t3.reach("BB")

# Pitching change (PHI): #50 Héctor Neris replaces #21 Vince Velasquez, batting 9th
t3.pitching_substitution(50)
t3.defensive_substitution(9, 50, "1")

# 6. BOS #19 Jackie Bradley Jr. (18 - 28 - 2)
t3.new_ab()
t3.pitch_list("b b b c")
t3.out("F9")

# 7. BOS #11 Rafael Devers (18 - 28 - 2)
t3.new_ab()
t3.pitch_list("s f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #17 Nathan Eovaldi
b3 = game.new_inning()

# Offensive change (PHI): Pinch-hitter #24 Roman Quinn replaces #50 Héctor Neris, batting 9th
b3.offensive_substitution(9, 24, "PH")

# 9. PHI #24 Roman Quinn (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("L1")

# 1. PHI #16 César Hernández (X - X - X)
b3.new_ab()
b3.pitch_list("b b f")
b3.out("L7")

# 2. PHI #33 Justin Bour (X - X - X)
b3.new_ab()
b3.hit(1)

# 3. PHI #13 Asdrúbal Cabrera (X - X - 33)
b3.new_ab()
b3.pitch_list("f s b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: PHI #54 Austin Davis
t4 = game.new_inning()

# Pitching change (PHI): #54 Austin Davis replaces #50 Héctor Neris, batting 9th
t4.pitching_substitution(54)
t4.defensive_substitution(9, 54, "1")

# 8. BOS #3  Sandy León (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c f f")
t4.out("L7")

# 9. BOS #17 Nathan Eovaldi (X - X - X)
t4.new_ab()
t4.pitch_list("c b c c")
t4.out("!K")

# 1. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.pitch_list("c f b")
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #17 Nathan Eovaldi
b4 = game.new_inning()

# 4. PHI #17 Rhys Hoskins (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.error(5)
b4.reach("E5")
b4.advance(3, "5 1B")
b4.advance("U", "40 2B")

# 5. PHI #5  Nick Williams (X - X - 17)
b4.new_ab()
b4.pitch_list("s c")
b4.hit(1)
b4.advance(3, "40 2B")
b4.advance(4, "37 G3")

# 6. PHI #40 Wilson Ramos (17 - X - 5)
b4.new_ab()
b4.pitch_list("d b")
b4.hit(2, rbis=1)
b4.advance(3, "37 G3")
b4.advance("U", "41 1B")

# 7. PHI #37 Odúbel Herrera (5 - 40 - X)
b4.new_ab()
b4.out("G3", rbis=1)

# 8. PHI #7  Maikel Franco (40 - X - X)
b4.new_ab()
b4.out("(F)P3")

# Offensive change (PHI): Pinch-hitter #41 Carlos Santana replaces #54 Austin Davis, batting 9th
b4.offensive_substitution(9, 41, "PH")

# 9. PHI #41 Carlos Santana (40 - X - X)
b4.new_ab()
b4.pitch_list("c f")
b4.hit(1, rbis=1)

# 1. PHI #16 César Hernández (X - X - 41)
b4.new_ab()
b4.out("L6")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: PHI #46 Adam Morgan
t5 = game.new_inning()

# Pitching change (PHI): #46 Adam Morgan replaces #54 Austin Davis, batting 9th
t5.pitching_substitution(46)
t5.defensive_substitution(9, 46, "1")

# 2. BOS #12 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("b c c b s")
t5.out("K")

# 3. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("c s s")
t5.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.pitch_list("f f b f b b f")
t5.out("G1-3")


# Bot 5th
# Pitching: BOS #17 Nathan Eovaldi
b5 = game.new_inning()

# 2. PHI #33 Justin Bour (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b b")
b5.out("G3-1")

# 3. PHI #13 Asdrúbal Cabrera (X - X - X)
b5.new_ab()
b5.pitch_list("b f s b s")
b5.out("K")

# 4. PHI #17 Rhys Hoskins (X - X - X)
b5.new_ab()
b5.pitch_list("b c c b f")
b5.hit(1)

# 5. PHI #5  Nick Williams (X - X - 17)
b5.new_ab()
b5.pitch_list("1 c f b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: PHI #46 Adam Morgan
t6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("s f")
t6.out("F8")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G1-3")

# 7. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("c c")
t6.hit(1)
t6.advance(2, "3 1B")

# 8. BOS #3  Sandy León (X - X - 11)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)

# Pitching change (PHI): #96 Tommy Hunter replaces #46 Adam Morgan, batting 9th
t6.pitching_substitution(96)
t6.defensive_substitution(9, 96, "1")

# Offensive change (BOS): Pinch-hitter #25 Steve Pearce replaces #17 Nathan Eovaldi, batting 9th
t6.offensive_substitution(9, 25, "PH")

# 9. BOS #25 Steve Pearce (X - 11 - 3)
t6.new_ab()
t6.pitch_list("c")
t6.out("G4-3")


# Bot 6th
# Pitching: BOS #56 Joe Kelly
b6 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #17 Nathan Eovaldi, batting 9th
b6.pitching_substitution(56)
b6.defensive_substitution(9, 56, "1")

# 6. PHI #40 Wilson Ramos (X - X - X)
b6.new_ab()
b6.pitch_list("f f b")
b6.hit(3)
b6.advance(4, "4 SF9")

# 7. PHI #37 Odúbel Herrera (40 - X - X)
b6.new_ab()
b6.pitch_list("s b b s d s")
b6.out("K")

# 8. PHI #7  Maikel Franco (40 - X - X)
b6.new_ab()
b6.pitch_list("b f s d d b")
b6.reach("BB")

# Offensive change (PHI): Pinch-hitter #4 Scott Kingery replaces #96 Tommy Hunter, batting 9th
b6.offensive_substitution(9, 4, "PH")

# 9. PHI #4  Scott Kingery (40 - X - 7)
b6.new_ab()
b6.out("SF9", rbis=1)

# 1. PHI #16 César Hernández (X - X - 7)
b6.new_ab()
b6.pitch_list("c f f c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: PHI #47 Aaron Loup
t7 = game.new_inning()

# Pitching change (PHI): #47 Aaron Loup replaces #96 Tommy Hunter, batting 9th
t7.pitching_substitution(47)
t7.defensive_substitution(9, 47, "1")

# 1. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b f f")
t7.hit(1)
t7.thrown_out(2, "36 DP4-6-3", 1, 47)

# Offensive change (BOS): Pinch-hitter #36 Eduardo Núñez replaces #12 Brock Holt, batting 2nd
t7.offensive_substitution(2, 36, "PH")

# 2. BOS #36 Eduardo Núñez (X - X - 16)
t7.new_ab()
t7.pitch_list("c 1 f")
t7.out("DP4-6-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #31 Drew Pomeranz
b7 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #56 Joe Kelly, batting 9th
b7.pitching_substitution(31)
b7.defensive_substitution(9, 31, "1")

# Defensive switch (BOS): #36 Eduardo Núñez moves to 2B
b7.defensive_switch(36, "4")

# 2. PHI #33 Justin Bour (X - X - X)
b7.new_ab()
b7.pitch_list("c c b f f f f f b")
b7.hit(1)
b7.advance(2, "13 BB")
b7.advance(3, "17 F9")
b7.advance(4, "40 2B")

# 3. PHI #13 Asdrúbal Cabrera (X - X - 33)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(4, "40 2B")

# 4. PHI #17 Rhys Hoskins (X - 33 - 13)
b7.new_ab()
b7.pitch_list("c")
b7.out("F9")

# 5. PHI #5  Nick Williams (33 - X - 13)
b7.new_ab()
b7.pitch_list("c s s")
b7.out("K")

# 6. PHI #40 Wilson Ramos (33 - X - 13)
b7.new_ab()
b7.pitch_list("c b s b f b")
b7.hit(2, rbis=2)
b7.advance(3, "37 1B")
b7.advance(4, "7 1B")

# 7. PHI #37 Odúbel Herrera (X - 40 - X)
b7.new_ab()
b7.pitch_list("s f")
b7.hit(1)
b7.advance(2, "7 1B")

# 8. PHI #7  Maikel Franco (40 - X - 37)
b7.new_ab()
b7.pitch_list("c")
b7.hit(1, rbis=1)

# Offensive change (PHI): Pinch-hitter #43 Nick Pivetta replaces #47 Aaron Loup, batting 9th
b7.offensive_substitution(9, 43, "PH")

# 9. PHI #43 Nick Pivetta (X - 37 - 7)
b7.new_ab()
b7.out("G1-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: PHI #93 Pat Neshek
t8 = game.new_inning()

# Pitching change (PHI): #93 Pat Neshek replaces #47 Aaron Loup, batting 9th
t8.pitching_substitution(93)
t8.defensive_substitution(9, 93, "1")

# 4. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.hit(1)
t8.advance(2, "2 1B")
t8.error(3)
t8.advance(3, "19 E3")
t8.advance("U", "50 1B")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(2, "19 E3")
t8.advance(3, "50 1B")

# 6. BOS #19 Jackie Bradley Jr. (X - 28 - 2)
t8.new_ab()
t8.pitch_list("b")
t8.reach("FC3")
t8.advance(2, "50 1B")

# 7. BOS #11 Rafael Devers (28 - 2 - 19)
t8.new_ab()
t8.pitch_list("b c s")
t8.out("L9")

# 8. BOS #3  Sandy León (28 - 2 - 19)
t8.new_ab()
t8.out("(F)P5")

# Offensive change (BOS): Pinch-hitter #50 Mookie Betts replaces #31 Drew Pomeranz, batting 9th
t8.offensive_substitution(9, 50, "PH")

# 9. BOS #50 Mookie Betts (28 - 2 - 19)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1, rbis=1)

# Pitching change (PHI): #58 Seranthony Domínguez replaces #93 Pat Neshek, batting 9th
t8.pitching_substitution(58)
t8.defensive_substitution(9, 58, "1")

# 1. BOS #16 Andrew Benintendi (2 - 19 - 50)
t8.new_ab()
t8.out("G3-1")


# Bot 8th
# Pitching: BOS #76 Hector Velázquez
b8 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #31 Drew Pomeranz, batting 9th
b8.pitching_substitution(76)
b8.defensive_substitution(9, 76, "1")

# 1. PHI #16 César Hernández (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("F9")

# 2. PHI #33 Justin Bour (X - X - X)
b8.new_ab()
b8.pitch_list("f f")
b8.out("P3")

# 3. PHI #13 Asdrúbal Cabrera (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("P6")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: PHI #58 Seranthony Domínguez
t9 = game.new_inning()

# 2. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("b b f b")
t9.out("F9")

# 3. BOS #18 Mitch Moreland (X - X - X)
t9.new_ab()
t9.pitch_list("b c b c b")
t9.out("G5-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("b b f s b")
t9.out("G6-3")

# Winning team: PHI
# WP: PHI #96 Tommy Hunter
game.winning_pitcher(96)
# SV: PHI #58 Seranthony Domínguez
game.save_pitcher(58)

# Loser team: BOS
# LP: BOS #56 Joe Kelly
game.losing_pitcher(56, is_away_team=True)

# print(game)
game.generate_scorecard()
