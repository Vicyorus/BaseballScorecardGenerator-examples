import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ KC, 2013-08-10
# https://www.baseball-reference.com/boxes/KCA/KCA201308100.shtml
# https://www.mlb.com/gameday/red-sox-vs-royals/2013/08/10/348475/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-10 19:12-22:40",
        "at": "Kauffman Stadium, Kansas City, MO",
        "att": "38,742",
        "temp": "82F, Clear",
        "wind": "7mph, In From RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                37: "Mike Carp",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                26: "Brock Holt",
                29: "Daniel Nava",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                62: "Rubby De La Rosa",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 32, 66, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [37, "7"],
                [12, "3"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
            ],
            "bench": [
                [26, "2B"],
                [29, "LF"],
                [5, "LF"],
                [20, "C"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 19, 62, 46],
        },
        "home": {
            "team": "Kansas City Royals",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Alcides Escobar",
                35: "Eric Hosmer",
                16: "Billy Butler",
                4: "Alex Gordon",
                27: "Justin Maxwell",
                24: "Miguel Tejada",
                8: "Mike Moustakas",
                12: "Brett Hayes",
                1: "Jarrod Dyson",
                # Starting pitcher
                11: "Jeremy Guthrie",
                # Bench
                7: "David Lough",
                26: "George Kottaras",
                23: "Elliot Johnson",
                # Bullpen
                56: "Greg Holland",
                54: "Ervin Santana",
                33: "James Shields",
                31: "Louis Coleman",
                52: "Bruce Chen",
                39: "Luis Mendoza",
                40: "Kelvin Herrera",
                53: "Will Smith",
                43: "Aaron Crow",
                44: "Luke Hochevar",
                55: "Tim Collins",
                49: "Donnie Joseph",
            },
            "lefties": [52, 53, 55, 49],
            "lineup": [
                [2, "6"],
                [35, "3"],
                [16, "0"],
                [4, "7"],
                [27, "9"],
                [24, "4"],
                [8, "5"],
                [12, "2"],
                [1, "8"],
            ],
            "bench": [
                [7, "LF"],
                [26, "C"],
                [23, "SS"],
            ],
            "bullpen": [56, 54, 33, 31, 52, 39, 40, 53, 43, 44, 55, 49],
        },
        "umpires": {
            "HP": "Alan Porter",
            "1B": "Greg Gibson",
            "2B": "Jerry Layne",
            "3B": "Hunter Wendelstedt",
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
# Pitching: KCR #11 Jeremy Guthrie
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b s f")
t1.hit(1)
t1.thrown_out(2, "18 FC1-6", 1, 11)

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("c c b b f 1 f")
t1.reach("FC1-6")
t1.advance(2, "34 SB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t1.new_ab()
t1.pitch_list("s 1 d 1 f 1 b f b f c")
t1.out("!K")

# 4. BOS #34 David Ortiz (X - X - 18)
t1.new_ab()
t1.pitch_list("c b b c s")
t1.out("K")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. KCR #2  Alcides Escobar (X - X - X)
b1.new_ab()
b1.pitch_list("c c f b")
b1.out("G4-3")

# 2. KCR #35 Eric Hosmer (X - X - X)
b1.new_ab()
b1.pitch_list("f b b c")
b1.hit(1)
b1.advance(2, "4 BB")
b1.advance(3, "27 WP")

# 3. KCR #16 Billy Butler (X - X - 35)
b1.new_ab()
b1.pitch_list("d c b b f f")
b1.out("F8")

# 4. KCR #4  Alex Gordon (X - X - 35)
b1.new_ab()
b1.pitch_list("1 b s b f b f b")
b1.reach("BB")
b1.advance(2, "27 WP")

# 5. KCR #27 Justin Maxwell (X - 35 - 4)
b1.new_ab()
b1.pitch_list("b c c b b d")
b1.wp()
b1.reach("BB")

# 6. KCR #24 Miguel Tejada (35 - 4 - 27)
b1.new_ab()
b1.pitch_list("b b c")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: KCR #11 Jeremy Guthrie
t2 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1)

# 6. BOS #12 Mike Napoli (X - X - 37)
t2.new_ab()
t2.pitch_list("c b 1 b s c")
t2.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t2.new_ab()
t2.pitch_list("b f f f d c")
t2.out("!K")

# 8. BOS #7  Stephen Drew (X - X - 37)
t2.new_ab()
t2.pitch_list("c d")
t2.out("(F)P5")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 7. KCR #8  Mike Moustakas (X - X - X)
b2.new_ab()
b2.pitch_list("b f f b c")
b2.out("!K")

# 8. KCR #12 Brett Hayes (X - X - X)
b2.new_ab()
b2.pitch_list("c f f b f b b f f")
b2.out("G6-3")

# 9. KCR #1  Jarrod Dyson (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b c b")
b2.reach("BB")

# 1. KCR #2  Alcides Escobar (X - X - 1)
b2.new_ab()
b2.pitch_list("f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: KCR #11 Jeremy Guthrie
t3 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c f b f b")
t3.hit(1)
t3.advance(2, "15 SB")
t3.advance(3, "15 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
t3.new_ab()
t3.pitch_list("1 1 c 1")
t3.out("L6")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t3.new_ab()
t3.pitch_list("p b c b c")
t3.hit(1)

# 4. BOS #34 David Ortiz (2 - X - 15)
t3.new_ab()
t3.pitch_list("b f b")
t3.out("F7")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 2. KCR #35 Eric Hosmer (X - X - X)
b3.new_ab()
b3.pitch_list("c b t s")
b3.out("K")

# 3. KCR #16 Billy Butler (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(1)
b3.advance(2, "27 1B")

# 4. KCR #4  Alex Gordon (X - X - 16)
b3.new_ab()
b3.out("F9")

# 5. KCR #27 Justin Maxwell (X - X - 16)
b3.new_ab()
b3.pitch_list("c f")
b3.hit(1)

# 6. KCR #24 Miguel Tejada (X - 16 - 27)
b3.new_ab()
b3.pitch_list("b c f f f")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: KCR #11 Jeremy Guthrie
t4 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("b b c b f f b")
t4.reach("BB")
t4.advance(2, "39 1B")
t4.advance(4, "7 2B")

# 6. BOS #12 Mike Napoli (X - X - 37)
t4.new_ab()
t4.pitch_list("b f f b s")
t4.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(1)
t4.advance(3, "7 2B")
t4.advance(4, "16 1B")

# 8. BOS #7  Stephen Drew (X - 37 - 39)
t4.new_ab()
t4.pitch_list("b b c")
t4.hit(2, rbis=1)
t4.advance(4, "16 1B")

# 9. BOS #16 Will Middlebrooks (39 - 7 - X)
t4.new_ab()
t4.pitch_list("b b")
t4.hit(1, rbis=2)
t4.advance(4, "2 2B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
t4.new_ab()
t4.pitch_list("b b")
t4.hit(2, rbis=1)

# 2. BOS #18 Shane Victorino (X - 2 - X)
t4.new_ab()
t4.pitch_list("f f 2 b")
t4.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
t4.new_ab()
t4.pitch_list("d b")
t4.out("F8")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 7. KCR #8  Mike Moustakas (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("F9")

# 8. KCR #12 Brett Hayes (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("F8")

# 9. KCR #1  Jarrod Dyson (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b c f")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: KCR #11 Jeremy Guthrie
t5 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c c f")
t5.out("P5")

# 5. BOS #37 Mike Carp (X - X - X)
t5.new_ab()
t5.out("G3")

# 6. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("F8")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 1. KCR #2  Alcides Escobar (X - X - X)
b5.new_ab()
b5.pitch_list("b c f b f b b")
b5.reach("BB")
b5.advance(4, "35 2B")

# 2. KCR #35 Eric Hosmer (X - X - 2)
b5.new_ab()
b5.hit(2, rbis=1)
b5.advance(4, "16 2B")

# 3. KCR #16 Billy Butler (X - 35 - X)
b5.new_ab()
b5.hit(2, rbis=1)
b5.advance(3, "4 1B")
b5.advance(4, "24 1B")

# 4. KCR #4  Alex Gordon (X - 16 - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)
b5.advance(2, "24 1B")
b5.advance(3, "8 SB")

# Pitching change (BOS): #67 Brandon Workman replaces #22 Felix Doubront
b5.pitching_substitution(67)

# 5. KCR #27 Justin Maxwell (16 - X - 4)
b5.new_ab()
b5.pitch_list("c c s")
b5.out("K")

# 6. KCR #24 Miguel Tejada (16 - X - 4)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1, rbis=1)
b5.advance(2, "8 SB")

# 7. KCR #8  Mike Moustakas (X - 4 - 24)
b5.new_ab()
b5.pitch_list("c c b")
b5.out("P6")

# 8. KCR #12 Brett Hayes (4 - 24 - X)
b5.new_ab()
b5.pitch_list("c s s")
b5.out("K2-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: KCR #11 Jeremy Guthrie
t6 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("F8")

# 8. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c f")
t6.out("G3")

# 9. BOS #16 Will Middlebrooks (X - X - X)
t6.new_ab()
t6.pitch_list("c t b f b b")
t6.hit(1)
t6.advance(4, "2 2B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
t6.new_ab()
t6.pitch_list("b d")
t6.hit(2, rbis=1)
t6.thrown_out(3, "7-6-2-5", 3, 11)


# Bot 6th
# Pitching: BOS #67 Brandon Workman
b6 = game.new_inning()

# 9. KCR #1  Jarrod Dyson (X - X - X)
b6.new_ab()
b6.pitch_list("c b b f b t")
b6.out("KT")

# 1. KCR #2  Alcides Escobar (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.thrown_out(2, "35 DP4-6-3", 2, 32)

# Pitching change (BOS): #32 Craig Breslow replaces #67 Brandon Workman
b6.pitching_substitution(32)

# 2. KCR #35 Eric Hosmer (X - X - 2)
b6.new_ab()
b6.pitch_list("c f b f f")
b6.out("DP4-6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: KCR #44 Luke Hochevar
t7 = game.new_inning()

# Pitching change (KCR): #44 Luke Hochevar replaces #11 Jeremy Guthrie
t7.pitching_substitution(44)

# 2. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.pitch_list("f f b b s")
t7.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c b")
t7.reach("BB")
t7.advance(2, "37 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
t7.new_ab()
t7.pitch_list("b s 1 b b f")
t7.out("F9")

# 5. BOS #37 Mike Carp (X - X - 15)
t7.new_ab()
t7.pitch_list("b f c d")
t7.hit(1)
# Offensive change (BOS): Pinch-runner #29 Daniel Nava replaces #37 Mike Carp
t7.offensive_substitution(5, 29, "PR")
t7.atbase("PR")

# Defensive change (KCR): #23 Elliot Johnson replaces #24 Miguel Tejada (2B), playing 2B, batting 6th
t7.defensive_substitution(6, 23, "4")

# 6. BOS #12 Mike Napoli (X - 15 - 37)
t7.new_ab()
t7.pitch_list("c d s s")
t7.out("K")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
b7.pitching_substitution(36)

# Defensive switch (BOS): #29 Daniel Nava moves to LF
b7.defensive_switch(29, "7")

# 3. KCR #16 Billy Butler (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.hit(2)

# 4. KCR #4  Alex Gordon (X - 16 - X)
b7.new_ab()
b7.out("F7")

# 5. KCR #27 Justin Maxwell (X - 16 - X)
b7.new_ab()
b7.pitch_list("s b d c b s")
b7.out("K")

# 6. KCR #23 Elliot Johnson (X - 16 - X)
b7.new_ab()
b7.pitch_list("l c c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: KCR #49 Donnie Joseph
t8 = game.new_inning()

# Pitching change (KCR): #49 Donnie Joseph replaces #44 Luke Hochevar
t8.pitching_substitution(49)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.out("G6-3")

# 8. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("c s b s")
t8.out("K")

# 9. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.pitch_list("b c f")
t8.out("G1-4-3")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# 7. KCR #8  Mike Moustakas (X - X - X)
b8.new_ab()
b8.pitch_list("b c c f")
b8.out("F7")

# 8. KCR #12 Brett Hayes (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(2)

# 9. KCR #1  Jarrod Dyson (X - 12 - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("L8")

# 1. KCR #2  Alcides Escobar (X - 12 - X)
b8.new_ab()
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: KCR #49 Donnie Joseph
t9 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("b b f b f")
t9.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.hit(1)
t9.advance(2, "34 BB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t9.new_ab()
t9.pitch_list("b f t f s")
t9.out("K")

# 4. BOS #34 David Ortiz (X - X - 18)
t9.new_ab()
t9.pitch_list("b b f b b")
t9.reach("BB")

# 5. BOS #29 Daniel Nava (X - 18 - 34)
t9.new_ab()
t9.pitch_list("b")
t9.out("F9")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
b9.pitching_substitution(19)

# 2. KCR #35 Eric Hosmer (X - X - X)
b9.new_ab()
b9.pitch_list("b c f")
b9.out("G3")

# 3. KCR #16 Billy Butler (X - X - X)
b9.new_ab()
b9.pitch_list("b c b b f")
b9.out("G5-3")

# 4. KCR #4  Alex Gordon (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("F7")

# Winning team: BOS
# WP: BOS #67 Brandon Workman
game.winning_pitcher(67, is_away_team=True)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19, is_away_team=True)

# Loser team: KCR
# LP: KCR #11 Jeremy Guthrie
game.losing_pitcher(11)

# print(game)
game.generate_scorecard()
