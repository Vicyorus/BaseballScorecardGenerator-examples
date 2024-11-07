import os
from baseball_scorecard.baseball_scorecard import Scorecard

# KC @ BOS, 2013-04-21
# https://www.baseball-reference.com/boxes/BOS/BOS201304211.shtml
# https://www.mlb.com/gameday/royals-vs-red-sox/2013/04/21/347011/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-21 13:35-16:29",
        "at": "Fenway Park, Boston, MA",
        "att": "31,483",
        "temp": "48F, Sunny",
        "wind": "13mph, L To R",
        "away": {
            "team": "Kansas City Royals",
            "starter": 54,
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
                54: "Ervin Santana",
                # Bench
                26: "George Kottaras",
                24: "Miguel Tejada",
                23: "Elliot Johnson",
                1: "Jarrod Dyson",
                # Bullpen
                56: "Greg Holland",
                11: "Jeremy Guthrie",
                33: "James Shields",
                27: "Juan Gutierrez",
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
            "bullpen": [56, 11, 33, 27, 52, 39, 22, 40, 53, 43, 44, 55],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                5: "Jonny Gomes",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                37: "Mike Carp",
                18: "Shane Victorino",
                3: "David Ross",
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
                11: "Clay Buchholz",
                64: "Allen Webster",
                19: "Koji Uehara",
                22: "Felix Doubront",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
                [5, "7"],
            ],
            "bench": [
                [37, "1B"],
                [18, "CF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [63, 35, 40, 30, 91, 31, 59, 36, 11, 64, 19, 22],
        },
        "umpires": {
            "HP": "Larry Vanover",
            "1B": "Lance Barrett",
            "2B": "Manny Gonzalez",
            "3B": "Wally Bell",
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
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. KCR #4  Alex Gordon (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("F7")

# 2. KCR #2  Alcides Escobar (X - X - X)
t1.new_ab()
t1.hit(4)

# 3. KCR #16 Billy Butler (X - X - X)
t1.new_ab()
t1.pitch_list("c b f f b s")
t1.out("K")

# 4. KCR #35 Eric Hosmer (X - X - X)
t1.new_ab()
t1.pitch_list("s b b s f")
t1.hit(1)
t1.advance(2, "6 SB")

# 5. KCR #6  Lorenzo Cain (X - X - 35)
t1.new_ab(is_risp=True)
t1.pitch_list("c b")
t1.out("G5-3")


# Bot 1st
# Pitching: KCR #54 Ervin Santana
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("(F)P3")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.hit(1)
b1.advance(2, "15 1B")
b1.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b1.new_ab()
b1.pitch_list("c f")
b1.hit(1)
b1.advance(3, "34 1B")
b1.advance(4, "12 G4-3")

# 4. BOS #34 David Ortiz (X - 29 - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("b f d c d f")
b1.hit(1, rbis=1)
b1.advance(2, "12 G4-3")

# 5. BOS #12 Mike Napoli (15 - X - 34)
b1.new_ab(is_risp=True)
b1.pitch_list("b f s b f")
b1.out("G4-3", rbis=1)

# 6. BOS #39 Jarrod Saltalamacchia (X - 34 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c b s")
b1.out("L9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 6. KCR #8  Mike Moustakas (X - X - X)
t2.new_ab()
t2.pitch_list("b b c")
t2.out("G3")

# 7. KCR #21 Jeff Francoeur (X - X - X)
t2.new_ab()
t2.pitch_list("b b f s f s")
t2.out("K")

# 8. KCR #13 Salvador Perez (X - X - X)
t2.new_ab()
t2.pitch_list("c f s")
t2.out("K")


# Bot 2nd
# Pitching: KCR #54 Ervin Santana
b2 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.hit(1)
b2.advance(2, "2 1B")

# 8. BOS #7  Stephen Drew (X - X - 16)
b2.new_ab()
b2.pitch_list("c b f d f t")
b2.out("KT")

# 9. BOS #5  Jonny Gomes (X - X - 16)
b2.new_ab()
b2.pitch_list("c 1 b d")
b2.out("P6")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b2.new_ab()
b2.hit(1)

# 2. BOS #29 Daniel Nava (X - 16 - 2)
b2.new_ab(is_risp=True)
b2.pitch_list("c b c d b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 9. KCR #17 Chris Getz (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("F7")

# 1. KCR #4  Alex Gordon (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c s b")
t3.reach("BB")
t3.thrown_out(2, "2 DP6-4-3", 2, 46)

# 2. KCR #2  Alcides Escobar (X - X - 4)
t3.new_ab()
t3.pitch_list("f b b 1 f f 1")
t3.out("DP6-4-3")


# Bot 3rd
# Pitching: KCR #54 Ervin Santana
b3 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("c b f")
b3.out("L7")

# 4. BOS #34 David Ortiz (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("G3-1")

# 5. BOS #12 Mike Napoli (X - X - X)
b3.new_ab()
b3.pitch_list("c f f b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 3. KCR #16 Billy Butler (X - X - X)
t4.new_ab()
t4.hit(1)
t4.advance(2, "35 1B")
t4.advance(4, "6 2B")

# 4. KCR #35 Eric Hosmer (X - X - 16)
t4.new_ab()
t4.pitch_list("b c f")
t4.hit(1)
t4.advance(3, "6 2B")
t4.advance(4, "13 1B")

# 5. KCR #6  Lorenzo Cain (X - 16 - 35)
t4.new_ab(is_risp=True)
t4.hit(2, rbis=1)
t4.advance(4, "13 1B")

# 6. KCR #8  Mike Moustakas (35 - 6 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b s b f f s")
t4.out("K")

# 7. KCR #21 Jeff Francoeur (35 - 6 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b s f s")
t4.out("K")

# 8. KCR #13 Salvador Perez (35 - 6 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c b")
t4.hit(1, rbis=2)

# 9. KCR #17 Chris Getz (X - X - 13)
t4.new_ab()
t4.pitch_list("c c")
t4.out("(F)P5")


# Bot 4th
# Pitching: KCR #54 Ervin Santana
b4 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("F8")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s s")
b4.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 1. KCR #4  Alex Gordon (X - X - X)
t5.new_ab()
t5.pitch_list("c f c")
t5.out("!K")

# 2. KCR #2  Alcides Escobar (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("G3")

# 3. KCR #16 Billy Butler (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("F7")


# Bot 5th
# Pitching: KCR #54 Ervin Santana
b5 = game.new_inning()

# 9. BOS #5  Jonny Gomes (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("f b b")
b5.out("F9")

# 2. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("c f b")
b5.out("G3-1")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 4. KCR #35 Eric Hosmer (X - X - X)
t6.new_ab()
t6.pitch_list("f f")
t6.out("F7")

# 5. KCR #6  Lorenzo Cain (X - X - X)
t6.new_ab()
t6.pitch_list("b c b b b")
t6.reach("BB")
t6.advance(2, "8 BB")

# 6. KCR #8  Mike Moustakas (X - X - 6)
t6.new_ab()
t6.pitch_list("1 b d 1 b b")
t6.reach("BB")

# 7. KCR #21 Jeff Francoeur (X - 6 - 8)
t6.new_ab(is_risp=True)
t6.pitch_list("c c s")
t6.out("K")

# 8. KCR #13 Salvador Perez (X - 6 - 8)
t6.new_ab(is_risp=True)
t6.pitch_list("f f")
t6.out("F8")


# Bot 6th
# Pitching: KCR #54 Ervin Santana
b6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("b b c c")
b6.out("P5")

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(2)
b6.advance(3, "12 F9")

# 5. BOS #12 Mike Napoli (X - 34 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f")
b6.out("F9")

# 6. BOS #39 Jarrod Saltalamacchia (34 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f b s d s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #46 Ryan Dempster
t7 = game.new_inning()

# 9. KCR #17 Chris Getz (X - X - X)
t7.new_ab()
t7.pitch_list("c b s f")
t7.out("G3")

# 1. KCR #4  Alex Gordon (X - X - X)
t7.new_ab()
t7.pitch_list("c s f b s")
t7.out("K")

# 2. KCR #2  Alcides Escobar (X - X - X)
t7.new_ab()
t7.out("P4")


# Bot 7th
# Pitching: KCR #54 Ervin Santana
b7 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("F9")

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("b c f s")
b7.out("K")

# 9. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("f f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #59 Clayton Mortensen
t8 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #46 Ryan Dempster
t8.pitching_substitution(59)

# 3. KCR #16 Billy Butler (X - X - X)
t8.new_ab()
t8.pitch_list("c b c")
t8.out("G5-3")

# 4. KCR #35 Eric Hosmer (X - X - X)
t8.new_ab()
t8.pitch_list("c b s s")
t8.out("K")

# 5. KCR #6  Lorenzo Cain (X - X - X)
t8.new_ab()
t8.pitch_list("b s b f s")
t8.out("K")


# Bot 8th
# Pitching: KCR #52 Bruce Chen
b8 = game.new_inning()

# Pitching change (KCR): #52 Bruce Chen replaces #54 Ervin Santana
b8.pitching_substitution(52)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G4-3")

# 2. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.hit(1)
b8.advance(2, "34 1B")
b8.advance(3, "12 BB")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b8.new_ab()
b8.pitch_list("b b f b 1 c")
b8.out("F8")

# 4. BOS #34 David Ortiz (X - X - 29)
b8.new_ab()
b8.pitch_list("b s s b")
b8.hit(1)
# Offensive change (BOS): Pinch-runner #23 Pedro Ciriaco replaces #34 David Ortiz
b8.offensive_substitution(4, 23, "PR")
b8.atbase("PR")
b8.advance(2, "12 BB")

# Pitching change (KCR): #43 Aaron Crow replaces #52 Bruce Chen
b8.pitching_substitution(43)

# 5. BOS #12 Mike Napoli (X - 29 - 34)
b8.new_ab(is_risp=True)
b8.pitch_list("b b b b")
b8.reach("BB")

# 6. BOS #39 Jarrod Saltalamacchia (29 - 23 - 12)
b8.new_ab(is_risp=True)
b8.pitch_list("b b")
b8.out("G1-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #63 Alex Wilson
t9 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #59 Clayton Mortensen
t9.pitching_substitution(63)

# Defensive switch (BOS): #23 Pedro Ciriaco moves to DH
t9.defensive_switch(23, "0")

# 6. KCR #8  Mike Moustakas (X - X - X)
t9.new_ab()
t9.pitch_list("b b c f")
t9.hit(1)
t9.advance(2, "21 1B")
t9.thrown_out(3, "13 DP5-4", 1, 63)

# 7. KCR #21 Jeff Francoeur (X - X - 8)
t9.new_ab()
t9.pitch_list("b b d c s")
t9.hit(1)
t9.thrown_out(2, "13 DP5-4", 2, 63)

# 8. KCR #13 Salvador Perez (X - 8 - 21)
t9.new_ab(is_risp=True)
t9.pitch_list("c b")
t9.reach("DP5-4")

# 9. KCR #17 Chris Getz (X - X - 13)
t9.new_ab()
t9.pitch_list("c")
t9.out("F7")


# Bot 9th
# Pitching: KCR #56 Greg Holland
b9 = game.new_inning()

# Pitching change (KCR): #56 Greg Holland replaces #43 Aaron Crow
b9.pitching_substitution(56)

# 7. BOS #16 Will Middlebrooks (X - X - X)
b9.new_ab()
b9.pitch_list("b b c s s")
b9.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b9.new_ab()
b9.pitch_list("c c s")
b9.out("K")

# 9. BOS #5  Jonny Gomes (X - X - X)
b9.new_ab()
b9.pitch_list("b b")
b9.out("F8")

# Winning team: KCR
# WP: KCR #54 Ervin Santana
game.winning_pitcher(54, is_away_team=True)
# SV: KCR #56 Greg Holland
game.save_pitcher(56, is_away_team=True)

# Loser team: BOS
# LP: BOS #46 Ryan Dempster
game.losing_pitcher(46)

# print(game)
game.generate_scorecard()
