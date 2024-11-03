import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-03-29
# https://www.baseball-reference.com/boxes/TBA/TBA201803290.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/03/29/529406/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-03-29 16:00-19:00",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "31,042",
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
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 61, 66, 24],
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
            "bullpen": [39, 22, 61, 66, 37, 24, 46, 76, 64, 56, 32],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 22,
            "roster": {
                # Lineup
                5: "Matt Duffy",
                39: "Kevin Kiermaier",
                27: "Carlos Gómez",
                44: "C.J. Cron",
                40: "Wilson Ramos",
                2: "Denard Span",
                11: "Adeiny Hechavarría",
                28: "Daniel Robertson",
                8: "Rob Refsnyder",
                # Starting pitcher
                22: "Chris Archer",
                # Bench
                13: "Brad Miller",
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
                72: "Yonny Chirinos",
                35: "Matt Andriese",
                54: "Sergio Romo",
            },
            "lefties": [46, 48, 4],
            "lineup": [
                [5, "5"],
                [39, "8"],
                [27, "9"],
                [44, "3"],
                [40, "2"],
                [2, "7"],
                [11, "6"],
                [28, "4"],
                [8, "0"],
            ],
            "bench": [
                [13, "DH"],
                [18, "2B"],
                [0, "OF"],
                [45, "C"],
            ],
            "bullpen": [37, 46, 48, 52, 50, 36, 34, 4, 72, 35, 54],
        },
        "umpires": {
            "HP": "Jeff Nelson",
            "1B": "Laz Diaz",
            "2B": "Andy Fletcher",
            "3B": "Manny Gonzalez",
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
# Pitching: TBR #22 Chris Archer
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("f b s f b f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. TBR #5  Matt Duffy (X - X - X)
b1.new_ab()
b1.pitch_list("c c b b f s")
b1.out("K")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
b1.new_ab()
b1.pitch_list("b c f s")
b1.out("K")

# 3. TBR #27 Carlos Gómez (X - X - X)
b1.new_ab()
b1.pitch_list("f b")
b1.out("P6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #22 Chris Archer
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("b s b b f d")
t2.reach("BB")
t2.advance(3, "2 2B")
t2.advance(4, "11 G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t2.new_ab()
t2.pitch_list("b f b")
t2.hit(2)
t2.advance(3, "11 G6-3")
t2.advance(4, "36 HR")

# 6. BOS #11 Rafael Devers (28 - 2 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b s f b")
t2.out("G6-3", rbis=1)

# 7. BOS #36 Eduardo Núñez (2 - X - X)
t2.new_ab(is_risp=True)
t2.hit(4, rbis=2)

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.out("P6")

# 9. BOS #7  Christian Vázquez (X - X - X)
t2.new_ab()
t2.pitch_list("b c f b")
t2.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 7)
t2.new_ab()
t2.pitch_list("f f b d")
t2.out("(F)P3")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 4. TBR #44 C.J. Cron (X - X - X)
b2.new_ab()
b2.pitch_list("b c f s")
b2.out("K")

# 5. TBR #40 Wilson Ramos (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("G6-3")

# 6. TBR #2  Denard Span (X - X - X)
b2.new_ab()
b2.pitch_list("f b b b c b")
b2.reach("BB")
b2.advance(2, "11 1B")
b2.advance(3, "28 PB")

# 7. TBR #11 Adeiny Hechavarría (X - X - 2)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(1)
b2.advance(2, "28 PB")

# 8. TBR #28 Daniel Robertson (X - 2 - 11)
b2.new_ab(is_risp=True)
b2.pitch_list("c b c b f c")
b2.pb()
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #22 Chris Archer
t3 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("P3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t3.new_ab()
t3.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("c b s s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 9. TBR #8  Rob Refsnyder (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b b")
b3.reach("BB")

# 1. TBR #5  Matt Duffy (X - X - 8)
b3.new_ab()
b3.pitch_list("b b")
b3.out("F8")

# 2. TBR #39 Kevin Kiermaier (X - X - 8)
b3.new_ab()
b3.pitch_list("b f b f f b s")
b3.out("K")

# 3. TBR #27 Carlos Gómez (X - X - 8)
b3.new_ab()
b3.pitch_list("b s f f b")
b3.out("L8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #22 Chris Archer
t4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("c f f f b")
t4.hit(1)
t4.thrown_out(1, "11 DP9-3", 2, 22)

# 6. BOS #11 Rafael Devers (X - X - 2)
t4.new_ab()
t4.pitch_list("b b")
t4.out("DP9-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("c f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 4. TBR #44 C.J. Cron (X - X - X)
b4.new_ab()
b4.pitch_list("b f f b s")
b4.out("K")

# 5. TBR #40 Wilson Ramos (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("L8")

# 6. TBR #2  Denard Span (X - X - X)
b4.new_ab()
b4.out("L6")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #22 Chris Archer
t5 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.out("G3")

# 9. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G5-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("b c b c s")
t5.out("K")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
b5.new_ab()
b5.pitch_list("b s")
b5.out("G5-3")

# 8. TBR #28 Daniel Robertson (X - X - X)
b5.new_ab()
b5.pitch_list("c s s")
b5.out("K")

# 9. TBR #8  Rob Refsnyder (X - X - X)
b5.new_ab()
b5.pitch_list("f b b s b b")
b5.reach("BB")

# 1. TBR #5  Matt Duffy (X - X - 8)
b5.new_ab()
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #22 Chris Archer
t6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t6.new_ab()
t6.pitch_list("c b s b s")
t6.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("s b s f c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 2. TBR #39 Kevin Kiermaier (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G6-3")

# 3. TBR #27 Carlos Gómez (X - X - X)
b6.new_ab()
b6.pitch_list("s c b s")
b6.out("K")

# 4. TBR #44 C.J. Cron (X - X - X)
b6.new_ab()
b6.pitch_list("c s b b b f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #22 Chris Archer
t7 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("f f")
t7.hit(2)
t7.advance(4, "11 2B")

# 6. BOS #11 Rafael Devers (X - 2 - X)
t7.new_ab(is_risp=True)
t7.hit(2, rbis=1)

# Pitching change (TBR): #50 Austin Pruitt replaces #22 Chris Archer
t7.pitching_substitution(50)

# 7. BOS #36 Eduardo Núñez (X - 11 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c")
t7.out("G6-3")

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b c")
t7.out("P5")

# 9. BOS #7  Christian Vázquez (X - 11 - X)
t7.new_ab(is_risp=True)
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #32 Matt Barnes
b7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #41 Chris Sale
b7.pitching_substitution(32)

# 5. TBR #40 Wilson Ramos (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G5-3")

# 6. TBR #2  Denard Span (X - X - X)
b7.new_ab()
b7.pitch_list("c b c b")
b7.out("L9")

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
b7.new_ab()
b7.pitch_list("c b f f b")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #50 Austin Pruitt
t8 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("c c")
t8.hit(1)
t8.thrown_out(1, "13 2-3", 2, 50)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t8.new_ab()
t8.pitch_list("c 1 b 1 b b f f")
t8.out("F7")

# 3. BOS #13 Hanley Ramirez (X - X - 50)
t8.new_ab()
t8.pitch_list("b f 1 f d b f b")
t8.reach("BB")
t8.thrown_out(2, "28 FC5-4", 3, 50)

# 4. BOS #28 J.D. Martinez (X - X - 13)
t8.new_ab()
t8.pitch_list("s s")
t8.reach("FC5-4")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
b8.pitching_substitution(56)

# Defensive change (BOS): #18 Mitch Moreland replaces #13 Hanley Ramirez (1B), playing 1B, batting 3rd
b8.defensive_substitution(3, 18, "3")

# 8. TBR #28 Daniel Robertson (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c c f b")
b8.reach("BB")
b8.advance(4, "5 2B")

# 9. TBR #8  Rob Refsnyder (X - X - 28)
b8.new_ab()
b8.pitch_list("b b c s c")
b8.out("!K")

# 1. TBR #5  Matt Duffy (X - X - 28)
b8.new_ab()
b8.pitch_list("f c b b")
b8.hit(2, rbis=1)
b8.advance(3, "27 BB")
b8.advance(4, "13 BB")

# 2. TBR #39 Kevin Kiermaier (X - 5 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b b b 2 c s b")
b8.reach("BB")
b8.advance(2, "27 BB")
b8.advance(3, "13 BB")
b8.advance(4, "2 3B")

# 3. TBR #27 Carlos Gómez (X - 5 - 39)
b8.new_ab(is_risp=True)
b8.pitch_list("c d t b b b")
b8.reach("BB")
b8.advance(2, "13 BB")
b8.advance(4, "2 3B")

# Pitching change (BOS): #39 Carson Smith replaces #56 Joe Kelly
b8.pitching_substitution(39)

# Offensive change (TBR): Pinch-hitter #13 Brad Miller replaces #44 C.J. Cron, batting 4th
b8.offensive_substitution(4, 13, "PH")

# 4. TBR #13 Brad Miller (5 - 39 - 27)
b8.new_ab(is_risp=True)
b8.pitch_list("c b b d b")
b8.reach("BB", rbis=1)
b8.advance(4, "2 3B")

# 5. TBR #40 Wilson Ramos (39 - 27 - 13)
b8.new_ab(is_risp=True)
b8.pitch_list("c c s")
b8.out("K")

# 6. TBR #2  Denard Span (39 - 27 - 13)
b8.new_ab(is_risp=True)
b8.pitch_list("c b f d b f")
b8.hit(3, rbis=3)
b8.advance(4, "11 1B")

# 7. TBR #11 Adeiny Hechavarría (2 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b b")
b8.hit(1, rbis=1)

# Offensive change (TBR): Pinch-hitter #18 Joey Wendle replaces #28 Daniel Robertson, batting 8th
b8.offensive_substitution(8, 18, "PH")

# 8. TBR #18 Joey Wendle (X - X - 11)
b8.new_ab()
b8.pitch_list("c 1 1")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #37 Alex Colomé
t9 = game.new_inning()

# Pitching change (TBR): #37 Alex Colomé replaces #50 Austin Pruitt
t9.pitching_substitution(37)

# Defensive switch (TBR): #13 Brad Miller moves to 1B
t9.defensive_switch(13, "3")

# Defensive change (TBR): #0 Mallex Smith replaces #2 Denard Span (LF), playing LF, batting 6th
t9.defensive_substitution(6, 0, "7")

# Defensive switch (TBR): #18 Joey Wendle moves to 2B
t9.defensive_switch(18, "4")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("c s")
t9.out("L8")

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("b c f f b")
t9.out("G4-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(2)

# 8. BOS #19 Jackie Bradley Jr. (X - 36 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c d f d")
t9.out("G4-3")

# Winning team: TBR
# WP: TBR #50 Austin Pruitt
game.winning_pitcher(50)
# SV: TBR #37 Alex Colomé
game.save_pitcher(37)

# Loser team: BOS
# LP: BOS #39 Carson Smith
game.losing_pitcher(39, is_away_team=True)

# print(game)
game.generate_scorecard()
