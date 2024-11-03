import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-08-24
# https://www.baseball-reference.com/boxes/TBA/TBA201808240.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/08/24/531328/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-24 19:10-22:20",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "19,723",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 76,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                5: "Ian Kinsler",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                76: "Hector Velázquez",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "0"],
                [16, "7"],
                [25, "3"],
                [28, "9"],
                [2, "6"],
                [5, "4"],
                [36, "5"],
                [23, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 24, 46, 70, 56, 17, 32],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 63,
            "roster": {
                # Lineup
                18: "Joey Wendle",
                5: "Matt Duffy",
                9: "Jake Bauers",
                26: "Ji Man Choi",
                1: "Willy Adames",
                39: "Kevin Kiermaier",
                27: "Carlos Gómez",
                35: "Brandon Lowe",
                43: "Michael Pérez",
                # Starting pitcher
                63: "Diego Castillo",
                # Bench
                45: "Jesús Sucre",
                29: "Tommy Pham",
                44: "C.J. Cron",
                # Bullpen
                52: "Chaz Roe",
                46: "José Alvarado",
                20: "Tyler Glasnow",
                55: "Ryne Stanek",
                61: "Hunter Wood",
                42: "Blake Snell",
                48: "Ryan Yarbrough",
                68: "Jalen Beeks",
                72: "Yonny Chirinos",
                56: "Adam Kolarek",
                54: "Sergio Romo",
            },
            "lefties": [46, 42, 48, 68, 56],
            "lineup": [
                [18, "4"],
                [5, "5"],
                [9, "3"],
                [26, "0"],
                [1, "6"],
                [39, "8"],
                [27, "9"],
                [35, "7"],
                [43, "2"],
            ],
            "bench": [
                [45, "C"],
                [29, "LF"],
                [44, "1B"],
            ],
            "bullpen": [52, 46, 20, 55, 61, 42, 48, 68, 72, 56, 54],
        },
        "umpires": {
            "HP": "Angel Hernandez",
            "1B": "Alan Porter",
            "2B": "Todd Tichenor",
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
# Pitching: TBR #63 Diego Castillo
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("f f c")
t1.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("s f s")
t1.out("K")

# 3. BOS #25 Steve Pearce (X - X - X)
t1.new_ab()
t1.pitch_list("b b c b c")
t1.out("P3")


# Bot 1st
# Pitching: BOS #76 Hector Velázquez
b1 = game.new_inning()

# 1. TBR #18 Joey Wendle (X - X - X)
b1.new_ab()
b1.pitch_list("c t b b f")
b1.out("P5")

# 2. TBR #5  Matt Duffy (X - X - X)
b1.new_ab()
b1.pitch_list("f b t s")
b1.out("K")

# 3. TBR #9  Jake Bauers (X - X - X)
b1.new_ab()
b1.pitch_list("f f f b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #63 Diego Castillo
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("f c s")
t2.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.advance(3, "36 1B")

# 6. BOS #5  Ian Kinsler (X - X - 2)
t2.new_ab()
t2.pitch_list("c s b f f s")
t2.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
t2.new_ab()
t2.pitch_list("b c")
t2.hit(1)

# Pitching change (TBR): #68 Jalen Beeks replaces #63 Diego Castillo
t2.pitching_substitution(68)

# 8. BOS #23 Blake Swihart (2 - X - 36)
t2.new_ab(is_risp=True)
t2.pitch_list("b b s")
t2.out("F7")


# Bot 2nd
# Pitching: BOS #76 Hector Velázquez
b2 = game.new_inning()

# 4. TBR #26 Ji Man Choi (X - X - X)
b2.new_ab()
b2.pitch_list("s")
b2.hit(2)
b2.advance(3, "27 SB")
b2.advance(4, "27 G5-3")

# 5. TBR #1  Willy Adames (X - 26 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b c b d f b")
b2.reach("BB")
b2.advance(2, "27 SB")
b2.advance(3, "27 G5-3")
b2.advance(4, "43 2B")

# 6. TBR #39 Kevin Kiermaier (X - 26 - 1)
b2.new_ab(is_risp=True)
b2.pitch_list("f s b b t")
b2.out("KT")

# 7. TBR #27 Carlos Gómez (X - 26 - 1)
b2.new_ab(is_risp=True)
b2.pitch_list("b d f")
b2.out("G5-3", rbis=1)

# 8. TBR #35 Brandon Lowe (1 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f b b f b b")
b2.reach("BB")
b2.advance(4, "43 2B")

# 9. TBR #43 Michael Pérez (1 - X - 35)
b2.new_ab(is_risp=True)
b2.pitch_list("f f")
b2.hit(2, rbis=2)

# 1. TBR #18 Joey Wendle (X - 43 - X)
b2.new_ab(is_risp=True)
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #68 Jalen Beeks
t3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b c f b f b f c")
t3.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(2, "25 1B")
t3.advance(3, "28 1B")
t3.advance(4, "2 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t3.new_ab()
t3.pitch_list("1 b b s s s")
t3.out("K")

# 3. BOS #25 Steve Pearce (X - X - 50)
t3.new_ab()
t3.pitch_list("b s b s")
t3.hit(1)
t3.advance(2, "28 1B")
t3.advance(4, "2 1B")

# 4. BOS #28 J.D. Martinez (X - 50 - 25)
t3.new_ab(is_risp=True)
t3.pitch_list("s")
t3.hit(1)
t3.advance(2, "2 1B")

# 5. BOS #2  Xander Bogaerts (50 - 25 - 28)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.hit(1, rbis=2)

# 6. BOS #5  Ian Kinsler (X - 28 - 2)
t3.new_ab(is_risp=True)
t3.out("P4")


# Bot 3rd
# Pitching: BOS #76 Hector Velázquez
b3 = game.new_inning()

# 2. TBR #5  Matt Duffy (X - X - X)
b3.new_ab()
b3.pitch_list("c c b f b")
b3.hit(1)
b3.thrown_out(2, "9 CS", 1, 76)

# 3. TBR #9  Jake Bauers (X - X - 5)
b3.new_ab()
b3.pitch_list("f 1 1 b s s")
b3.out("K")

# 4. TBR #26 Ji Man Choi (X - X - X)
b3.new_ab()
b3.pitch_list("b c b")
b3.hit(1)
b3.advance(2, "1 1B")
b3.advance("U", "39 E3")

# 5. TBR #1  Willy Adames (X - X - 26)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.advance(3, "39 E3")
b3.advance("U", "27 1B")

# 6. TBR #39 Kevin Kiermaier (X - 26 - 1)
b3.new_ab(is_risp=True)
b3.pitch_list("b f")
b3.error(3)
b3.reach("E3")
b3.advance(2, "27 1B")
b3.advance("U", "35 1B")

# 7. TBR #27 Carlos Gómez (1 - X - 39)
b3.new_ab(is_risp=True)
b3.hit(1, rbis=1)
b3.advance(3, "35 1B")
b3.advance("U", "43 1B")

# 8. TBR #35 Brandon Lowe (X - 39 - 27)
b3.new_ab(is_risp=True)
b3.pitch_list("f b f")
b3.hit(1, rbis=1)
b3.advance(2, "43 SB")
b3.advance("U", "43 1B")

# 9. TBR #43 Michael Pérez (27 - X - 35)
b3.new_ab(is_risp=True)
b3.pitch_list("s f f b b")
b3.hit(1, rbis=2)

# Pitching change (BOS): #31 Drew Pomeranz replaces #76 Hector Velázquez
b3.pitching_substitution(31)

# 1. TBR #18 Joey Wendle (X - X - 43)
b3.new_ab()
b3.pitch_list("b c c d 1 f")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #68 Jalen Beeks
t4 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.out("(F)F9")

# 8. BOS #23 Blake Swihart (X - X - X)
t4.new_ab()
t4.pitch_list("b s f b s")
t4.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("L7")


# Bot 4th
# Pitching: BOS #31 Drew Pomeranz
b4 = game.new_inning()

# 2. TBR #5  Matt Duffy (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("P4")

# 3. TBR #9  Jake Bauers (X - X - X)
b4.new_ab()
b4.pitch_list("c f f b f")
b4.out("G4-3")

# 4. TBR #26 Ji Man Choi (X - X - X)
b4.new_ab()
b4.pitch_list("b b b b")
b4.reach("BB")
b4.advance(4, "1 HR")

# 5. TBR #1  Willy Adames (X - X - 26)
b4.new_ab()
b4.pitch_list("b")
b4.hit(4, rbis=2)

# 6. TBR #39 Kevin Kiermaier (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #68 Jalen Beeks
t5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("c b b c f")
t5.hit(1)
t5.advance(2, "25 1B")
t5.advance(4, "28 1B")

# 3. BOS #25 Steve Pearce (X - X - 16)
t5.new_ab()
t5.pitch_list("c f b b")
t5.hit(1)
t5.advance(3, "28 1B")

# 4. BOS #28 J.D. Martinez (X - 16 - 25)
t5.new_ab(is_risp=True)
t5.pitch_list("c b b c")
t5.hit(1, rbis=1)
t5.thrown_out(2, "2 DP6-4-3", 2, 68)

# 5. BOS #2  Xander Bogaerts (25 - X - 28)
t5.new_ab(is_risp=True)
t5.pitch_list("s f f f")
t5.out("DP6-4-3")


# Bot 5th
# Pitching: BOS #31 Drew Pomeranz
b5 = game.new_inning()

# 7. TBR #27 Carlos Gómez (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c s s")
b5.out("K")

# 8. TBR #35 Brandon Lowe (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b b f f b")
b5.reach("BB")
b5.thrown_out(2, "18 FC4-6", 3, 31)

# 9. TBR #43 Michael Pérez (X - X - 35)
b5.new_ab()
b5.pitch_list("b b f f")
b5.out("F8")

# 1. TBR #18 Joey Wendle (X - X - 35)
b5.new_ab()
b5.pitch_list("b f")
b5.reach("FC4-6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #68 Jalen Beeks
t6 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
t6.new_ab()
t6.pitch_list("b f c")
t6.hit(1)
t6.thrown_out(2, "23 FC5-4", 2, 68)

# 7. BOS #36 Eduardo Núñez (X - X - 5)
t6.new_ab()
t6.out("L6")

# 8. BOS #23 Blake Swihart (X - X - 5)
t6.new_ab()
t6.pitch_list("f b s")
t6.reach("FC5-4")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 23)
t6.new_ab()
t6.pitch_list("c c d d s")
t6.out("K")


# Bot 6th
# Pitching: BOS #31 Drew Pomeranz
b6 = game.new_inning()

# 2. TBR #5  Matt Duffy (X - X - X)
b6.new_ab()
b6.pitch_list("c b f f b")
b6.out("G6-3")

# 3. TBR #9  Jake Bauers (X - X - X)
b6.new_ab()
b6.pitch_list("b f c")
b6.out("(F)P2")

# 4. TBR #26 Ji Man Choi (X - X - X)
b6.new_ab()
b6.pitch_list("f f b b b")
b6.out("P6")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #68 Jalen Beeks
t7 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")
t7.thrown_out(2, "16 DP4-6-3", 1, 68)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t7.new_ab()
t7.pitch_list("b c f f b")
t7.out("DP4-6-3")

# 3. BOS #25 Steve Pearce (X - X - X)
t7.new_ab()
t7.pitch_list("s b b b f b")
t7.reach("BB")

# 4. BOS #28 J.D. Martinez (X - X - 25)
t7.new_ab()
t7.pitch_list("f b")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #31 Drew Pomeranz
b7 = game.new_inning()

# 5. TBR #1  Willy Adames (X - X - X)
b7.new_ab()
b7.pitch_list("b c f s")
b7.out("K")

# 6. TBR #39 Kevin Kiermaier (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G6-3")

# 7. TBR #27 Carlos Gómez (X - X - X)
b7.new_ab()
b7.pitch_list("s t b f b")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #61 Hunter Wood
t8 = game.new_inning()

# Pitching change (TBR): #61 Hunter Wood replaces #68 Jalen Beeks
t8.pitching_substitution(61)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b")
t8.hit(1)
t8.advance(2, "5 1B")
t8.advance(3, "23 1B")

# 6. BOS #5  Ian Kinsler (X - X - 2)
t8.new_ab()
t8.pitch_list("b c f d f")
t8.hit(1)
t8.advance(2, "23 1B")
t8.thrown_out(3, "50 FC5", 3, 61)

# 7. BOS #36 Eduardo Núñez (X - 2 - 5)
t8.new_ab(is_risp=True)
t8.pitch_list("s b b c f s")
t8.out("K")

# 8. BOS #23 Blake Swihart (X - 2 - 5)
t8.new_ab(is_risp=True)
t8.hit(1)

# 9. BOS #19 Jackie Bradley Jr. (2 - 5 - 23)
t8.new_ab(is_risp=True)
t8.out("F7")

# 1. BOS #50 Mookie Betts (2 - 5 - 23)
t8.new_ab(is_risp=True)
t8.pitch_list("s s d b f")
t8.reach("FC5")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #31 Drew Pomeranz
b8.pitching_substitution(56)

# 8. TBR #35 Brandon Lowe (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.hit(1)
b8.advance(2, "18 1B")
b8.advance(3, "5 FC3-6")

# 9. TBR #43 Michael Pérez (X - X - 35)
b8.new_ab()
b8.pitch_list("c")
b8.out("(F)P3")

# 1. TBR #18 Joey Wendle (X - X - 35)
b8.new_ab()
b8.pitch_list("s s f")
b8.hit(1)
b8.thrown_out(2, "5 FC3-6", 2, 56)

# 2. TBR #5  Matt Duffy (X - 35 - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("b b")
b8.reach("FC3-6")

# 3. TBR #9  Jake Bauers (35 - X - 5)
b8.new_ab(is_risp=True)
b8.pitch_list("c b d f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #61 Hunter Wood
t9 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("f s b b f")
t9.out("G4-3")

# 3. BOS #25 Steve Pearce (X - X - X)
t9.new_ab()
t9.pitch_list("f s b s")
t9.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.hit(1)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t9.new_ab()
t9.pitch_list("c f f d b f c")
t9.out("!K")

# Winning team: TBR
# WP: TBR #68 Jalen Beeks
game.winning_pitcher(68)

# Loser team: BOS
# LP: BOS #76 Hector Velázquez
game.losing_pitcher(76, is_away_team=True)

# print(game)
game.generate_scorecard()
