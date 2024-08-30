import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-06-16
# https://www.baseball-reference.com/boxes/SEA/SEA201806160.shtml
# https://www.mlb.com/gameday/red-sox-vs-mariners/2018/06/16/530450/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-16 20:16-22:38",
        "at": "Safeco Field, Seattle, WA",
        "att": "44,151",
        "temp": "74F, Clear",
        "wind": "3mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 35,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                35: "Steven Wright",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
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
                [28, "0"],
                [11, "5"],
                [2, "6"],
                [36, "4"],
                [23, "3"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [3, "C"],
            ],
            "bullpen": [57, 44, 22, 41, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "home": {
            "team": "Seattle Mariners",
            "starter": 49,
            "roster": {
                # Lineup
                9: "Dee Strange-Gordon",
                2: "Jean Segura",
                17: "Mitch Haniger",
                23: "Nelson Cruz",
                15: "Kyle Seager",
                27: "Ryon Healy",
                4: "Denard Span",
                3: "Mike Zunino",
                5: "Guillermo Heredia",
                # Starting pitcher
                49: "Wade LeBlanc",
                # Bench
                16: "Ben Gamel",
                36: "David Freitas",
                7: "Andrew Romine",
                # Bullpen
                52: "Nick Rumbelow",
                48: "Alex Colomé",
                8: "Mike Leake",
                60: "Chasen Bradford",
                65: "James Paxton",
                47: "James Pazos",
                46: "Ryan Cook",
                63: "Rob Whalen",
                39: "Edwin Díaz",
                55: "Roenis Elías",
                32: "Marco Gonzales",
                34: "Félix Hernández",
            },
            "lefties": [49, 65, 47, 55, 32],
            "lineup": [
                [9, "4"],
                [2, "6"],
                [17, "9"],
                [23, "0"],
                [15, "5"],
                [27, "3"],
                [4, "7"],
                [3, "2"],
                [5, "8"],
            ],
            "bench": [
                [16, "RF"],
                [36, "C"],
                [7, "SS"],
            ],
            "bullpen": [52, 48, 8, 60, 65, 47, 46, 63, 39, 55, 32, 34],
        },
        "umpires": {
            "HP": "Lance Barrett",
            "1B": "Vic Carapazza",
            "2B": "Tony Randazzo",
            "3B": "Bill Welke",
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
# Pitching: SEA #49 Wade LeBlanc
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c f f b f f b b")
t1.hit(1)
t1.thrown_out(2, "16 DP4-6-3", 1, 49)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.pitch_list("f 1 c f")
t1.out("DP4-6-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("c f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #35 Steven Wright
b1 = game.new_inning()

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b1.new_ab()
b1.pitch_list("b f b b c")
b1.out("L7")

# 2. SEA #2  Jean Segura (X - X - X)
b1.new_ab()
b1.pitch_list("c s b")
b1.out("G4-3")

# 3. SEA #17 Mitch Haniger (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c b")
b1.reach("BB")

# 4. SEA #23 Nelson Cruz (X - X - 17)
b1.new_ab()
b1.pitch_list("c s s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SEA #49 Wade LeBlanc
t2 = game.new_inning()

# 4. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.out("G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("b c s s")
t2.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b s f f f")
t2.out("G6-3")


# Bot 2nd
# Pitching: BOS #35 Steven Wright
b2 = game.new_inning()

# 5. SEA #15 Kyle Seager (X - X - X)
b2.new_ab()
b2.pitch_list("b c c b")
b2.out("G6-3")

# 6. SEA #27 Ryon Healy (X - X - X)
b2.new_ab()
b2.pitch_list("c f f")
b2.out("G5-3")

# 7. SEA #4  Denard Span (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(1)

# 8. SEA #3  Mike Zunino (X - X - 4)
b2.new_ab()
b2.pitch_list("f 1 f c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SEA #49 Wade LeBlanc
t3 = game.new_inning()

# 7. BOS #23 Blake Swihart (X - X - X)
t3.new_ab()
t3.pitch_list("c b f c")
t3.out("!K")

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("F9")


# Bot 3rd
# Pitching: BOS #35 Steven Wright
b3 = game.new_inning()

# 9. SEA #5  Guillermo Heredia (X - X - X)
b3.new_ab()
b3.pitch_list("c c b f f s")
b3.out("K")

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.hit(1)
b3.advance(2, "17 1B")
b3.advance(4, "23 1B")

# 2. SEA #2  Jean Segura (X - X - 9)
b3.new_ab()
b3.pitch_list("b 1")
b3.out("F8")

# 3. SEA #17 Mitch Haniger (X - X - 9)
b3.new_ab()
b3.pitch_list("1 b 1 c")
b3.hit(1)
b3.advance(2, "23 1B")

# 4. SEA #23 Nelson Cruz (X - 9 - 17)
b3.new_ab()
b3.pitch_list("b t b s b")
b3.hit(1, rbis=1)

# 5. SEA #15 Kyle Seager (X - 17 - 23)
b3.new_ab()
b3.pitch_list("b b")
b3.out("G3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SEA #49 Wade LeBlanc
t4 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("c b c b c")
t4.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("F7")

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c b f b f f c")
t4.out("!K")


# Bot 4th
# Pitching: BOS #35 Steven Wright
b4 = game.new_inning()

# 6. SEA #27 Ryon Healy (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("F9")

# 7. SEA #4  Denard Span (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G3")

# 8. SEA #3  Mike Zunino (X - X - X)
b4.new_ab()
b4.pitch_list("b s b c")
b4.out("L9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SEA #49 Wade LeBlanc
t5 = game.new_inning()

# 4. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("L1")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("f b b s b")
t5.out("G4-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #35 Steven Wright
b5 = game.new_inning()

# 9. SEA #5  Guillermo Heredia (X - X - X)
b5.new_ab()
b5.pitch_list("s c b b b")
b5.error(5)
b5.reach("E5")
b5.thrown_out(2, "9 FC1-6-4", 1, 35)

# 1. SEA #9  Dee Strange-Gordon (X - X - 5)
b5.new_ab()
b5.pitch_list("f")
b5.reach("FC1-6-4")
b5.thrown_out(2, "17 CS", 3, 35)

# 2. SEA #2  Jean Segura (X - X - 9)
b5.new_ab()
b5.pitch_list("s 1 f s")
b5.out("K")

# 3. SEA #17 Mitch Haniger (X - X - 9)
b5.new_ab()
b5.pitch_list("1 c f b")
b5.no_ab("CS")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SEA #49 Wade LeBlanc
t6 = game.new_inning()

# 7. BOS #23 Blake Swihart (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("G4-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t6.new_ab()
t6.pitch_list("c f s")
t6.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("f b s c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #35 Steven Wright
b6 = game.new_inning()

# 3. SEA #17 Mitch Haniger (X - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.out("F7")

# 4. SEA #23 Nelson Cruz (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("L7")

# 5. SEA #15 Kyle Seager (X - X - X)
b6.new_ab()
b6.pitch_list("c b c b")
b6.hit(1)

# 6. SEA #27 Ryon Healy (X - X - 15)
b6.new_ab()
b6.pitch_list("c f f f b")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SEA #49 Wade LeBlanc
t7 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c s b s")
t7.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("s f")
t7.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("c f f")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #35 Steven Wright
b7 = game.new_inning()

# 7. SEA #4  Denard Span (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c c b")
b7.reach("BB")
b7.thrown_out(2, "3 DP6-4-3", 1, 35)

# 8. SEA #3  Mike Zunino (X - X - 4)
b7.new_ab()
b7.pitch_list("b b c")
b7.out("DP6-4-3")

# 9. SEA #5  Guillermo Heredia (X - X - X)
b7.new_ab()
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SEA #49 Wade LeBlanc
t8 = game.new_inning()

# 4. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("s f b c")
t8.out("!K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b f")
t8.out("G6-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("f s b f f")
t8.hit(1)

# Pitching change (SEA): #48 Alex Colomé replaces #49 Wade LeBlanc
t8.pitching_substitution(48)

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #23 Blake Swihart, batting 7th
t8.offensive_substitution(7, 18, "PH")

# 7. BOS #18 Mitch Moreland (X - X - 36)
t8.new_ab()
t8.pitch_list("t")
t8.out("P5")


# Bot 8th
# Pitching: BOS #44 Brandon Workman
b8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #35 Steven Wright
b8.pitching_substitution(44)

# Defensive switch (BOS): #18 Mitch Moreland moves to 1B
b8.defensive_switch(18, "3")

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b8.new_ab()
b8.pitch_list("f c s")
b8.out("K")

# 2. SEA #2  Jean Segura (X - X - X)
b8.new_ab()
b8.pitch_list("b b c")
b8.hit(2)

# 3. SEA #17 Mitch Haniger (X - 2 - X)
b8.new_ab()
b8.pitch_list("c b s b s")
b8.out("K")

# 4. SEA #23 Nelson Cruz (X - 2 - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("(F)P3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SEA #39 Edwin Díaz
t9 = game.new_inning()

# Pitching change (SEA): #39 Edwin Díaz replaces #48 Alex Colomé
t9.pitching_substitution(39)

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #7 Christian Vázquez, batting 8th
t9.offensive_substitution(8, 12, "PH")

# 8. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("c t b s")
t9.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("f b s s")
t9.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("c f b b b f s")
t9.out("K")

# Winning team: SEA
# WP: SEA #49 Wade LeBlanc
game.winning_pitcher(49)
# SV: SEA #39 Edwin Díaz
game.save_pitcher(39)

# Loser team: BOS
# LP: BOS #35 Steven Wright
game.losing_pitcher(35, is_away_team=True)

# print(game)
game.generate_scorecard()
