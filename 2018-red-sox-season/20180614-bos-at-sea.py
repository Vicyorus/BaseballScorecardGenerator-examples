import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-06-14
# https://www.baseball-reference.com/boxes/SEA/SEA201806140.shtml
# https://www.mlb.com/gameday/red-sox-vs-mariners/2018/06/14/530426/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-14 22:10-01:06 +1",
        "at": "Safeco Field, Seattle, WA",
        "att": "30,479",
        "temp": "64F, Cloudy",
        "wind": "2mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Starting pitcher
                24: "David Price",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [7, "2"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 35, 44, 22, 41, 61, 37, 46, 76, 65, 56, 32],
        },
        "home": {
            "team": "Seattle Mariners",
            "starter": 34,
            "roster": {
                # Lineup
                9: "Dee Strange-Gordon",
                2: "Jean Segura",
                17: "Mitch Haniger",
                23: "Nelson Cruz",
                15: "Kyle Seager",
                27: "Ryon Healy",
                5: "Guillermo Heredia",
                4: "Denard Span",
                3: "Mike Zunino",
                # Starting pitcher
                34: "Félix Hernández",
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
                49: "Wade LeBlanc",
                39: "Edwin Díaz",
                55: "Roenis Elías",
                32: "Marco Gonzales",
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
                [4, "7"],
                [3, "2"],
            ],
            "bench": [
                [16, "RF"],
                [36, "C"],
                [7, "SS"],
            ],
            "bullpen": [52, 48, 8, 60, 65, 47, 46, 63, 49, 39, 55, 32],
        },
        "umpires": {
            "HP": "Tony Randazzo",
            "1B": "Bill Welke",
            "2B": "Lance Barrett",
            "3B": "Vic Carapazza",
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
# Pitching: SEA #34 Félix Hernández
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b b")
t1.out("F7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("f f")
t1.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c")
t1.hit(1)

# 4. BOS #18 Mitch Moreland (X - X - 28)
t1.new_ab()
t1.pitch_list("b c")
t1.out("F8")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b1.new_ab()
b1.pitch_list("f")
b1.out("L7")

# 2. SEA #2  Jean Segura (X - X - X)
b1.new_ab()
b1.pitch_list("c b c f b b t")
b1.out("KT")

# 3. SEA #17 Mitch Haniger (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)

# 4. SEA #23 Nelson Cruz (X - X - 17)
b1.new_ab()
b1.pitch_list("f c b")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SEA #34 Félix Hernández
t2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("b b c s f b s")
t2.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("b s b b")
t2.error(9)
t2.reach("E9")
t2.advance(2, "36 SB")
t2.advance(3, "19 2B")
t2.advance("U", "19 2B")

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t2.new_ab()
t2.pitch_list("s d c s")
t2.out("K")

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - X)
t2.new_ab()
t2.pitch_list("b f d b")
t2.hit(2, rbis=1)

# 9. BOS #7  Christian Vázquez (X - 19 - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 5. SEA #15 Kyle Seager (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.out("F9")

# 6. SEA #27 Ryon Healy (X - X - X)
b2.new_ab()
b2.pitch_list("c b f")
b2.out("G6-3")

# 7. SEA #5  Guillermo Heredia (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b")
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SEA #34 Félix Hernández
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b c")
t3.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("c b s s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 8. SEA #4  Denard Span (X - X - X)
b3.new_ab()
b3.pitch_list("c b f f t")
b3.out("KT")

# 9. SEA #3  Mike Zunino (X - X - X)
b3.new_ab()
b3.pitch_list("f f")
b3.out("F9")

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b3.new_ab()
b3.pitch_list("f b")
b3.hit(1)
b3.thrown_out(2, "2 POCS", 3, 24)

# 2. SEA #2  Jean Segura (X - X - 9)
b3.new_ab()
b3.pitch_list("f n 1")
b3.no_ab("POCS")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SEA #34 Félix Hernández
t4 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("F9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("c b s s")
t4.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("c b f b")
t4.hit(2)

# 7. BOS #36 Eduardo Núñez (X - 11 - X)
t4.new_ab()
t4.out("G5-3")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 2. SEA #2  Jean Segura (X - X - X)
b4.new_ab()
b4.pitch_list("s f c")
b4.out("!K")

# 3. SEA #17 Mitch Haniger (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c")
b4.out("F9")

# 4. SEA #23 Nelson Cruz (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SEA #34 Félix Hernández
t5 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.out("G6-3")

# 9. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("b b f c f f b f")
t5.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 7)
t5.new_ab()
t5.pitch_list("c f d 1 s")
t5.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - 7)
t5.new_ab()
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# 5. SEA #15 Kyle Seager (X - X - X)
b5.new_ab()
b5.pitch_list("f b c")
b5.hit(1)
b5.advance(2, "27 1B")
b5.advance(3, "5 SB")
b5.advance(4, "5 SF7")

# 6. SEA #27 Ryon Healy (X - X - 15)
b5.new_ab()
b5.pitch_list("s")
b5.hit(1)

# 7. SEA #5  Guillermo Heredia (X - 15 - 27)
b5.new_ab()
b5.pitch_list("b")
b5.out("SF7", rbis=1)

# 8. SEA #4  Denard Span (X - X - 27)
b5.new_ab()
b5.pitch_list("c b f t")
b5.out("KT")

# 9. SEA #3  Mike Zunino (X - X - 27)
b5.new_ab()
b5.pitch_list("b f f d f f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SEA #34 Félix Hernández
t6 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("f b b")
t6.hit(1)
t6.thrown_out(2, "18 DP6-3", 1, 34)

# 4. BOS #18 Mitch Moreland (X - X - 28)
t6.new_ab()
t6.pitch_list("b")
t6.out("DP6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("s s f b b f")
t6.hit(4, rbis=1)

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G3")


# Bot 6th
# Pitching: BOS #24 David Price
b6 = game.new_inning()

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.reach("HBP")
b6.thrown_out(2, "2 DP6-3", 1, 24)

# 2. SEA #2  Jean Segura (X - X - 9)
b6.new_ab()
b6.pitch_list("f 1 b f b f 1 1 f b f f f")
b6.out("DP6-3")

# 3. SEA #17 Mitch Haniger (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SEA #34 Félix Hernández
t7 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G6-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b b b d")
t7.reach("BB")
t7.advance(2, "7 1B")

# 9. BOS #7  Christian Vázquez (X - X - 19)
t7.new_ab()
t7.pitch_list("1 p 1 c f")
t7.hit(1)
t7.thrown_out(2, "50 DP5-4-3", 2, 34)

# 1. BOS #50 Mookie Betts (X - 19 - 7)
t7.new_ab()
t7.out("DP5-4-3")


# Bot 7th
# Pitching: BOS #24 David Price
b7 = game.new_inning()

# 4. SEA #23 Nelson Cruz (X - X - X)
b7.new_ab()
b7.pitch_list("c b b s f f")
b7.out("(F)P2")

# 5. SEA #15 Kyle Seager (X - X - X)
b7.new_ab()
b7.pitch_list("c f s")
b7.out("K")

# 6. SEA #27 Ryon Healy (X - X - X)
b7.new_ab()
b7.pitch_list("b b c")
b7.hit(1)

# 7. SEA #5  Guillermo Heredia (X - X - 27)
b7.new_ab()
b7.pitch_list("b s b f c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SEA #47 James Pazos
t8 = game.new_inning()

# Pitching change (SEA): #47 James Pazos replaces #34 Félix Hernández
t8.pitching_substitution(47)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("s")
t8.out("L7")

# 3. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b s b")
t8.reach("BB")
t8.advance(3, "2 1B")

# 4. BOS #18 Mitch Moreland (X - X - 28)
t8.new_ab()
t8.pitch_list("c b f")
t8.out("L8")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)

# 6. BOS #11 Rafael Devers (28 - X - 2)
t8.new_ab()
t8.pitch_list("f b b 1")
t8.out("(F)P5")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #24 David Price
b8.pitching_substitution(56)

# 8. SEA #4  Denard Span (X - X - X)
b8.new_ab()
b8.out("F7")

# 9. SEA #3  Mike Zunino (X - X - X)
b8.new_ab()
b8.pitch_list("c c b f b b s")
b8.out("K")

# 1. SEA #9  Dee Strange-Gordon (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.hit(1)
b8.thrown_out(2, "2 FC6-4", 3, 56)

# 2. SEA #2  Jean Segura (X - X - 9)
b8.new_ab()
b8.reach("FC6-4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SEA #52 Nick Rumbelow
t9 = game.new_inning()

# Pitching change (SEA): #52 Nick Rumbelow replaces #47 James Pazos
t9.pitching_substitution(52)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.out("G6-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("f b f")
t9.out("F9")

# 9. BOS #7  Christian Vázquez (X - X - X)
t9.new_ab()
t9.pitch_list("c f b b f t")
t9.out("KT")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
b9.pitching_substitution(46)

# 3. SEA #17 Mitch Haniger (X - X - X)
b9.new_ab()
b9.pitch_list("b b b d")
b9.reach("BB")
b9.advance(2, "23 WP")

# 4. SEA #23 Nelson Cruz (X - X - 17)
b9.new_ab()
b9.pitch_list("s d b s b d")
b9.wp()
b9.reach("BB")
# Offensive change (SEA): Pinch-runner #7 Andrew Romine replaces #23 Nelson Cruz
b9.offensive_substitution(4, 7, "PR")
b9.atbase("PR")
b9.thrown_out(2, "27 DP6-4-3", 2, 46)

# 5. SEA #15 Kyle Seager (X - 17 - 23)
b9.new_ab()
b9.pitch_list("c s c")
b9.out("!K")

# 6. SEA #27 Ryon Healy (X - 17 - 7)
b9.new_ab()
b9.pitch_list("b t")
b9.out("DP6-4-3")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: SEA
# LP: SEA #34 Félix Hernández
game.losing_pitcher(34)

# print(game)
game.generate_scorecard()
