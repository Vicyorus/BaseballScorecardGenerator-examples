import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-05-22
# https://www.baseball-reference.com/boxes/TBA/TBA201805220.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/05/22/530119/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-22 19:10-22:05",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "10,642",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 31, 61, 66, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 22, 31, 61, 66, 37, 24, 46, 56, 32],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 34,
            "roster": {
                # Lineup
                28: "Daniel Robertson",
                44: "C.J. Cron",
                5: "Matt Duffy",
                40: "Wilson Ramos",
                1: "Willy Adames",
                10: "Johnny Field",
                21: "Christian Arroyo",
                8: "Rob Refsnyder",
                0: "Mallex Smith",
                # Starting pitcher
                34: "Jake Faria",
                # Bench
                13: "Brad Miller",
                2: "Denard Span",
                45: "Jesús Sucre",
                # Bullpen
                49: "Jonny Venters",
                37: "Alex Colomé",
                46: "José Alvarado",
                48: "Ryan Yarbrough",
                53: "Anthony Banda",
                52: "Chaz Roe",
                50: "Austin Pruitt",
                55: "Ryne Stanek",
                4: "Blake Snell",
                35: "Matt Andriese",
                22: "Chris Archer",
                54: "Sergio Romo",
            },
            "lefties": [49, 46, 48, 53, 4],
            "lineup": [
                [28, "4"],
                [44, "3"],
                [5, "0"],
                [40, "2"],
                [1, "6"],
                [10, "9"],
                [21, "5"],
                [8, "7"],
                [0, "8"],
            ],
            "bench": [
                [13, "DH"],
                [2, "CF"],
                [45, "C"],
            ],
            "bullpen": [49, 37, 46, 48, 53, 52, 50, 55, 4, 35, 22, 54],
        },
        "umpires": {
            "HP": "Adam Hamari",
            "1B": "Dan Bellino",
            "2B": "Tom Hallion",
            "3B": "Phil Cuzzi",
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
# Pitching: TBR #34 Jake Faria
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b c b")
t1.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b s f c")
t1.out("!K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.out("P3")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. TBR #28 Daniel Robertson (X - X - X)
b1.new_ab()
b1.out("P3")

# 2. TBR #44 C.J. Cron (X - X - X)
b1.new_ab()
b1.pitch_list("c c s")
b1.out("K")

# 3. TBR #5  Matt Duffy (X - X - X)
b1.new_ab()
b1.pitch_list("c c b b b b")
b1.reach("BB")
b1.advance(3, "40 1B")

# 4. TBR #40 Wilson Ramos (X - X - 5)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)

# 5. TBR #1  Willy Adames (5 - X - 40)
b1.new_ab()
b1.pitch_list("c b t f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #34 Jake Faria
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("f b s")
t2.hit(1)
t2.thrown_out(2, "2 DP6-4-3", 1, 34)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t2.new_ab()
t2.pitch_list("c b")
t2.out("DP6-4-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("f b f")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 6. TBR #10 Johnny Field (X - X - X)
b2.new_ab()
b2.pitch_list("b s b b")
b2.hit(1)

# 7. TBR #21 Christian Arroyo (X - X - 10)
b2.new_ab()
b2.pitch_list("c b f s")
b2.out("K")

# 8. TBR #8  Rob Refsnyder (X - X - 10)
b2.new_ab()
b2.pitch_list("c")
b2.out("F9")

# 9. TBR #0  Mallex Smith (X - X - 10)
b2.new_ab()
b2.pitch_list("1")
b2.out("L1")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #34 Jake Faria
t3 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t3.new_ab()
t3.out("(F)P3")

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("b b f b b")
t3.reach("BB")
t3.advance(2, "19 1B")
t3.advance(4, "50 HR")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t3.new_ab()
t3.hit(1)
t3.advance(4, "50 HR")

# 1. BOS #50 Mookie Betts (X - 3 - 19)
t3.new_ab()
t3.pitch_list("f c d b d")
t3.hit(4, rbis=3)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("b c f b t")
t3.out("KT")

# Pitching change (TBR): #50 Austin Pruitt replaces #34 Jake Faria
t3.pitching_substitution(50)

# 3. BOS #13 Hanley Ramirez (X - X - X)
t3.new_ab()
t3.pitch_list("c f b f b b b")
t3.reach("BB")
t3.advance(2, "28 BB")
t3.advance(3, "2 HBP")

# 4. BOS #28 J.D. Martinez (X - X - 13)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(2, "2 HBP")

# Defensive change (TBR): #45 Jesús Sucre replaces #40 Wilson Ramos (C), playing C, batting 4th
t3.defensive_substitution(4, 45, "2")

# 5. BOS #2  Xander Bogaerts (X - 13 - 28)
t3.new_ab()
t3.pitch_list("c c d f")
t3.reach("HBP")

# 6. BOS #11 Rafael Devers (13 - 28 - 2)
t3.new_ab()
t3.pitch_list("f c")
t3.out("F8")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 1. TBR #28 Daniel Robertson (X - X - X)
b3.new_ab()
b3.pitch_list("c f f")
b3.reach("HBP")
b3.thrown_out(2, "44 DP8-6-3", 2, 41)

# 2. TBR #44 C.J. Cron (X - X - 28)
b3.new_ab()
b3.pitch_list("c")
b3.out("DP8-6-3")

# 3. TBR #5  Matt Duffy (X - X - X)
b3.new_ab()
b3.pitch_list("b c b")
b3.out("G1-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #50 Austin Pruitt
t4 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("F7")

# 8. BOS #3  Sandy León (X - X - X)
t4.new_ab()
t4.pitch_list("b s c b c")
t4.out("!K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 19)
t4.new_ab()
t4.pitch_list("c d 1 b")
t4.out("L8")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 4. TBR #45 Jesús Sucre (X - X - X)
b4.new_ab()
b4.pitch_list("b c s b s")
b4.out("K")

# 5. TBR #1  Willy Adames (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(4, rbis=1)

# 6. TBR #10 Johnny Field (X - X - X)
b4.new_ab()
b4.pitch_list("b c s b b")
b4.out("L3")

# 7. TBR #21 Christian Arroyo (X - X - X)
b4.new_ab()
b4.pitch_list("c f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #50 Austin Pruitt
t5 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.out("F7")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t5.new_ab()
t5.pitch_list("c c b")
t5.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.pitch_list("f f b")
t5.out("F9")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 8. TBR #8  Rob Refsnyder (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(2)
b5.advance(3, "28 PB")
b5.advance("U", "28 SF7")

# 9. TBR #0  Mallex Smith (X - 8 - X)
b5.new_ab()
b5.pitch_list("c b b")
b5.out("B5")

# 1. TBR #28 Daniel Robertson (X - 8 - X)
b5.new_ab()
b5.pitch_list("b b c")
b5.pb()
b5.out("SF7", rbis=1)

# 2. TBR #44 C.J. Cron (X - X - X)
b5.new_ab()
b5.pitch_list("c b b s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #50 Austin Pruitt
t6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("F9")

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("b b f b f")
t6.hit(4, rbis=1)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("b f")
t6.out("G6-3")

# 8. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("b f s c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 3. TBR #5  Matt Duffy (X - X - X)
b6.new_ab()
b6.pitch_list("c f b")
b6.out("G5-3")

# 4. TBR #45 Jesús Sucre (X - X - X)
b6.new_ab()
b6.pitch_list("b c s b")
b6.out("G6-3")

# 5. TBR #1  Willy Adames (X - X - X)
b6.new_ab()
b6.pitch_list("c s s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #50 Austin Pruitt
t7 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c")
t7.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.thrown_out(2, "16 DP4-6-3", 2, 50)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t7.new_ab()
t7.pitch_list("b 1 1 c b f 1")
t7.out("DP4-6-3")


# Bot 7th
# Pitching: BOS #41 Chris Sale
b7 = game.new_inning()

# 6. TBR #10 Johnny Field (X - X - X)
b7.new_ab()
b7.out("G1-3")

# 7. TBR #21 Christian Arroyo (X - X - X)
b7.new_ab()
b7.pitch_list("c c b b b c")
b7.out("!K")

# 8. TBR #8  Rob Refsnyder (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c b")
b7.reach("BB")

# 9. TBR #0  Mallex Smith (X - X - 8)
b7.new_ab()
b7.pitch_list("c f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #50 Austin Pruitt
t8 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
t8.new_ab()
t8.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("c b s b")
t8.out("P4")


# Bot 8th
# Pitching: BOS #41 Chris Sale
b8 = game.new_inning()

# 1. TBR #28 Daniel Robertson (X - X - X)
b8.new_ab()
b8.pitch_list("c b c b")
b8.out("G6-3")

# 2. TBR #44 C.J. Cron (X - X - X)
b8.new_ab()
b8.pitch_list("c b b b c f f f")
b8.out("P5")

# Pitching change (BOS): #56 Joe Kelly replaces #41 Chris Sale
b8.pitching_substitution(56)

# 3. TBR #5  Matt Duffy (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b c c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #55 Ryne Stanek
t9 = game.new_inning()

# Pitching change (TBR): #55 Ryne Stanek replaces #50 Austin Pruitt
t9.pitching_substitution(55)

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b b")
t9.reach("BB")
t9.thrown_out(2, "36 DP6-4-3", 1, 55)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t9.new_ab()
t9.pitch_list("b b t")
t9.out("DP6-4-3")

# 8. BOS #3  Sandy León (X - X - X)
t9.new_ab()
t9.pitch_list("b c b b")
t9.hit(1)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t9.new_ab()
t9.pitch_list("c s b b b c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
b9.pitching_substitution(46)

# 4. TBR #45 Jesús Sucre (X - X - X)
b9.new_ab()
b9.pitch_list("c b s f b f b")
b9.hit(1)
b9.advance(3, "13 2B")

# 5. TBR #1  Willy Adames (X - X - 45)
b9.new_ab()
b9.pitch_list("b s f b b f f s")
b9.out("K")

# Offensive change (TBR): Pinch-hitter #2 Denard Span replaces #10 Johnny Field, batting 6th
b9.offensive_substitution(6, 2, "PH")

# 6. TBR #2  Denard Span (X - X - 45)
b9.new_ab()
b9.pitch_list("f s b")
b9.out("(F)P2")

# Offensive change (TBR): Pinch-hitter #13 Brad Miller replaces #21 Christian Arroyo, batting 7th
b9.offensive_substitution(7, 13, "PH")

# 7. TBR #13 Brad Miller (X - X - 45)
b9.new_ab()
b9.pitch_list("c")
b9.hit(2)

# 8. TBR #8  Rob Refsnyder (45 - 13 - X)
b9.new_ab()
b9.pitch_list("b b s d b")
b9.reach("BB")
b9.thrown_out(2, "0 FC6-4", 3, 46)

# 9. TBR #0  Mallex Smith (45 - 13 - 8)
b9.new_ab()
b9.pitch_list("f b b f")
b9.reach("FC6-4")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: TBR
# LP: TBR #34 Jake Faria
game.losing_pitcher(34)

# print(game)
game.generate_scorecard()
