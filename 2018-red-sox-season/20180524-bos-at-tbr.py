import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-05-24
# https://www.baseball-reference.com/boxes/TBA/TBA201805240.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/05/24/530147/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-24 19:10-22:08",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "12,468",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 24],
            "lineup": [
                [50, "9"],
                [13, "0"],
                [28, "7"],
                [18, "3"],
                [2, "6"],
                [36, "4"],
                [11, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [16, "LF"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 41, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 4,
            "roster": {
                # Lineup
                2: "Denard Span",
                44: "C.J. Cron",
                5: "Matt Duffy",
                40: "Wilson Ramos",
                13: "Brad Miller",
                28: "Daniel Robertson",
                0: "Mallex Smith",
                10: "Johnny Field",
                1: "Willy Adames",
                # Starting pitcher
                4: "Blake Snell",
                # Bench
                8: "Rob Refsnyder",
                21: "Christian Arroyo",
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
                38: "Vidal Nuño",
                35: "Matt Andriese",
                22: "Chris Archer",
                54: "Sergio Romo",
            },
            "lefties": [4, 49, 46, 48, 53, 38],
            "lineup": [
                [2, "7"],
                [44, "0"],
                [5, "5"],
                [40, "2"],
                [13, "3"],
                [28, "4"],
                [0, "8"],
                [10, "9"],
                [1, "6"],
            ],
            "bench": [
                [8, "LF"],
                [21, "2B"],
                [45, "C"],
            ],
            "bullpen": [49, 37, 46, 48, 53, 52, 50, 55, 38, 35, 22, 54],
        },
        "umpires": {
            "HP": "Tom Hallion",
            "1B": "Phil Cuzzi",
            "2B": "Adam Hamari",
            "3B": "Dan Bellino",
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
# Pitching: TBR #4  Blake Snell
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c c s")
t1.out("K")

# 2. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("b f c f b b c")
t1.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.out("G4-3")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. TBR #2  Denard Span (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c")
b1.hit(2)
b1.advance(3, "5 1B")
b1.advance("U", "40 E2")

# 2. TBR #44 C.J. Cron (X - 2 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b f b b b")
b1.reach("BB")
b1.advance(2, "5 1B")
b1.advance(3, "40 E2")
b1.advance(4, "13 SF8")

# 3. TBR #5  Matt Duffy (X - 2 - 44)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.hit(1)
b1.advance(2, "40 E2")
b1.advance(3, "28 1B")
b1.thrown_out(4, "0 DP1-2-3", 2, 22)

# 4. TBR #40 Wilson Ramos (2 - 44 - 5)
b1.new_ab(is_risp=True)
b1.pitch_list("f f b f d b f f")
b1.error(2)
b1.reach("E2")
b1.advance(2, "28 1B")

# 5. TBR #13 Brad Miller (44 - 5 - 40)
b1.new_ab(is_risp=True)
b1.pitch_list("c f b f b b")
b1.out("SF8", rbis=1)

# 6. TBR #28 Daniel Robertson (X - 5 - 40)
b1.new_ab(is_risp=True)
b1.pitch_list("f b d")
b1.hit(1)

# 7. TBR #0  Mallex Smith (5 - 40 - 28)
b1.new_ab(is_risp=True)
b1.out("DP1-2-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #4  Blake Snell
t2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("b b f f b")
t2.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("b f f b f f")
t2.out("L4")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("s f c")
t2.out("!K")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 8. TBR #10 Johnny Field (X - X - X)
b2.new_ab()
b2.pitch_list("c c b b")
b2.out("G1-3")

# 9. TBR #1  Willy Adames (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(2, "2 BB")
b2.advance(3, "5 HBP")
b2.advance(4, "40 1B")

# 1. TBR #2  Denard Span (X - X - 1)
b2.new_ab()
b2.pitch_list("b d b b")
b2.reach("BB")
b2.advance(2, "5 HBP")
b2.advance(4, "40 1B")

# 2. TBR #44 C.J. Cron (X - 1 - 2)
b2.new_ab(is_risp=True)
b2.pitch_list("b c s f f s")
b2.out("K")

# 3. TBR #5  Matt Duffy (X - 1 - 2)
b2.new_ab(is_risp=True)
b2.pitch_list("b b s f")
b2.reach("HBP")
b2.error(9)
b2.advance(2, "40 1B")
b2.advance("U", "40 E9")

# 4. TBR #40 Wilson Ramos (1 - 2 - 5)
b2.new_ab(is_risp=True)
b2.pitch_list("b s s b b f")
b2.hit(1, rbis=2)

# 5. TBR #13 Brad Miller (X - X - 40)
b2.new_ab()
b2.out("P4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #4  Blake Snell
t3 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
t3.new_ab()
t3.pitch_list("c b c f b s")
t3.out("K")

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b")
t3.hit(1)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t3.new_ab()
t3.pitch_list("b s b b")
t3.out("F7")

# 1. BOS #50 Mookie Betts (X - X - 3)
t3.new_ab()
t3.out("L7")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 6. TBR #28 Daniel Robertson (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("G5-3")

# 7. TBR #0  Mallex Smith (X - X - X)
b3.new_ab()
b3.out("G4-3")

# 8. TBR #10 Johnny Field (X - X - X)
b3.new_ab()
b3.pitch_list("c b b s b f")
b3.out("P6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #4  Blake Snell
t4 = game.new_inning()

# 2. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("c b b f b f f")
t4.out("G6-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c c b s")
t4.out("K")

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("f b c b s")
t4.out("K")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 9. TBR #1  Willy Adames (X - X - X)
b4.new_ab()
b4.pitch_list("c c b f f")
b4.out("G3")

# 1. TBR #2  Denard Span (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b")
b4.hit(1)
b4.advance(2, "44 SB")
b4.advance(4, "5 1B")

# 2. TBR #44 C.J. Cron (X - X - 2)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b f s")
b4.out("K")

# 3. TBR #5  Matt Duffy (X - 2 - X)
b4.new_ab(is_risp=True)
b4.hit(1, rbis=1)
b4.advance(2, "40 1B")

# 4. TBR #40 Wilson Ramos (X - X - 5)
b4.new_ab()
b4.hit(1)

# Pitching change (BOS): #61 Brian Johnson replaces #22 Rick Porcello
b4.pitching_substitution(61)

# 5. TBR #13 Brad Miller (X - 5 - 40)
b4.new_ab(is_risp=True)
b4.pitch_list("f b f d s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #4  Blake Snell
t5 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")
t5.thrown_out(2, "36 DP5-4-3", 1, 4)

# 6. BOS #36 Eduardo Núñez (X - X - 2)
t5.new_ab()
t5.pitch_list("b b f f")
t5.out("DP5-4-3")

# 7. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("b c b f b f f b")
t5.reach("BB")
t5.advance(2, "3 1B")

# 8. BOS #3  Sandy León (X - X - 11)
t5.new_ab()
t5.pitch_list("b b c c f")
t5.hit(1)

# 9. BOS #19 Jackie Bradley Jr. (X - 11 - 3)
t5.new_ab(is_risp=True)
t5.pitch_list("f b c s")
t5.out("K")


# Bot 5th
# Pitching: BOS #61 Brian Johnson
b5 = game.new_inning()

# 6. TBR #28 Daniel Robertson (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("L8")

# 7. TBR #0  Mallex Smith (X - X - X)
b5.new_ab()
b5.pitch_list("c c b f b f f")
b5.hit(1)
b5.advance(2, "10 SB")

# 8. TBR #10 Johnny Field (X - X - 0)
b5.new_ab(is_risp=True)
b5.pitch_list("c b 1 b f s")
b5.out("K")

# 9. TBR #1  Willy Adames (X - 0 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c b")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #4  Blake Snell
t6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.hit(1)
t6.advance(2, "13 SB")

# 2. BOS #13 Hanley Ramirez (X - X - 50)
t6.new_ab()
t6.pitch_list("f f s")
t6.out("K")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("f f d")
t6.out("G5-3")

# 4. BOS #18 Mitch Moreland (X - 50 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b b")
t6.out("L5")


# Bot 6th
# Pitching: BOS #61 Brian Johnson
b6 = game.new_inning()

# 1. TBR #2  Denard Span (X - X - X)
b6.new_ab()
b6.pitch_list("c c b")
b6.out("G4-3")

# 2. TBR #44 C.J. Cron (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1)
b6.thrown_out(2, "5 FC5-4", 2, 61)

# 3. TBR #5  Matt Duffy (X - X - 44)
b6.new_ab()
b6.pitch_list("b")
b6.reach("FC5-4")
b6.advance(2, "40 1B")
b6.advance(3, "13 1B")
b6.thrown_out(4, "13 4-3-2", 3, 61)

# 4. TBR #40 Wilson Ramos (X - X - 5)
b6.new_ab()
b6.pitch_list("d s b")
b6.hit(1)
b6.advance(2, "13 4-3-2")

# 5. TBR #13 Brad Miller (X - 5 - 40)
b6.new_ab(is_risp=True)
b6.hit(1)


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #35 Matt Andriese
t7 = game.new_inning()

# Pitching change (TBR): #35 Matt Andriese replaces #4  Blake Snell
t7.pitching_substitution(35)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b c")
t7.out("G5-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(2)
t7.error(3)
t7.advance("U", "11 E3")

# 7. BOS #11 Rafael Devers (X - 36 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("f c b b")
t7.out("G5-3")

# 8. BOS #3  Sandy León (X - X - X)
t7.new_ab()
t7.pitch_list("b f s s")
t7.out("K")


# Bot 7th
# Pitching: BOS #76 Hector Velázquez
b7 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #61 Brian Johnson
b7.pitching_substitution(76)

# 6. TBR #28 Daniel Robertson (X - X - X)
b7.new_ab()
b7.pitch_list("c b c f f b b f d")
b7.reach("BB")
b7.thrown_out(2, "0 DP3-6-3", 1, 76)

# 7. TBR #0  Mallex Smith (X - X - 28)
b7.new_ab()
b7.pitch_list("s b")
b7.out("DP3-6-3")

# 8. TBR #10 Johnny Field (X - X - X)
b7.new_ab()
b7.pitch_list("s b")
b7.out("P3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #35 Matt Andriese
t8 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("s s b")
t8.out("F7")

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("f c")
t8.out("G6-3")

# 2. BOS #13 Hanley Ramirez (X - X - X)
t8.new_ab()
t8.pitch_list("f f b c")
t8.out("!K")


# Bot 8th
# Pitching: BOS #35 Steven Wright
b8 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #76 Hector Velázquez
b8.pitching_substitution(35)

# 9. TBR #1  Willy Adames (X - X - X)
b8.new_ab()
b8.pitch_list("c f")
b8.out("L9")

# 1. TBR #2  Denard Span (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b b")
b8.reach("BB")

# 2. TBR #44 C.J. Cron (X - X - 2)
b8.new_ab()
b8.pitch_list("f c f b 1")
b8.out("L8")

# 3. TBR #5  Matt Duffy (X - X - 2)
b8.new_ab()
b8.pitch_list("c f b b c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #35 Matt Andriese
t9 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.out("F9")

# 4. BOS #18 Mitch Moreland (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(4)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("c s s")
t9.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("c f b")
t9.hit(1)
t9.advance(2, "11 DI")
t9.advance(4, "11 2B")

# 7. BOS #11 Rafael Devers (X - X - 36)
t9.new_ab(is_risp=True)
t9.pitch_list("b f s f f")
t9.hit(2, rbis=1)

# Pitching change (TBR): #37 Alex Colomé replaces #35 Matt Andriese
t9.pitching_substitution(37)

# 8. BOS #3  Sandy León (X - 11 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.out("G3")

# Winning team: TBR
# WP: TBR #4 Blake Snell
game.winning_pitcher(4)
# SV: TBR #37 Alex Colomé
game.save_pitcher(37)

# Loser team: BOS
# LP: BOS #22 Rick Porcello
game.losing_pitcher(22, is_away_team=True)

# print(game)
game.generate_scorecard()
