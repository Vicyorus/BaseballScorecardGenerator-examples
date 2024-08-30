import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TBA @ BOS, 2018-04-07
# https://www.baseball-reference.com/boxes/BOS/BOS201804070.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2018/04/07/529530/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-07 13:07-15:55",
        "at": "Fenway Park, Boston, MA",
        "att": "31,821",
        "temp": "43F, Cloudy",
        "wind": "14mph, Out To RF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 34,
            "roster": {
                # Lineup
                2: "Denard Span",
                0: "Mallex Smith",
                27: "Carlos Gómez",
                13: "Brad Miller",
                5: "Matt Duffy",
                44: "C.J. Cron",
                40: "Wilson Ramos",
                18: "Joey Wendle",
                11: "Adeiny Hechavarría",
                # Starting pitcher
                34: "Jake Faria",
                # Bench
                8: "Rob Refsnyder",
                39: "Kevin Kiermaier",
                28: "Daniel Robertson",
                45: "Jesús Sucre",
                # Bullpen
                37: "Alex Colomé",
                46: "José Alvarado",
                48: "Ryan Yarbrough",
                52: "Chaz Roe",
                50: "Austin Pruitt",
                36: "Andrew Kittredge",
                4: "Blake Snell",
                72: "Yonny Chirinos",
                35: "Matt Andriese",
                22: "Chris Archer",
                54: "Sergio Romo",
            },
            "lefties": [46, 48, 4],
            "lineup": [
                [2, "7"],
                [0, "9"],
                [27, "8"],
                [13, "3"],
                [5, "5"],
                [44, "0"],
                [40, "2"],
                [18, "4"],
                [11, "6"],
            ],
            "bench": [
                [8, "LF"],
                [39, "CF"],
                [28, "SS"],
                [45, "C"],
            ],
            "bullpen": [37, 46, 48, 52, 50, 36, 4, 72, 35, 22, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
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
                3: "Sandy León",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                39: "Carson Smith",
                41: "Chris Sale",
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
                [3, "2"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [39, 41, 61, 66, 37, 24, 46, 76, 64, 56, 32],
        },
        "umpires": {
            "HP": "Alan Porter",
            "1B": "Bill Miller",
            "2B": "Angel Hernandez",
            "3B": "Todd Tichenor",
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
# Pitching: BOS #22 Rick Porcello
t1 = game.new_inning()

# 1. TBR #2  Denard Span (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.hit(1)
t1.advance(3, "27 1B")
t1.advance(4, "13 2B")

# 2. TBR #0  Mallex Smith (X - X - 2)
t1.new_ab()
t1.pitch_list("f s f t")
t1.out("KT")

# 3. TBR #27 Carlos Gómez (X - X - 2)
t1.new_ab()
t1.pitch_list("1 1")
t1.hit(1)
t1.advance(4, "13 2B")

# 4. TBR #13 Brad Miller (2 - X - 27)
t1.new_ab()
t1.hit(2, rbis=2)

# 5. TBR #5  Matt Duffy (X - 13 - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("F9")

# 6. TBR #44 C.J. Cron (X - 13 - X)
t1.new_ab()
t1.pitch_list("b f f b s")
t1.out("K")


# Bot 1st
# Pitching: TBR #34 Jake Faria
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c b c b")
b1.hit(2)
b1.advance(3, "13 1B")
b1.advance(4, "28 SF8")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b1.new_ab()
b1.pitch_list("b d b b")
b1.reach("BB")
b1.advance(2, "13 1B")
b1.advance(3, "28 SF8")
b1.advance(4, "2 2B")

# 3. BOS #13 Hanley Ramirez (X - 50 - 16)
b1.new_ab()
b1.pitch_list("f f d")
b1.hit(1)
b1.advance(2, "28 SF8")
b1.advance(4, "2 2B")

# 4. BOS #28 J.D. Martinez (50 - 16 - 13)
b1.new_ab()
b1.pitch_list("b s b f f b")
b1.out("SF8", rbis=1)

# 5. BOS #2  Xander Bogaerts (16 - 13 - X)
b1.new_ab()
b1.pitch_list("c d 3 b c")
b1.hit(2, rbis=2)
b1.advance(4, "11 1B")

# 6. BOS #11 Rafael Devers (X - 2 - X)
b1.new_ab()
b1.pitch_list("c f f")
b1.hit(1, rbis=1)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
b1.new_ab()
b1.pitch_list("b b b c")
b1.out("P4")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 11)
b1.new_ab()
b1.pitch_list("b d c")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 7. TBR #40 Wilson Ramos (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b b b f f")
t2.out("G4-3")

# 8. TBR #18 Joey Wendle (X - X - X)
t2.new_ab()
t2.pitch_list("b f")
t2.hit(1)

# 9. TBR #11 Adeiny Hechavarría (X - X - 18)
t2.new_ab()
t2.pitch_list("c c b f f b s")
t2.out("K")

# 1. TBR #2  Denard Span (X - X - 18)
t2.new_ab()
t2.out("G3")


# Bot 2nd
# Pitching: TBR #34 Jake Faria
b2 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
b2.new_ab()
b2.pitch_list("b b c b")
b2.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b b")
b2.reach("BB")
b2.advance(2, "16 BB")
b2.advance(3, "28 BB")
b2.advance(4, "2 HR")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b2.new_ab()
b2.pitch_list("d 1 1 b b f b")
b2.reach("BB")
b2.advance(2, "28 BB")
b2.advance(4, "2 HR")

# 3. BOS #13 Hanley Ramirez (X - 50 - 16)
b2.new_ab()
b2.pitch_list("c")
b2.out("IF3")

# 4. BOS #28 J.D. Martinez (X - 50 - 16)
b2.new_ab()
b2.pitch_list("b b f b b")
b2.reach("BB")
b2.advance(4, "2 HR")

# 5. BOS #2  Xander Bogaerts (50 - 16 - 28)
b2.new_ab()
b2.pitch_list("c b b b f")
b2.hit(4, rbis=4)

# 6. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("b c f b f b b")
b2.reach("BB")
b2.advance(3, "36 2B")

# Pitching change (TBR): #50 Austin Pruitt replaces #34 Jake Faria
b2.pitching_substitution(50)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
b2.new_ab()
b2.pitch_list("b b b f c f")
b2.hit(2)

# 8. BOS #19 Jackie Bradley Jr. (11 - 36 - X)
b2.new_ab()
b2.out("L4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 2. TBR #0  Mallex Smith (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("P4")

# 3. TBR #27 Carlos Gómez (X - X - X)
t3.new_ab()
t3.pitch_list("c b f")
t3.out("P6")

# 4. TBR #13 Brad Miller (X - X - X)
t3.new_ab()
t3.pitch_list("b f")
t3.out("G6-3")


# Bot 3rd
# Pitching: TBR #50 Austin Pruitt
b3 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("s")
b3.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c b t f b f f c")
b3.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("s b")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 5. TBR #5  Matt Duffy (X - X - X)
t4.new_ab()
t4.pitch_list("c t b s")
t4.out("K")

# 6. TBR #44 C.J. Cron (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G5-3")

# 7. TBR #40 Wilson Ramos (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G5-3")


# Bot 4th
# Pitching: TBR #50 Austin Pruitt
b4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
b4.new_ab()
b4.out("F8")

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("b b f f t")
b4.out("KT")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c f b")
b4.reach("BB")

# 6. BOS #11 Rafael Devers (X - X - 2)
b4.new_ab()
b4.pitch_list("f")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 8. TBR #18 Joey Wendle (X - X - X)
t5.new_ab()
t5.pitch_list("b b c s s")
t5.out("K")

# 9. TBR #11 Adeiny Hechavarría (X - X - X)
t5.new_ab()
t5.pitch_list("s")
t5.out("G5-3")

# 1. TBR #2  Denard Span (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("L8")


# Bot 5th
# Pitching: TBR #50 Austin Pruitt
b5 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("F7")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G6-3")

# 9. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# 2. TBR #0  Mallex Smith (X - X - X)
t6.new_ab()
t6.pitch_list("b b c f c")
t6.out("!K")

# 3. TBR #27 Carlos Gómez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G5-3")

# 4. TBR #13 Brad Miller (X - X - X)
t6.new_ab()
t6.pitch_list("b f b b")
t6.out("L8")


# Bot 6th
# Pitching: TBR #50 Austin Pruitt
b6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("b b c")
b6.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("f b c b")
b6.out("G5-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b6.new_ab()
b6.pitch_list("b b f b")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Rick Porcello
t7 = game.new_inning()

# 5. TBR #5  Matt Duffy (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("F9")

# 6. TBR #44 C.J. Cron (X - X - X)
t7.new_ab()
t7.out("G6-3")

# 7. TBR #40 Wilson Ramos (X - X - X)
t7.new_ab()
t7.pitch_list("c b s b b s")
t7.out("K")


# Bot 7th
# Pitching: TBR #52 Chaz Roe
b7 = game.new_inning()

# Pitching change (TBR): #52 Chaz Roe replaces #50 Austin Pruitt
b7.pitching_substitution(52)

# 4. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.hit(4, rbis=1)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("b f b c f s")
b7.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("s b b c")
b7.hit(4, rbis=1)

# 7. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b f s b")
b7.hit(1)
b7.advance(2, "19 G4-3")

# Pitching change (TBR): #54 Sergio Romo replaces #52 Chaz Roe
b7.pitching_substitution(54)

# 8. BOS #19 Jackie Bradley Jr. (X - X - 36)
b7.new_ab()
b7.pitch_list("d b f")
b7.out("G4-3")

# 9. BOS #3  Sandy León (X - 36 - X)
b7.new_ab()
b7.pitch_list("f d b s")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #22 Rick Porcello
t8 = game.new_inning()

# Defensive change (BOS): #12 Brock Holt replaces #50 Mookie Betts (RF), playing RF, batting 1st
t8.defensive_substitution(1, 12, "9")

# 8. TBR #18 Joey Wendle (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.hit(2)
t8.advance(4, "2 1B")

# 9. TBR #11 Adeiny Hechavarría (X - 18 - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G6-3")

# 1. TBR #2  Denard Span (X - 18 - X)
t8.new_ab()
t8.pitch_list("b c t")
t8.hit(1, rbis=1)
t8.thrown_out(2, "0 DP1-6-3", 2, 64)

# Pitching change (BOS): #64 Marcus Walden replaces #22 Rick Porcello
t8.pitching_substitution(64)

# 2. TBR #0  Mallex Smith (X - X - 2)
t8.new_ab()
t8.pitch_list("s b s b")
t8.out("DP1-6-3")


# Bot 8th
# Pitching: TBR #28 Daniel Robertson
b8 = game.new_inning()

# Pitching change (TBR): #28 Daniel Robertson replaces #54 Sergio Romo
b8.pitching_substitution(28)

# 1. BOS #12 Brock Holt (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.out("P4")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("c b f f b")
b8.out("L8")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #13 Hanley Ramirez, batting 3rd
b8.offensive_substitution(3, 23, "PH")

# 3. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.out("L7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #64 Marcus Walden
t9 = game.new_inning()

# Defensive switch (BOS): #23 Blake Swihart moves to 1B
t9.defensive_switch(23, "3")

# 3. TBR #27 Carlos Gómez (X - X - X)
t9.new_ab()
t9.pitch_list("f f s")
t9.out("K")

# 4. TBR #13 Brad Miller (X - X - X)
t9.new_ab()
t9.out("F7")

# 5. TBR #5  Matt Duffy (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22)

# Loser team: TBR
# LP: TBR #34 Jake Faria
game.losing_pitcher(34, is_away_team=True)

# print(game)
game.generate_scorecard()
