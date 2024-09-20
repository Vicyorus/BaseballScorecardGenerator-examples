import os
from baseball_scorecard.baseball_scorecard import Scorecard

# SEA @ BOS, 2018-06-22
# https://www.baseball-reference.com/boxes/BOS/BOS201806220.shtml
# https://www.mlb.com/gameday/mariners-vs-red-sox/2018/06/22/530539/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-22 19:11-22:45",
        "at": "Fenway Park, Boston, MA",
        "att": "37,342",
        "temp": "69F, Partly Cloudy",
        "wind": "9mph, In From RF",
        "away": {
            "team": "Seattle Mariners",
            "starter": 49,
            "roster": {
                # Lineup
                9: "Dee Strange-Gordon",
                17: "Mitch Haniger",
                4: "Denard Span",
                23: "Nelson Cruz",
                15: "Kyle Seager",
                27: "Ryon Healy",
                3: "Mike Zunino",
                5: "Guillermo Heredia",
                7: "Andrew Romine",
                # Starting pitcher
                49: "Wade LeBlanc",
                # Bench
                2: "Jean Segura",
                16: "Ben Gamel",
                26: "Chris Herrmann",
                # Bullpen
                52: "Nick Rumbelow",
                48: "Alex Colomé",
                8: "Mike Leake",
                60: "Chasen Bradford",
                65: "James Paxton",
                47: "James Pazos",
                50: "Nick Vincent",
                12: "Juan Nicasio",
                39: "Edwin Díaz",
                55: "Roenis Elías",
                32: "Marco Gonzales",
                34: "Félix Hernández",
            },
            "lefties": [49, 65, 47, 55, 32],
            "lineup": [
                [9, "4"],
                [17, "9"],
                [4, "7"],
                [23, "0"],
                [15, "5"],
                [27, "3"],
                [3, "2"],
                [5, "8"],
                [7, "6"],
            ],
            "bench": [
                [2, "2B"],
                [16, "RF"],
                [26, "C"],
            ],
            "bullpen": [52, 48, 8, 60, 65, 47, 50, 12, 39, 55, 32, 34],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 35,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                12: "Brock Holt",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                23: "Blake Swihart",
                # Starting pitcher
                35: "Steven Wright",
                # Bench
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 63, 24],
            "lineup": [
                [50, "9"],
                [16, "8"],
                [28, "7"],
                [18, "3"],
                [2, "6"],
                [12, "4"],
                [11, "5"],
                [7, "2"],
                [23, "0"],
            ],
            "bench": [
                [36, "SS"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [57, 44, 22, 41, 61, 37, 63, 24, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "Mike Estabrook",
            "1B": "Alfonso Márquez",
            "2B": "Bruce Dreckman",
            "3B": "Chad Fairchild",
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
# Pitching: BOS #35 Steven Wright
t1 = game.new_inning()

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
t1.new_ab()
t1.hit(1)
t1.advance(2, "4 1B")
t1.advance(4, "23 HR")

# 2. SEA #17 Mitch Haniger (X - X - 9)
t1.new_ab()
t1.pitch_list("b 1 f c s")
t1.out("K")

# 3. SEA #4  Denard Span (X - X - 9)
t1.new_ab()
t1.pitch_list("c 1 1")
t1.hit(1)
t1.advance(4, "23 HR")

# 4. SEA #23 Nelson Cruz (X - 9 - 4)
t1.new_ab()
t1.hit(4, rbis=3)

# 5. SEA #15 Kyle Seager (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G1-3")

# 6. SEA #27 Ryon Healy (X - X - X)
t1.new_ab()
t1.hit(4)

# 7. SEA #3  Mike Zunino (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.out("G5-3")


# Bot 1st
# Pitching: SEA #49 Wade LeBlanc
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.advance(2, "16 1B")
b1.advance(4, "28 2B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.hit(1)
b1.advance(3, "28 2B")
b1.advance(4, "18 1B")

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
b1.new_ab()
b1.hit(2, rbis=1)
b1.advance(3, "18 1B")
b1.advance(4, "12 2B")

# 4. BOS #18 Mitch Moreland (16 - 28 - X)
b1.new_ab()
b1.pitch_list("b f b")
b1.hit(1, rbis=1)
b1.advance(3, "12 2B")
b1.advance(4, "11 G4-3")

# 5. BOS #2  Xander Bogaerts (28 - X - 18)
b1.new_ab()
b1.pitch_list("b s f b s")
b1.out("K")

# 6. BOS #12 Brock Holt (28 - X - 18)
b1.new_ab()
b1.pitch_list("b")
b1.hit(2, rbis=1)
b1.advance(3, "11 G4-3")
b1.advance(4, "7 2B")

# 7. BOS #11 Rafael Devers (18 - 12 - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G4-3", rbis=1)

# 8. BOS #7  Christian Vázquez (12 - X - X)
b1.new_ab()
b1.pitch_list("d d s b")
b1.hit(2, rbis=1)

# 9. BOS #23 Blake Swihart (X - 7 - X)
b1.new_ab()
b1.pitch_list("c s")
b1.out("L7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #35 Steven Wright
t2 = game.new_inning()

# 8. SEA #5  Guillermo Heredia (X - X - X)
t2.new_ab()
t2.out("G1-3")

# 9. SEA #7  Andrew Romine (X - X - X)
t2.new_ab()
t2.pitch_list("c b c f")
t2.hit(1)
t2.advance(2, "9 PB")
t2.advance(4, "17 1B")

# 1. SEA #9  Dee Strange-Gordon (X - X - 7)
t2.new_ab()
t2.pitch_list("b f b d b")
t2.pb()
t2.reach("BB")
t2.advance(2, "17 1B")
t2.advance(3, "4 FC4-6")
t2.advance(4, "23 1B")

# 2. SEA #17 Mitch Haniger (X - 7 - 9)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1, rbis=1)
t2.thrown_out(2, "4 FC4-6", 2, 35)

# 3. SEA #4  Denard Span (X - 9 - 17)
t2.new_ab()
t2.pitch_list("c")
t2.reach("FC4-6")
t2.advance(3, "23 1B")

# 4. SEA #23 Nelson Cruz (9 - X - 4)
t2.new_ab()
t2.pitch_list("s 1 b")
t2.hit(1, rbis=1)
t2.thrown_out(2, "15 FC6", 3, 35)

# 5. SEA #15 Kyle Seager (4 - X - 23)
t2.new_ab()
t2.pitch_list("c f")
t2.reach("FC6")


# Bot 2nd
# Pitching: SEA #49 Wade LeBlanc
b2 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b b")
b2.reach("BB")
b2.advance(3, "28 2B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b2.new_ab()
b2.pitch_list("b")
b2.out("F7")

# 3. BOS #28 J.D. Martinez (X - X - 50)
b2.new_ab()
b2.hit(2)

# 4. BOS #18 Mitch Moreland (50 - 28 - X)
b2.new_ab()
b2.pitch_list("b f b")
b2.out("L6")

# 5. BOS #2  Xander Bogaerts (50 - 28 - X)
b2.new_ab()
b2.pitch_list("b b c")
b2.out("L7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #35 Steven Wright
t3 = game.new_inning()

# 6. SEA #27 Ryon Healy (X - X - X)
t3.new_ab()
t3.pitch_list("c s s")
t3.out("K")

# 7. SEA #3  Mike Zunino (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("F8")

# 8. SEA #5  Guillermo Heredia (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("(F)P2")


# Bot 3rd
# Pitching: SEA #49 Wade LeBlanc
b3 = game.new_inning()

# 6. BOS #12 Brock Holt (X - X - X)
b3.new_ab()
b3.pitch_list("c c s")
b3.out("K2-3")

# 7. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.out("F7")

# 8. BOS #7  Christian Vázquez (X - X - X)
b3.new_ab()
b3.pitch_list("c b b")
b3.hit(1)
b3.thrown_out(2, "7-4", 3, 49)


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #35 Steven Wright
t4 = game.new_inning()

# 9. SEA #7  Andrew Romine (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.hit(1)
t4.advance(2, "17 PB")
t4.advance(4, "4 2B")

# 1. SEA #9  Dee Strange-Gordon (X - X - 7)
t4.new_ab()
t4.pitch_list("b")
t4.out("F7")

# 2. SEA #17 Mitch Haniger (X - X - 7)
t4.new_ab()
t4.pitch_list("b c b 1 b b")
t4.pb()
t4.reach("BB")
t4.advance(3, "4 2B")
t4.advance(4, "23 HR")

# 3. SEA #4  Denard Span (X - 7 - 17)
t4.new_ab()
t4.hit(2, rbis=1)
t4.advance(4, "23 HR")

# 4. SEA #23 Nelson Cruz (17 - 4 - X)
t4.new_ab()
t4.pitch_list("f b b f f")
t4.hit(4, rbis=3)

# Pitching change (BOS): #61 Brian Johnson replaces #35 Steven Wright
t4.pitching_substitution(61)

# 5. SEA #15 Kyle Seager (X - X - X)
t4.new_ab()
t4.pitch_list("b b c f f s")
t4.out("K")

# 6. SEA #27 Ryon Healy (X - X - X)
t4.new_ab()
t4.pitch_list("b c b")
t4.out("F8")


# Bot 4th
# Pitching: SEA #49 Wade LeBlanc
b4 = game.new_inning()

# 9. BOS #23 Blake Swihart (X - X - X)
b4.new_ab()
b4.pitch_list("f f")
b4.out("P6")

# 1. BOS #50 Mookie Betts (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.out("G3-1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #61 Brian Johnson
t5 = game.new_inning()

# 7. SEA #3  Mike Zunino (X - X - X)
t5.new_ab()
t5.pitch_list("s c b b f s")
t5.out("K")

# 8. SEA #5  Guillermo Heredia (X - X - X)
t5.new_ab()
t5.pitch_list("c f b f s")
t5.out("K")

# 9. SEA #7  Andrew Romine (X - X - X)
t5.new_ab()
t5.hit(1)
t5.advance(2, "9 1B")
t5.advance(3, "17 1B")

# 1. SEA #9  Dee Strange-Gordon (X - X - 7)
t5.new_ab()
t5.pitch_list("f s")
t5.hit(1)
t5.advance(2, "17 1B")

# 2. SEA #17 Mitch Haniger (X - 7 - 9)
t5.new_ab()
t5.pitch_list("c b c b")
t5.hit(1)

# 3. SEA #4  Denard Span (7 - 9 - 17)
t5.new_ab()
t5.pitch_list("f")
t5.out("F7")


# Bot 5th
# Pitching: SEA #49 Wade LeBlanc
b5 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("c s b f")
b5.out("L9")

# 4. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("c b b")
b5.hit(1)
b5.advance(3, "12 1B")
b5.advance(4, "11 1B")

# 5. BOS #2  Xander Bogaerts (X - X - 18)
b5.new_ab()
b5.pitch_list("f b d f b")
b5.out("F9")

# 6. BOS #12 Brock Holt (X - X - 18)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(2, "11 1B")

# 7. BOS #11 Rafael Devers (18 - X - 12)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1, rbis=1)

# Pitching change (SEA): #47 James Pazos replaces #49 Wade LeBlanc
b5.pitching_substitution(47)

# 8. BOS #7  Christian Vázquez (X - 12 - 11)
b5.new_ab()
b5.pitch_list("b b c f b f f f")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #61 Brian Johnson
t6 = game.new_inning()

# 4. SEA #23 Nelson Cruz (X - X - X)
t6.new_ab()
t6.pitch_list("c b b s b")
t6.hit(1)
t6.thrown_out(2, "27 DP4-6-3", 2, 61)

# 5. SEA #15 Kyle Seager (X - X - 23)
t6.new_ab()
t6.pitch_list("f")
t6.out("P5")

# 6. SEA #27 Ryon Healy (X - X - 23)
t6.new_ab()
t6.pitch_list("c s")
t6.out("DP4-6-3")


# Bot 6th
# Pitching: SEA #47 James Pazos
b6 = game.new_inning()

# 9. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.pitch_list("b b f b f")
b6.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("P4")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.advance(4, "28 HR")

# Pitching change (SEA): #50 Nick Vincent replaces #47 James Pazos
b6.pitching_substitution(50)

# 3. BOS #28 J.D. Martinez (X - X - 16)
b6.new_ab()
b6.pitch_list("b f f")
b6.hit(4, rbis=2)

# 4. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.hit(3)
b6.advance(4, "2 1B")

# 5. BOS #2  Xander Bogaerts (18 - X - X)
b6.new_ab()
b6.pitch_list("c f f")
b6.hit(1, rbis=1)
b6.advance(2, "12 SB")

# 6. BOS #12 Brock Holt (X - X - 2)
b6.new_ab()
b6.pitch_list("c b c f f f b f")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Matt Barnes
t7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #61 Brian Johnson
t7.pitching_substitution(32)

# 7. SEA #3  Mike Zunino (X - X - X)
t7.new_ab()
t7.pitch_list("c b s b s")
t7.out("K")

# 8. SEA #5  Guillermo Heredia (X - X - X)
t7.new_ab()
t7.pitch_list("b b c f c")
t7.out("!K")

# 9. SEA #7  Andrew Romine (X - X - X)
t7.new_ab()
t7.pitch_list("c f f s")
t7.out("K2-3")


# Bot 7th
# Pitching: SEA #12 Juan Nicasio
b7 = game.new_inning()

# Pitching change (SEA): #12 Juan Nicasio replaces #50 Nick Vincent
b7.pitching_substitution(12)

# 7. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.hit(1)
b7.advance(2, "23 1B")
b7.advance(3, "50 BB")
b7.advance(4, "16 1B")

# 8. BOS #7  Christian Vázquez (X - X - 11)
b7.new_ab()
b7.pitch_list("1 c c f b 1 c")
b7.out("!K")

# 9. BOS #23 Blake Swihart (X - X - 11)
b7.new_ab()
b7.pitch_list("1 d c")
b7.hit(1)
b7.advance(2, "50 BB")
b7.advance(3, "16 1B")
b7.advance(4, "28 1B")

# 1. BOS #50 Mookie Betts (X - 11 - 23)
b7.new_ab()
b7.pitch_list("c b b b b")
b7.reach("BB")
b7.advance(2, "16 1B")
b7.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (11 - 23 - 50)
b7.new_ab()
b7.pitch_list("b f c")
b7.hit(1, rbis=1)
b7.advance(3, "28 1B")
b7.advance(4, "36 WP")

# 3. BOS #28 J.D. Martinez (23 - 50 - 16)
b7.new_ab()
b7.pitch_list("b b f f")
b7.hit(1, rbis=2)
b7.advance(2, "36 SB")
b7.advance(3, "36 WP")
b7.advance(4, "36 1B")

# Pitching change (SEA): #52 Nick Rumbelow replaces #12 Juan Nicasio
b7.pitching_substitution(52)

# 4. BOS #18 Mitch Moreland (16 - X - 28)
b7.new_ab()
b7.pitch_list("c f 1 p c")
b7.out("!K")

# Offensive change (BOS): Pinch-hitter #36 Eduardo Núñez replaces #2 Xander Bogaerts, batting 5th
b7.offensive_substitution(5, 36, "PH")

# 5. BOS #36 Eduardo Núñez (16 - X - 28)
b7.new_ab()
b7.pitch_list("f t 1 f 1 b b")
b7.wp()
b7.wp()
b7.hit(1, rbis=1)

# 6. BOS #12 Brock Holt (X - X - 36)
b7.new_ab()
b7.pitch_list("b f f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
t8.pitching_substitution(56)

# Defensive switch (BOS): #36 Eduardo Núñez moves to 2B
t8.defensive_switch(36, "4")

# Defensive switch (BOS): #12 Brock Holt moves to SS
t8.defensive_switch(12, "6")

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
t8.new_ab()
t8.pitch_list("c c b c")
t8.out("!K")

# 2. SEA #17 Mitch Haniger (X - X - X)
t8.new_ab()
t8.pitch_list("c b c b f b d")
t8.reach("BB")
t8.thrown_out(2, "4 DP3-6", 3, 56)

# 3. SEA #4  Denard Span (X - X - 17)
t8.new_ab()
t8.pitch_list("b")
t8.out("DP3-6")


# Bot 8th
# Pitching: SEA #55 Roenis Elías
b8 = game.new_inning()

# Pitching change (SEA): #55 Roenis Elías replaces #52 Nick Rumbelow
b8.pitching_substitution(55)

# 7. BOS #11 Rafael Devers (X - X - X)
b8.new_ab()
b8.hit(2)
b8.thrown_out(3, "7 FC6-5", 1, 55)

# 8. BOS #7  Christian Vázquez (X - 11 - X)
b8.new_ab()
b8.pitch_list("b f b b")
b8.reach("FC6-5")
b8.advance(2, "50 WP")

# 9. BOS #23 Blake Swihart (X - X - 7)
b8.new_ab()
b8.pitch_list("f f f f b b b f f")
b8.out("F7")

# 1. BOS #50 Mookie Betts (X - X - 7)
b8.new_ab()
b8.pitch_list("b c b")
b8.wp()
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
t9.pitching_substitution(46)

# 4. SEA #23 Nelson Cruz (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("P3")

# 5. SEA #15 Kyle Seager (X - X - X)
t9.new_ab()
t9.pitch_list("c f f b s")
t9.out("K")

# 6. SEA #27 Ryon Healy (X - X - X)
t9.new_ab()
t9.pitch_list("c b f")
t9.out("L8")

# Winning team: BOS
# WP: BOS #32 Matt Barnes
game.winning_pitcher(32)

# Loser team: SEA
# LP: SEA #12 Juan Nicasio
game.losing_pitcher(12, is_away_team=True)

# print(game)
game.generate_scorecard()
