import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ KC, 2013-08-09
# https://www.baseball-reference.com/boxes/KCA/KCA201308090.shtml
# https://www.mlb.com/gameday/red-sox-vs-royals/2013/08/09/348460/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-09 20:11-23:36",
        "at": "Kauffman Stadium, Kansas City, MO",
        "att": "29,485",
        "temp": "75F, Cloudy",
        "wind": "3mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 44,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                12: "Mike Napoli",
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                26: "Brock Holt",
                # Starting pitcher
                44: "Jake Peavy",
                # Bench
                37: "Mike Carp",
                20: "Ryan Lavarnway",
                5: "Jonny Gomes",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                19: "Koji Uehara",
                66: "Drake Britton",
                54: "Pedro Beato",
                62: "Rubby De La Rosa",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "7"],
                [12, "3"],
                [7, "6"],
                [39, "2"],
                [26, "5"],
            ],
            "bench": [
                [37, "1B"],
                [20, "C"],
                [5, "LF"],
            ],
            "bullpen": [41, 67, 32, 19, 66, 54, 62, 31, 36, 22, 46],
        },
        "home": {
            "team": "Kansas City Royals",
            "starter": 54,
            "roster": {
                # Lineup
                7: "David Lough",
                35: "Eric Hosmer",
                16: "Billy Butler",
                4: "Alex Gordon",
                27: "Justin Maxwell",
                8: "Mike Moustakas",
                2: "Alcides Escobar",
                26: "George Kottaras",
                23: "Elliot Johnson",
                # Starting pitcher
                54: "Ervin Santana",
                # Bench
                24: "Miguel Tejada",
                1: "Jarrod Dyson",
                12: "Brett Hayes",
                # Bullpen
                56: "Greg Holland",
                11: "Jeremy Guthrie",
                40: "Kelvin Herrera",
                67: "Francisley Bueno",
                33: "James Shields",
                43: "Aaron Crow",
                31: "Louis Coleman",
                44: "Luke Hochevar",
                55: "Tim Collins",
                52: "Bruce Chen",
                39: "Luis Mendoza",
            },
            "lefties": [67, 55, 52],
            "lineup": [
                [7, "9"],
                [35, "3"],
                [16, "0"],
                [4, "7"],
                [27, "8"],
                [8, "5"],
                [2, "6"],
                [26, "2"],
                [23, "4"],
            ],
            "bench": [
                [24, "SS"],
                [1, "CF"],
                [12, "C"],
            ],
            "bullpen": [56, 11, 40, 67, 33, 43, 31, 44, 55, 52, 39],
        },
        "umpires": {
            "HP": "Hunter Wendelstedt",
            "1B": "Alan Porter",
            "2B": "Greg Gibson",
            "3B": "Jerry Layne",
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
# Pitching: KCR #54 Ervin Santana
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.out("L6")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.advance(2, "15 BB")
t1.advance(3, "34 (F)F9")
t1.advance(4, "29 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t1.new_ab()
t1.pitch_list("c b 1 f f p d f f d")
t1.reach("BB")
t1.advance(3, "29 1B")

# 4. BOS #34 David Ortiz (X - 18 - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("b b f")
t1.out("(F)F9")

# 5. BOS #29 Daniel Nava (18 - X - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.hit(1, rbis=1)
t1.advance(2, "12 BB")

# 6. BOS #12 Mike Napoli (15 - X - 29)
t1.new_ab(is_risp=True)
t1.pitch_list("b b s s b d")
t1.reach("BB")

# 7. BOS #7  Stephen Drew (15 - 29 - 12)
t1.new_ab(is_risp=True)
t1.pitch_list("b c f b d")
t1.out("G3")


# Bot 1st
# Pitching: BOS #44 Jake Peavy
b1 = game.new_inning()

# 1. KCR #7  David Lough (X - X - X)
b1.new_ab()
b1.pitch_list("c f b b f f")
b1.out("G3")

# 2. KCR #35 Eric Hosmer (X - X - X)
b1.new_ab()
b1.pitch_list("f b")
b1.out("L4")

# 3. KCR #16 Billy Butler (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)

# 4. KCR #4  Alex Gordon (X - X - 16)
b1.new_ab()
b1.pitch_list("c b b s b f f f")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: KCR #54 Ervin Santana
t2 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b b c")
t2.out("G3-1")

# 9. BOS #26 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("b b c")
t2.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t2.new_ab()
t2.hit(1)
t2.advance(2, "18 SB")

# 2. BOS #18 Shane Victorino (X - X - 2)
t2.new_ab(is_risp=True)
t2.pitch_list("b 1 c")
t2.out("L7")


# Bot 2nd
# Pitching: BOS #44 Jake Peavy
b2 = game.new_inning()

# 5. KCR #27 Justin Maxwell (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(4)

# 6. KCR #8  Mike Moustakas (X - X - X)
b2.new_ab()
b2.pitch_list("c b f b f b")
b2.out("L9")

# 7. KCR #2  Alcides Escobar (X - X - X)
b2.new_ab()
b2.pitch_list("c b f f b")
b2.hit(1)
b2.advance(2, "26 BB")
b2.advance(4, "7 1B")

# 8. KCR #26 George Kottaras (X - X - 2)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.advance(2, "7 1B")

# 9. KCR #23 Elliot Johnson (X - 2 - 26)
b2.new_ab(is_risp=True)
b2.pitch_list("s b c f b")
b2.out("F8")

# 1. KCR #7  David Lough (X - 2 - 26)
b2.new_ab(is_risp=True)
b2.pitch_list("f f b b")
b2.hit(1, rbis=1)

# 2. KCR #35 Eric Hosmer (X - 26 - 7)
b2.new_ab(is_risp=True)
b2.pitch_list("b b f c f")
b2.out("P5")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: KCR #54 Ervin Santana
t3 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b f")
t3.hit(4)

# 5. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b s")
t3.out("K")

# 6. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("s")
t3.reach("HBP")
t3.advance(3, "7 1B")
t3.advance(4, "39 2B")

# 7. BOS #7  Stephen Drew (X - X - 12)
t3.new_ab()
t3.pitch_list("b c")
t3.hit(1)
t3.advance(3, "39 2B")

# 8. BOS #39 Jarrod Saltalamacchia (12 - X - 7)
t3.new_ab(is_risp=True)
t3.pitch_list("b s")
t3.hit(2, rbis=1)

# 9. BOS #26 Brock Holt (7 - 39 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b f")
t3.out("G3")


# Bot 3rd
# Pitching: BOS #44 Jake Peavy
b3 = game.new_inning()

# 3. KCR #16 Billy Butler (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.out("G6-3")

# 4. KCR #4  Alex Gordon (X - X - X)
b3.new_ab()
b3.pitch_list("b b c b")
b3.hit(4)

# 5. KCR #27 Justin Maxwell (X - X - X)
b3.new_ab()
b3.out("P6")

# 6. KCR #8  Mike Moustakas (X - X - X)
b3.new_ab()
b3.pitch_list("f b b c f")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: KCR #54 Ervin Santana
t4 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t4.new_ab()
t4.pitch_list("s b f b f b f f")
t4.out("G1-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("c s b b s")
t4.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.hit(1)
t4.advance(2, "34 1B")
t4.advance(3, "29 HBP")
t4.advance(4, "12 2B")

# 4. BOS #34 David Ortiz (X - X - 15)
t4.new_ab()
t4.pitch_list("c f b f b f")
t4.hit(1)
t4.advance(2, "29 HBP")
t4.advance(4, "12 2B")

# 5. BOS #29 Daniel Nava (X - 15 - 34)
t4.new_ab(is_risp=True)
t4.pitch_list("f b s")
t4.reach("HBP")
t4.advance(4, "12 2B")

# 6. BOS #12 Mike Napoli (15 - 34 - 29)
t4.new_ab(is_risp=True)
t4.pitch_list("b s b")
t4.hit(2, rbis=3)

# Pitching change (KCR): #67 Francisley Bueno replaces #54 Ervin Santana
t4.pitching_substitution(67)

# 7. BOS #7  Stephen Drew (X - 12 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c")
t4.out("P2")


# Bot 4th
# Pitching: BOS #44 Jake Peavy
b4 = game.new_inning()

# 7. KCR #2  Alcides Escobar (X - X - X)
b4.new_ab()
b4.pitch_list("c f b")
b4.out("G1-4-3")

# 8. KCR #26 George Kottaras (X - X - X)
b4.new_ab()
b4.pitch_list("b c b c b")
b4.out("F9")

# 9. KCR #23 Elliot Johnson (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("L7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: KCR #67 Francisley Bueno
t5 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.hit(1)
t5.thrown_out(2, "2 FC4-6", 2, 67)

# 9. BOS #26 Brock Holt (X - X - 39)
t5.new_ab()
t5.pitch_list("c d l f")
t5.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - 39)
t5.new_ab()
t5.pitch_list("d")
t5.reach("FC4-6")
t5.thrown_out(2, "18 FC5-4", 3, 67)

# 2. BOS #18 Shane Victorino (X - X - 2)
t5.new_ab()
t5.pitch_list("1 1 b b 1 b f")
t5.reach("FC5-4")


# Bot 5th
# Pitching: BOS #44 Jake Peavy
b5 = game.new_inning()

# 1. KCR #7  David Lough (X - X - X)
b5.new_ab()
b5.out("P3")

# 2. KCR #35 Eric Hosmer (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(1)
b5.advance(2, "16 1B")
b5.thrown_out(2, "4 DP3-6", 3, 44)

# 3. KCR #16 Billy Butler (X - X - 35)
b5.new_ab()
b5.pitch_list("c c d")
b5.hit(1)

# 4. KCR #4  Alex Gordon (X - 35 - 16)
b5.new_ab(is_risp=True)
b5.out("DP3-6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: KCR #67 Francisley Bueno
t6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G3-1")

# 5. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("c b b")
t6.out("G6-3")


# Bot 6th
# Pitching: BOS #44 Jake Peavy
b6 = game.new_inning()

# 5. KCR #27 Justin Maxwell (X - X - X)
b6.new_ab()
b6.pitch_list("c f b")
b6.hit(1)
b6.advance(3, "8 1B")
b6.advance(4, "2 1B")

# 6. KCR #8  Mike Moustakas (X - X - 27)
b6.new_ab()
b6.pitch_list("f b 1 1 1")
b6.hit(1)
b6.advance(2, "2 1B")
b6.advance(3, "26 BB")
b6.advance(4, "7 SF9")

# 7. KCR #2  Alcides Escobar (27 - X - 8)
b6.new_ab(is_risp=True)
b6.pitch_list("b f f")
b6.hit(1, rbis=1)
b6.advance(2, "26 BB")
b6.advance(3, "7 SF9")
b6.advance(4, "35 1B")

# Pitching change (BOS): #66 Drake Britton replaces #44 Jake Peavy
b6.pitching_substitution(66)

# 8. KCR #26 George Kottaras (X - 8 - 2)
b6.new_ab(is_risp=True)
b6.pitch_list("c d b b c b")
b6.reach("BB")
b6.advance(2, "7 SF9")
b6.advance(4, "35 1B")

# Offensive change (KCR): Pinch-hitter #24 Miguel Tejada replaces #23 Elliot Johnson, batting 9th
b6.offensive_substitution(9, 24, "PH")

# 9. KCR #24 Miguel Tejada (8 - 2 - 26)
b6.new_ab(is_risp=True)
b6.pitch_list("s")
b6.out("(F)P3")

# 1. KCR #7  David Lough (8 - 2 - 26)
b6.new_ab(is_risp=True)
b6.pitch_list("b d c")
b6.out("SF9", rbis=1)

# 2. KCR #35 Eric Hosmer (2 - 26 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("d b c s")
b6.hit(1, rbis=2)
b6.advance(2, "T")
b6.advance(4, "16 2B")

# Pitching change (BOS): #54 Pedro Beato replaces #66 Drake Britton
b6.pitching_substitution(54)

# 3. KCR #16 Billy Butler (X - 35 - X)
b6.new_ab(is_risp=True)
b6.hit(2, rbis=1)
b6.advance(4, "27 1B")

# 4. KCR #4  Alex Gordon (X - 16 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c b b d b")
b6.reach("BB")
b6.advance(2, "27 1B")

# 5. KCR #27 Justin Maxwell (X - 16 - 4)
b6.new_ab(is_risp=True)
b6.pitch_list("f b b d s")
b6.hit(1, rbis=1)

# 6. KCR #8  Mike Moustakas (X - 4 - 27)
b6.new_ab(is_risp=True)
b6.pitch_list("b c")
b6.out("(F)P4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: KCR #40 Kelvin Herrera
t7 = game.new_inning()

# Pitching change (KCR): #40 Kelvin Herrera replaces #67 Francisley Bueno
t7.pitching_substitution(40)

# Defensive switch (KCR): #24 Miguel Tejada moves to 2B
t7.defensive_switch(24, "4")

# 6. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("b c b c f")
t7.hit(1)

# 7. BOS #7  Stephen Drew (X - X - 12)
t7.new_ab()
t7.pitch_list("c d f s")
t7.out("K")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - 12)
t7.new_ab()
t7.pitch_list("c b")
t7.out("F9")

# 9. BOS #26 Brock Holt (X - X - 12)
t7.new_ab()
t7.pitch_list("c b")
t7.out("L9")


# Bot 7th
# Pitching: BOS #54 Pedro Beato
b7 = game.new_inning()

# 7. KCR #2  Alcides Escobar (X - X - X)
b7.new_ab()
b7.pitch_list("c c f f f")
b7.out("F9")

# 8. KCR #26 George Kottaras (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.hit(1)

# 9. KCR #24 Miguel Tejada (X - X - 26)
b7.new_ab()
b7.pitch_list("b f")
b7.out("L8")

# 1. KCR #7  David Lough (X - X - 26)
b7.new_ab()
b7.pitch_list("c c b s")
b7.out("K2-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: KCR #55 Tim Collins
t8 = game.new_inning()

# Pitching change (KCR): #55 Tim Collins replaces #40 Kelvin Herrera
t8.pitching_substitution(55)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c b c b b f f f f b")
t8.reach("BB")
t8.advance(2, "18 BB")
t8.thrown_out(3, "15 DP5-4", 1, 55)

# 2. BOS #18 Shane Victorino (X - X - 2)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
t8.thrown_out(2, "15 DP5-4", 2, 55)

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t8.new_ab(is_risp=True)
t8.pitch_list("c f b b f f")
t8.reach("DP5-4")

# 4. BOS #34 David Ortiz (X - X - 15)
t8.new_ab()
t8.pitch_list("b c s")
t8.out("P5")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #54 Pedro Beato
b8.pitching_substitution(32)

# 2. KCR #35 Eric Hosmer (X - X - X)
b8.new_ab()
b8.pitch_list("s s")
b8.hit(1)
b8.thrown_out(2, "16 DP4-6-3", 1, 32)

# 3. KCR #16 Billy Butler (X - X - 35)
b8.new_ab()
b8.out("DP4-6-3")

# 4. KCR #4  Alex Gordon (X - X - X)
b8.new_ab()
b8.pitch_list("b b f")
b8.hit(1)
b8.advance(2, "27 WP")

# 5. KCR #27 Justin Maxwell (X - X - 4)
b8.new_ab(is_risp=True)
b8.pitch_list("s b b s s")
b8.wp()
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: KCR #56 Greg Holland
t9 = game.new_inning()

# Pitching change (KCR): #56 Greg Holland replaces #55 Tim Collins
t9.pitching_substitution(56)

# 5. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.out("(F)P5")

# 6. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("c b c s")
t9.out("K")

# 7. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("c s s")
t9.out("K")

# Winning team: KCR
# WP: KCR #67 Francisley Bueno
game.winning_pitcher(67)
# SV: KCR #56 Greg Holland
game.save_pitcher(56)

# Loser team: BOS
# LP: BOS #66 Drake Britton
game.losing_pitcher(66, is_away_team=True)

# print(game)
game.generate_scorecard()
