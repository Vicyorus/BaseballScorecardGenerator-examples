import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ KC, 2013-08-11
# https://www.baseball-reference.com/boxes/KCA/KCA201308110.shtml
# https://www.mlb.com/gameday/red-sox-vs-royals/2013/08/11/348490/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-11 14:13-17:09",
        "at": "Kauffman Stadium, Kansas City, MO",
        "att": "24,935",
        "temp": "86F, Sunny",
        "wind": "6mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                12: "Mike Napoli",
                7: "Stephen Drew",
                20: "Ryan Lavarnway",
                16: "Will Middlebrooks",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                26: "Brock Holt",
                5: "Jonny Gomes",
                # Bullpen
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "7"],
                [12, "3"],
                [7, "6"],
                [20, "2"],
                [16, "5"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [26, "2B"],
                [5, "LF"],
            ],
            "bullpen": [67, 56, 32, 66, 44, 31, 36, 19, 62, 22, 46],
        },
        "home": {
            "team": "Kansas City Royals",
            "starter": 33,
            "roster": {
                # Lineup
                7: "David Lough",
                35: "Eric Hosmer",
                16: "Billy Butler",
                4: "Alex Gordon",
                13: "Salvador Perez",
                8: "Mike Moustakas",
                2: "Alcides Escobar",
                1: "Jarrod Dyson",
                23: "Elliot Johnson",
                # Starting pitcher
                33: "James Shields",
                # Bench
                27: "Justin Maxwell",
                26: "George Kottaras",
                19: "Irving Falu",
                # Bullpen
                56: "Greg Holland",
                54: "Ervin Santana",
                11: "Jeremy Guthrie",
                31: "Louis Coleman",
                52: "Bruce Chen",
                39: "Luis Mendoza",
                22: "Wade Davis",
                40: "Kelvin Herrera",
                53: "Will Smith",
                43: "Aaron Crow",
                44: "Luke Hochevar",
                55: "Tim Collins",
            },
            "lefties": [52, 53, 55],
            "lineup": [
                [7, "9"],
                [35, "3"],
                [16, "0"],
                [4, "7"],
                [13, "2"],
                [8, "5"],
                [2, "6"],
                [1, "8"],
                [23, "4"],
            ],
            "bench": [
                [27, "RF"],
                [26, "C"],
                [19, "2B"],
            ],
            "bullpen": [56, 54, 11, 31, 52, 39, 22, 40, 53, 43, 44, 55],
        },
        "umpires": {
            "HP": "Greg Gibson",
            "1B": "Jerry Layne",
            "2B": "Hunter Wendelstedt",
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
# Pitching: KCR #33 James Shields
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(2)
t1.advance(3, "34 SB")
t1.error(2)
t1.advance("U", "29 POE2")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b f f b b b")
t1.reach("BB")
t1.advance(2, "29 POE2")

# 4. BOS #34 David Ortiz (X - 18 - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("c s s")
t1.out("K")

# 5. BOS #29 Daniel Nava (18 - X - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("b c b c 3 b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. KCR #7  David Lough (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b c b")
b1.reach("BB")
b1.advance(2, "35 BB")
b1.advance(3, "16 DP5-4-3")
b1.advance(4, "4 1B")

# 2. KCR #35 Eric Hosmer (X - X - 7)
b1.new_ab()
b1.pitch_list("b b b c c b")
b1.reach("BB")
b1.thrown_out(2, "16 DP5-4-3", 1, 41)

# 3. KCR #16 Billy Butler (X - 7 - 35)
b1.new_ab(is_risp=True)
b1.pitch_list("b c b f b")
b1.out("DP5-4-3")

# 4. KCR #4  Alex Gordon (7 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.hit(1, rbis=1)
b1.advance(2, "13 SB")

# 5. KCR #13 Salvador Perez (X - X - 4)
b1.new_ab(is_risp=True)
b1.pitch_list("c b")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: KCR #33 James Shields
t2 = game.new_inning()

# 6. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c b b s f b c")
t2.out("!K")

# 7. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1)
t2.thrown_out(2, "20 DP5-4-3", 2, 33)

# 8. BOS #20 Ryan Lavarnway (X - X - 7)
t2.new_ab()
t2.pitch_list("f")
t2.out("DP5-4-3")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 6. KCR #8  Mike Moustakas (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(2)
b2.advance(3, "2 SAC5-3")
b2.advance(4, "1 1B")

# 7. KCR #2  Alcides Escobar (X - 8 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f")
b2.out("SAC5-3")

# 8. KCR #1  Jarrod Dyson (8 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.hit(1, rbis=1)
b2.advance(2, "23 SB")
b2.advance(4, "7 1B")

# 9. KCR #23 Elliot Johnson (X - X - 1)
b2.new_ab(is_risp=True)
b2.pitch_list("b 1 l b s c")
b2.out("!K")

# 1. KCR #7  David Lough (X - 1 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("s f f")
b2.hit(1, rbis=1)
b2.advance(2, "35 SB")

# 2. KCR #35 Eric Hosmer (X - X - 7)
b2.new_ab(is_risp=True)
b2.pitch_list("1 b b b c s")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: KCR #33 James Shields
t3 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("b c b")
t3.hit(1)
t3.thrown_out(2, "2 DP4-6-3", 1, 33)

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
t3.new_ab()
t3.pitch_list("s")
t3.out("DP4-6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c s")
t3.reach("HBP")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t3.new_ab()
t3.pitch_list("b 1")
t3.out("P4")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 3. KCR #16 Billy Butler (X - X - X)
b3.new_ab()
b3.pitch_list("f s c")
b3.out("!K")

# 4. KCR #4  Alex Gordon (X - X - X)
b3.new_ab()
b3.pitch_list("c b b s")
b3.hit(4)

# 5. KCR #13 Salvador Perez (X - X - X)
b3.new_ab()
b3.pitch_list("f f")
b3.out("G5-3")

# 6. KCR #8  Mike Moustakas (X - X - X)
b3.new_ab()
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: KCR #33 James Shields
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G3")

# 5. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("F8")

# 6. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b b")
t4.reach("BB")

# 7. BOS #7  Stephen Drew (X - X - 12)
t4.new_ab()
t4.pitch_list("s b d b")
t4.out("(F)P5")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 7. KCR #2  Alcides Escobar (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("L5")

# 8. KCR #1  Jarrod Dyson (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("B1-3")

# 9. KCR #23 Elliot Johnson (X - X - X)
b4.new_ab()
b4.pitch_list("c f f b b f f b")
b4.out("P5")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: KCR #33 James Shields
t5 = game.new_inning()

# 8. BOS #20 Ryan Lavarnway (X - X - X)
t5.new_ab()
t5.pitch_list("f c f b")
t5.hit(1)
t5.advance(2, "16 BB")

# 9. BOS #16 Will Middlebrooks (X - X - 20)
t5.new_ab()
t5.pitch_list("b f b b b")
t5.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (X - 20 - 16)
t5.new_ab(is_risp=True)
t5.pitch_list("b f")
t5.out("(F)F7")

# 2. BOS #18 Shane Victorino (X - 20 - 16)
t5.new_ab(is_risp=True)
t5.pitch_list("d")
t5.out("L7")

# 3. BOS #15 Dustin Pedroia (X - 20 - 16)
t5.new_ab(is_risp=True)
t5.pitch_list("b s")
t5.out("L9")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 1. KCR #7  David Lough (X - X - X)
b5.new_ab()
b5.pitch_list("c t f b")
b5.out("G3-1")

# 2. KCR #35 Eric Hosmer (X - X - X)
b5.new_ab()
b5.pitch_list("c b b s b f f")
b5.out("(F)P4")

# 3. KCR #16 Billy Butler (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.out("P5")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: KCR #33 James Shields
t6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("f b b")
t6.out("G3")

# 5. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c f")
t6.hit(1)
t6.advance(3, "7 2B")
t6.advance(4, "20 1B")

# 6. BOS #12 Mike Napoli (X - X - 29)
t6.new_ab()
t6.pitch_list("b f f s")
t6.out("K")

# 7. BOS #7  Stephen Drew (X - X - 29)
t6.new_ab()
t6.pitch_list("b c")
t6.hit(2)
t6.advance(4, "20 1B")

# 8. BOS #20 Ryan Lavarnway (29 - 7 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c d")
t6.hit(1, rbis=2)

# 9. BOS #16 Will Middlebrooks (X - X - 20)
t6.new_ab()
t6.pitch_list("c b s b s")
t6.out("K")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 4. KCR #4  Alex Gordon (X - X - X)
b6.new_ab()
b6.pitch_list("c c c")
b6.out("!K")

# 5. KCR #13 Salvador Perez (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1)
b6.advance(2, "2 1B")

# 6. KCR #8  Mike Moustakas (X - X - 13)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")

# 7. KCR #2  Alcides Escobar (X - X - 13)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)

# 8. KCR #1  Jarrod Dyson (X - 13 - 2)
b6.new_ab(is_risp=True)
b6.pitch_list("b s f b d f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: KCR #33 James Shields
t7 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("b f b")
t7.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c")
t7.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("b c c")
t7.out("G1-3")


# Bot 7th
# Pitching: BOS #41 John Lackey
b7 = game.new_inning()

# 9. KCR #23 Elliot Johnson (X - X - X)
b7.new_ab()
b7.pitch_list("b s f s")
b7.out("K")

# 1. KCR #7  David Lough (X - X - X)
b7.new_ab()
b7.pitch_list("b f l")
b7.out("G3")

# 2. KCR #35 Eric Hosmer (X - X - X)
b7.new_ab()
b7.pitch_list("s b")
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: KCR #55 Tim Collins
t8 = game.new_inning()

# Pitching change (KCR): #55 Tim Collins replaces #33 James Shields
t8.pitching_substitution(55)

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("s b b c b f")
t8.out("F7")

# Pitching change (KCR): #43 Aaron Crow replaces #55 Tim Collins
t8.pitching_substitution(43)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #29 Daniel Nava, batting 5th
t8.offensive_substitution(5, 5, "PH")

# 5. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("b c b b b")
t8.reach("BB")

# 6. BOS #12 Mike Napoli (X - X - 5)
t8.new_ab()
t8.pitch_list("c s b b s")
t8.out("K")

# 7. BOS #7  Stephen Drew (X - X - 5)
t8.new_ab()
t8.pitch_list("c b b f f d f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #66 Drake Britton
b8 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #41 John Lackey
b8.pitching_substitution(66)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
b8.defensive_switch(5, "7")

# 3. KCR #16 Billy Butler (X - X - X)
b8.new_ab()
b8.pitch_list("b s b b c")
b8.hit(1)
# Offensive change (KCR): Pinch-runner #27 Justin Maxwell replaces #16 Billy Butler
b8.offensive_substitution(3, 27, "PR")
b8.atbase("PR")
b8.thrown_out(2, "4 3-6", 1, 66)

# 4. KCR #4  Alex Gordon (X - X - 16)
b8.new_ab()
b8.pitch_list("b c d 1 f b")
b8.hit(2)
b8.advance(3, "8 BB")
b8.thrown_out(4, "2 FC5-2", 2, 66)

# 5. KCR #13 Salvador Perez (X - 4 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("i i i i")
b8.reach("IBB")
b8.advance(2, "8 BB")
b8.advance(3, "2 FC5-2")

# 6. KCR #8  Mike Moustakas (X - 4 - 13)
b8.new_ab(is_risp=True)
b8.pitch_list("b b c b d")
b8.reach("BB")
b8.advance(2, "2 FC5-2")

# 7. KCR #2  Alcides Escobar (4 - 13 - 8)
b8.new_ab(is_risp=True)
b8.reach("FC5-2")

# 8. KCR #1  Jarrod Dyson (13 - 8 - 2)
b8.new_ab(is_risp=True)
b8.pitch_list("b c c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: KCR #56 Greg Holland
t9 = game.new_inning()

# Pitching change (KCR): #56 Greg Holland replaces #43 Aaron Crow
t9.pitching_substitution(56)

# Defensive switch (KCR): #27 Justin Maxwell moves to DH
t9.defensive_switch(27, "0")

# 8. BOS #20 Ryan Lavarnway (X - X - X)
t9.new_ab()
t9.pitch_list("b s c")
t9.out("G6-3")

# 9. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("s c c")
t9.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b f s")
t9.out("K")

# Winning team: KCR
# WP: KCR #33 James Shields
game.winning_pitcher(33)
# SV: KCR #56 Greg Holland
game.save_pitcher(56)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
