import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TBA @ BOS, 2018-04-28
# https://www.baseball-reference.com/boxes/BOS/BOS201804280.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2018/04/28/529813/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-28 16:08-20:00",
        "at": "Fenway Park, Boston, MA",
        "att": "35,795",
        "temp": "60F, Sunny",
        "wind": "12mph, In From RF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 72,
            "roster": {
                # Lineup
                5: "Matt Duffy",
                44: "C.J. Cron",
                27: "Carlos Gómez",
                40: "Wilson Ramos",
                28: "Daniel Robertson",
                2: "Denard Span",
                11: "Adeiny Hechavarría",
                8: "Rob Refsnyder",
                10: "Johnny Field",
                # Starting pitcher
                72: "Yonny Chirinos",
                # Bench
                13: "Brad Miller",
                18: "Joey Wendle",
                0: "Mallex Smith",
                45: "Jesús Sucre",
                # Bullpen
                49: "Jonny Venters",
                37: "Alex Colomé",
                46: "José Alvarado",
                48: "Ryan Yarbrough",
                52: "Chaz Roe",
                36: "Andrew Kittredge",
                34: "Jake Faria",
                4: "Blake Snell",
                35: "Matt Andriese",
                22: "Chris Archer",
                54: "Sergio Romo",
            },
            "lefties": [49, 46, 48, 4],
            "lineup": [
                [5, "5"],
                [44, "3"],
                [27, "9"],
                [40, "2"],
                [28, "4"],
                [2, "7"],
                [11, "6"],
                [8, "0"],
                [10, "8"],
            ],
            "bench": [
                [13, "DH"],
                [18, "2B"],
                [0, "OF"],
                [45, "C"],
            ],
            "bullpen": [49, 37, 46, 48, 52, 36, 34, 4, 35, 22, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Starting pitcher
                24: "David Price",
                # Bench
                5: "Tzu-Wei Lin",
                23: "Blake Swihart",
                18: "Mitch Moreland",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [24, 57, 41, 31, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [7, "2"],
            ],
            "bench": [
                [5, "OF"],
                [23, "C"],
                [18, "1B"],
                [3, "C"],
            ],
            "bullpen": [57, 46, 76, 39, 22, 41, 31, 61, 32, 37],
        },
        "umpires": {
            "HP": "Ryan Blakney",
            "1B": "Jim Wolf",
            "2B": "D.J. Reyburn",
            "3B": "Sam Holbrook",
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
# Pitching: BOS #24 David Price
t1 = game.new_inning()

# 1. TBR #5  Matt Duffy (X - X - X)
t1.new_ab()
t1.hit(2)
t1.thrown_out(3, "44 DP5", 1, 24)

# 2. TBR #44 C.J. Cron (X - 5 - X)
t1.new_ab()
t1.pitch_list("f")
t1.out("DP5-3")

# 3. TBR #27 Carlos Gómez (X - X - X)
t1.new_ab()
t1.pitch_list("b f f c")
t1.out("!K")


# Bot 1st
# Pitching: TBR #72 Yonny Chirinos
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c f")
b1.reach("HBP")
b1.advance(2, "16 1B")
b1.advance(3, "13 WP")
b1.advance(4, "2 SF8")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("b f b")
b1.hit(1)
b1.advance(2, "13 WP")

# 3. BOS #13 Hanley Ramirez (X - 50 - 16)
b1.new_ab()
b1.pitch_list("c b b f d b")
b1.wp()
b1.reach("BB")

# 4. BOS #28 J.D. Martinez (50 - 16 - 13)
b1.new_ab()
b1.pitch_list("c t s")
b1.out("K")

# 5. BOS #2  Xander Bogaerts (50 - 16 - 13)
b1.new_ab()
b1.pitch_list("f b")
b1.out("SF8", rbis=1)

# 6. BOS #11 Rafael Devers (X - 16 - 13)
b1.new_ab()
b1.pitch_list("s s f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 4. TBR #40 Wilson Ramos (X - X - X)
t2.new_ab()
t2.hit(2)
t2.advance(4, "2 HR")

# 5. TBR #28 Daniel Robertson (X - 40 - X)
t2.new_ab()
t2.pitch_list("f")
t2.out("F9")

# 6. TBR #2  Denard Span (X - 40 - X)
t2.new_ab()
t2.pitch_list("c d b b c")
t2.hit(4, rbis=2)

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
t2.new_ab()
t2.pitch_list("b f b f b b")
t2.reach("BB")

# 8. TBR #8  Rob Refsnyder (X - X - 11)
t2.new_ab()
t2.pitch_list("s f b c")
t2.out("!K")

# 9. TBR #10 Johnny Field (X - X - 11)
t2.new_ab()
t2.pitch_list("1 c f t")
t2.out("KT")


# Bot 2nd
# Pitching: TBR #72 Yonny Chirinos
b2 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("c b b c")
b2.hit(1)
b2.advance(2, "19 1B")
b2.advance(3, "7 WP")
b2.advance(4, "7 DP6-4-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 36)
b2.new_ab()
b2.hit(1)
b2.thrown_out(2, "7 DP6-4-3", 1, 72)

# 9. BOS #7  Christian Vázquez (X - 36 - 19)
b2.new_ab()
b2.pitch_list("b c b f f f")
b2.wp()
b2.out("DP6-4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b2.new_ab()
b2.pitch_list("b b c f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 1. TBR #5  Matt Duffy (X - X - X)
t3.new_ab()
t3.pitch_list("c c c")
t3.out("!K")

# 2. TBR #44 C.J. Cron (X - X - X)
t3.new_ab()
t3.hit(2)
t3.advance(4, "40 HR")

# 3. TBR #27 Carlos Gómez (X - 44 - X)
t3.new_ab()
t3.pitch_list("f f b t")
t3.out("KT")

# 4. TBR #40 Wilson Ramos (X - 44 - X)
t3.new_ab()
t3.pitch_list("t f")
t3.hit(4, rbis=2)

# 5. TBR #28 Daniel Robertson (X - X - X)
t3.new_ab()
t3.pitch_list("b f")
t3.out("G1-3")


# Bot 3rd
# Pitching: TBR #72 Yonny Chirinos
b3 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.hit(2)
b3.advance(3, "13 1B")
b3.advance(4, "2 1B")

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
b3.new_ab()
b3.hit(1)
b3.advance(2, "28 BB")
b3.advance(3, "2 1B")

# 4. BOS #28 J.D. Martinez (16 - X - 13)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.advance(2, "2 1B")

# 5. BOS #2  Xander Bogaerts (16 - 13 - 28)
b3.new_ab()
b3.pitch_list("f b")
b3.hit(1, rbis=1)

# Pitching change (TBR): #48 Ryan Yarbrough replaces #72 Yonny Chirinos
b3.pitching_substitution(48)

# 6. BOS #11 Rafael Devers (13 - 28 - 2)
b3.new_ab()
b3.pitch_list("b f f c")
b3.out("!K")

# 7. BOS #36 Eduardo Núñez (13 - 28 - 2)
b3.new_ab()
b3.pitch_list("b")
b3.out("L6")

# 8. BOS #19 Jackie Bradley Jr. (13 - 28 - 2)
b3.new_ab()
b3.pitch_list("b c d f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 6. TBR #2  Denard Span (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c f b")
t4.reach("BB")
t4.thrown_out(2, "8 DP4-6-3", 2, 24)

# 7. TBR #11 Adeiny Hechavarría (X - X - 2)
t4.new_ab()
t4.pitch_list("f f b b")
t4.out("L9")

# 8. TBR #8  Rob Refsnyder (X - X - 2)
t4.new_ab()
t4.out("DP4-6-3")


# Bot 4th
# Pitching: TBR #48 Ryan Yarbrough
b4 = game.new_inning()

# 9. BOS #7  Christian Vázquez (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(2)
b4.advance(3, "16 G3-1")
b4.advance(4, "13 1B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b4.new_ab()
b4.pitch_list("f f b b f")
b4.out("G3-1")

# 3. BOS #13 Hanley Ramirez (50 - X - X)
b4.new_ab()
b4.hit(1, rbis=1)

# 4. BOS #28 J.D. Martinez (X - X - 13)
b4.new_ab()
b4.pitch_list("f f 1 s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# Defensive change (BOS): #23 Blake Swihart replaces #50 Mookie Betts (RF), playing LF, batting 1st
t5.defensive_substitution(1, 23, "7")

# Defensive switch (BOS): #16 Andrew Benintendi moves to CF
t5.defensive_switch(16, "8")

# Defensive switch (BOS): #19 Jackie Bradley Jr. moves to RF
t5.defensive_switch(19, "9")

# 9. TBR #10 Johnny Field (X - X - X)
t5.new_ab()
t5.pitch_list("f c")
t5.out("F8")

# 1. TBR #5  Matt Duffy (X - X - X)
t5.new_ab()
t5.hit(1)
t5.thrown_out(2, "44 FC6-4", 2, 24)

# 2. TBR #44 C.J. Cron (X - X - 5)
t5.new_ab()
t5.pitch_list("c f 1")
t5.reach("FC6-4")
t5.advance(2, "27 1B")
t5.advance(3, "40 BB")
t5.advance(4, "28 BB")

# 3. TBR #27 Carlos Gómez (X - X - 44)
t5.new_ab()
t5.pitch_list("b b s f")
t5.hit(1)
t5.advance(2, "40 BB")
t5.advance(3, "28 BB")

# 4. TBR #40 Wilson Ramos (X - 44 - 27)
t5.new_ab()
t5.pitch_list("b t b b f b")
t5.reach("BB")
t5.advance(2, "28 BB")

# 5. TBR #28 Daniel Robertson (44 - 27 - 40)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB", rbis=1)

# 6. TBR #2  Denard Span (27 - 40 - 28)
t5.new_ab()
t5.out("L6")


# Bot 5th
# Pitching: TBR #48 Ryan Yarbrough
b5 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.out("P6")

# 6. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(4, rbis=1)

# 7. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c f b")
b5.out("G6-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("c c b f t")
b5.out("KT")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
t6.new_ab()
t6.hit(1)
t6.advance(2, "10 PB")
t6.advance("U", "5 E4")

# 8. TBR #8  Rob Refsnyder (X - X - 11)
t6.new_ab()
t6.pitch_list("b c c")
t6.out("F9")

# 9. TBR #10 Johnny Field (X - X - 11)
t6.new_ab()
t6.pitch_list("b")
t6.pb()
t6.out("G6-3")

# Pitching change (BOS): #37 Heath Hembree replaces #24 David Price
t6.pitching_substitution(37)

# 1. TBR #5  Matt Duffy (X - 11 - X)
t6.new_ab()
t6.pitch_list("b f s b b f")
t6.hit(1)
t6.error(4)
t6.advance(2, "E4")

# 2. TBR #44 C.J. Cron (X - 5 - X)
t6.new_ab()
t6.pitch_list("b b b c s")
t6.out("L8")


# Bot 6th
# Pitching: TBR #48 Ryan Yarbrough
b6 = game.new_inning()

# 9. BOS #7  Christian Vázquez (X - X - X)
b6.new_ab()
b6.pitch_list("c c t")
b6.out("KT")

# 1. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("f c s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# 3. TBR #27 Carlos Gómez (X - X - X)
t7.new_ab()
t7.pitch_list("s b f f f")
t7.hit(4, rbis=1)

# 4. TBR #40 Wilson Ramos (X - X - X)
t7.new_ab()
t7.pitch_list("c b b")
t7.hit(1)
# Offensive change (TBR): Pinch-runner #45 Jesús Sucre replaces #40 Wilson Ramos
t7.offensive_substitution(4, 45, "PR")
t7.atbase("PR")
t7.advance(2, "28 BB")
t7.advance(3, "11 G4-3")

# 5. TBR #28 Daniel Robertson (X - X - 40)
t7.new_ab()
t7.pitch_list("c b b c f f f b b")
t7.reach("BB")
t7.advance(2, "11 G4-3")

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree
t7.pitching_substitution(32)

# 6. TBR #2  Denard Span (X - 45 - 28)
t7.new_ab()
t7.pitch_list("c c b s")
t7.out("K")

# 7. TBR #11 Adeiny Hechavarría (X - 45 - 28)
t7.new_ab()
t7.out("G4-3")

# Offensive change (TBR): Pinch-hitter #13 Brad Miller replaces #8 Rob Refsnyder, batting 8th
t7.offensive_substitution(8, 13, "PH")

# 8. TBR #13 Brad Miller (45 - 28 - X)
t7.new_ab()
t7.pitch_list("b s s s")
t7.out("K")


# Bot 7th
# Pitching: TBR #52 Chaz Roe
b7 = game.new_inning()

# Pitching change (TBR): #52 Chaz Roe replaces #48 Ryan Yarbrough
b7.pitching_substitution(52)

# Defensive switch (TBR): #45 Jesús Sucre moves to C
b7.defensive_switch(45, "2")

# Defensive switch (TBR): #13 Brad Miller moves to DH
b7.defensive_switch(13, "0")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("s b")
b7.error(5)
b7.reach("E5", end_base=2)
b7.advance(3, "11 1B")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
b7.new_ab()
b7.pitch_list("c s f f s")
b7.out("K")

# Pitching change (TBR): #46 José Alvarado replaces #52 Chaz Roe
b7.pitching_substitution(46)

# 6. BOS #11 Rafael Devers (X - 28 - X)
b7.new_ab()
b7.hit(1)

# 7. BOS #36 Eduardo Núñez (28 - X - 11)
b7.new_ab()
b7.pitch_list("s c d s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #61 Brian Johnson
t8 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #32 Matt Barnes
t8.pitching_substitution(61)

# 9. TBR #10 Johnny Field (X - X - X)
t8.new_ab()
t8.pitch_list("c f f b")
t8.hit(1)
t8.advance(2, "5 1B")
t8.advance(4, "45 2B")

# 1. TBR #5  Matt Duffy (X - X - 10)
t8.new_ab()
t8.pitch_list("c c b 1")
t8.hit(1)
t8.advance(3, "45 2B")

# 2. TBR #44 C.J. Cron (X - 10 - 5)
t8.new_ab()
t8.pitch_list("c f s")
t8.out("K")

# 3. TBR #27 Carlos Gómez (X - 10 - 5)
t8.new_ab()
t8.pitch_list("f b t b")
t8.out("L7")

# 4. TBR #45 Jesús Sucre (X - 10 - 5)
t8.new_ab()
t8.pitch_list("b t")
t8.hit(2, rbis=1)

# 5. TBR #28 Daniel Robertson (5 - 45 - X)
t8.new_ab()
t8.pitch_list("c b s d")
t8.out("G5-3")


# Bot 8th
# Pitching: TBR #46 José Alvarado
b8 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("c f f b")
b8.out("G4-3")

# 9. BOS #7  Christian Vázquez (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G1-3")

# 1. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("b c f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #61 Brian Johnson
t9 = game.new_inning()

# 6. TBR #2  Denard Span (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.hit(1)
t9.advance(3, "11 1B")
t9.advance(4, "13 1B")

# 7. TBR #11 Adeiny Hechavarría (X - X - 2)
t9.new_ab()
t9.hit(1)
t9.advance(2, "13 1B")
t9.advance(4, "10 HR")

# 8. TBR #13 Brad Miller (2 - X - 11)
t9.new_ab()
t9.pitch_list("b s b b c")
t9.hit(1, rbis=1)
t9.advance(4, "10 HR")

# 9. TBR #10 Johnny Field (X - 11 - 13)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(4, rbis=3)

# 1. TBR #5  Matt Duffy (X - X - X)
t9.new_ab()
t9.pitch_list("c c b s")
t9.out("K")

# 2. TBR #44 C.J. Cron (X - X - X)
t9.new_ab()
t9.pitch_list("f s")
t9.out("F9")

# 3. TBR #27 Carlos Gómez (X - X - X)
t9.new_ab()
t9.pitch_list("f b")
t9.out("G4-3")


# Bot 9th
# Pitching: TBR #54 Sergio Romo
b9 = game.new_inning()

# Pitching change (TBR): #54 Sergio Romo replaces #46 José Alvarado
b9.pitching_substitution(54)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b9.new_ab()
b9.pitch_list("f b f b f b")
b9.hit(2)
b9.advance(3, "11 WP")
b9.advance(4, "11 1B")

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
b9.new_ab()
b9.pitch_list("b b b c b")
b9.reach("BB")
b9.advance(2, "11 WP")
b9.advance(3, "11 1B")

# 4. BOS #28 J.D. Martinez (X - 16 - 13)
b9.new_ab()
b9.pitch_list("b f c t")
b9.out("KT")

# 5. BOS #2  Xander Bogaerts (X - 16 - 13)
b9.new_ab()
b9.pitch_list("b c f")
b9.out("F8")

# 6. BOS #11 Rafael Devers (X - 16 - 13)
b9.new_ab()
b9.pitch_list("c f b d")
b9.wp()
b9.hit(1, rbis=1)
b9.advance(2, "36 DI")

# 7. BOS #36 Eduardo Núñez (13 - X - 11)
b9.new_ab()
b9.pitch_list("c b t b s")
b9.out("K")

# Winning team: TBR
# WP: TBR #48 Ryan Yarbrough
game.winning_pitcher(48, is_away_team=True)

# Loser team: BOS
# LP: BOS #24 David Price
game.losing_pitcher(24)

# print(game)
game.generate_scorecard()
