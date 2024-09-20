import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TBA @ BOS, 2018-04-08
# https://www.baseball-reference.com/boxes/BOS/BOS201804080.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2018/04/08/529545/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-08 13:07-16:57",
        "at": "Fenway Park, Boston, MA",
        "att": "31,979",
        "temp": "38F, Cloudy",
        "wind": "15mph, In From CF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 36,
            "roster": {
                # Lineup
                5: "Matt Duffy",
                39: "Kevin Kiermaier",
                27: "Carlos Gómez",
                44: "C.J. Cron",
                28: "Daniel Robertson",
                13: "Brad Miller",
                45: "Jesús Sucre",
                11: "Adeiny Hechavarría",
                8: "Rob Refsnyder",
                # Starting pitcher
                36: "Andrew Kittredge",
                # Bench
                2: "Denard Span",
                18: "Joey Wendle",
                40: "Wilson Ramos",
                0: "Mallex Smith",
                # Bullpen
                37: "Alex Colomé",
                46: "José Alvarado",
                48: "Ryan Yarbrough",
                52: "Chaz Roe",
                50: "Austin Pruitt",
                34: "Jake Faria",
                4: "Blake Snell",
                72: "Yonny Chirinos",
                35: "Matt Andriese",
                22: "Chris Archer",
                54: "Sergio Romo",
            },
            "lefties": [46, 48, 4],
            "lineup": [
                [5, "5"],
                [39, "8"],
                [27, "9"],
                [44, "0"],
                [28, "4"],
                [13, "3"],
                [45, "2"],
                [11, "6"],
                [8, "7"],
            ],
            "bench": [
                [2, "CF"],
                [18, "2B"],
                [40, "C"],
                [0, "OF"],
            ],
            "bullpen": [37, 46, 48, 52, 50, 34, 4, 72, 35, 22, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 66, 24],
            "lineup": [
                [50, "9"],
                [16, "8"],
                [13, "0"],
                [28, "7"],
                [2, "6"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [7, "2"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [39, 22, 41, 61, 66, 37, 24, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "Bill Miller",
            "1B": "Angel Hernandez",
            "2B": "Todd Tichenor",
            "3B": "Alan Porter",
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
# Pitching: BOS #57 Eduardo Rodriguez
t1 = game.new_inning()

# 1. TBR #5  Matt Duffy (X - X - X)
t1.new_ab()
t1.pitch_list("c b b t b s")
t1.out("K")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
t1.new_ab()
t1.pitch_list("b b c f f c")
t1.out("!K")

# 3. TBR #27 Carlos Gómez (X - X - X)
t1.new_ab()
t1.pitch_list("b f b b f f f f s")
t1.out("K")


# Bot 1st
# Pitching: TBR #36 Andrew Kittredge
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(2)
b1.advance(3, "16 G4-3")
b1.advance(4, "13 G6-3")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G4-3")

# 3. BOS #13 Hanley Ramirez (50 - X - X)
b1.new_ab()
b1.pitch_list("f b b d f f")
b1.out("G6-3", rbis=1)

# 4. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("f f b")
b1.out("L9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 4. TBR #44 C.J. Cron (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c")
t2.hit(4)

# 5. TBR #28 Daniel Robertson (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b c")
t2.out("!K")

# 6. TBR #13 Brad Miller (X - X - X)
t2.new_ab()
t2.pitch_list("s f b b c")
t2.out("!K")

# 7. TBR #45 Jesús Sucre (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G6-3")


# Bot 2nd
# Pitching: TBR #36 Andrew Kittredge
b2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("c b f f")
b2.hit(1)

# 6. BOS #18 Mitch Moreland (X - X - 2)
b2.new_ab()
b2.out("F9")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
b2.new_ab()
b2.pitch_list("b b 1 b f c")
b2.out("F9")

# 8. BOS #11 Rafael Devers (X - X - 2)
b2.new_ab()
b2.pitch_list("s c b b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 8. TBR #11 Adeiny Hechavarría (X - X - X)
t3.new_ab()
t3.pitch_list("b s c f b f f")
t3.out("G3")

# 9. TBR #8  Rob Refsnyder (X - X - X)
t3.new_ab()
t3.pitch_list("f s b f f f b b b")
t3.reach("BB")
t3.advance(2, "5 1B")
t3.advance(4, "27 2B")

# 1. TBR #5  Matt Duffy (X - X - 8)
t3.new_ab()
t3.pitch_list("f b b")
t3.hit(1)
t3.advance(3, "27 2B")

# 2. TBR #39 Kevin Kiermaier (X - 8 - 5)
t3.new_ab()
t3.pitch_list("s s b b b s")
t3.out("K")

# 3. TBR #27 Carlos Gómez (X - 8 - 5)
t3.new_ab()
t3.pitch_list("f")
t3.hit(2, rbis=1)

# 4. TBR #44 C.J. Cron (5 - 27 - X)
t3.new_ab()
t3.pitch_list("f b b s f s")
t3.out("K")


# Bot 3rd
# Pitching: TBR #48 Ryan Yarbrough
b3 = game.new_inning()

# Pitching change (TBR): #48 Ryan Yarbrough replaces #36 Andrew Kittredge
b3.pitching_substitution(48)

# 9. BOS #7  Christian Vázquez (X - X - X)
b3.new_ab()
b3.pitch_list("b f c b")
b3.out("F7")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c b c b")
b3.out("G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("s b")
b3.out("L4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 5. TBR #28 Daniel Robertson (X - X - X)
t4.new_ab()
t4.pitch_list("f s f")
t4.hit(1)
t4.advance(2, "13 BB")
t4.advance(3, "45 G6-3")
t4.advance(4, "11 1B")

# 6. TBR #13 Brad Miller (X - X - 28)
t4.new_ab()
t4.pitch_list("b b b b")
t4.reach("BB")
t4.advance(2, "45 G6-3")
t4.advance(3, "5 1B")

# 7. TBR #45 Jesús Sucre (X - 28 - 13)
t4.new_ab()
t4.out("G6-3")

# 8. TBR #11 Adeiny Hechavarría (28 - 13 - X)
t4.new_ab()
t4.pitch_list("f b b")
t4.hit(1, rbis=1)
t4.advance(2, "5 1B")

# 9. TBR #8  Rob Refsnyder (X - 13 - 11)
t4.new_ab()
t4.pitch_list("b b b c s")
t4.out("L7")

# Pitching change (BOS): #76 Hector Velázquez replaces #57 Eduardo Rodriguez
t4.pitching_substitution(76)

# 1. TBR #5  Matt Duffy (X - 13 - 11)
t4.new_ab()
t4.pitch_list("s t")
t4.hit(1)

# 2. TBR #39 Kevin Kiermaier (13 - 11 - 5)
t4.new_ab()
t4.pitch_list("b b c b f f")
t4.out("F7")


# Bot 4th
# Pitching: TBR #48 Ryan Yarbrough
b4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f f f b f b")
b4.reach("BB")

# 4. BOS #28 J.D. Martinez (X - X - 13)
b4.new_ab()
b4.pitch_list("b b c")
b4.out("F9")

# 5. BOS #2  Xander Bogaerts (X - X - 13)
b4.new_ab()
b4.pitch_list("b b c c f")
b4.out("F9")

# 6. BOS #18 Mitch Moreland (X - X - 13)
b4.new_ab()
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #76 Hector Velázquez
t5 = game.new_inning()

# 3. TBR #27 Carlos Gómez (X - X - X)
t5.new_ab()
t5.out("P3")

# 4. TBR #44 C.J. Cron (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G5-3")

# 5. TBR #28 Daniel Robertson (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b")
t5.hit(1)
t5.advance(2, "13 SB")
t5.advance(4, "13 1B")

# 6. TBR #13 Brad Miller (X - X - 28)
t5.new_ab()
t5.pitch_list("c f b")
t5.hit(1, rbis=1)
t5.thrown_out(2, "45 FC4", 3, 76)

# 7. TBR #45 Jesús Sucre (X - X - 13)
t5.new_ab()
t5.pitch_list("c")
t5.reach("FC4")


# Bot 5th
# Pitching: TBR #48 Ryan Yarbrough
b5 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("b c s f b b b")
b5.reach("BB")
b5.advance(2, "7 1B")
b5.advance(3, "50 BB")
b5.advance(4, "13 1B")

# 8. BOS #11 Rafael Devers (X - X - 36)
b5.new_ab()
b5.pitch_list("b s c")
b5.out("P4")

# 9. BOS #7  Christian Vázquez (X - X - 36)
b5.new_ab()
b5.hit(1)
b5.advance(2, "50 BB")
b5.advance(3, "13 1B")

# 1. BOS #50 Mookie Betts (X - 36 - 7)
b5.new_ab()
b5.pitch_list("b b c b d")
b5.reach("BB")
b5.advance(2, "13 1B")

# 2. BOS #16 Andrew Benintendi (36 - 7 - 50)
b5.new_ab()
b5.pitch_list("b f b b f f c")
b5.out("!K")

# 3. BOS #13 Hanley Ramirez (36 - 7 - 50)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1, rbis=1)

# 4. BOS #28 J.D. Martinez (7 - 50 - 13)
b5.new_ab()
b5.pitch_list("f b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #76 Hector Velázquez
t6 = game.new_inning()

# 8. TBR #11 Adeiny Hechavarría (X - X - X)
t6.new_ab()
t6.pitch_list("b f b b")
t6.out("G6-3")

# 9. TBR #8  Rob Refsnyder (X - X - X)
t6.new_ab()
t6.pitch_list("c c f t")
t6.out("KT")

# 1. TBR #5  Matt Duffy (X - X - X)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")
t6.advance(4, "39 3B")

# Pitching change (BOS): #66 Bobby Poyner replaces #76 Hector Velázquez
t6.pitching_substitution(66)

# 2. TBR #39 Kevin Kiermaier (X - X - 5)
t6.new_ab()
t6.hit(3, rbis=1)

# 3. TBR #27 Carlos Gómez (39 - X - X)
t6.new_ab()
t6.pitch_list("b f s b s")
t6.out("K")


# Bot 6th
# Pitching: TBR #48 Ryan Yarbrough
b6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c b f")
b6.out("L6")

# 6. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("c f b s")
b6.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #61 Brian Johnson
t7 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #66 Bobby Poyner
t7.pitching_substitution(61)

# 4. TBR #44 C.J. Cron (X - X - X)
t7.new_ab()
t7.pitch_list("s b f f s")
t7.out("K")

# 5. TBR #28 Daniel Robertson (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b b")
t7.reach("BB")
t7.advance(4, "18 3B")

# Offensive change (TBR): Pinch-hitter #18 Joey Wendle replaces #13 Brad Miller, batting 6th
t7.offensive_substitution(6, 18, "PH")

# 6. TBR #18 Joey Wendle (X - X - 28)
t7.new_ab()
t7.pitch_list("c f 1 f")
t7.hit(3, rbis=1)
t7.advance(4, "45 SF9")

# Pitching change (BOS): #37 Heath Hembree replaces #61 Brian Johnson
t7.pitching_substitution(37)

# Defensive change (BOS): #12 Brock Holt replaces #2 Xander Bogaerts (SS), playing SS, batting 5th
t7.defensive_substitution(5, 12, "6")

# 7. TBR #45 Jesús Sucre (18 - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("SF9", rbis=1)

# 8. TBR #11 Adeiny Hechavarría (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G5-3")


# Bot 7th
# Pitching: TBR #46 José Alvarado
b7 = game.new_inning()

# Pitching change (TBR): #46 José Alvarado replaces #48 Ryan Yarbrough
b7.pitching_substitution(46)

# Defensive switch (TBR): #28 Daniel Robertson moves to 1B
b7.defensive_switch(28, "3")

# Defensive switch (TBR): #18 Joey Wendle moves to 2B
b7.defensive_switch(18, "4")

# 8. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("b c b c b d")
b7.reach("BB")
b7.advance(2, "7 G3")
b7.advance(3, "50 PB")

# 9. BOS #7  Christian Vázquez (X - X - 11)
b7.new_ab()
b7.pitch_list("c")
b7.out("G3")

# 1. BOS #50 Mookie Betts (X - 11 - X)
b7.new_ab()
b7.pitch_list("b b c f")
b7.pb()
b7.out("P4")

# 2. BOS #16 Andrew Benintendi (11 - X - X)
b7.new_ab()
b7.pitch_list("f")
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #39 Carson Smith
t8 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #37 Heath Hembree
t8.pitching_substitution(39)

# Offensive change (TBR): Pinch-hitter #0 Mallex Smith replaces #8 Rob Refsnyder, batting 9th
t8.offensive_substitution(9, 0, "PH")

# 9. TBR #0  Mallex Smith (X - X - X)
t8.new_ab()
t8.pitch_list("b s")
t8.out("G4-3")

# 1. TBR #5  Matt Duffy (X - X - X)
t8.new_ab()
t8.pitch_list("s b")
t8.out("G6-3")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
t8.new_ab()
t8.pitch_list("b f s b b f b")
t8.reach("BB")
t8.advance(2, "27 1B")
t8.advance(3, "44 BB")

# 3. TBR #27 Carlos Gómez (X - X - 39)
t8.new_ab()
t8.hit(1)
t8.advance(2, "44 BB")

# 4. TBR #44 C.J. Cron (X - 39 - 27)
t8.new_ab()
t8.pitch_list("f f d d b d")
t8.reach("BB")

# 5. TBR #28 Daniel Robertson (39 - 27 - 44)
t8.new_ab()
t8.pitch_list("c s b b s")
t8.out("K")


# Bot 8th
# Pitching: TBR #35 Matt Andriese
b8 = game.new_inning()

# Pitching change (TBR): #35 Matt Andriese replaces #46 José Alvarado
b8.pitching_substitution(35)

# Defensive switch (TBR): #0 Mallex Smith moves to LF
b8.defensive_switch(0, "7")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b8.new_ab()
b8.pitch_list("b b f")
b8.hit(1)
b8.advance(2, "28 WP")
b8.advance(4, "18 2B")

# 4. BOS #28 J.D. Martinez (X - X - 13)
b8.new_ab()
b8.pitch_list("f f b f b f b f f s")
b8.wp()
b8.out("K")

# 5. BOS #12 Brock Holt (X - 13 - X)
b8.new_ab()
b8.pitch_list("c d")
b8.out("F7")

# 6. BOS #18 Mitch Moreland (X - 13 - X)
b8.new_ab()
b8.pitch_list("c f f b")
b8.hit(2, rbis=1)
b8.advance(3, "36 1B")
b8.advance(4, "11 2B")

# 7. BOS #36 Eduardo Núñez (X - 18 - X)
b8.new_ab()
b8.pitch_list("b c c")
b8.hit(1)
b8.advance(4, "11 2B")

# 8. BOS #11 Rafael Devers (18 - X - 36)
b8.new_ab()
b8.pitch_list("c")
b8.hit(2, rbis=2)
b8.advance(4, "7 1B")

# Pitching change (TBR): #37 Alex Colomé replaces #35 Matt Andriese
b8.pitching_substitution(37)

# 9. BOS #7  Christian Vázquez (X - 11 - X)
b8.new_ab()
b8.pitch_list("b c f f f")
b8.hit(1, rbis=1)
b8.advance(2, "50 WP")
b8.advance(4, "50 1B")

# 1. BOS #50 Mookie Betts (X - X - 7)
b8.new_ab()
b8.pitch_list("b b")
b8.wp()
b8.hit(1, rbis=1)
b8.advance(2, "T")
b8.advance(4, "16 2B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b8.new_ab()
b8.pitch_list("c b")
b8.hit(2, rbis=1)

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
b8.new_ab()
b8.pitch_list("t b s f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #39 Carson Smith
t9.pitching_substitution(46)

# 6. TBR #18 Joey Wendle (X - X - X)
t9.new_ab()
t9.pitch_list("c f")
t9.out("P5")

# Offensive change (TBR): Pinch-hitter #2 Denard Span replaces #45 Jesús Sucre, batting 7th
t9.offensive_substitution(7, 2, "PH")

# 7. TBR #2  Denard Span (X - X - X)
t9.new_ab()
t9.pitch_list("b f c b")
t9.out("P5")

# 8. TBR #11 Adeiny Hechavarría (X - X - X)
t9.new_ab()
t9.pitch_list("b b f")
t9.out("G6-3")

# Winning team: BOS
# WP: BOS #39 Carson Smith
game.winning_pitcher(39)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: TBR
# LP: TBR #37 Alex Colomé
game.losing_pitcher(37, is_away_team=True)

# print(game)
game.generate_scorecard()
