import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-06-15
# https://www.baseball-reference.com/boxes/SEA/SEA201806150.shtml
# https://www.mlb.com/gameday/red-sox-vs-mariners/2018/06/15/530435/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-15 22:10-01:19 +1",
        "at": "Safeco Field, Seattle, WA",
        "att": "44,459",
        "temp": "70F, Partly Cloudy",
        "wind": "6mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                12: "Brock Holt",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
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
                [12, "4"],
                [28, "7"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [36, "0"],
                [19, "8"],
                [3, "2"],
            ],
            "bench": [
                [23, "C"],
                [16, "LF"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 44, 41, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "home": {
            "team": "Seattle Mariners",
            "starter": 65,
            "roster": {
                # Lineup
                9: "Dee Strange-Gordon",
                2: "Jean Segura",
                17: "Mitch Haniger",
                23: "Nelson Cruz",
                15: "Kyle Seager",
                27: "Ryon Healy",
                16: "Ben Gamel",
                5: "Guillermo Heredia",
                3: "Mike Zunino",
                # Starting pitcher
                65: "James Paxton",
                # Bench
                4: "Denard Span",
                36: "David Freitas",
                7: "Andrew Romine",
                # Bullpen
                52: "Nick Rumbelow",
                48: "Alex Colomé",
                8: "Mike Leake",
                60: "Chasen Bradford",
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
                [16, "7"],
                [5, "8"],
                [3, "2"],
            ],
            "bench": [
                [4, "CF"],
                [36, "C"],
                [7, "SS"],
            ],
            "bullpen": [52, 48, 8, 60, 47, 46, 63, 49, 39, 55, 32, 34],
        },
        "umpires": {
            "HP": "Bill Welke",
            "1B": "Lance Barrett",
            "2B": "Vic Carapazza",
            "3B": "Tony Randazzo",
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
# Pitching: SEA #65 James Paxton
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.error(6)
t1.reach("E6")
t1.advance(2, "12 WP")

# 2. BOS #12 Brock Holt (X - X - 50)
t1.new_ab()
t1.pitch_list("b c c s")
t1.wp()
t1.out("K")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
t1.new_ab()
t1.pitch_list("c b s d s")
t1.out("K")

# 4. BOS #18 Mitch Moreland (X - 50 - X)
t1.new_ab()
t1.pitch_list("b s d f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b1.new_ab()
b1.pitch_list("c b b f c")
b1.out("!K")

# 2. SEA #2  Jean Segura (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(4)

# 3. SEA #17 Mitch Haniger (X - X - X)
b1.new_ab()
b1.pitch_list("b c f b s")
b1.out("K")

# 4. SEA #23 Nelson Cruz (X - X - X)
b1.new_ab()
b1.pitch_list("c c c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SEA #65 James Paxton
t2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b")
t2.out("F9")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("f b b f")
t2.out("L7")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b b")
t2.out("L8")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 5. SEA #15 Kyle Seager (X - X - X)
b2.new_ab()
b2.hit(2)
b2.advance(3, "27 1B")
b2.advance(4, "16 FC1-6")

# 6. SEA #27 Ryon Healy (X - 15 - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)
b2.thrown_out(2, "16 FC1-6", 1, 22)

# 7. SEA #16 Ben Gamel (15 - X - 27)
b2.new_ab()
b2.pitch_list("b f c b d f")
b2.reach("FC1-6", rbis=1)
b2.advance(2, "5 SB")
b2.advance(4, "3 1B")

# 8. SEA #5  Guillermo Heredia (X - X - 16)
b2.new_ab()
b2.pitch_list("b b f b f 1 s")
b2.out("K")

# 9. SEA #3  Mike Zunino (X - 16 - X)
b2.new_ab()
b2.pitch_list("f c b f b")
b2.hit(1, rbis=1)

# 1. SEA #9  Dee Strange-Gordon (X - X - 3)
b2.new_ab()
b2.pitch_list("s")
b2.out("G3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SEA #65 James Paxton
t3 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b c f b b f")
t3.hit(1)
t3.error(6)
t3.advance(2, "50 1B")
t3.advance(3, "50 E6")
t3.advance(4, "12 1B")

# 9. BOS #3  Sandy León (X - X - 19)
t3.new_ab()
t3.pitch_list("b s f 1 c")
t3.out("!K")

# 1. BOS #50 Mookie Betts (X - X - 19)
t3.new_ab()
t3.pitch_list("c b d f b")
t3.hit(1)
t3.advance(2, "12 1B")
t3.advance(3, "28 1B")
t3.advance(4, "18 1B")

# 2. BOS #12 Brock Holt (19 - X - 50)
t3.new_ab()
t3.hit(1, rbis=1)
t3.advance(2, "28 1B")
t3.advance(4, "18 1B")

# 3. BOS #28 J.D. Martinez (X - 50 - 12)
t3.new_ab()
t3.pitch_list("d f s b")
t3.hit(1)
t3.advance(2, "18 1B")
t3.advance(3, "2 WP")
t3.advance(4, "2 HR")

# 4. BOS #18 Mitch Moreland (50 - 12 - 28)
t3.new_ab()
t3.hit(1, rbis=2)
t3.advance(2, "2 WP")
t3.advance(4, "2 HR")

# 5. BOS #2  Xander Bogaerts (X - 28 - 18)
t3.new_ab()
t3.pitch_list("b d c b")
t3.wp()
t3.hit(4, rbis=3)

# 6. BOS #11 Rafael Devers (X - X - X)
t3.new_ab()
t3.pitch_list("b b s f")
t3.hit(1)
t3.advance(2, "36 SB")

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t3.new_ab()
t3.pitch_list("s b b f b b")
t3.reach("BB")

# Pitching change (SEA): #60 Chasen Bradford replaces #65 James Paxton
t3.pitching_substitution(60)

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - 36)
t3.new_ab()
t3.pitch_list("b f c f f")
t3.out("L3")

# 9. BOS #3  Sandy León (X - 11 - 36)
t3.new_ab()
t3.pitch_list("b")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 2. SEA #2  Jean Segura (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G5-3")

# 3. SEA #17 Mitch Haniger (X - X - X)
b3.new_ab()
b3.pitch_list("c b b")
b3.out("P4")

# 4. SEA #23 Nelson Cruz (X - X - X)
b3.new_ab()
b3.pitch_list("b f b")
b3.out("P6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SEA #63 Rob Whalen
t4 = game.new_inning()

# Pitching change (SEA): #63 Rob Whalen replaces #60 Chasen Bradford
t4.pitching_substitution(63)

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("c c")
t4.out("L4")

# 2. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("b b c f")
t4.out("G6-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("s b s b")
t4.out("G5-3")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 5. SEA #15 Kyle Seager (X - X - X)
b4.new_ab()
b4.pitch_list("b c s f b f b f s")
b4.out("K")

# 6. SEA #27 Ryon Healy (X - X - X)
b4.new_ab()
b4.out("F8")

# 7. SEA #16 Ben Gamel (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SEA #63 Rob Whalen
t5 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("c b b f")
t5.out("F8")

# 6. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G3")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 8. SEA #5  Guillermo Heredia (X - X - X)
b5.new_ab()
b5.pitch_list("c b c s")
b5.out("K")

# 9. SEA #3  Mike Zunino (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G5-3")

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b5.new_ab()
b5.pitch_list("c c b b f f")
b5.hit(1)
b5.advance(2, "2 1B")
b5.advance(4, "17 1B")

# 2. SEA #2  Jean Segura (X - X - 9)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)
b5.advance(2, "17 1B")
b5.advance(3, "23 BB")

# 3. SEA #17 Mitch Haniger (X - 9 - 2)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1, rbis=1)
b5.advance(2, "23 BB")

# 4. SEA #23 Nelson Cruz (X - 2 - 17)
b5.new_ab()
b5.pitch_list("c f b b d b")
b5.reach("BB")

# 5. SEA #15 Kyle Seager (2 - 17 - 23)
b5.new_ab()
b5.pitch_list("f c f")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SEA #63 Rob Whalen
t6 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G4-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("f b b")
t6.out("L8")

# 9. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("b s")
t6.out("F8")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 6. SEA #27 Ryon Healy (X - X - X)
b6.new_ab()
b6.pitch_list("c c s")
b6.out("K")

# 7. SEA #16 Ben Gamel (X - X - X)
b6.new_ab()
b6.pitch_list("c c c")
b6.out("!K")

# 8. SEA #5  Guillermo Heredia (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("L4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SEA #63 Rob Whalen
t7 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.hit(1)
t7.advance(2, "28 BB")

# 2. BOS #12 Brock Holt (X - X - 50)
t7.new_ab()
t7.pitch_list("c b 1 1 f")
t7.out("F9")

# 3. BOS #28 J.D. Martinez (X - X - 50)
t7.new_ab()
t7.pitch_list("d b b b")
t7.reach("BB")
t7.thrown_out(2, "2 FC4-6", 3, 63)

# 4. BOS #18 Mitch Moreland (X - 50 - 28)
t7.new_ab()
t7.out("L9")

# 5. BOS #2  Xander Bogaerts (X - 50 - 28)
t7.new_ab()
t7.pitch_list("d b b c")
t7.reach("FC4-6")


# Bot 7th
# Pitching: BOS #37 Heath Hembree
b7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #22 Rick Porcello
b7.pitching_substitution(37)

# 9. SEA #3  Mike Zunino (X - X - X)
b7.new_ab()
b7.pitch_list("b s f b b")
b7.hit(4)

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b7.new_ab()
b7.pitch_list("l s f")
b7.out("G5-3")

# 2. SEA #2  Jean Segura (X - X - X)
b7.new_ab()
b7.pitch_list("b f")
b7.out("L7")

# 3. SEA #17 Mitch Haniger (X - X - X)
b7.new_ab()
b7.pitch_list("c b c b b d")
b7.reach("BB")

# 4. SEA #23 Nelson Cruz (X - X - 17)
b7.new_ab()
b7.pitch_list("b s b")
b7.out("P4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SEA #46 Ryan Cook
t8 = game.new_inning()

# Pitching change (SEA): #46 Ryan Cook replaces #63 Rob Whalen
t8.pitching_substitution(46)

# 6. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(2, "36 BB")
t8.thrown_out(3, "16 FC5", 2, 46)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t8.new_ab()
t8.pitch_list("1 f b b b b")
t8.reach("BB")
t8.advance(2, "16 FC5")
t8.advance(3, "50 IBB")

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - 36)
t8.new_ab()
t8.pitch_list("b m f b s")
t8.out("K")

# Offensive change (BOS): Pinch-hitter #16 Andrew Benintendi replaces #3 Sandy León, batting 9th
t8.offensive_substitution(9, 16, "PH")

# 9. BOS #16 Andrew Benintendi (X - 11 - 36)
t8.new_ab()
t8.reach("FC5")
t8.advance(2, "50 IBB")

# 1. BOS #50 Mookie Betts (X - 36 - 16)
t8.new_ab()
t8.pitch_list("b b b v")
t8.reach("IBB")

# 2. BOS #12 Brock Holt (36 - 16 - 50)
t8.new_ab()
t8.pitch_list("b c c")
t8.out("L7")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree
b8.pitching_substitution(32)

# Defensive change (BOS): #7 Christian Vázquez replaces #16 Andrew Benintendi (PH), playing C, batting 9th
b8.defensive_substitution(9, 7, "2")

# 5. SEA #15 Kyle Seager (X - X - X)
b8.new_ab()
b8.pitch_list("c b s b s")
b8.out("K")

# 6. SEA #27 Ryon Healy (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
# Offensive change (SEA): Pinch-runner #7 Andrew Romine replaces #27 Ryon Healy
b8.offensive_substitution(6, 7, "PR")
b8.atbase("PR")
b8.advance(2, "16 1B")
b8.advance(4, "4 2B")

# 7. SEA #16 Ben Gamel (X - X - 27)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.advance(4, "4 2B")

# Offensive change (SEA): Pinch-hitter #4 Denard Span replaces #5 Guillermo Heredia, batting 8th
b8.offensive_substitution(8, 4, "PH")

# 8. SEA #4  Denard Span (X - 7 - 16)
b8.new_ab()
b8.pitch_list("c b f b")
b8.hit(2, rbis=2)

# 9. SEA #3  Mike Zunino (X - 4 - X)
b8.new_ab()
b8.pitch_list("c b f s")
b8.out("K")

# 1. SEA #9  Dee Strange-Gordon (X - 4 - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SEA #39 Edwin Díaz
t9 = game.new_inning()

# Pitching change (SEA): #39 Edwin Díaz replaces #46 Ryan Cook
t9.pitching_substitution(39)

# Defensive switch (SEA): #17 Mitch Haniger moves to CF
t9.defensive_switch(17, "8")

# Defensive switch (SEA): #7 Andrew Romine moves to 1B
t9.defensive_switch(7, "3")

# Defensive switch (SEA): #16 Ben Gamel moves to RF
t9.defensive_switch(16, "9")

# Defensive switch (SEA): #4 Denard Span moves to LF
t9.defensive_switch(4, "7")

# 3. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(1)
# Offensive change (BOS): Pinch-runner #23 Blake Swihart replaces #28 J.D. Martinez
t9.offensive_substitution(3, 23, "PR")
t9.atbase("PR")
t9.advance(2, "2 SB")

# 4. BOS #18 Mitch Moreland (X - X - 28)
t9.new_ab()
t9.pitch_list("c d b f s")
t9.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - 23)
t9.new_ab()
t9.pitch_list("c s f d d d f b")
t9.reach("BB")

# 6. BOS #11 Rafael Devers (X - 23 - 2)
t9.new_ab()
t9.out("IF6")

# 7. BOS #36 Eduardo Núñez (X - 23 - 2)
t9.new_ab()
t9.pitch_list("f f")
t9.out("G3")

# Winning team: SEA
# WP: SEA #46 Ryan Cook
game.winning_pitcher(46)
# SV: SEA #39 Edwin Díaz
game.save_pitcher(39)

# Loser team: BOS
# LP: BOS #32 Matt Barnes
game.losing_pitcher(32, is_away_team=True)

# print(game)
game.generate_scorecard()
