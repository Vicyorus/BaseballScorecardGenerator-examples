import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TBA @ BOS, 2018-04-05
# https://www.baseball-reference.com/boxes/BOS/BOS201804050.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2018/04/05/529506/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-05 14:07-18:02",
        "at": "Fenway Park, Boston, MA",
        "att": "36,134",
        "temp": "40F, Sunny",
        "wind": "18mph, Out To RF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 72,
            "roster": {
                # Lineup
                5: "Matt Duffy",
                39: "Kevin Kiermaier",
                27: "Carlos Gómez",
                44: "C.J. Cron",
                40: "Wilson Ramos",
                13: "Brad Miller",
                11: "Adeiny Hechavarría",
                28: "Daniel Robertson",
                8: "Rob Refsnyder",
                # Starting pitcher
                72: "Yonny Chirinos",
                # Bench
                2: "Denard Span",
                18: "Joey Wendle",
                0: "Mallex Smith",
                45: "Jesús Sucre",
                # Bullpen
                37: "Alex Colomé",
                46: "José Alvarado",
                48: "Ryan Yarbrough",
                52: "Chaz Roe",
                50: "Austin Pruitt",
                36: "Andrew Kittredge",
                34: "Jake Faria",
                4: "Blake Snell",
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
                [40, "2"],
                [13, "3"],
                [11, "6"],
                [28, "4"],
                [8, "7"],
            ],
            "bench": [
                [2, "CF"],
                [18, "2B"],
                [0, "OF"],
                [45, "C"],
            ],
            "bullpen": [37, 46, 48, 52, 50, 36, 34, 4, 35, 22, 54],
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
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 41, 61, 66],
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
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [39, 22, 41, 61, 66, 37, 46, 76, 64, 56, 32],
        },
        "umpires": {
            "HP": "Todd Tichenor",
            "1B": "Alan Porter",
            "2B": "Bill Miller",
            "3B": "Angel Hernandez",
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
t1.pitch_list("b c s f b b")
t1.out("G4-3")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
t1.new_ab()
t1.out("F9")

# 3. TBR #27 Carlos Gómez (X - X - X)
t1.new_ab()
t1.pitch_list("b s b f f c")
t1.out("!K")


# Bot 1st
# Pitching: TBR #72 Yonny Chirinos
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.out("P1")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.thrown_out(2, "13 2-4", 3, 72)

# 3. BOS #13 Hanley Ramirez (X - X - 16)
b1.new_ab()
b1.pitch_list("f b b c s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 4. TBR #44 C.J. Cron (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b f f b s")
t2.out("K")

# 5. TBR #40 Wilson Ramos (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("F8")

# 6. TBR #13 Brad Miller (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.hit(1)

# 7. TBR #11 Adeiny Hechavarría (X - X - 13)
t2.new_ab()
t2.pitch_list("b c")
t2.out("F9")


# Bot 2nd
# Pitching: TBR #72 Yonny Chirinos
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(3)

# 5. BOS #2  Xander Bogaerts (28 - X - X)
b2.new_ab()
b2.pitch_list("f")
b2.out("G1-3")

# 6. BOS #11 Rafael Devers (28 - X - X)
b2.new_ab()
b2.pitch_list("d b")
b2.out("G3")

# 7. BOS #36 Eduardo Núñez (28 - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 8. TBR #28 Daniel Robertson (X - X - X)
t3.new_ab()
t3.pitch_list("s s")
t3.hit(2)
t3.advance(3, "5 FC4-6")

# 9. TBR #8  Rob Refsnyder (X - 28 - X)
t3.new_ab()
t3.pitch_list("b b b c s f b")
t3.reach("BB")
t3.thrown_out(2, "5 FC4-6", 1, 24)

# 1. TBR #5  Matt Duffy (X - 28 - 8)
t3.new_ab()
t3.pitch_list("c f b")
t3.reach("FC4-6")

# 2. TBR #39 Kevin Kiermaier (28 - X - 5)
t3.new_ab()
t3.pitch_list("b s b")
t3.out("P6")

# 3. TBR #27 Carlos Gómez (28 - X - 5)
t3.new_ab()
t3.out("P3")


# Bot 3rd
# Pitching: TBR #72 Yonny Chirinos
b3 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b s")
b3.out("G4-3")

# 9. BOS #7  Christian Vázquez (X - X - X)
b3.new_ab()
b3.pitch_list("c f f b f b f t")
b3.out("KT")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b3.new_ab()
b3.pitch_list("f")
b3.out("G3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 4. TBR #44 C.J. Cron (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("F8")

# 5. TBR #40 Wilson Ramos (X - X - X)
t4.new_ab()
t4.pitch_list("f b b")
t4.out("F8")

# 6. TBR #13 Brad Miller (X - X - X)
t4.new_ab()
t4.pitch_list("f b")
t4.out("F8")


# Bot 4th
# Pitching: TBR #72 Yonny Chirinos
b4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
b4.new_ab()
b4.out("G5-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("c s f f b s")
b4.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b c c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
t5.new_ab()
t5.out("G4-3")

# 8. TBR #28 Daniel Robertson (X - X - X)
t5.new_ab()
t5.pitch_list("b b c b b")
t5.reach("BB")
t5.advance(2, "8 BB")

# 9. TBR #8  Rob Refsnyder (X - X - 28)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")

# 1. TBR #5  Matt Duffy (X - 28 - 8)
t5.new_ab()
t5.pitch_list("f f c")
t5.out("!K")

# 2. TBR #39 Kevin Kiermaier (X - 28 - 8)
t5.new_ab()
t5.pitch_list("c d")
t5.out("G6-3")


# Bot 5th
# Pitching: TBR #72 Yonny Chirinos
b5 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.out("F8")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G4-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b c s b")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 3. TBR #27 Carlos Gómez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F8")

# 4. TBR #44 C.J. Cron (X - X - X)
t6.new_ab()
t6.hit(1)
t6.thrown_out(2, "40 DP5-4-3", 2, 24)

# 5. TBR #40 Wilson Ramos (X - X - 44)
t6.new_ab()
t6.pitch_list("b f f b")
t6.out("DP5-4-3")


# Bot 6th
# Pitching: TBR #52 Chaz Roe
b6 = game.new_inning()

# Pitching change (TBR): #52 Chaz Roe replaces #72 Yonny Chirinos
b6.pitching_substitution(52)

# 9. BOS #7  Christian Vázquez (X - X - X)
b6.new_ab()
b6.pitch_list("b s b")
b6.out("L8")

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b f")
b6.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #24 David Price
t7 = game.new_inning()

# 6. TBR #13 Brad Miller (X - X - X)
t7.new_ab()
t7.out("F7")

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
t7.new_ab()
t7.pitch_list("c f b s")
t7.out("K")

# 8. TBR #28 Daniel Robertson (X - X - X)
t7.new_ab()
t7.pitch_list("c b c s")
t7.out("K")


# Bot 7th
# Pitching: TBR #54 Sergio Romo
b7 = game.new_inning()

# Pitching change (TBR): #54 Sergio Romo replaces #52 Chaz Roe
b7.pitching_substitution(54)

# 3. BOS #13 Hanley Ramirez (X - X - X)
b7.new_ab()
b7.pitch_list("b c f b b c")
b7.out("!K")

# 4. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.out("L7")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(2, "11 PB")

# 6. BOS #11 Rafael Devers (X - X - 2)
b7.new_ab()
b7.pitch_list("s s d s")
b7.pb()
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #39 Carson Smith
t8 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #24 David Price
t8.pitching_substitution(39)

# Offensive change (TBR): Pinch-hitter #0 Mallex Smith replaces #8 Rob Refsnyder, batting 9th
t8.offensive_substitution(9, 0, "PH")

# 9. TBR #0  Mallex Smith (X - X - X)
t8.new_ab()
t8.pitch_list("b b c f f b f b")
t8.reach("BB")
t8.advance(4, "5 HR")

# 1. TBR #5  Matt Duffy (X - X - 0)
t8.new_ab()
t8.pitch_list("b c 1")
t8.hit(4, rbis=2)

# 2. TBR #39 Kevin Kiermaier (X - X - X)
t8.new_ab()
t8.pitch_list("b c c c")
t8.out("!K")

# 3. TBR #27 Carlos Gómez (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c f f")
t8.out("L3")

# 4. TBR #44 C.J. Cron (X - X - X)
t8.new_ab()
t8.pitch_list("c s b f f f f")
t8.out("G3-1")


# Bot 8th
# Pitching: TBR #46 José Alvarado
b8 = game.new_inning()

# Pitching change (TBR): #46 José Alvarado replaces #54 Sergio Romo
b8.pitching_substitution(46)

# Defensive switch (TBR): #0 Mallex Smith moves to LF
b8.defensive_switch(0, "7")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b8.new_ab()
b8.out("G4-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("c b c s")
b8.out("K")

# 9. BOS #7  Christian Vázquez (X - X - X)
b8.new_ab()
b8.pitch_list("c f c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #76 Hector Velázquez
t9 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #39 Carson Smith
t9.pitching_substitution(76)

# 5. TBR #40 Wilson Ramos (X - X - X)
t9.new_ab()
t9.out("G6-3")

# 6. TBR #13 Brad Miller (X - X - X)
t9.new_ab()
t9.pitch_list("c f b")
t9.out("G3-1")

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.out("F8")


# Bot 9th
# Pitching: TBR #37 Alex Colomé
b9 = game.new_inning()

# Pitching change (TBR): #37 Alex Colomé replaces #46 José Alvarado
b9.pitching_substitution(37)

# 1. BOS #50 Mookie Betts (X - X - X)
b9.new_ab()
b9.pitch_list("c c")
b9.hit(1)
b9.advance(2, "16 BB")
b9.advance(4, "13 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b9.new_ab()
b9.pitch_list("c f d b b 1 f b")
b9.reach("BB")
b9.advance(2, "13 1B")
b9.advance(3, "28 DP6-3")
b9.advance(4, "2 2B")

# 3. BOS #13 Hanley Ramirez (X - 50 - 16)
b9.new_ab()
b9.pitch_list("s")
b9.hit(1, rbis=1)
b9.thrown_out(2, "28 DP6-3", 1, 37)

# 4. BOS #28 J.D. Martinez (X - 16 - 13)
b9.new_ab()
b9.pitch_list("b s f b")
b9.out("DP6-3")

# 5. BOS #2  Xander Bogaerts (16 - X - X)
b9.new_ab()
b9.pitch_list("b s f")
b9.hit(2, rbis=1)
b9.advance(3, "36 1B")

# 6. BOS #11 Rafael Devers (X - 2 - X)
b9.new_ab()
b9.pitch_list("v v v v")
b9.reach("IBB")
b9.advance(2, "36 1B")

# 7. BOS #36 Eduardo Núñez (X - 2 - 11)
b9.new_ab()
b9.pitch_list("b b f")
b9.hit(1)

# 8. BOS #19 Jackie Bradley Jr. (2 - 11 - 36)
b9.new_ab()
b9.pitch_list("c b f")
b9.out("G4-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #46 Craig Kimbrel
t10 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #76 Hector Velázquez
t10.pitching_substitution(46)

# Offensive change (TBR): Pinch-hitter #2 Denard Span replaces #28 Daniel Robertson, batting 8th
t10.offensive_substitution(8, 2, "PH")

# 8. TBR #2  Denard Span (X - X - X)
t10.new_ab()
t10.pitch_list("c b b")
t10.hit(1)
t10.advance(2, "0 G6-3")
t10.advance(3, "27 BB")

# 9. TBR #0  Mallex Smith (X - X - 2)
t10.new_ab()
t10.pitch_list("b")
t10.out("G6-3")

# 1. TBR #5  Matt Duffy (X - 2 - X)
t10.new_ab()
t10.pitch_list("b s s s")
t10.out("K")

# 2. TBR #39 Kevin Kiermaier (X - 2 - X)
t10.new_ab()
t10.pitch_list("b d b b")
t10.reach("BB")
t10.advance(2, "27 BB")

# 3. TBR #27 Carlos Gómez (X - 2 - 39)
t10.new_ab()
t10.pitch_list("d b b c b")
t10.reach("BB")

# 4. TBR #44 C.J. Cron (2 - 39 - 27)
t10.new_ab()
t10.pitch_list("b c c s")
t10.out("K")


# Bot 10th
# Pitching: TBR #36 Andrew Kittredge
b10 = game.new_inning()

# Pitching change (TBR): #36 Andrew Kittredge replaces #37 Alex Colomé
b10.pitching_substitution(36)

# Defensive change (TBR): #18 Joey Wendle replaces #2 Denard Span (PH), playing 2B, batting 8th
b10.defensive_substitution(8, 18, "4")

# 9. BOS #7  Christian Vázquez (X - X - X)
b10.new_ab()
b10.pitch_list("s s b")
b10.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b10.new_ab()
b10.pitch_list("c c f b s")
b10.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b10.new_ab()
b10.pitch_list("b b")
b10.out("F8")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: BOS #66 Bobby Poyner
t11 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #46 Craig Kimbrel
t11.pitching_substitution(66)

# 5. TBR #40 Wilson Ramos (X - X - X)
t11.new_ab()
t11.pitch_list("s f b f b b f s")
t11.out("K")

# 6. TBR #13 Brad Miller (X - X - X)
t11.new_ab()
t11.pitch_list("b s s f s")
t11.out("K")

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
t11.new_ab()
t11.pitch_list("b f c f b")
t11.out("L9")


# Bot 11th
# Pitching: TBR #36 Andrew Kittredge
b11 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
b11.new_ab()
b11.pitch_list("c f")
b11.out("G6-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
b11.new_ab()
b11.pitch_list("f b f")
b11.hit(1)
# Offensive change (BOS): Pinch-runner #23 Blake Swihart replaces #28 J.D. Martinez
b11.offensive_substitution(4, 23, "PR")
b11.atbase("PR")
b11.advance(2, "11 PB")
b11.thrown_out(3, "36 FC5", 3, 36)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b11.new_ab()
b11.pitch_list("d 1 b c")
b11.out("L5")

# 6. BOS #11 Rafael Devers (X - X - 23)
b11.new_ab()
b11.pitch_list("b v v v")
b11.pb()
b11.reach("IBB")
b11.advance(2, "36 FC5")

# 7. BOS #36 Eduardo Núñez (X - 23 - 11)
b11.new_ab()
b11.pitch_list("b b f b c")
b11.reach("FC5")


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: BOS #66 Bobby Poyner
t12 = game.new_inning()

# Defensive switch (BOS): #23 Blake Swihart moves to DH
t12.defensive_switch(23, "0")

# 8. TBR #18 Joey Wendle (X - X - X)
t12.new_ab()
t12.pitch_list("b f c")
t12.hit(1)
t12.advance(2, "0 SAC3-4")
t12.advance(3, "5 L9")

# 9. TBR #0  Mallex Smith (X - X - 18)
t12.new_ab()
t12.out("SAC3-4")

# 1. TBR #5  Matt Duffy (X - 18 - X)
t12.new_ab()
t12.out("L9")

# 2. TBR #39 Kevin Kiermaier (18 - X - X)
t12.new_ab()
t12.pitch_list("b f b s s")
t12.out("K")


# Bot 12th
# Pitching: TBR #36 Andrew Kittredge
b12 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b12.new_ab()
b12.pitch_list("c b b")
b12.hit(2)
b12.advance(3, "7 SAC1-4")
b12.advance(4, "13 1B")

# 9. BOS #7  Christian Vázquez (X - 19 - X)
b12.new_ab()
b12.out("SAC1-4")

# 1. BOS #50 Mookie Betts (19 - X - X)
b12.new_ab()
b12.pitch_list("v v v v")
b12.reach("IBB")
b12.advance(2, "16 SB")
b12.advance(3, "13 1B")

# Pitching change (TBR): #48 Ryan Yarbrough replaces #36 Andrew Kittredge
b12.pitching_substitution(48)

# 2. BOS #16 Andrew Benintendi (19 - X - 50)
b12.new_ab()
b12.pitch_list("c f b f f b b b")
b12.reach("BB")
b12.advance(2, "13 1B")

# 3. BOS #13 Hanley Ramirez (19 - 50 - 16)
b12.new_ab()
b12.hit(1, rbis=1)

# Winning team: BOS
# WP: BOS #66 Bobby Poyner
game.winning_pitcher(66)

# Loser team: TBR
# LP: TBR #36 Andrew Kittredge
game.losing_pitcher(36, is_away_team=True)

# print(game)
game.generate_scorecard()
