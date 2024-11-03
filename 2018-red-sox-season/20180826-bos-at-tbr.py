import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-08-26
# https://www.baseball-reference.com/boxes/TBA/TBA201808260.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/08/26/531358/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-26 13:10-16:15",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "23,448",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                36: "Eduardo Núñez",
                2: "Xander Bogaerts",
                25: "Steve Pearce",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                28: "J.D. Martinez",
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "9"],
                [36, "5"],
                [2, "6"],
                [25, "0"],
                [18, "3"],
                [5, "4"],
                [12, "7"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [28, "DH"],
                [23, "C"],
                [16, "LF"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 24, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 42,
            "roster": {
                # Lineup
                18: "Joey Wendle",
                5: "Matt Duffy",
                26: "Ji Man Choi",
                29: "Tommy Pham",
                9: "Jake Bauers",
                39: "Kevin Kiermaier",
                1: "Willy Adames",
                35: "Brandon Lowe",
                43: "Michael Pérez",
                # Starting pitcher
                42: "Blake Snell",
                # Bench
                44: "C.J. Cron",
                27: "Carlos Gómez",
                45: "Jesús Sucre",
                # Bullpen
                46: "José Alvarado",
                20: "Tyler Glasnow",
                61: "Hunter Wood",
                48: "Ryan Yarbrough",
                68: "Jalen Beeks",
                56: "Adam Kolarek",
                52: "Chaz Roe",
                55: "Ryne Stanek",
                36: "Andrew Kittredge",
                72: "Yonny Chirinos",
                63: "Diego Castillo",
                54: "Sergio Romo",
            },
            "lefties": [42, 46, 48, 68, 56],
            "lineup": [
                [18, "4"],
                [5, "5"],
                [26, "0"],
                [29, "7"],
                [9, "3"],
                [39, "8"],
                [1, "6"],
                [35, "9"],
                [43, "2"],
            ],
            "bench": [
                [44, "1B"],
                [27, "CF"],
                [45, "C"],
            ],
            "bullpen": [46, 20, 61, 48, 68, 56, 52, 55, 36, 72, 63, 54],
        },
        "umpires": {
            "HP": "Todd Tichenor",
            "1B": "Manny Gonzalez",
            "2B": "Angel Hernandez",
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
# Pitching: TBR #42 Blake Snell
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b c b s f c")
t1.out("!K")

# 2. BOS #36 Eduardo Núñez (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c")
t1.out("F8")

# 3. BOS #2  Xander Bogaerts (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G4-3")


# Bot 1st
# Pitching: BOS #17 Nathan Eovaldi
b1 = game.new_inning()

# 1. TBR #18 Joey Wendle (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(2)
b1.advance(3, "5 1B")
b1.advance(4, "26 1B")

# 2. TBR #5  Matt Duffy (X - 18 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("f c b")
b1.hit(1)
b1.advance(3, "26 1B")
b1.advance(4, "9 SF9")

# 3. TBR #26 Ji Man Choi (18 - X - 5)
b1.new_ab(is_risp=True)
b1.pitch_list("f s")
b1.hit(1, rbis=1)

# 4. TBR #29 Tommy Pham (5 - X - 26)
b1.new_ab(is_risp=True)
b1.pitch_list("s s b c")
b1.out("!K")

# 5. TBR #9  Jake Bauers (5 - X - 26)
b1.new_ab(is_risp=True)
b1.pitch_list("d b 1 b f s")
b1.out("SF9", rbis=1)

# 6. TBR #39 Kevin Kiermaier (X - X - 26)
b1.new_ab()
b1.pitch_list("s s")
b1.out("(F)P3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #42 Blake Snell
t2 = game.new_inning()

# 4. BOS #25 Steve Pearce (X - X - X)
t2.new_ab()
t2.pitch_list("s s b b b b")
t2.reach("BB")
t2.thrown_out(2, "5 2-4", 2, 42)

# 5. BOS #18 Mitch Moreland (X - X - 25)
t2.new_ab()
t2.pitch_list("b b s s")
t2.out("F7")

# 6. BOS #5  Ian Kinsler (X - X - 25)
t2.new_ab()
t2.pitch_list("b c s f c")
t2.out("!K")


# Bot 2nd
# Pitching: BOS #17 Nathan Eovaldi
b2 = game.new_inning()

# 7. TBR #1  Willy Adames (X - X - X)
b2.new_ab()
b2.pitch_list("b s")
b2.out("G4-3")

# 8. TBR #35 Brandon Lowe (X - X - X)
b2.new_ab()
b2.pitch_list("b s")
b2.out("G4-3")

# 9. TBR #43 Michael Pérez (X - X - X)
b2.new_ab()
b2.pitch_list("b b c s f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #42 Blake Snell
t3 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
t3.new_ab()
t3.pitch_list("c b b f s")
t3.out("K")

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("s s b s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #17 Nathan Eovaldi
b3 = game.new_inning()

# 1. TBR #18 Joey Wendle (X - X - X)
b3.new_ab()
b3.pitch_list("b c f c")
b3.out("!K")

# 2. TBR #5  Matt Duffy (X - X - X)
b3.new_ab()
b3.pitch_list("f c b b b f f")
b3.hit(1)
b3.advance(3, "26 1B")
b3.advance(4, "29 1B")

# 3. TBR #26 Ji Man Choi (X - X - 5)
b3.new_ab()
b3.pitch_list("c b c 1 b")
b3.hit(1)
b3.advance(2, "29 1B")
b3.advance(4, "39 3B")

# 4. TBR #29 Tommy Pham (5 - X - 26)
b3.new_ab(is_risp=True)
b3.pitch_list("c s")
b3.hit(1, rbis=1)
b3.advance(4, "39 3B")

# 5. TBR #9  Jake Bauers (X - 26 - 29)
b3.new_ab(is_risp=True)
b3.pitch_list("d b f c")
b3.out("L9")

# 6. TBR #39 Kevin Kiermaier (X - 26 - 29)
b3.new_ab(is_risp=True)
b3.pitch_list("s s")
b3.hit(3, rbis=2)

# 7. TBR #1  Willy Adames (39 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b c s f c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #42 Blake Snell
t4 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("c b c")
t4.hit(1)
t4.advance(2, "2 SB")

# 2. BOS #36 Eduardo Núñez (X - X - 50)
t4.new_ab()
t4.pitch_list("f f s")
t4.out("K")

# 3. BOS #2  Xander Bogaerts (X - X - 50)
t4.new_ab(is_risp=True)
t4.pitch_list("c b b s s")
t4.out("K")

# 4. BOS #25 Steve Pearce (X - 50 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b d c b s")
t4.out("F8")


# Bot 4th
# Pitching: BOS #17 Nathan Eovaldi
b4 = game.new_inning()

# 8. TBR #35 Brandon Lowe (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.error(3)
b4.reach("E3")
b4.thrown_out(2, "43 FC4-6", 1, 17)

# 9. TBR #43 Michael Pérez (X - X - 35)
b4.new_ab()
b4.pitch_list("s s b d")
b4.reach("FC4-6")
b4.advance(2, "18 1B")
b4.advance(3, "5 WP")
b4.advance("U", "5 SF8")

# 1. TBR #18 Joey Wendle (X - X - 43)
b4.new_ab()
b4.pitch_list("f")
b4.hit(1)
b4.advance(2, "5 WP")

# 2. TBR #5  Matt Duffy (X - 43 - 18)
b4.new_ab(is_risp=True)
b4.pitch_list("b b f s f")
b4.wp()
b4.out("SF8", rbis=1)

# 3. TBR #26 Ji Man Choi (X - 18 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("f b f f f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #42 Blake Snell
t5 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("(F)P5")

# 6. BOS #5  Ian Kinsler (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("F8")

# 7. BOS #12 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("f b c b t")
t5.out("KT")


# Bot 5th
# Pitching: BOS #56 Joe Kelly
b5 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #17 Nathan Eovaldi
b5.pitching_substitution(56)

# 4. TBR #29 Tommy Pham (X - X - X)
b5.new_ab()
b5.pitch_list("c b c")
b5.hit(1)
b5.thrown_out(1, "9 PO", 1, 56)

# 5. TBR #9  Jake Bauers (X - X - 29)
b5.new_ab()
b5.pitch_list("1 c b b")
b5.out("G3")

# 6. TBR #39 Kevin Kiermaier (X - X - X)
b5.new_ab()
b5.pitch_list("b c b f b b")
b5.reach("BB")

# 7. TBR #1  Willy Adames (X - X - 39)
b5.new_ab()
b5.pitch_list("b f b s d")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #42 Blake Snell
t6 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c b")
t6.reach("BB")
t6.advance(3, "19 2B")
t6.advance(4, "50 SF8")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t6.new_ab()
t6.pitch_list("b b")
t6.hit(2)
t6.advance(3, "36 G4-3")

# 1. BOS #50 Mookie Betts (3 - 19 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c b b f")
t6.out("SF8", rbis=1)

# 2. BOS #36 Eduardo Núñez (X - 19 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b b c")
t6.out("G4-3")

# 3. BOS #2  Xander Bogaerts (19 - X - X)
t6.new_ab(is_risp=True)
t6.pitch_list("f c f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #37 Heath Hembree
b6 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #56 Joe Kelly
b6.pitching_substitution(37)

# 8. TBR #35 Brandon Lowe (X - X - X)
b6.new_ab()
b6.pitch_list("b b s f b")
b6.hit(1)
b6.advance(2, "43 SB")
b6.advance(4, "5 2B")

# 9. TBR #43 Michael Pérez (X - X - 35)
b6.new_ab()
b6.pitch_list("f f d f b 1 b s")
b6.out("K")

# 1. TBR #18 Joey Wendle (X - 35 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b s f b f s")
b6.out("K2-3")

# 2. TBR #5  Matt Duffy (X - 35 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c")
b6.hit(2, rbis=1)

# 3. TBR #26 Ji Man Choi (X - 5 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f b f d d b")
b6.reach("BB")

# 4. TBR #29 Tommy Pham (X - 5 - 26)
b6.new_ab(is_risp=True)
b6.pitch_list("b f s b b")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #63 Diego Castillo
t7 = game.new_inning()

# Pitching change (TBR): #63 Diego Castillo replaces #42 Blake Snell
t7.pitching_substitution(63)

# 4. BOS #25 Steve Pearce (X - X - X)
t7.new_ab()
t7.pitch_list("s")
t7.out("G5-3")

# 5. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.out("F8")

# 6. BOS #5  Ian Kinsler (X - X - X)
t7.new_ab()
t7.pitch_list("c c")
t7.out("P3")


# Bot 7th
# Pitching: BOS #32 Matt Barnes
b7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree
b7.pitching_substitution(32)

# 5. TBR #9  Jake Bauers (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c c b")
b7.reach("BB")
b7.advance(2, "35 BB")
b7.advance(4, "43 2B")

# 6. TBR #39 Kevin Kiermaier (X - X - 9)
b7.new_ab()
b7.pitch_list("b f c d b s")
b7.out("K")

# 7. TBR #1  Willy Adames (X - X - 9)
b7.new_ab()
b7.pitch_list("c 1 s d s")
b7.out("K")

# 8. TBR #35 Brandon Lowe (X - X - 9)
b7.new_ab()
b7.pitch_list("1 b b b c b")
b7.reach("BB")
b7.advance(4, "43 2B")

# 9. TBR #43 Michael Pérez (X - 9 - 35)
b7.new_ab(is_risp=True)
b7.pitch_list("s")
b7.hit(2, rbis=2)

# 1. TBR #18 Joey Wendle (X - 43 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b c")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #36 Andrew Kittredge
t8 = game.new_inning()

# Pitching change (TBR): #36 Andrew Kittredge replaces #63 Diego Castillo
t8.pitching_substitution(36)

# 7. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("(F)P5")

# 8. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.out("(F)P5")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("c s b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #46 Craig Kimbrel
b8 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
b8.pitching_substitution(46)

# Defensive change (BOS): #23 Blake Swihart replaces #50 Mookie Betts (RF), playing RF, batting 1st
b8.defensive_substitution(1, 23, "9")

# 2. TBR #5  Matt Duffy (X - X - X)
b8.new_ab()
b8.pitch_list("f f b c")
b8.out("!K")

# 3. TBR #26 Ji Man Choi (X - X - X)
b8.new_ab()
b8.pitch_list("b s b s b c")
b8.out("!K")

# 4. TBR #29 Tommy Pham (X - X - X)
b8.new_ab()
b8.pitch_list("s b c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #36 Andrew Kittredge
t9 = game.new_inning()

# 1. BOS #23 Blake Swihart (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.out("G3")

# 2. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.hit(1)
t9.advance(2, "2 DI")

# 3. BOS #2  Xander Bogaerts (X - X - 36)
t9.new_ab(is_risp=True)
t9.pitch_list("b d c f b")
t9.out("G5-3")

# 4. BOS #25 Steve Pearce (X - 36 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b c")
t9.out("G4-3")

# Winning team: TBR
# WP: TBR #42 Blake Snell
game.winning_pitcher(42)

# Loser team: BOS
# LP: BOS #17 Nathan Eovaldi
game.losing_pitcher(17, is_away_team=True)

# print(game)
game.generate_scorecard()
