import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-08-25
# https://www.baseball-reference.com/boxes/TBA/TBA201808250.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/08/25/531343/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-25 18:10-21:03",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "25,695",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                36: "Eduardo Núñez",
                3: "Sandy León",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "8"],
                [16, "7"],
                [25, "0"],
                [28, "9"],
                [2, "6"],
                [18, "3"],
                [5, "4"],
                [36, "5"],
                [3, "2"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [19, "CF"],
            ],
            "bullpen": [47, 44, 31, 61, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 48,
            "roster": {
                # Lineup
                18: "Joey Wendle",
                5: "Matt Duffy",
                26: "Ji Man Choi",
                29: "Tommy Pham",
                44: "C.J. Cron",
                39: "Kevin Kiermaier",
                1: "Willy Adames",
                35: "Brandon Lowe",
                43: "Michael Pérez",
                # Starting pitcher
                48: "Ryan Yarbrough",
                # Bench
                9: "Jake Bauers",
                27: "Carlos Gómez",
                45: "Jesús Sucre",
                # Bullpen
                46: "José Alvarado",
                20: "Tyler Glasnow",
                61: "Hunter Wood",
                68: "Jalen Beeks",
                56: "Adam Kolarek",
                52: "Chaz Roe",
                55: "Ryne Stanek",
                36: "Andrew Kittredge",
                42: "Blake Snell",
                72: "Yonny Chirinos",
                63: "Diego Castillo",
                54: "Sergio Romo",
            },
            "lefties": [48, 46, 68, 56, 42],
            "lineup": [
                [18, "4"],
                [5, "5"],
                [26, "0"],
                [29, "7"],
                [44, "3"],
                [39, "8"],
                [1, "6"],
                [35, "9"],
                [43, "2"],
            ],
            "bench": [
                [9, "1B"],
                [27, "CF"],
                [45, "C"],
            ],
            "bullpen": [46, 20, 61, 68, 56, 52, 55, 36, 42, 72, 63, 54],
        },
        "umpires": {
            "HP": "Alan Porter",
            "1B": "Todd Tichenor",
            "2B": "Manny Gonzalez",
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
# Pitching: TBR #48 Ryan Yarbrough
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b c s b t")
t1.out("KT")

# 3. BOS #25 Steve Pearce (X - X - X)
t1.new_ab()
t1.pitch_list("b b f b f f")
t1.out("G1-3")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. TBR #18 Joey Wendle (X - X - X)
b1.new_ab()
b1.hit(1)
b1.advance(2, "5 SB")

# 2. TBR #5  Matt Duffy (X - X - 18)
b1.new_ab(is_risp=True)
b1.pitch_list("c f b b t")
b1.out("KT")

# 3. TBR #26 Ji Man Choi (X - 18 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c b d")
b1.out("L8")

# 4. TBR #29 Tommy Pham (X - 18 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c c b b c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #48 Ryan Yarbrough
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(2)
t2.advance(3, "2 1B")
t2.advance(4, "18 DP4-6-3")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c f b f")
t2.hit(1)
t2.thrown_out(2, "18 DP4-6-3", 1, 48)

# 6. BOS #18 Mitch Moreland (28 - X - 2)
t2.new_ab(is_risp=True)
t2.pitch_list("b b")
t2.out("DP4-6-3")

# 7. BOS #5  Ian Kinsler (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 5. TBR #44 C.J. Cron (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G5-3")

# 6. TBR #39 Kevin Kiermaier (X - X - X)
b2.new_ab()
b2.pitch_list("f b b s s")
b2.out("K")

# 7. TBR #1  Willy Adames (X - X - X)
b2.new_ab()
b2.pitch_list("c f c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #48 Ryan Yarbrough
t3 = game.new_inning()

# 8. BOS #36 Eduardo Núñez (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)
t3.thrown_out(2, "50 FC6-4", 2, 48)

# 9. BOS #3  Sandy León (X - X - 36)
t3.new_ab()
t3.pitch_list("b f 1 1 f")
t3.out("L9")

# 1. BOS #50 Mookie Betts (X - X - 36)
t3.new_ab()
t3.pitch_list("1 c")
t3.reach("FC6-4")
t3.advance(2, "16 SB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t3.new_ab(is_risp=True)
t3.pitch_list("f b b f b t")
t3.out("KT")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 8. TBR #35 Brandon Lowe (X - X - X)
b3.new_ab()
b3.pitch_list("c b s b b f b")
b3.reach("BB")
b3.thrown_out(2, "43 FC4-6", 1, 22)

# 9. TBR #43 Michael Pérez (X - X - 35)
b3.new_ab()
b3.pitch_list("b")
b3.reach("FC4-6")
b3.advance(2, "18 BB")
b3.advance(3, "5 1B")

# 1. TBR #18 Joey Wendle (X - X - 43)
b3.new_ab()
b3.pitch_list("b b c c d 1 f b")
b3.reach("BB")
b3.advance(2, "5 1B")

# 2. TBR #5  Matt Duffy (X - 43 - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("b b")
b3.hit(1)

# 3. TBR #26 Ji Man Choi (43 - 18 - 5)
b3.new_ab(is_risp=True)
b3.pitch_list("c c f c")
b3.out("!K")

# 4. TBR #29 Tommy Pham (43 - 18 - 5)
b3.new_ab(is_risp=True)
b3.pitch_list("c b b f c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #48 Ryan Yarbrough
t4 = game.new_inning()

# 3. BOS #25 Steve Pearce (X - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.out("L8")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("b c c f")
t4.hit(2)

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c")
t4.out("G5-3")

# 6. BOS #18 Mitch Moreland (X - 28 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c")
t4.out("(F)P5")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 5. TBR #44 C.J. Cron (X - X - X)
b4.new_ab()
b4.reach("HBP")
b4.advance(2, "39 SAC1-3")
b4.advance(4, "35 1B")

# 6. TBR #39 Kevin Kiermaier (X - X - 44)
b4.new_ab()
b4.pitch_list("s")
b4.out("SAC1-3")

# 7. TBR #1  Willy Adames (X - 44 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c c s")
b4.out("K")

# 8. TBR #35 Brandon Lowe (X - 44 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c s")
b4.hit(1, rbis=1)

# 9. TBR #43 Michael Pérez (X - X - 35)
b4.new_ab()
b4.pitch_list("d d f b")
b4.out("P5")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #48 Ryan Yarbrough
t5 = game.new_inning()

# 7. BOS #5  Ian Kinsler (X - X - X)
t5.new_ab()
t5.pitch_list("b f f")
t5.out("P5")

# 8. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.hit(1)

# 9. BOS #3  Sandy León (X - X - 36)
t5.new_ab()
t5.pitch_list("b b b")
t5.out("F8")

# 1. BOS #50 Mookie Betts (X - X - 36)
t5.new_ab()
t5.pitch_list("c b f")
t5.out("F9")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 1. TBR #18 Joey Wendle (X - X - X)
b5.new_ab()
b5.pitch_list("b c f")
b5.hit(1)
b5.advance(2, "5 1B")
b5.advance(3, "29 G5-3")

# 2. TBR #5  Matt Duffy (X - X - 18)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(2, "29 G5-3")

# 3. TBR #26 Ji Man Choi (X - 18 - 5)
b5.new_ab(is_risp=True)
b5.out("IF6")

# 4. TBR #29 Tommy Pham (X - 18 - 5)
b5.new_ab(is_risp=True)
b5.out("G5-3")

# 5. TBR #44 C.J. Cron (18 - 5 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("s f f f b f b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #48 Ryan Yarbrough
t6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("c b c b b b")
t6.reach("BB")
t6.thrown_out(1, "28 PO", 2, 55)

# Pitching change (TBR): #55 Ryne Stanek replaces #48 Ryan Yarbrough
t6.pitching_substitution(55)

# 3. BOS #25 Steve Pearce (X - X - 16)
t6.new_ab()
t6.pitch_list("b b b")
t6.out("F9")

# 4. BOS #28 J.D. Martinez (X - X - 16)
t6.new_ab()
t6.pitch_list("1 b s f 1 f b d 1 s")
t6.out("K")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 6. TBR #39 Kevin Kiermaier (X - X - X)
b6.new_ab()
b6.pitch_list("c f f")
b6.hit(3)
b6.advance(4, "35 WP")

# 7. TBR #1  Willy Adames (39 - X - X)
b6.new_ab(is_risp=True)
b6.reach("HBP")
b6.advance(2, "35 WP")
b6.advance(3, "43 SAC1-4")
b6.advance(4, "18 SF7")

# Pitching change (BOS): #70 Ryan Brasier replaces #22 Rick Porcello
b6.pitching_substitution(70)

# 8. TBR #35 Brandon Lowe (39 - X - 1)
b6.new_ab(is_risp=True)
b6.pitch_list("1 1 f 1 1 b 1 s 1 f b b b")
b6.wp()
b6.reach("BB")
b6.advance(2, "43 SAC1-4")

# 9. TBR #43 Michael Pérez (X - 1 - 35)
b6.new_ab(is_risp=True)
b6.pitch_list("d c")
b6.out("SAC1-4")

# 1. TBR #18 Joey Wendle (1 - 35 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f s")
b6.out("SF7", rbis=1)

# 2. TBR #5  Matt Duffy (X - 35 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b b")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #52 Chaz Roe
t7 = game.new_inning()

# Pitching change (TBR): #52 Chaz Roe replaces #55 Ryne Stanek
t7.pitching_substitution(52)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("P4")

# 6. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G3")

# 7. BOS #5  Ian Kinsler (X - X - X)
t7.new_ab()
t7.pitch_list("b c c")
t7.out("P4")


# Bot 7th
# Pitching: BOS #44 Brandon Workman
b7 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #70 Ryan Brasier
b7.pitching_substitution(44)

# 3. TBR #26 Ji Man Choi (X - X - X)
b7.new_ab()
b7.pitch_list("b c s")
b7.out("(F)P2")

# 4. TBR #29 Tommy Pham (X - X - X)
b7.new_ab()
b7.hit(4)

# 5. TBR #44 C.J. Cron (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b d")
b7.reach("BB")
b7.advance(3, "39 1B")

# 6. TBR #39 Kevin Kiermaier (X - X - 44)
b7.new_ab()
b7.pitch_list("c f 1")
b7.hit(1)
b7.advance(2, "1 SB")

# 7. TBR #1  Willy Adames (44 - X - 39)
b7.new_ab(is_risp=True)
b7.pitch_list("c b b f f s")
b7.out("K")

# 8. TBR #35 Brandon Lowe (44 - 39 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b c")
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #46 José Alvarado
t8 = game.new_inning()

# Pitching change (TBR): #46 José Alvarado replaces #52 Chaz Roe
t8.pitching_substitution(46)

# 8. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c c c")
t8.out("!K")

# 9. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.out("F9")


# Bot 8th
# Pitching: BOS #47 Tyler Thornburg
b8 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #44 Brandon Workman
b8.pitching_substitution(47)

# 9. TBR #43 Michael Pérez (X - X - X)
b8.new_ab()
b8.pitch_list("b f b f f c")
b8.out("!K")

# 1. TBR #18 Joey Wendle (X - X - X)
b8.new_ab()
b8.pitch_list("b c f")
b8.out("G4-3")

# 2. TBR #5  Matt Duffy (X - X - X)
b8.new_ab()
b8.pitch_list("s b b b b")
b8.reach("BB")
b8.advance(4, "26 3B")

# 3. TBR #26 Ji Man Choi (X - X - 5)
b8.new_ab()
b8.pitch_list("b c 1")
b8.hit(3, rbis=1)

# 4. TBR #29 Tommy Pham (26 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c c d d f f")
b8.out("L4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #54 Sergio Romo
t9 = game.new_inning()

# Pitching change (TBR): #54 Sergio Romo replaces #46 José Alvarado
t9.pitching_substitution(54)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b f f s")
t9.out("K")

# 3. BOS #25 Steve Pearce (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("F8")

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("f c b b f s")
t9.out("K")

# Winning team: TBR
# WP: TBR #55 Ryne Stanek
game.winning_pitcher(55)

# Loser team: BOS
# LP: BOS #22 Rick Porcello
game.losing_pitcher(22, is_away_team=True)

# print(game)
game.generate_scorecard()
