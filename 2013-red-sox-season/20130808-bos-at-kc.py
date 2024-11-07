import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ KC, 2013-08-08
# https://www.baseball-reference.com/boxes/KCA/KCA201308080.shtml
# https://www.mlb.com/gameday/red-sox-vs-royals/2013/08/08/348451/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-08 20:11-22:49",
        "at": "Kauffman Stadium, Kansas City, MO",
        "att": "21,121",
        "temp": "73F, Cloudy",
        "wind": "8mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                26: "Brock Holt",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                34: "David Ortiz",
                20: "Ryan Lavarnway",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                19: "Koji Uehara",
                66: "Drake Britton",
                44: "Jake Peavy",
                54: "Pedro Beato",
                62: "Rubby De La Rosa",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 32, 66, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [5, "7"],
                [7, "6"],
                [12, "0"],
                [29, "3"],
                [39, "2"],
                [26, "5"],
            ],
            "bench": [
                [37, "1B"],
                [34, "DH"],
                [20, "C"],
            ],
            "bullpen": [41, 67, 32, 19, 66, 44, 54, 62, 36, 22, 46],
        },
        "home": {
            "team": "Kansas City Royals",
            "starter": 52,
            "roster": {
                # Lineup
                6: "Lorenzo Cain",
                35: "Eric Hosmer",
                16: "Billy Butler",
                4: "Alex Gordon",
                24: "Miguel Tejada",
                27: "Justin Maxwell",
                8: "Mike Moustakas",
                12: "Brett Hayes",
                2: "Alcides Escobar",
                # Starting pitcher
                52: "Bruce Chen",
                # Bench
                7: "David Lough",
                26: "George Kottaras",
                23: "Elliot Johnson",
                1: "Jarrod Dyson",
                # Bullpen
                56: "Greg Holland",
                54: "Ervin Santana",
                11: "Jeremy Guthrie",
                33: "James Shields",
                31: "Louis Coleman",
                39: "Luis Mendoza",
                40: "Kelvin Herrera",
                67: "Francisley Bueno",
                43: "Aaron Crow",
                44: "Luke Hochevar",
                55: "Tim Collins",
            },
            "lefties": [52, 67, 55],
            "lineup": [
                [6, "8"],
                [35, "3"],
                [16, "0"],
                [4, "7"],
                [24, "4"],
                [27, "9"],
                [8, "5"],
                [12, "2"],
                [2, "6"],
            ],
            "bench": [
                [7, "LF"],
                [26, "C"],
                [23, "SS"],
                [1, "CF"],
            ],
            "bullpen": [56, 54, 11, 33, 31, 39, 40, 67, 43, 44, 55],
        },
        "umpires": {
            "HP": "Jerry Layne",
            "1B": "Hunter Wendelstedt",
            "2B": "Alan Porter",
            "3B": "Greg Gibson",
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
# Pitching: KCR #52 Bruce Chen
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.thrown_out(2, "18 POCS", 1, 52)

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("c f f 1 1 f f")
t1.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c t f b b")
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. KCR #6  Lorenzo Cain (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.hit(2)
b1.advance(3, "35 G3-1")
b1.advance(4, "4 SF7")

# 2. KCR #35 Eric Hosmer (X - 6 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c f f f b f")
b1.out("G3-1")

# 3. KCR #16 Billy Butler (6 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b b c b")
b1.reach("BB")
b1.advance(2, "4 SF7")
b1.advance(3, "27 BB")
b1.advance("U", "8 1B")

# 4. KCR #4  Alex Gordon (6 - X - 16)
b1.new_ab(is_risp=True)
b1.pitch_list("d b f b f f")
b1.error(7)
b1.reach("SF7", rbis=1)
b1.advance(2, "27 BB")
b1.advance("U", "8 1B")

# 5. KCR #24 Miguel Tejada (X - 16 - 4)
b1.new_ab(is_risp=True)
b1.pitch_list("f f")
b1.out("IF4")

# 6. KCR #27 Justin Maxwell (X - 16 - 4)
b1.new_ab(is_risp=True)
b1.pitch_list("b b b b")
b1.reach("BB")
b1.advance(3, "8 1B")

# 7. KCR #8  Mike Moustakas (16 - 4 - 27)
b1.new_ab(is_risp=True)
b1.pitch_list("b c b")
b1.hit(1, rbis=2)

# 8. KCR #12 Brett Hayes (27 - X - 8)
b1.new_ab(is_risp=True)
b1.pitch_list("b c f f b f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: KCR #52 Bruce Chen
t2 = game.new_inning()

# 4. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("c f b f")
t2.out("F9")

# 5. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("F7")

# 6. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c b f")
t2.hit(1)

# 7. BOS #29 Daniel Nava (X - X - 12)
t2.new_ab()
t2.pitch_list("c b b")
t2.out("G5-3")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 9. KCR #2  Alcides Escobar (X - X - X)
b2.new_ab()
b2.pitch_list("f f b")
b2.out("L9")

# 1. KCR #6  Lorenzo Cain (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G5-3")

# 2. KCR #35 Eric Hosmer (X - X - X)
b2.new_ab()
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: KCR #52 Bruce Chen
t3 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("F8")

# 9. BOS #26 Brock Holt (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c c b")
t3.out("F7")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 3. KCR #16 Billy Butler (X - X - X)
b3.new_ab()
b3.pitch_list("c f b")
b3.out("G5-3")

# 4. KCR #4  Alex Gordon (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c")
b3.out("F8")

# 5. KCR #24 Miguel Tejada (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: KCR #52 Bruce Chen
t4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("P4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b c b")
t4.reach("BB")

# 4. BOS #5  Jonny Gomes (X - X - 15)
t4.new_ab()
t4.pitch_list("b f")
t4.out("P3")

# 5. BOS #7  Stephen Drew (X - X - 15)
t4.new_ab()
t4.pitch_list("b")
t4.out("P6")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 6. KCR #27 Justin Maxwell (X - X - X)
b4.new_ab()
b4.out("L7")

# 7. KCR #8  Mike Moustakas (X - X - X)
b4.new_ab()
b4.pitch_list("c b c")
b4.hit(1)
b4.thrown_out(2, "12 CS", 2, 31)

# 8. KCR #12 Brett Hayes (X - X - 8)
b4.new_ab()
b4.pitch_list("c b s")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: KCR #52 Bruce Chen
t5 = game.new_inning()

# 6. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("b b s f f s")
t5.out("K")

# 7. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("c b b f")
t5.out("(F)P2")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("L7")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 9. KCR #2  Alcides Escobar (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(2, "35 E3")

# 1. KCR #6  Lorenzo Cain (X - X - 2)
b5.new_ab()
b5.pitch_list("c b b b c t")
b5.out("KT")

# 2. KCR #35 Eric Hosmer (X - X - 2)
b5.new_ab()
b5.pitch_list("d b f c")
b5.error(3)
b5.reach("E3")

# 3. KCR #16 Billy Butler (X - 2 - 35)
b5.new_ab(is_risp=True)
b5.pitch_list("c f s")
b5.out("K")

# 4. KCR #4  Alex Gordon (X - 2 - 35)
b5.new_ab(is_risp=True)
b5.pitch_list("c b f b")
b5.out("P4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: KCR #52 Bruce Chen
t6 = game.new_inning()

# 9. BOS #26 Brock Holt (X - X - X)
t6.new_ab()
t6.pitch_list("c f f b b")
t6.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c f b b s")
t6.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("b c f")
t6.out("F7")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 5. KCR #24 Miguel Tejada (X - X - X)
b6.new_ab()
b6.pitch_list("f b f f b f")
b6.out("G5-3")

# 6. KCR #27 Justin Maxwell (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b b t")
b6.out("KT")

# 7. KCR #8  Mike Moustakas (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: KCR #52 Bruce Chen
t7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("b f f")
t7.out("G1-3")

# 4. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G4-3")

# 5. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("c b c b")
t7.hit(1)

# 6. BOS #12 Mike Napoli (X - X - 7)
t7.new_ab()
t7.pitch_list("b c")
t7.out("(F)F7")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# 8. KCR #12 Brett Hayes (X - X - X)
b7.new_ab()
b7.pitch_list("s b")
b7.out("F9")

# 9. KCR #2  Alcides Escobar (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.hit(1)
b7.advance(2, "6 SB")

# 1. KCR #6  Lorenzo Cain (X - X - 2)
b7.new_ab(is_risp=True)
b7.pitch_list("c d f f")
b7.out("L8")

# 2. KCR #35 Eric Hosmer (X - 2 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c d c f d f")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: KCR #52 Bruce Chen
t8 = game.new_inning()

# Defensive change (KCR): #23 Elliot Johnson replaces #24 Miguel Tejada (2B), playing 2B, batting 5th
t8.defensive_substitution(5, 23, "4")

# 7. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.advance(2, "2 1B")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t8.new_ab()
t8.pitch_list("c b")
t8.out("F8")

# 9. BOS #26 Brock Holt (X - X - 29)
t8.new_ab()
t8.pitch_list("c b b")
t8.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - X - 29)
t8.new_ab()
t8.pitch_list("f b b f")
t8.hit(1)

# Pitching change (KCR): #44 Luke Hochevar replaces #52 Bruce Chen
t8.pitching_substitution(44)

# 2. BOS #18 Shane Victorino (X - 29 - 2)
t8.new_ab(is_risp=True)
t8.pitch_list("f")
t8.out("P5")


# Bot 8th
# Pitching: BOS #62 Rubby De La Rosa
b8 = game.new_inning()

# Pitching change (BOS): #62 Rubby De La Rosa replaces #31 Jon Lester
b8.pitching_substitution(62)

# 3. KCR #16 Billy Butler (X - X - X)
b8.new_ab()
b8.hit(4)

# 4. KCR #4  Alex Gordon (X - X - X)
b8.new_ab()
b8.pitch_list("c s f f")
b8.out("G4-3")

# 5. KCR #23 Elliot Johnson (X - X - X)
b8.new_ab()
b8.pitch_list("s s b")
b8.out("F9")

# 6. KCR #27 Justin Maxwell (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c")
b8.hit(4)

# 7. KCR #8  Mike Moustakas (X - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: KCR #44 Luke Hochevar
t9 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G6-3")

# 4. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("c c b f")
t9.hit(2)
t9.advance(4, "7 1B")

# 5. BOS #7  Stephen Drew (X - 5 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b")
t9.hit(1, rbis=1)
t9.thrown_out(2, "12 DP5-4-3", 2, 44)

# 6. BOS #12 Mike Napoli (X - X - 7)
t9.new_ab()
t9.pitch_list("c")
t9.out("DP5-4-3")

# Winning team: KCR
# WP: KCR #52 Bruce Chen
game.winning_pitcher(52)
# SV: KCR #44 Luke Hochevar
game.save_pitcher(44)

# Loser team: BOS
# LP: BOS #31 Jon Lester
game.losing_pitcher(31, is_away_team=True)

# print(game)
game.generate_scorecard()
