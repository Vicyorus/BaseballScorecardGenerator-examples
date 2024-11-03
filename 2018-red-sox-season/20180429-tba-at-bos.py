import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TBA @ BOS, 2018-04-29
# https://www.baseball-reference.com/boxes/BOS/BOS201804290.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2018/04/29/529828/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-29 13:08-16:09",
        "at": "Fenway Park, Boston, MA",
        "att": "32,888",
        "temp": "52F, Cloudy",
        "wind": "7mph, Out To LF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 35,
            "roster": {
                # Lineup
                2: "Denard Span",
                44: "C.J. Cron",
                18: "Joey Wendle",
                13: "Brad Miller",
                28: "Daniel Robertson",
                0: "Mallex Smith",
                11: "Adeiny Hechavarría",
                45: "Jesús Sucre",
                10: "Johnny Field",
                # Starting pitcher
                35: "Matt Andriese",
                # Bench
                40: "Wilson Ramos",
                27: "Carlos Gómez",
                5: "Matt Duffy",
                8: "Rob Refsnyder",
                # Bullpen
                52: "Chaz Roe",
                49: "Jonny Venters",
                37: "Alex Colomé",
                46: "José Alvarado",
                36: "Andrew Kittredge",
                34: "Jake Faria",
                4: "Blake Snell",
                58: "Chih-Wei Hu",
                22: "Chris Archer",
                54: "Sergio Romo",
            },
            "lefties": [49, 46, 4],
            "lineup": [
                [2, "7"],
                [44, "0"],
                [18, "4"],
                [13, "3"],
                [28, "5"],
                [0, "8"],
                [11, "6"],
                [45, "2"],
                [10, "9"],
            ],
            "bench": [
                [40, "C"],
                [27, "CF"],
                [5, "3B"],
                [8, "LF"],
            ],
            "bullpen": [52, 49, 37, 46, 36, 34, 4, 58, 22, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                36: "Eduardo Núñez",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                11: "Rafael Devers",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                5: "Tzu-Wei Lin",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                23: "Blake Swihart",
                50: "Mookie Betts",
                2: "Xander Bogaerts",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                39: "Carson Smith",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [57, 24, 41, 31, 61],
            "lineup": [
                [36, "4"],
                [16, "8"],
                [13, "0"],
                [28, "7"],
                [18, "3"],
                [11, "5"],
                [19, "9"],
                [3, "2"],
                [5, "6"],
            ],
            "bench": [
                [23, "C"],
                [50, "SS"],
                [2, "2B"],
                [7, "C"],
            ],
            "bullpen": [57, 24, 46, 76, 39, 41, 31, 61, 32, 37],
        },
        "umpires": {
            "HP": "Jim Wolf",
            "1B": "D.J. Reyburn",
            "2B": "Sam Holbrook",
            "3B": "Ryan Blakney",
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
t1.pitch_list("c c f f b f f")
t1.out("F8")

# 2. TBR #44 C.J. Cron (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.out("G5-3")

# 3. TBR #18 Joey Wendle (X - X - X)
t1.new_ab()
t1.out("G4-3")


# Bot 1st
# Pitching: TBR #35 Matt Andriese
b1 = game.new_inning()

# 1. BOS #36 Eduardo Núñez (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b f")
b1.out("F7")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b1.new_ab()
b1.pitch_list("b s c b b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 4. TBR #13 Brad Miller (X - X - X)
t2.new_ab()
t2.pitch_list("f b f b b f f f f t")
t2.out("KT")

# 5. TBR #28 Daniel Robertson (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G5-3")

# 6. TBR #0  Mallex Smith (X - X - X)
t2.new_ab()
t2.pitch_list("c f b c")
t2.out("!K")


# Bot 2nd
# Pitching: TBR #35 Matt Andriese
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.hit(1)

# 5. BOS #18 Mitch Moreland (X - X - 28)
b2.new_ab()
b2.pitch_list("b d")
b2.out("F9")

# 6. BOS #11 Rafael Devers (X - X - 28)
b2.new_ab()
b2.pitch_list("c f b s")
b2.out("K")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 28)
b2.new_ab()
b2.pitch_list("c d s")
b2.out("G3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
t3.new_ab()
t3.pitch_list("c b f")
t3.hit(1)
t3.error(1)
t3.advance(2, "45 POE1")
t3.advance(4, "2 HR")

# 8. TBR #45 Jesús Sucre (X - X - 11)
t3.new_ab(is_risp=True)
t3.pitch_list("b f 1 1 1 b s")
t3.out("F8")

# 9. TBR #10 Johnny Field (X - 11 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b")
t3.out("(F)P3")

# 1. TBR #2  Denard Span (X - 11 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("s d")
t3.hit(4, rbis=2)

# 2. TBR #44 C.J. Cron (X - X - X)
t3.new_ab()
t3.pitch_list("b s b c")
t3.out("G4-3")


# Bot 3rd
# Pitching: TBR #35 Matt Andriese
b3 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("f c f")
b3.out("F7")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b3.new_ab()
b3.pitch_list("c s b")
b3.out("F8")

# 1. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("f c b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 3. TBR #18 Joey Wendle (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("F9")

# 4. TBR #13 Brad Miller (X - X - X)
t4.new_ab()
t4.pitch_list("c s")
t4.hit(2)
t4.advance(4, "0 1B")

# 5. TBR #28 Daniel Robertson (X - 13 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c b b t f f f s")
t4.out("K")

# 6. TBR #0  Mallex Smith (X - 13 - X)
t4.new_ab(is_risp=True)
t4.hit(1, rbis=1)
t4.thrown_out(1, "11 PO", 3, 22)

# 7. TBR #11 Adeiny Hechavarría (X - X - 0)
t4.new_ab()
t4.pitch_list("f 1 1")
t4.no_ab("PO")


# Bot 4th
# Pitching: TBR #35 Matt Andriese
b4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.pitch_list("b b f b c f")
b4.out("L4")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b4.new_ab()
b4.pitch_list("f f f b b b")
b4.reach("HBP")
b4.advance(2, "28 1B")

# 4. BOS #28 J.D. Martinez (X - X - 13)
b4.new_ab()
b4.pitch_list("b f")
b4.hit(1)

# Pitching change (TBR): #49 Jonny Venters replaces #35 Matt Andriese
b4.pitching_substitution(49)

# 5. BOS #18 Mitch Moreland (X - 13 - 28)
b4.new_ab(is_risp=True)
b4.pitch_list("b s")
b4.out("F8")

# 6. BOS #11 Rafael Devers (X - 13 - 28)
b4.new_ab(is_risp=True)
b4.pitch_list("b f b")
b4.out("P4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
t5.new_ab()
t5.pitch_list("f l")
t5.out("G5-3")

# 8. TBR #45 Jesús Sucre (X - X - X)
t5.new_ab()
t5.pitch_list("c c b")
t5.out("G1-3")

# 9. TBR #10 Johnny Field (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G6-3")


# Bot 5th
# Pitching: TBR #49 Jonny Venters
b5 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G4-3")

# Pitching change (TBR): #36 Andrew Kittredge replaces #49 Jonny Venters
b5.pitching_substitution(36)

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("f b b f")
b5.out("F7")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("L7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# 1. TBR #2  Denard Span (X - X - X)
t6.new_ab()
t6.pitch_list("c f b b b c")
t6.out("!K")

# 2. TBR #44 C.J. Cron (X - X - X)
t6.new_ab()
t6.pitch_list("b s b s s")
t6.out("K")

# 3. TBR #18 Joey Wendle (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)

# 4. TBR #13 Brad Miller (X - X - 18)
t6.new_ab()
t6.out("G6-3")


# Bot 6th
# Pitching: TBR #36 Andrew Kittredge
b6 = game.new_inning()

# 1. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c c f b b")
b6.hit(1)
b6.advance(2, "16 BB")
b6.advance(3, "13 1B")
b6.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 36)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.advance(2, "13 1B")
b6.advance(4, "28 1B")

# 3. BOS #13 Hanley Ramirez (X - 36 - 16)
b6.new_ab(is_risp=True)
b6.pitch_list("b b c")
b6.hit(1)
b6.advance(2, "28 1B")
b6.advance(3, "18 BB")
b6.advance(4, "19 SF9")

# 4. BOS #28 J.D. Martinez (36 - 16 - 13)
b6.new_ab(is_risp=True)
b6.pitch_list("b s b")
b6.hit(1, rbis=2)
b6.advance(2, "18 BB")
b6.advance(3, "19 SF9")

# 5. BOS #18 Mitch Moreland (X - 13 - 28)
b6.new_ab(is_risp=True)
b6.pitch_list("b b b b")
b6.reach("BB")
b6.advance(2, "3 SB")

# Pitching change (TBR): #54 Sergio Romo replaces #36 Andrew Kittredge
b6.pitching_substitution(54)

# 6. BOS #11 Rafael Devers (13 - 28 - 18)
b6.new_ab(is_risp=True)
b6.pitch_list("c f d d c")
b6.out("!K")

# 7. BOS #19 Jackie Bradley Jr. (13 - 28 - 18)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.out("SF9", rbis=1)

# 8. BOS #3  Sandy León (28 - X - 18)
b6.new_ab(is_risp=True)
b6.pitch_list("c b s")
b6.reach("HBP")

# 9. BOS #5  Tzu-Wei Lin (28 - 18 - 3)
b6.new_ab(is_risp=True)
b6.pitch_list("c")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Rick Porcello
t7 = game.new_inning()

# 5. TBR #28 Daniel Robertson (X - X - X)
t7.new_ab()
t7.pitch_list("b c b f")
t7.hit(1)
t7.advance(2, "11 G4-6-3")

# 6. TBR #0  Mallex Smith (X - X - 28)
t7.new_ab()
t7.pitch_list("c b b f")
t7.out("L7")

# 7. TBR #11 Adeiny Hechavarría (X - X - 28)
t7.new_ab()
t7.pitch_list("f s b 1")
t7.out("G4-6-3")

# 8. TBR #45 Jesús Sucre (X - 28 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("t")
t7.out("L9")


# Bot 7th
# Pitching: TBR #54 Sergio Romo
b7 = game.new_inning()

# 1. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("s b s s")
b7.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F9")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b7.new_ab()
b7.pitch_list("b f s t")
b7.out("KT")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #22 Rick Porcello
t8 = game.new_inning()

# 9. TBR #10 Johnny Field (X - X - X)
t8.new_ab()
t8.pitch_list("c b c f s")
t8.out("K")

# 1. TBR #2  Denard Span (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.out("F7")

# 2. TBR #44 C.J. Cron (X - X - X)
t8.new_ab()
t8.pitch_list("c b b f b")
t8.hit(1)
t8.advance(3, "18 2B")

# Pitching change (BOS): #46 Craig Kimbrel replaces #22 Rick Porcello
t8.pitching_substitution(46)

# 3. TBR #18 Joey Wendle (X - X - 44)
t8.new_ab()
t8.pitch_list("b c b s f")
t8.hit(2)

# 4. TBR #13 Brad Miller (44 - 18 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("f s s")
t8.out("K")


# Bot 8th
# Pitching: TBR #37 Alex Colomé
b8 = game.new_inning()

# Pitching change (TBR): #37 Alex Colomé replaces #54 Sergio Romo
b8.pitching_substitution(37)

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("c f b f b f b")
b8.hit(1)
b8.advance(2, "19 BB")
b8.advance(4, "3 1B")

# 5. BOS #18 Mitch Moreland (X - X - 28)
b8.new_ab()
b8.pitch_list("f 1 b s s")
b8.out("K")

# 6. BOS #11 Rafael Devers (X - X - 28)
b8.new_ab()
b8.out("L7")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 28)
b8.new_ab()
b8.pitch_list("b c d b b")
b8.reach("BB")
b8.advance(3, "3 1B")

# 8. BOS #3  Sandy León (X - 28 - 19)
b8.new_ab(is_risp=True)
b8.hit(1, rbis=1)
b8.advance(2, "5 SB")

# 9. BOS #5  Tzu-Wei Lin (19 - X - 3)
b8.new_ab(is_risp=True)
b8.pitch_list("c b s b")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# 5. TBR #28 Daniel Robertson (X - X - X)
t9.new_ab()
t9.pitch_list("c s b b b")
t9.hit(1)
t9.advance(2, "0 1B")
t9.advance(3, "11 SAC3")

# 6. TBR #0  Mallex Smith (X - X - 28)
t9.new_ab()
t9.pitch_list("s c")
t9.hit(1)
t9.advance(2, "11 SAC3")

# 7. TBR #11 Adeiny Hechavarría (X - 28 - 0)
t9.new_ab(is_risp=True)
t9.out("SAC3")

# 8. TBR #45 Jesús Sucre (28 - 0 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("f b f s")
t9.out("K")

# Offensive change (TBR): Pinch-hitter #27 Carlos Gómez replaces #10 Johnny Field, batting 9th
t9.offensive_substitution(9, 27, "PH")

# 9. TBR #27 Carlos Gómez (28 - 0 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c s s")
t9.out("K")

# Winning team: BOS
# WP: BOS #46 Craig Kimbrel
game.winning_pitcher(46)

# Loser team: TBR
# LP: TBR #37 Alex Colomé
game.losing_pitcher(37, is_away_team=True)

# print(game)
game.generate_scorecard()
