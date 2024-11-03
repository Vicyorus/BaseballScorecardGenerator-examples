import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-05-23
# https://www.baseball-reference.com/boxes/TBA/TBA201805230.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/05/23/530134/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-23 19:10-22:20",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "10,194",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
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
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 31, 61, 66],
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
            "bullpen": [57, 35, 22, 41, 31, 61, 66, 37, 46, 56, 32],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Denard Span",
                44: "C.J. Cron",
                28: "Daniel Robertson",
                5: "Matt Duffy",
                1: "Willy Adames",
                10: "Johnny Field",
                8: "Rob Refsnyder",
                21: "Christian Arroyo",
                45: "Jesús Sucre",
                # Starting pitcher
                22: "Chris Archer",
                # Bench
                13: "Brad Miller",
                40: "Wilson Ramos",
                0: "Mallex Smith",
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
                38: "Vidal Nuño",
                35: "Matt Andriese",
                54: "Sergio Romo",
            },
            "lefties": [49, 46, 48, 53, 4, 38],
            "lineup": [
                [2, "7"],
                [44, "3"],
                [28, "0"],
                [5, "5"],
                [1, "6"],
                [10, "8"],
                [8, "9"],
                [21, "4"],
                [45, "2"],
            ],
            "bench": [
                [13, "DH"],
                [40, "C"],
                [0, "OF"],
            ],
            "bullpen": [49, 37, 46, 48, 53, 52, 50, 55, 4, 38, 35, 54],
        },
        "umpires": {
            "HP": "Dan Bellino",
            "1B": "Tom Hallion",
            "2B": "Phil Cuzzi",
            "3B": "Adam Hamari",
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
t1.pitch_list("c b f f b c")
t1.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c b")
t1.reach("BB")
t1.thrown_out(2, "13 DP4-6-3", 2, 22)

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t1.new_ab()
t1.out("DP4-6-3")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. TBR #2  Denard Span (X - X - X)
b1.new_ab()
b1.pitch_list("c b c f f s")
b1.out("K")

# 2. TBR #44 C.J. Cron (X - X - X)
b1.new_ab()
b1.pitch_list("c f b c")
b1.out("!K")

# 3. TBR #28 Daniel Robertson (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.hit(1)

# 4. TBR #5  Matt Duffy (X - X - 28)
b1.new_ab()
b1.pitch_list("b f c b b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #22 Chris Archer
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("b c b s c")
t2.out("!K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b c")
t2.out("!K")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("s b")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 5. TBR #1  Willy Adames (X - X - X)
b2.new_ab()
b2.pitch_list("c f s")
b2.out("K")

# 6. TBR #10 Johnny Field (X - X - X)
b2.new_ab()
b2.pitch_list("b s")
b2.out("G4-3")

# 7. TBR #8  Rob Refsnyder (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #22 Chris Archer
t3 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t3.new_ab()
t3.pitch_list("b c f")
t3.hit(1)
t3.advance(2, "7 G6-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 36)
t3.new_ab()
t3.pitch_list("b c s")
t3.out("P5")

# 9. BOS #7  Christian Vázquez (X - X - 36)
t3.new_ab()
t3.pitch_list("b 1 1")
t3.out("G6-3")

# 1. BOS #50 Mookie Betts (X - 36 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b c s b b")
t3.out("P6")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 8. TBR #21 Christian Arroyo (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f s")
b3.out("K")

# 9. TBR #45 Jesús Sucre (X - X - X)
b3.new_ab()
b3.pitch_list("b f b b b")
b3.reach("BB")
b3.thrown_out(2, "2 FC5-4", 2, 24)

# 1. TBR #2  Denard Span (X - X - 45)
b3.new_ab()
b3.pitch_list("f b f b")
b3.reach("FC5-4")

# 2. TBR #44 C.J. Cron (X - X - 2)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #22 Chris Archer
t4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.pitch_list("f f s")
t4.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("f b b f s")
t4.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("b s f f b b c")
t4.out("!K")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 3. TBR #28 Daniel Robertson (X - X - X)
b4.new_ab()
b4.pitch_list("b c f t")
b4.out("KT")

# 4. TBR #5  Matt Duffy (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G5-3")

# 5. TBR #1  Willy Adames (X - X - X)
b4.new_ab()
b4.pitch_list("s f c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #22 Chris Archer
t5 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("b s")
t5.out("(F)P3")

# 6. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("c f f b")
t5.out("G4-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("c f b b")
t5.hit(1)
t5.advance(3, "19 2B")
t5.thrown_out(4, "19 8-6-2", 3, 22)

# 8. BOS #19 Jackie Bradley Jr. (X - X - 36)
t5.new_ab()
t5.pitch_list("c t 1 b f")
t5.hit(2)


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# 6. TBR #10 Johnny Field (X - X - X)
b5.new_ab()
b5.pitch_list("c b b")
b5.out("G5-3")

# 7. TBR #8  Rob Refsnyder (X - X - X)
b5.new_ab()
b5.pitch_list("s b b f b b")
b5.reach("BB")
b5.thrown_out(2, "21 CS", 2, 24)

# 8. TBR #21 Christian Arroyo (X - X - 8)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1)

# 9. TBR #45 Jesús Sucre (X - X - 21)
b5.new_ab()
b5.pitch_list("b f")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #22 Chris Archer
t6 = game.new_inning()

# 9. BOS #7  Christian Vázquez (X - X - X)
t6.new_ab()
t6.hit(1)
t6.advance(2, "50 BB")
t6.advance(3, "16 BB")
t6.advance(4, "13 DP6-4-3")

# 1. BOS #50 Mookie Betts (X - X - 7)
t6.new_ab()
t6.pitch_list("b c b b c b")
t6.reach("BB")
t6.advance(2, "16 BB")
t6.advance(3, "13 DP6-4-3")

# 2. BOS #16 Andrew Benintendi (X - 7 - 50)
t6.new_ab(is_risp=True)
t6.pitch_list("b f b f b b")
t6.reach("BB")
t6.thrown_out(2, "13 DP6-4-3", 1, 22)

# 3. BOS #13 Hanley Ramirez (7 - 50 - 16)
t6.new_ab(is_risp=True)
t6.pitch_list("b")
t6.out("DP6-4-3")

# 4. BOS #28 J.D. Martinez (50 - X - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c b s f d")
t6.out("G5-3")


# Bot 6th
# Pitching: BOS #24 David Price
b6 = game.new_inning()

# 1. TBR #2  Denard Span (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b c b")
b6.reach("BB")
b6.advance(4, "44 2B")

# 2. TBR #44 C.J. Cron (X - X - 2)
b6.new_ab()
b6.hit(2, rbis=1)
b6.advance(3, "5 G6-3")

# 3. TBR #28 Daniel Robertson (X - 44 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b c b c b c")
b6.out("!K")

# 4. TBR #5  Matt Duffy (X - 44 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f f b b")
b6.out("G6-3")

# 5. TBR #1  Willy Adames (44 - X - X)
b6.new_ab(is_risp=True)
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #46 José Alvarado
t7 = game.new_inning()

# Pitching change (TBR): #46 José Alvarado replaces #22 Chris Archer
t7.pitching_substitution(46)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("c b b s b s")
t7.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("b f c b b s")
t7.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("b s b f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #32 Matt Barnes
b7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #24 David Price
b7.pitching_substitution(32)

# 6. TBR #10 Johnny Field (X - X - X)
b7.new_ab()
b7.pitch_list("c c b")
b7.out("G6-3")

# 7. TBR #8  Rob Refsnyder (X - X - X)
b7.new_ab()
b7.pitch_list("b b c c f f f c")
b7.out("!K")

# Offensive change (TBR): Pinch-hitter #13 Brad Miller replaces #21 Christian Arroyo, batting 8th
b7.offensive_substitution(8, 13, "PH")

# 8. TBR #13 Brad Miller (X - X - X)
b7.new_ab()
b7.pitch_list("s b s b f c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #46 José Alvarado
t8 = game.new_inning()

# Defensive switch (TBR): #13 Brad Miller moves to 2B
t8.defensive_switch(13, "4")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("c c b b c")
t8.out("!K")

# 9. BOS #7  Christian Vázquez (X - X - X)
t8.new_ab()
t8.pitch_list("c b c b f f b")
t8.out("(F)P3")

# Pitching change (TBR): #52 Chaz Roe replaces #46 José Alvarado
t8.pitching_substitution(52)

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b b")
t8.reach("BB")
t8.advance(2, "16 BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t8.new_ab()
t8.pitch_list("b b s 1 b b")
t8.reach("BB")

# 3. BOS #13 Hanley Ramirez (X - 50 - 16)
t8.new_ab(is_risp=True)
t8.pitch_list("c b b")
t8.out("F8")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
b8.pitching_substitution(56)

# 9. TBR #45 Jesús Sucre (X - X - X)
b8.new_ab()
b8.pitch_list("b b t")
b8.out("G4-3")

# 1. TBR #2  Denard Span (X - X - X)
b8.new_ab()
b8.pitch_list("c f")
b8.out("P5")

# 2. TBR #44 C.J. Cron (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #37 Alex Colomé
t9 = game.new_inning()

# Pitching change (TBR): #37 Alex Colomé replaces #52 Chaz Roe
t9.pitching_substitution(37)

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("b f t f")
t9.error(6)
t9.reach("E6", end_base=2)
t9.advance("U", "2 2B")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("f b s")
t9.hit(2, rbis=1)
t9.advance(3, "36 WP")
t9.advance(4, "36 SF8")

# 6. BOS #11 Rafael Devers (X - 2 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b b d")
t9.reach("BB")
t9.advance(2, "36 WP")
t9.advance(3, "36 SF8")
t9.advance("U", "19 PB")

# 7. BOS #36 Eduardo Núñez (X - 2 - 11)
t9.new_ab(is_risp=True)
t9.pitch_list("l f b")
t9.wp()
t9.out("SF8", rbis=1)

# 8. BOS #19 Jackie Bradley Jr. (11 - X - X)
t9.new_ab()
t9.pitch_list("c c b s")
t9.pb()
t9.out("K")

# Pitching change (TBR): #55 Ryne Stanek replaces #37 Alex Colomé
t9.pitching_substitution(55)

# 9. BOS #7  Christian Vázquez (X - X - X)
t9.new_ab()
t9.pitch_list("c f")
t9.out("F9")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
b9.pitching_substitution(46)

# 3. TBR #28 Daniel Robertson (X - X - X)
b9.new_ab()
b9.pitch_list("c s b s")
b9.out("K")

# 4. TBR #5  Matt Duffy (X - X - X)
b9.new_ab()
b9.pitch_list("b f")
b9.out("G1-3")

# 5. TBR #1  Willy Adames (X - X - X)
b9.new_ab()
b9.pitch_list("s c s")
b9.out("K")

# Winning team: BOS
# WP: BOS #56 Joe Kelly
game.winning_pitcher(56, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: TBR
# LP: TBR #37 Alex Colomé
game.losing_pitcher(37)

# print(game)
game.generate_scorecard()
