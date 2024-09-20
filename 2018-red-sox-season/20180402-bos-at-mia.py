import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ MIA, 2018-04-02
# https://www.baseball-reference.com/boxes/MIA/MIA201804020.shtml
# https://www.mlb.com/gameday/red-sox-vs-marlins/2018/04/02/529458/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-02 19:10-22:19",
        "at": "Marlins Park, Miami, FL",
        "att": "11,113",
        "temp": "76F, Clear",
        "wind": "11mph, In From LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                11: "Rafael Devers",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                61: "Brian Johnson",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                28: "J.D. Martinez",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [61, 41, 66, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [11, "5"],
                [2, "6"],
                [36, "4"],
                [19, "8"],
                [7, "2"],
                [61, "1"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [28, "DH"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [39, 22, 41, 66, 37, 24, 46, 76, 64, 56, 32],
        },
        "home": {
            "team": "Miami Marlins",
            "starter": 63,
            "roster": {
                # Lineup
                9: "Lewis Brinson",
                32: "Derek Dietrich",
                13: "Starlin Castro",
                15: "Brian Anderson",
                41: "Justin Bour",
                1: "Cameron Maybin",
                19: "Miguel Rojas",
                28: "Bryan Holaday",
                63: "Trevor Richards",
                # Starting pitcher
                63: "Trevor Richards",
                # Bench
                30: "Garrett Cooper",
                18: "Tomás Telis",
                2: "Yadiel Rivera",
                17: "Chad Wallach",
                # Bullpen
                56: "Tayron Guerrero",
                62: "José Ureña",
                44: "Jacob Turner",
                46: "Kyle Barraclough",
                66: "Jarlín García",
                76: "Dillon Peters",
                25: "Junichi Tazawa",
                50: "Chris O'Grady",
                43: "Odrisamer Despaigne",
                29: "Brad Ziegler",
                31: "Caleb Smith",
                71: "Drew Steckenrider",
            },
            "lefties": [66, 76, 50, 31],
            "lineup": [
                [9, "8"],
                [32, "7"],
                [13, "4"],
                [15, "5"],
                [41, "3"],
                [1, "9"],
                [19, "6"],
                [28, "2"],
                [63, "1"],
            ],
            "bench": [
                [30, "1B"],
                [18, "C"],
                [2, "3B"],
                [17, "C"],
            ],
            "bullpen": [56, 62, 44, 46, 66, 76, 25, 50, 43, 29, 31, 71],
        },
        "umpires": {
            "HP": "Jerry Meals",
            "1B": "Ben May",
            "2B": "Ron Kulpa",
            "3B": "Ed Hickox",
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
# Pitching: MIA #63 Trevor Richards
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c f")
t1.out("P6")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("t s s")
t1.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #61 Brian Johnson
b1 = game.new_inning()

# 1. MIA #9  Lewis Brinson (X - X - X)
b1.new_ab()
b1.out("B2")

# 2. MIA #32 Derek Dietrich (X - X - X)
b1.new_ab()
b1.pitch_list("c s b b b t")
b1.out("KT")

# 3. MIA #13 Starlin Castro (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: MIA #63 Trevor Richards
t2 = game.new_inning()

# 4. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("b f t b b s")
t2.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G4-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G3-1")


# Bot 2nd
# Pitching: BOS #61 Brian Johnson
b2 = game.new_inning()

# 4. MIA #15 Brian Anderson (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(4)

# 5. MIA #41 Justin Bour (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G6-3")

# 6. MIA #1  Cameron Maybin (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G6-3")

# 7. MIA #19 Miguel Rojas (X - X - X)
b2.new_ab()
b2.pitch_list("c f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: MIA #63 Trevor Richards
t3 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("s s b b s")
t3.out("K")

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("f f b f b b")
t3.hit(1)
t3.advance(2, "50 1B")

# 9. BOS #61 Brian Johnson (X - X - 7)
t3.new_ab()
t3.pitch_list("b l l 1 l")
t3.out("K")

# 1. BOS #50 Mookie Betts (X - X - 7)
t3.new_ab()
t3.pitch_list("c b d f b f")
t3.hit(1)

# 2. BOS #16 Andrew Benintendi (X - 7 - 50)
t3.new_ab()
t3.pitch_list("b b 2 t f")
t3.out("(F)P5")


# Bot 3rd
# Pitching: BOS #61 Brian Johnson
b3 = game.new_inning()

# 8. MIA #28 Bryan Holaday (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.out("G5-3")

# 9. MIA #63 Trevor Richards (X - X - X)
b3.new_ab()
b3.pitch_list("c c b s")
b3.out("K")

# 1. MIA #9  Lewis Brinson (X - X - X)
b3.new_ab()
b3.pitch_list("c s f")
b3.hit(1)
b3.advance(2, "32 BB")
b3.advance(3, "13 1B")

# 2. MIA #32 Derek Dietrich (X - X - 9)
b3.new_ab()
b3.pitch_list("b b d c 1 b")
b3.reach("BB")
b3.advance(2, "13 1B")

# 3. MIA #13 Starlin Castro (X - 9 - 32)
b3.new_ab()
b3.pitch_list("b c c")
b3.hit(1)
b3.thrown_out(2, "15 FC6-4", 3, 61)

# 4. MIA #15 Brian Anderson (9 - 32 - 13)
b3.new_ab()
b3.reach("FC6-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: MIA #63 Trevor Richards
t4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("b b b")
t4.out("P4")

# 4. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("b f b b c c")
t4.out("!K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("b b c f")
t4.hit(1)
t4.advance(4, "36 2B")

# 6. BOS #36 Eduardo Núñez (X - X - 2)
t4.new_ab()
t4.pitch_list("1 c 1 b f")
t4.hit(2, rbis=1)
t4.advance(4, "7 2B")

# 7. BOS #19 Jackie Bradley Jr. (X - 36 - X)
t4.new_ab()
t4.pitch_list("2 b b b c b")
t4.reach("BB")
t4.advance(4, "7 2B")

# 8. BOS #7  Christian Vázquez (X - 36 - 19)
t4.new_ab()
t4.hit(2, rbis=2)

# 9. BOS #61 Brian Johnson (X - 7 - X)
t4.new_ab()
t4.pitch_list("c f b b f")
t4.out("G5-3")


# Bot 4th
# Pitching: BOS #61 Brian Johnson
b4 = game.new_inning()

# 5. MIA #41 Justin Bour (X - X - X)
b4.new_ab()
b4.pitch_list("b c c b")
b4.hit(1)
b4.advance(2, "1 1B")

# 6. MIA #1  Cameron Maybin (X - X - 41)
b4.new_ab()
b4.pitch_list("c c d")
b4.hit(1)
b4.thrown_out(2, "28 DP4-6-3", 2, 61)

# 7. MIA #19 Miguel Rojas (X - 41 - 1)
b4.new_ab()
b4.pitch_list("d")
b4.out("L9")

# 8. MIA #28 Bryan Holaday (X - 41 - 1)
b4.new_ab()
b4.pitch_list("c c b b")
b4.out("DP4-6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: MIA #63 Trevor Richards
t5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c b b")
t5.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.advance(4, "13 HR")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t5.new_ab()
t5.pitch_list("d f")
t5.hit(4, rbis=2)

# 4. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.hit(1)
t5.thrown_out(2, "2 CS", 3, 25)

# Pitching change (MIA): #25 Junichi Tazawa replaces #63 Trevor Richards, batting 8th
t5.pitching_substitution(25)
t5.defensive_substitution(8, 25, "1")

# Defensive change (MIA): #18 Tomás Telis replaces #63 Trevor Richards (P), playing C, batting 9th
t5.defensive_substitution(9, 18, "2")

# 5. BOS #2  Xander Bogaerts (X - X - 11)
t5.new_ab()
t5.pitch_list("b t b c b s")
t5.out("KDP2-4")


# Bot 5th
# Pitching: BOS #61 Brian Johnson
b5 = game.new_inning()

# 9. MIA #18 Tomás Telis (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("F9")

# 1. MIA #9  Lewis Brinson (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G5-3")

# 2. MIA #32 Derek Dietrich (X - X - X)
b5.new_ab()
b5.pitch_list("b b c c c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: MIA #25 Junichi Tazawa
t6 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.out("G6-3")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("c b s b f b")
t6.out("G4-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G4-3")


# Bot 6th
# Pitching: BOS #61 Brian Johnson
b6 = game.new_inning()

# 3. MIA #13 Starlin Castro (X - X - X)
b6.new_ab()
b6.hit(1)
b6.advance(2, "15 BB")

# 4. MIA #15 Brian Anderson (X - X - 13)
b6.new_ab()
b6.pitch_list("b c b b b")
b6.reach("BB")

# 5. MIA #41 Justin Bour (X - 13 - 15)
b6.new_ab()
b6.out("F7")

# 6. MIA #1  Cameron Maybin (X - 13 - 15)
b6.new_ab()
b6.pitch_list("b c")
b6.out("F8")

# 7. MIA #19 Miguel Rojas (X - 13 - 15)
b6.new_ab()
b6.pitch_list("c")
b6.out("(F)P3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: MIA #50 Chris O'Grady
t7 = game.new_inning()

# Pitching change (MIA): #50 Chris O'Grady replaces #25 Junichi Tazawa, batting 8th
t7.pitching_substitution(50)
t7.defensive_substitution(8, 50, "1")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #61 Brian Johnson, batting 9th
t7.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Blake Swihart (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c b c")
t7.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("b c c b f f b b")
t7.reach("BB")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t7.new_ab()
t7.pitch_list("t b")
t7.out("F7")

# 4. BOS #11 Rafael Devers (X - X - 16)
t7.new_ab()
t7.pitch_list("c")
t7.out("L9")


# Bot 7th
# Pitching: BOS #37 Heath Hembree
b7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #61 Brian Johnson, batting 9th
b7.pitching_substitution(37)
b7.defensive_substitution(9, 37, "1")

# Offensive change (MIA): Pinch-hitter #2 Yadiel Rivera replaces #50 Chris O'Grady, batting 8th
b7.offensive_substitution(8, 2, "PH")

# 8. MIA #2  Yadiel Rivera (X - X - X)
b7.new_ab()
b7.pitch_list("b f c b s")
b7.out("K")

# 9. MIA #18 Tomás Telis (X - X - X)
b7.new_ab()
b7.pitch_list("c s f")
b7.hit(1)

# 1. MIA #9  Lewis Brinson (X - X - 18)
b7.new_ab()
b7.pitch_list("b f b")
b7.out("F8")

# 2. MIA #32 Derek Dietrich (X - X - 18)
b7.new_ab()
b7.pitch_list("t b b")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: MIA #44 Jacob Turner
t8 = game.new_inning()

# Pitching change (MIA): #44 Jacob Turner replaces #50 Chris O'Grady, batting 2nd
t8.pitching_substitution(44)
t8.defensive_substitution(2, 44, "1")

# Defensive switch (MIA): #2 Yadiel Rivera moves to LF
t8.defensive_switch(2, "7")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(2, "19 BB")
t8.advance(3, "7 L9")

# 6. BOS #36 Eduardo Núñez (X - X - 2)
t8.new_ab()
t8.pitch_list("f")
t8.out("F9")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 2)
t8.new_ab()
t8.pitch_list("c b b b f d")
t8.reach("BB")

# 8. BOS #7  Christian Vázquez (X - 2 - 19)
t8.new_ab()
t8.pitch_list("c f d")
t8.out("L9")

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #37 Heath Hembree, batting 9th
t8.offensive_substitution(9, 18, "PH")

# 9. BOS #18 Mitch Moreland (2 - X - 19)
t8.new_ab()
t8.pitch_list("b f b")
t8.out("G1-3")


# Bot 8th
# Pitching: BOS #64 Marcus Walden
b8 = game.new_inning()

# Pitching change (BOS): #64 Marcus Walden replaces #37 Heath Hembree, batting 9th
b8.pitching_substitution(64)
b8.defensive_substitution(9, 64, "1")

# 3. MIA #13 Starlin Castro (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.hit(2)
b8.advance(4, "1 1B")

# 4. MIA #15 Brian Anderson (X - 13 - X)
b8.new_ab()
b8.reach("HBP")
b8.advance(2, "1 1B")
b8.advance(3, "19 FC1-6")

# 5. MIA #41 Justin Bour (X - 13 - 15)
b8.new_ab()
b8.pitch_list("c b f b b s")
b8.out("K")

# 6. MIA #1  Cameron Maybin (X - 13 - 15)
b8.new_ab()
b8.pitch_list("b b")
b8.hit(1, rbis=1)
b8.thrown_out(2, "19 FC1-6", 2, 64)

# 7. MIA #19 Miguel Rojas (X - 15 - 1)
b8.new_ab()
b8.pitch_list("c")
b8.reach("FC1-6")

# 8. MIA #2  Yadiel Rivera (15 - X - 19)
b8.new_ab()
b8.pitch_list("b d")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: MIA #44 Jacob Turner
t9 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
t9.advance(2, "11 SB")
t9.advance(4, "11 2B")

# 4. BOS #11 Rafael Devers (X - X - 13)
t9.new_ab()
t9.pitch_list("d c s")
t9.hit(2, rbis=1)

# 5. BOS #2  Xander Bogaerts (X - 11 - X)
t9.new_ab()
t9.pitch_list("b c")
t9.out("F8")


# Bot 9th
# Pitching: BOS #64 Marcus Walden
b9 = game.new_inning()

# 9. MIA #18 Tomás Telis (X - X - X)
b9.new_ab()
b9.pitch_list("b b c b c f b")
b9.reach("BB")
b9.advance(2, "9 1B")
b9.advance(3, "17 WP")
b9.advance(4, "13 G3")

# 1. MIA #9  Lewis Brinson (X - X - 18)
b9.new_ab()
b9.pitch_list("c b s")
b9.hit(1)
b9.advance(2, "17 WP")
b9.advance(3, "13 G3")

# Offensive change (MIA): Pinch-hitter #17 Chad Wallach replaces #44 Jacob Turner, batting 2nd
b9.offensive_substitution(2, 17, "PH")

# 2. MIA #17 Chad Wallach (X - 18 - 9)
b9.new_ab()
b9.pitch_list("f b s")
b9.wp()
b9.out("G5-3")

# 3. MIA #13 Starlin Castro (18 - 9 - X)
b9.new_ab()
b9.pitch_list("s s")
b9.out("G3", rbis=1)

# 4. MIA #15 Brian Anderson (9 - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("P6")

# Winning team: BOS
# WP: BOS #61 Brian Johnson
game.winning_pitcher(61, is_away_team=True)

# Loser team: MIA
# LP: MIA #63 Trevor Richards
game.losing_pitcher(63)

# print(game)
game.generate_scorecard()
