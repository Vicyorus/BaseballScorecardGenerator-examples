import os
from baseball_scorecard.baseball_scorecard import Scorecard

# KC @ BOS, 2013-04-20
# https://www.baseball-reference.com/boxes/BOS/BOS201304200.shtml
# https://www.mlb.com/gameday/royals-vs-red-sox/2013/04/20/346997/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-20 13:35-16:33",
        "at": "Fenway Park, Boston, MA",
        "att": "35,152",
        "temp": "56F, Cloudy",
        "wind": "15mph, Out To RF",
        "away": {
            "team": "Kansas City Royals",
            "starter": 33,
            "roster": {
                # Lineup
                4: "Alex Gordon",
                2: "Alcides Escobar",
                16: "Billy Butler",
                35: "Eric Hosmer",
                6: "Lorenzo Cain",
                8: "Mike Moustakas",
                21: "Jeff Francoeur",
                13: "Salvador Perez",
                17: "Chris Getz",
                # Starting pitcher
                33: "James Shields",
                # Bench
                26: "George Kottaras",
                24: "Miguel Tejada",
                23: "Elliot Johnson",
                1: "Jarrod Dyson",
                # Bullpen
                56: "Greg Holland",
                54: "Ervin Santana",
                11: "Jeremy Guthrie",
                27: "Juan Gutierrez",
                52: "Bruce Chen",
                39: "Luis Mendoza",
                22: "Wade Davis",
                40: "Kelvin Herrera",
                43: "Aaron Crow",
                44: "Luke Hochevar",
                55: "Tim Collins",
            },
            "lefties": [52, 55],
            "lineup": [
                [4, "7"],
                [2, "6"],
                [16, "0"],
                [35, "3"],
                [6, "8"],
                [8, "5"],
                [21, "9"],
                [13, "2"],
                [17, "4"],
            ],
            "bench": [
                [26, "C"],
                [24, "SS"],
                [23, "SS"],
                [1, "CF"],
            ],
            "bullpen": [56, 54, 11, 27, 52, 39, 22, 40, 43, 44, 55],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                3: "David Ross",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                5: "Jonny Gomes",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                35: "Steven Wright",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [16, "5"],
                [7, "6"],
                [3, "2"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [5, "LF"],
                [23, "3B"],
            ],
            "bullpen": [63, 35, 40, 30, 91, 31, 59, 36, 19, 22, 46],
        },
        "umpires": {
            "HP": "Wally Bell",
            "1B": "Larry Vanover",
            "2B": "Tony Randazzo",
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
# Pitching: BOS #11 Clay Buchholz
t1 = game.new_inning()

# 1. KCR #4  Alex Gordon (X - X - X)
t1.new_ab()
t1.pitch_list("c s b b b s")
t1.out("K")

# 2. KCR #2  Alcides Escobar (X - X - X)
t1.new_ab()
t1.hit(1)
t1.thrown_out(2, "16 DP4-3", 2, 11)

# 3. KCR #16 Billy Butler (X - X - 2)
t1.new_ab()
t1.pitch_list("1 c 1")
t1.out("DP4-3")


# Bot 1st
# Pitching: KCR #33 James Shields
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b s")
b1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b b f")
b1.out("P6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b f f b f f b b")
b1.reach("BB")

# 4. BOS #34 David Ortiz (X - X - 15)
b1.new_ab()
b1.pitch_list("c b")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #11 Clay Buchholz
t2 = game.new_inning()

# 4. KCR #35 Eric Hosmer (X - X - X)
t2.new_ab()
t2.pitch_list("b b c c b f t")
t2.out("KT")

# 5. KCR #6  Lorenzo Cain (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "21 SB")

# 6. KCR #8  Mike Moustakas (X - X - 6)
t2.new_ab()
t2.pitch_list("1 c 1")
t2.out("F8")

# 7. KCR #21 Jeff Francoeur (X - X - 6)
t2.new_ab()
t2.pitch_list("b f 1 s b b c")
t2.out("!K")


# Bot 2nd
# Pitching: KCR #33 James Shields
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b s f f b")
b2.reach("BB")
b2.thrown_out(2, "29 DP3-6", 2, 33)

# 6. BOS #29 Daniel Nava (X - X - 12)
b2.new_ab()
b2.pitch_list("b 1 1 b 1 c")
b2.out("DP3-6")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("s s f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #11 Clay Buchholz
t3 = game.new_inning()

# 8. KCR #13 Salvador Perez (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G5-3")

# 9. KCR #17 Chris Getz (X - X - X)
t3.new_ab()
t3.pitch_list("b b c c f b")
t3.out("G4-3")

# 1. KCR #4  Alex Gordon (X - X - X)
t3.new_ab()
t3.pitch_list("c b c b f f s")
t3.out("K")


# Bot 3rd
# Pitching: KCR #33 James Shields
b3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("f s b b f c")
b3.out("!K")

# 9. BOS #3  David Ross (X - X - X)
b3.new_ab()
b3.pitch_list("c b c f f c")
b3.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b s")
b3.out("G1-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #11 Clay Buchholz
t4 = game.new_inning()

# 2. KCR #2  Alcides Escobar (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G6-3")

# 3. KCR #16 Billy Butler (X - X - X)
t4.new_ab()
t4.pitch_list("c b f")
t4.out("G6-3")

# 4. KCR #35 Eric Hosmer (X - X - X)
t4.new_ab()
t4.out("P6")


# Bot 4th
# Pitching: KCR #33 James Shields
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b b s")
b4.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G4-3")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b s")
b4.hit(1)

# 5. BOS #12 Mike Napoli (X - X - 34)
b4.new_ab()
b4.pitch_list("b s c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #11 Clay Buchholz
t5 = game.new_inning()

# 5. KCR #6  Lorenzo Cain (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(2)
t5.advance(3, "8 F8")
t5.advance(4, "21 1B")

# 6. KCR #8  Mike Moustakas (X - 6 - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("F8")

# 7. KCR #21 Jeff Francoeur (6 - X - X)
t5.new_ab()
t5.hit(1, rbis=1)
t5.advance(2, "13 SB")

# 8. KCR #13 Salvador Perez (X - X - 21)
t5.new_ab()
t5.pitch_list("1 1 b 1 b f f b c")
t5.out("!K")

# 9. KCR #17 Chris Getz (X - 21 - X)
t5.new_ab()
t5.pitch_list("s b b s c")
t5.out("!K")


# Bot 5th
# Pitching: KCR #33 James Shields
b5 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("b c b b b")
b5.reach("BB")
b5.thrown_out(2, "16 DP6-4-3", 1, 33)

# 7. BOS #16 Will Middlebrooks (X - X - 29)
b5.new_ab()
b5.pitch_list("s s")
b5.out("DP6-4-3")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b c b b")
b5.hit(1)

# 9. BOS #3  David Ross (X - X - 7)
b5.new_ab()
b5.pitch_list("b 1 b c f b f f f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #11 Clay Buchholz
t6 = game.new_inning()

# 1. KCR #4  Alex Gordon (X - X - X)
t6.new_ab()
t6.pitch_list("c f b")
t6.hit(2)
t6.advance(3, "2 SAC1-4")

# 2. KCR #2  Alcides Escobar (X - 4 - X)
t6.new_ab()
t6.pitch_list("l")
t6.out("SAC1-4")

# 3. KCR #16 Billy Butler (4 - X - X)
t6.new_ab()
t6.out("L6")

# 4. KCR #35 Eric Hosmer (4 - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("G4-3")


# Bot 6th
# Pitching: KCR #33 James Shields
b6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(1)
b6.advance(2, "18 SAC2-3")
b6.advance(3, "15 G5-3")
b6.advance(4, "34 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b6.new_ab()
b6.out("SAC2-3")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G5-3")

# 4. BOS #34 David Ortiz (2 - X - X)
b6.new_ab()
b6.pitch_list("d f b d")
b6.hit(1, rbis=1)

# 5. BOS #12 Mike Napoli (X - X - 34)
b6.new_ab()
b6.pitch_list("c b s s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #11 Clay Buchholz
t7 = game.new_inning()

# 5. KCR #6  Lorenzo Cain (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(2)
t7.advance(3, "21 G1-3")
t7.advance(4, "13 3B")

# 6. KCR #8  Mike Moustakas (X - 6 - X)
t7.new_ab()
t7.pitch_list("b f c")
t7.out("F7")

# 7. KCR #21 Jeff Francoeur (X - 6 - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G1-3")

# 8. KCR #13 Salvador Perez (6 - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(3, rbis=1)

# 9. KCR #17 Chris Getz (13 - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("B4-3")


# Bot 7th
# Pitching: KCR #43 Aaron Crow
b7 = game.new_inning()

# Pitching change (KCR): #43 Aaron Crow replaces #33 James Shields
b7.pitching_substitution(43)

# 6. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("c b f")
b7.reach("HBP")
b7.advance(2, "16 1B")
b7.thrown_out(2, "7 PO", 1, 43)

# 7. BOS #16 Will Middlebrooks (X - X - 29)
b7.new_ab()
b7.hit(1)
b7.error(5)
b7.advance(2, "7 E5")

# 8. BOS #7  Stephen Drew (X - 29 - 16)
b7.new_ab()
b7.pitch_list("b 2 f")
b7.reach("FC5")

# Pitching change (KCR): #55 Tim Collins replaces #43 Aaron Crow
b7.pitching_substitution(55)

# Offensive change (BOS): Pinch-hitter #39 Jarrod Saltalamacchia replaces #3 David Ross, batting 9th
b7.offensive_substitution(9, 39, "PH")

# 9. BOS #39 Jarrod Saltalamacchia (X - 16 - 7)
b7.new_ab()
b7.pitch_list("c")
b7.out("(F)P5")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - 7)
b7.new_ab()
b7.pitch_list("c b b")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #11 Clay Buchholz
t8 = game.new_inning()

# Defensive switch (BOS): #39 Jarrod Saltalamacchia moves to C
t8.defensive_switch(39, "2")

# 1. KCR #4  Alex Gordon (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G2-3")

# 2. KCR #2  Alcides Escobar (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.error(2)
t8.advance(2, "16 BB")
t8.advance(3, "16 E2")

# 3. KCR #16 Billy Butler (X - X - 2)
t8.new_ab()
t8.pitch_list("b 1 f d f d b")
t8.reach("BB")
t8.thrown_out(2, "35 DP4-6-3", 2, 11)

# 4. KCR #35 Eric Hosmer (2 - X - 16)
t8.new_ab()
t8.pitch_list("s")
t8.out("DP4-6-3")


# Bot 8th
# Pitching: KCR #55 Tim Collins
b8 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #18 Shane Victorino, batting 2nd
b8.offensive_substitution(2, 5, "PH")

# 2. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("c s b b")
b8.hit(2)
b8.advance(3, "34 DP6-3")
b8.advance(4, "29 HR")

# 3. BOS #15 Dustin Pedroia (X - 5 - X)
b8.new_ab()
b8.pitch_list("d b b s b")
b8.reach("BB")
b8.thrown_out(2, "34 DP6-3", 1, 55)

# 4. BOS #34 David Ortiz (X - 5 - 15)
b8.new_ab()
b8.pitch_list("c b b 2")
b8.out("DP6-3")

# Pitching change (KCR): #40 Kelvin Herrera replaces #55 Tim Collins
b8.pitching_substitution(40)

# 5. BOS #12 Mike Napoli (5 - X - X)
b8.new_ab()
b8.pitch_list("d b b b")
b8.reach("BB")
b8.advance(4, "29 HR")

# 6. BOS #29 Daniel Nava (5 - X - 12)
b8.new_ab()
b8.pitch_list("c b")
b8.hit(4, rbis=3)

# 7. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #11 Clay Buchholz
t9.pitching_substitution(40)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t9.defensive_switch(5, "7")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
t9.defensive_switch(29, "9")

# 5. KCR #6  Lorenzo Cain (X - X - X)
t9.new_ab()
t9.pitch_list("c b s b")
t9.hit(4)

# 6. KCR #8  Mike Moustakas (X - X - X)
t9.new_ab()
t9.out("F8")

# 7. KCR #21 Jeff Francoeur (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
t9.advance(2, "26 BB")

# 8. KCR #13 Salvador Perez (X - X - 21)
t9.new_ab()
t9.pitch_list("s f s")
t9.out("K")

# Offensive change (KCR): Pinch-hitter #26 George Kottaras replaces #17 Chris Getz, batting 9th
t9.offensive_substitution(9, 26, "PH")

# 9. KCR #26 George Kottaras (X - X - 21)
t9.new_ab()
t9.pitch_list("b b s b b")
t9.reach("BB")
# Offensive change (KCR): Pinch-runner #23 Elliot Johnson replaces #26 George Kottaras
t9.offensive_substitution(9, 23, "PR")
t9.atbase("PR")

# 1. KCR #4  Alex Gordon (X - 21 - 26)
t9.new_ab()
t9.pitch_list("b f b f b")
t9.out("G6-3")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11)
# SV: BOS #40 Andrew Bailey
game.save_pitcher(40)

# Loser team: KCR
# LP: KCR #40 Kelvin Herrera
game.losing_pitcher(40, is_away_team=True)

# print(game)
game.generate_scorecard()
