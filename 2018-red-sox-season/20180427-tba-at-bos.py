import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TBA @ BOS, 2018-04-27
# https://www.baseball-reference.com/boxes/BOS/BOS201804270.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2018/04/27/529798/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-27 19:10-22:20",
        "at": "Fenway Park, Boston, MA",
        "att": "32,620",
        "temp": "48F, Overcast",
        "wind": "7mph, Out To RF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 4,
            "roster": {
                # Lineup
                5: "Matt Duffy",
                44: "C.J. Cron",
                27: "Carlos Gómez",
                40: "Wilson Ramos",
                28: "Daniel Robertson",
                13: "Brad Miller",
                11: "Adeiny Hechavarría",
                0: "Mallex Smith",
                8: "Rob Refsnyder",
                # Starting pitcher
                4: "Blake Snell",
                # Bench
                2: "Denard Span",
                18: "Joey Wendle",
                45: "Jesús Sucre",
                10: "Johnny Field",
                # Bullpen
                49: "Jonny Venters",
                37: "Alex Colomé",
                46: "José Alvarado",
                48: "Ryan Yarbrough",
                52: "Chaz Roe",
                36: "Andrew Kittredge",
                34: "Jake Faria",
                72: "Yonny Chirinos",
                35: "Matt Andriese",
                22: "Chris Archer",
                54: "Sergio Romo",
            },
            "lefties": [4, 49, 46, 48],
            "lineup": [
                [5, "5"],
                [44, "0"],
                [27, "9"],
                [40, "2"],
                [28, "4"],
                [13, "3"],
                [11, "6"],
                [0, "8"],
                [8, "7"],
            ],
            "bench": [
                [2, "CF"],
                [18, "2B"],
                [45, "C"],
                [10, "RF"],
            ],
            "bullpen": [49, 37, 46, 48, 52, 36, 34, 72, 35, 22, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                5: "Tzu-Wei Lin",
                # Starting pitcher
                31: "Drew Pomeranz",
                # Bench
                11: "Rafael Devers",
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [31, 57, 24, 41, 61],
            "lineup": [
                [50, "9"],
                [13, "0"],
                [28, "7"],
                [18, "3"],
                [2, "6"],
                [36, "5"],
                [19, "8"],
                [7, "2"],
                [5, "4"],
            ],
            "bench": [
                [11, "3B"],
                [23, "C"],
                [16, "LF"],
                [3, "C"],
            ],
            "bullpen": [57, 24, 46, 76, 39, 22, 41, 61, 32, 37],
        },
        "umpires": {
            "HP": "Sam Holbrook",
            "1B": "Ryan Blakney",
            "2B": "Jim Wolf",
            "3B": "D.J. Reyburn",
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
# Pitching: BOS #31 Drew Pomeranz
t1 = game.new_inning()

# 1. TBR #5  Matt Duffy (X - X - X)
t1.new_ab()
t1.pitch_list("b s")
t1.out("L5")

# 2. TBR #44 C.J. Cron (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.hit(1)
t1.advance(4, "40 HR")

# 3. TBR #27 Carlos Gómez (X - X - 44)
t1.new_ab()
t1.pitch_list("c d f c")
t1.out("!K")

# 4. TBR #40 Wilson Ramos (X - X - 44)
t1.new_ab()
t1.pitch_list("b")
t1.hit(4, rbis=2)

# 5. TBR #28 Daniel Robertson (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("L9")


# Bot 1st
# Pitching: TBR #4  Blake Snell
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.out("G6-3")

# 2. BOS #13 Hanley Ramirez (X - X - X)
b1.new_ab()
b1.out("P3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c c s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Drew Pomeranz
t2 = game.new_inning()

# 6. TBR #13 Brad Miller (X - X - X)
t2.new_ab()
t2.out("F7")

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
t2.new_ab()
t2.pitch_list("b f s")
t2.hit(1)
t2.thrown_out(2, "0 DP4-6-3", 2, 31)

# 8. TBR #0  Mallex Smith (X - X - 11)
t2.new_ab()
t2.pitch_list("b b f")
t2.out("DP4-6-3")


# Bot 2nd
# Pitching: TBR #4  Blake Snell
b2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("b c s b s")
b2.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("c f s")
b2.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b b c s f t")
b2.out("KT")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Drew Pomeranz
t3 = game.new_inning()

# 9. TBR #8  Rob Refsnyder (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(4)

# 1. TBR #5  Matt Duffy (X - X - X)
t3.new_ab()
t3.out("G5-3")

# 2. TBR #44 C.J. Cron (X - X - X)
t3.new_ab()
t3.pitch_list("b f f")
t3.hit(1)
t3.thrown_out(2, "40 FC6-4", 3, 31)

# 3. TBR #27 Carlos Gómez (X - X - 44)
t3.new_ab()
t3.pitch_list("b s b f b c")
t3.out("!K")

# 4. TBR #40 Wilson Ramos (X - X - 44)
t3.new_ab()
t3.pitch_list("s b")
t3.reach("FC6-4")


# Bot 3rd
# Pitching: TBR #4  Blake Snell
b3 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b b f t s")
b3.out("K2-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b c f")
b3.out("L7")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b3.new_ab()
b3.pitch_list("b c b")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Drew Pomeranz
t4 = game.new_inning()

# 5. TBR #28 Daniel Robertson (X - X - X)
t4.new_ab()
t4.pitch_list("c b b")
t4.hit(4)

# 6. TBR #13 Brad Miller (X - X - X)
t4.new_ab()
t4.pitch_list("s b s")
t4.out("F8")

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
t4.new_ab()
t4.out("F9")

# 8. TBR #0  Mallex Smith (X - X - X)
t4.new_ab()
t4.pitch_list("s b f b f b f f")
t4.out("F8")


# Bot 4th
# Pitching: TBR #4  Blake Snell
b4 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b4.new_ab()
b4.pitch_list("b s b b b")
b4.reach("BB")
b4.advance(2, "28 SB")
b4.advance(3, "28 E1")

# 2. BOS #13 Hanley Ramirez (X - X - 50)
b4.new_ab()
b4.pitch_list("c d f c")
b4.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - 50)
b4.new_ab()
b4.pitch_list("c")
b4.error(1)
b4.reach("E1")
b4.thrown_out(2, "18 DP6-4-3", 2, 4)

# 4. BOS #18 Mitch Moreland (50 - X - 28)
b4.new_ab()
b4.pitch_list("s b s d b")
b4.out("DP6-4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Drew Pomeranz
t5 = game.new_inning()

# 9. TBR #8  Rob Refsnyder (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b b")
t5.reach("BB")
t5.thrown_out(2, "5 CS", 2, 31)

# 1. TBR #5  Matt Duffy (X - X - 8)
t5.new_ab()
t5.pitch_list("b c b 1 c s")
t5.out("KDP2-4")

# 2. TBR #44 C.J. Cron (X - X - X)
t5.new_ab()
t5.pitch_list("b b f f b b")
t5.reach("BB")

# 3. TBR #27 Carlos Gómez (X - X - 44)
t5.new_ab()
t5.pitch_list("b f s f d s")
t5.out("K")


# Bot 5th
# Pitching: TBR #4  Blake Snell
b5 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.hit(1)
b5.thrown_out(2, "36 FC4-6", 1, 4)

# 6. BOS #36 Eduardo Núñez (X - X - 2)
b5.new_ab()
b5.pitch_list("b 1 1 c")
b5.reach("FC4-6")
b5.thrown_out(2, "19 DP4-6-3", 2, 4)

# 7. BOS #19 Jackie Bradley Jr. (X - X - 36)
b5.new_ab()
b5.pitch_list("b s 1 s d b f")
b5.out("DP4-6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #76 Hector Velázquez
t6 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #31 Drew Pomeranz
t6.pitching_substitution(76)

# 4. TBR #40 Wilson Ramos (X - X - X)
t6.new_ab()
t6.pitch_list("b f f f")
t6.out("G6-3")

# 5. TBR #28 Daniel Robertson (X - X - X)
t6.new_ab()
t6.pitch_list("b s b")
t6.hit(2)

# 6. TBR #13 Brad Miller (X - 28 - X)
t6.new_ab()
t6.pitch_list("b s b")
t6.out("L8")

# 7. TBR #11 Adeiny Hechavarría (X - 28 - X)
t6.new_ab()
t6.pitch_list("b f")
t6.out("G4-3")


# Bot 6th
# Pitching: TBR #4  Blake Snell
b6 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
b6.new_ab()
b6.pitch_list("f f f b")
b6.hit(2)
b6.advance(4, "50 2B")

# 9. BOS #5  Tzu-Wei Lin (X - 7 - X)
b6.new_ab()
b6.pitch_list("l")
b6.out("G1-3")

# 1. BOS #50 Mookie Betts (X - 7 - X)
b6.new_ab()
b6.pitch_list("b f d")
b6.hit(2, rbis=1)
b6.advance(4, "28 2B")

# 2. BOS #13 Hanley Ramirez (X - 50 - X)
b6.new_ab()
b6.pitch_list("c b c s")
b6.out("K")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(2, rbis=1)

# 4. BOS #18 Mitch Moreland (X - 28 - X)
b6.new_ab()
b6.pitch_list("f f d s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #76 Hector Velázquez
t7 = game.new_inning()

# 8. TBR #0  Mallex Smith (X - X - X)
t7.new_ab()
t7.out("(F)B2")

# 9. TBR #8  Rob Refsnyder (X - X - X)
t7.new_ab()
t7.pitch_list("c b f")
t7.hit(1)
t7.advance(2, "5 1B")

# 1. TBR #5  Matt Duffy (X - X - 8)
t7.new_ab()
t7.pitch_list("b c f d 1 f")
t7.hit(1)
t7.thrown_out(2, "44 DP1-4-3", 2, 76)

# 2. TBR #44 C.J. Cron (X - 8 - 5)
t7.new_ab()
t7.pitch_list("c")
t7.out("DP1-4-3")


# Bot 7th
# Pitching: TBR #4  Blake Snell
b7 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("b c f")
b7.hit(2)
b7.advance(3, "19 G4-3")

# 6. BOS #36 Eduardo Núñez (X - 2 - X)
b7.new_ab()
b7.pitch_list("f s s")
b7.out("K")

# 7. BOS #19 Jackie Bradley Jr. (X - 2 - X)
b7.new_ab()
b7.pitch_list("b b f")
b7.out("G4-3")

# 8. BOS #7  Christian Vázquez (2 - X - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #76 Hector Velázquez
t8 = game.new_inning()

# 3. TBR #27 Carlos Gómez (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G5-3")

# 4. TBR #40 Wilson Ramos (X - X - X)
t8.new_ab()
t8.pitch_list("b s f")
t8.out("G6-3")

# 5. TBR #28 Daniel Robertson (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.reach("HBP")
t8.advance(2, "13 1B")

# 6. TBR #13 Brad Miller (X - X - 28)
t8.new_ab()
t8.pitch_list("1")
t8.hit(1)

# 7. TBR #11 Adeiny Hechavarría (X - 28 - 13)
t8.new_ab()
t8.pitch_list("d b")
t8.out("P6")


# Bot 8th
# Pitching: TBR #4  Blake Snell
b8 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #5 Tzu-Wei Lin, batting 9th
b8.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("F9")

# Pitching change (TBR): #52 Chaz Roe replaces #4  Blake Snell
b8.pitching_substitution(52)

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("b f c b b")
b8.hit(2)
b8.advance(4, "28 1B")

# 2. BOS #13 Hanley Ramirez (X - 50 - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("P3")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
b8.new_ab()
b8.pitch_list("b b f c f")
b8.hit(1, rbis=1)

# 4. BOS #18 Mitch Moreland (X - X - 28)
b8.new_ab()
b8.out("G3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #76 Hector Velázquez
t9 = game.new_inning()

# Defensive switch (BOS): #36 Eduardo Núñez moves to 2B
t9.defensive_switch(36, "4")

# Defensive change (BOS): #11 Rafael Devers replaces #23 Blake Swihart (PH), playing 3B, batting 9th
t9.defensive_substitution(9, 11, "5")

# 8. TBR #0  Mallex Smith (X - X - X)
t9.new_ab()
t9.out("F7")

# Offensive change (TBR): Pinch-hitter #2 Denard Span replaces #8 Rob Refsnyder, batting 9th
t9.offensive_substitution(9, 2, "PH")

# 9. TBR #2  Denard Span (X - X - X)
t9.new_ab()
t9.pitch_list("b f c f f b f f f b d")
t9.reach("BB")
t9.thrown_out(2, "5 CS", 2, 37)

# Pitching change (BOS): #37 Heath Hembree replaces #76 Hector Velázquez
t9.pitching_substitution(37)

# 1. TBR #5  Matt Duffy (X - X - 2)
t9.new_ab()
t9.pitch_list("1 b c f b s")
t9.out("K")


# Bot 9th
# Pitching: TBR #37 Alex Colomé
b9 = game.new_inning()

# Pitching change (TBR): #37 Alex Colomé replaces #52 Chaz Roe
b9.pitching_substitution(37)

# Defensive switch (TBR): #2 Denard Span moves to LF
b9.defensive_switch(2, "7")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b9.new_ab()
b9.pitch_list("b b f f")
b9.hit(1)

# 6. BOS #36 Eduardo Núñez (X - X - 2)
b9.new_ab()
b9.out("(F)P2")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 2)
b9.new_ab()
b9.pitch_list("b f b t d f s")
b9.out("K")

# Offensive change (BOS): Pinch-hitter #16 Andrew Benintendi replaces #7 Christian Vázquez, batting 8th
b9.offensive_substitution(8, 16, "PH")

# 8. BOS #16 Andrew Benintendi (X - X - 2)
b9.new_ab()
b9.pitch_list("b c f b b c")
b9.out("!K")

# Winning team: TBR
# WP: TBR #4 Blake Snell
game.winning_pitcher(4, is_away_team=True)
# SV: TBR #37 Alex Colomé
game.save_pitcher(37, is_away_team=True)

# Loser team: BOS
# LP: BOS #31 Drew Pomeranz
game.losing_pitcher(31)

# print(game)
game.generate_scorecard()
