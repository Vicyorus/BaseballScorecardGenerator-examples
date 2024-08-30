import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-06-17
# https://www.baseball-reference.com/boxes/SEA/SEA201806170.shtml
# https://www.mlb.com/gameday/red-sox-vs-mariners/2018/06/17/530465/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-17 16:10-19:25",
        "at": "Safeco Field, Seattle, WA",
        "att": "46,462",
        "temp": "76F, Sunny",
        "wind": "6mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                11: "Rafael Devers",
                12: "Brock Holt",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                35: "Steven Wright",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [2, "6"],
                [28, "0"],
                [18, "3"],
                [11, "5"],
                [12, "4"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [36, "SS"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [35, 44, 22, 41, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "home": {
            "team": "Seattle Mariners",
            "starter": 8,
            "roster": {
                # Lineup
                9: "Dee Strange-Gordon",
                2: "Jean Segura",
                17: "Mitch Haniger",
                23: "Nelson Cruz",
                15: "Kyle Seager",
                27: "Ryon Healy",
                5: "Guillermo Heredia",
                16: "Ben Gamel",
                36: "David Freitas",
                # Starting pitcher
                8: "Mike Leake",
                # Bench
                3: "Mike Zunino",
                4: "Denard Span",
                7: "Andrew Romine",
                # Bullpen
                52: "Nick Rumbelow",
                48: "Alex Colomé",
                60: "Chasen Bradford",
                65: "James Paxton",
                47: "James Pazos",
                46: "Ryan Cook",
                63: "Rob Whalen",
                49: "Wade LeBlanc",
                39: "Edwin Díaz",
                55: "Roenis Elías",
                32: "Marco Gonzales",
                34: "Félix Hernández",
            },
            "lefties": [65, 47, 49, 55, 32],
            "lineup": [
                [9, "4"],
                [2, "6"],
                [17, "9"],
                [23, "0"],
                [15, "5"],
                [27, "3"],
                [5, "8"],
                [16, "7"],
                [36, "2"],
            ],
            "bench": [
                [3, "C"],
                [4, "CF"],
                [7, "SS"],
            ],
            "bullpen": [52, 48, 60, 65, 47, 46, 63, 49, 39, 55, 32, 34],
        },
        "umpires": {
            "HP": "Vic Carapazza",
            "1B": "Tony Randazzo",
            "2B": "Bill Welke",
            "3B": "Lance Barrett",
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
# Pitching: SEA #8  Mike Leake
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("f b b")
t1.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.thrown_out(2, "2 DP5-4-3", 2, 8)

# 3. BOS #2  Xander Bogaerts (X - X - 16)
t1.new_ab()
t1.pitch_list("f b d")
t1.out("DP5-4-3")


# Bot 1st
# Pitching: BOS #57 Eduardo Rodriguez
b1 = game.new_inning()

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b1.new_ab()
b1.pitch_list("f f b b")
b1.hit(1)
b1.error(6)
b1.advance(2, "E6")

# 2. SEA #2  Jean Segura (X - 9 - X)
b1.new_ab()
b1.out("P3")

# 3. SEA #17 Mitch Haniger (X - 9 - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.out("G4-3")

# 4. SEA #23 Nelson Cruz (X - 9 - X)
b1.new_ab()
b1.pitch_list("f b b")
b1.out("G3-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SEA #8  Mike Leake
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.hit(1)
t2.advance(2, "11 1B")

# 5. BOS #18 Mitch Moreland (X - X - 28)
t2.new_ab()
t2.pitch_list("c b b")
t2.out("F8")

# 6. BOS #11 Rafael Devers (X - X - 28)
t2.new_ab()
t2.pitch_list("1 1 b b f f 1")
t2.hit(1)

# 7. BOS #12 Brock Holt (X - 28 - 11)
t2.new_ab()
t2.pitch_list("b c f f")
t2.out("L3")

# 8. BOS #7  Christian Vázquez (X - 28 - 11)
t2.new_ab()
t2.pitch_list("c b s")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #57 Eduardo Rodriguez
b2 = game.new_inning()

# 5. SEA #15 Kyle Seager (X - X - X)
b2.new_ab()
b2.pitch_list("f s b f b f f f f s")
b2.out("K")

# 6. SEA #27 Ryon Healy (X - X - X)
b2.new_ab()
b2.pitch_list("f s b f b")
b2.out("P4")

# 7. SEA #5  Guillermo Heredia (X - X - X)
b2.new_ab()
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SEA #8  Mike Leake
t3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b c f b")
t3.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("b f")
t3.hit(1)
t3.advance(2, "2 1B")
t3.advance(3, "28 BB")
t3.advance(4, "18 1B")

# 3. BOS #2  Xander Bogaerts (X - X - 16)
t3.new_ab()
t3.hit(1)
t3.advance(2, "28 BB")
t3.advance(4, "18 1B")

# 4. BOS #28 J.D. Martinez (X - 16 - 2)
t3.new_ab()
t3.pitch_list("s b c b d f f f b")
t3.reach("BB")
t3.advance(3, "18 1B")
t3.advance(4, "11 HR")

# 5. BOS #18 Mitch Moreland (16 - 2 - 28)
t3.new_ab()
t3.hit(1, rbis=2)
t3.advance(4, "11 HR")

# 6. BOS #11 Rafael Devers (28 - X - 18)
t3.new_ab()
t3.pitch_list("b f f")
t3.hit(4, rbis=3)

# 7. BOS #12 Brock Holt (X - X - X)
t3.new_ab()
t3.pitch_list("c f b")
t3.hit(1)

# 8. BOS #7  Christian Vázquez (X - X - 12)
t3.new_ab()
t3.pitch_list("c b f f b")
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #57 Eduardo Rodriguez
b3 = game.new_inning()

# 8. SEA #16 Ben Gamel (X - X - X)
b3.new_ab()
b3.pitch_list("c s f s")
b3.out("K")

# 9. SEA #36 David Freitas (X - X - X)
b3.new_ab()
b3.pitch_list("c b s c")
b3.out("!K")

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b")
b3.hit(1)
b3.advance(2, "2 BB")

# 2. SEA #2  Jean Segura (X - X - 9)
b3.new_ab()
b3.pitch_list("b b b c b")
b3.reach("BB")

# 3. SEA #17 Mitch Haniger (X - 9 - 2)
b3.new_ab()
b3.pitch_list("s b s b b c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SEA #8  Mike Leake
t4 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G3-1")

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("c b b c b f")
t4.out("P4")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.out("L8")


# Bot 4th
# Pitching: BOS #57 Eduardo Rodriguez
b4 = game.new_inning()

# 4. SEA #23 Nelson Cruz (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s f b")
b4.hit(4, rbis=1)

# 5. SEA #15 Kyle Seager (X - X - X)
b4.new_ab()
b4.pitch_list("f f b b s")
b4.out("K")

# 6. SEA #27 Ryon Healy (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f c")
b4.out("!K")

# 7. SEA #5  Guillermo Heredia (X - X - X)
b4.new_ab()
b4.pitch_list("f b b s f f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SEA #8  Mike Leake
t5 = game.new_inning()

# 3. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("b c f")
t5.out("G5-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.pitch_list("c f f b f f b f b")
t5.out("G6-3")

# 5. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("b f f b c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #57 Eduardo Rodriguez
b5 = game.new_inning()

# 8. SEA #16 Ben Gamel (X - X - X)
b5.new_ab()
b5.pitch_list("c c b")
b5.hit(2)
b5.advance(3, "9 1B")
b5.advance(4, "2 FC5-4")

# 9. SEA #36 David Freitas (X - 16 - X)
b5.new_ab()
b5.hit(1)
b5.advance(2, "9 1B")
b5.advance(3, "2 FC5-4")

# 1. SEA #9  Dee Strange-Gordon (X - 16 - 36)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(1)
b5.thrown_out(2, "2 FC5-4", 1, 57)

# 2. SEA #2  Jean Segura (16 - 36 - 9)
b5.new_ab()
b5.pitch_list("f")
b5.reach("FC5-4", rbis=1)

# 3. SEA #17 Mitch Haniger (36 - X - 2)
b5.new_ab()
b5.out("F9")

# 4. SEA #23 Nelson Cruz (36 - X - 2)
b5.new_ab()
b5.pitch_list("b b c t b f")
b5.out("(F)P3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SEA #8  Mike Leake
t6 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("b b s")
t6.out("L9")

# 7. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G3-1")

# 8. BOS #7  Christian Vázquez (X - X - X)
t6.new_ab()
t6.out("F9")


# Bot 6th
# Pitching: BOS #57 Eduardo Rodriguez
b6 = game.new_inning()

# 5. SEA #15 Kyle Seager (X - X - X)
b6.new_ab()
b6.pitch_list("s b b b f")
b6.out("F8")

# 6. SEA #27 Ryon Healy (X - X - X)
b6.new_ab()
b6.pitch_list("b b f s b s")
b6.out("K")

# 7. SEA #5  Guillermo Heredia (X - X - X)
b6.new_ab()
b6.pitch_list("l b c s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SEA #60 Chasen Bradford
t7 = game.new_inning()

# Pitching change (SEA): #60 Chasen Bradford replaces #8  Mike Leake
t7.pitching_substitution(60)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.hit(4, rbis=1)

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c f b")
t7.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(1)
t7.advance(2, "2 SB")
t7.advance(4, "2 HR")

# 3. BOS #2  Xander Bogaerts (X - X - 16)
t7.new_ab()
t7.pitch_list("1 b")
t7.hit(4, rbis=2)

# 4. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("s b")
t7.out("F9")

# Pitching change (SEA): #55 Roenis Elías replaces #60 Chasen Bradford
t7.pitching_substitution(55)

# 5. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.hit(1)

# 6. BOS #11 Rafael Devers (X - X - 18)
t7.new_ab()
t7.out("F8")


# Bot 7th
# Pitching: BOS #32 Matt Barnes
b7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #57 Eduardo Rodriguez
b7.pitching_substitution(32)

# 8. SEA #16 Ben Gamel (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c f f c")
b7.out("!K")

# 9. SEA #36 David Freitas (X - X - X)
b7.new_ab()
b7.pitch_list("b c c")
b7.out("G6-3")

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SEA #55 Roenis Elías
t8 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("b f f f b")
t8.out("G3-1")

# 8. BOS #7  Christian Vázquez (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(2)
t8.advance(3, "50 BB")
t8.advance(4, "16 SF8")

# 9. BOS #19 Jackie Bradley Jr. (X - 7 - X)
t8.new_ab()
t8.pitch_list("c b s b b f f d")
t8.reach("BB")
t8.advance(2, "50 BB")

# 1. BOS #50 Mookie Betts (X - 7 - 19)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")

# 2. BOS #16 Andrew Benintendi (7 - 19 - 50)
t8.new_ab()
t8.out("SF8", rbis=1)

# 3. BOS #2  Xander Bogaerts (X - 19 - 50)
t8.new_ab()
t8.pitch_list("b c f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #44 Brandon Workman
b8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #32 Matt Barnes
b8.pitching_substitution(44)

# Offensive change (SEA): Pinch-hitter #7 Andrew Romine replaces #2 Jean Segura, batting 2nd
b8.offensive_substitution(2, 7, "PH")

# 2. SEA #7  Andrew Romine (X - X - X)
b8.new_ab()
b8.pitch_list("b c f b f s")
b8.out("K")

# 3. SEA #17 Mitch Haniger (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c b")
b8.reach("BB")
b8.advance(2, "23 BB")
b8.advance(4, "27 2B")

# 4. SEA #23 Nelson Cruz (X - X - 17)
b8.new_ab()
b8.pitch_list("d c d d s f b")
b8.reach("BB")
b8.advance(3, "27 2B")

# 5. SEA #15 Kyle Seager (X - 17 - 23)
b8.new_ab()
b8.pitch_list("b")
b8.out("F7")

# 6. SEA #27 Ryon Healy (X - 17 - 23)
b8.new_ab()
b8.pitch_list("b b f")
b8.hit(2, rbis=1)

# Pitching change (BOS): #76 Hector Velázquez replaces #44 Brandon Workman
b8.pitching_substitution(76)

# 7. SEA #5  Guillermo Heredia (23 - 27 - X)
b8.new_ab()
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SEA #55 Roenis Elías
t9 = game.new_inning()

# Defensive switch (SEA): #7 Andrew Romine moves to SS
t9.defensive_switch(7, "6")

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #18 Mitch Moreland, batting 5th
t9.offensive_substitution(5, 23, "PH")

# 5. BOS #23 Blake Swihart (X - X - X)
t9.new_ab()
t9.pitch_list("c s b")
t9.out("P4")

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("c b b f f s")
t9.out("K")


# Bot 9th
# Pitching: BOS #76 Hector Velázquez
b9 = game.new_inning()

# Defensive switch (BOS): #23 Blake Swihart moves to 1B
b9.defensive_switch(23, "3")

# 8. SEA #16 Ben Gamel (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("G3-1")

# 9. SEA #36 David Freitas (X - X - X)
b9.new_ab()
b9.pitch_list("s b")
b9.hit(1)

# 1. SEA #9  Dee Strange-Gordon (X - X - 36)
b9.new_ab()
b9.pitch_list("f")
b9.out("F7")

# 2. SEA #7  Andrew Romine (X - X - 36)
b9.new_ab()
b9.pitch_list("b")
b9.out("G1-3")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57, is_away_team=True)

# Loser team: SEA
# LP: SEA #8 Mike Leake
game.losing_pitcher(8)

# print(game)
game.generate_scorecard()
