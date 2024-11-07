import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ SF, 2013-08-20
# https://www.baseball-reference.com/boxes/SFN/SFN201308200.shtml
# https://www.mlb.com/gameday/red-sox-vs-giants/2013/08/20/348612/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-20 22:15-01:14 +1",
        "at": "AT&T Park, San Francisco, CA",
        "att": "41,551",
        "temp": "64F, Clear",
        "wind": "8mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 44,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                37: "Mike Carp",
                16: "Will Middlebrooks",
                29: "Daniel Nava",
                72: "Xander Bogaerts",
                3: "David Ross",
                44: "Jake Peavy",
                # Starting pitcher
                44: "Jake Peavy",
                # Bench
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                34: "David Ortiz",
                5: "Jonny Gomes",
                12: "Mike Napoli",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                60: "Brayan Villarreal",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [37, "3"],
                [16, "5"],
                [29, "7"],
                [72, "6"],
                [3, "2"],
                [44, "1"],
            ],
            "bench": [
                [7, "SS"],
                [39, "C"],
                [34, "DH"],
                [5, "LF"],
                [12, "1B"],
            ],
            "bullpen": [41, 67, 56, 60, 32, 66, 31, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "San Francisco Giants",
            "starter": 32,
            "roster": {
                # Lineup
                7: "Grégor Blanco",
                19: "Marco Scutaro",
                9: "Brandon Belt",
                28: "Buster Posey",
                8: "Hunter Pence",
                35: "Brandon Crawford",
                22: "Roger Kieschnick",
                13: "Joaquin Arias",
                32: "Ryan Vogelsong",
                # Starting pitcher
                32: "Ryan Vogelsong",
                # Bench
                56: "Andres Torres",
                6: "Brett Pill",
                29: "Héctor Sánchez",
                48: "Pablo Sandoval",
                # Bullpen
                55: "Tim Lincecum",
                40: "Madison Bumgarner",
                63: "Jean Machi",
                43: "Sandy Rosario",
                34: "Guillermo Moscoso",
                75: "Barry Zito",
                50: "Jose Mijares",
                49: "Javier López",
                59: "Mike Kickham",
                18: "Matt Cain",
                46: "Santiago Casilla",
                54: "Sergio Romo",
            },
            "lefties": [40, 75, 50, 49, 59],
            "lineup": [
                [7, "8"],
                [19, "4"],
                [9, "3"],
                [28, "2"],
                [8, "9"],
                [35, "6"],
                [22, "7"],
                [13, "5"],
                [32, "1"],
            ],
            "bench": [
                [56, "CF"],
                [6, "1B"],
                [29, "C"],
                [48, "3B"],
            ],
            "bullpen": [55, 40, 63, 43, 34, 75, 50, 49, 59, 18, 46, 54],
        },
        "umpires": {
            "HP": "Mike Everitt",
            "1B": "Dan Bellino",
            "2B": "Bruce Dreckman",
            "3B": "Tim Welke",
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
# Pitching: SFG #32 Ryan Vogelsong
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.advance(2, "18 SB")
t1.advance(3, "15 1B")
t1.advance(4, "37 SF9")

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab(is_risp=True)
t1.pitch_list("c b")
t1.reach("HBP")
t1.advance(2, "15 1B")
t1.advance(3, "16 1B")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t1.new_ab(is_risp=True)
t1.pitch_list("b d c d")
t1.hit(1)
t1.advance(2, "16 1B")

# 4. BOS #37 Mike Carp (2 - 18 - 15)
t1.new_ab(is_risp=True)
t1.out("SF9", rbis=1)

# 5. BOS #16 Will Middlebrooks (X - 18 - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("f")
t1.hit(1)

# 6. BOS #29 Daniel Nava (18 - 15 - 16)
t1.new_ab(is_risp=True)
t1.pitch_list("f c")
t1.out("F7")

# 7. BOS #72 Xander Bogaerts (18 - 15 - 16)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.out("G1-4-3")


# Bot 1st
# Pitching: BOS #44 Jake Peavy
b1 = game.new_inning()

# 1. SFG #7  Grégor Blanco (X - X - X)
b1.new_ab()
b1.pitch_list("b c f")
b1.out("P5")

# 2. SFG #19 Marco Scutaro (X - X - X)
b1.new_ab()
b1.pitch_list("c c b")
b1.out("F7")

# 3. SFG #9  Brandon Belt (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SFG #32 Ryan Vogelsong
t2 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b f b")
t2.out("G5-3")

# 9. BOS #44 Jake Peavy (X - X - X)
t2.new_ab()
t2.out("G1-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t2.new_ab()
t2.pitch_list("c c c")
t2.out("!K")


# Bot 2nd
# Pitching: BOS #44 Jake Peavy
b2 = game.new_inning()

# 4. SFG #28 Buster Posey (X - X - X)
b2.new_ab()
b2.pitch_list("b b c c c")
b2.out("!K")

# 5. SFG #8  Hunter Pence (X - X - X)
b2.new_ab()
b2.pitch_list("b b c f b f f f b")
b2.reach("BB")
b2.advance(2, "22 1B")

# 6. SFG #35 Brandon Crawford (X - X - 8)
b2.new_ab()
b2.out("F7")

# 7. SFG #22 Roger Kieschnick (X - X - 8)
b2.new_ab()
b2.pitch_list("c s b")
b2.hit(1)

# 8. SFG #13 Joaquin Arias (X - 8 - 22)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SFG #32 Ryan Vogelsong
t3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("b b c c b")
t3.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b b b")
t3.reach("BB")
t3.advance(3, "29 2B")

# 4. BOS #37 Mike Carp (X - X - 15)
t3.new_ab()
t3.pitch_list("1 c b b c 1 b")
t3.out("L7")

# 5. BOS #16 Will Middlebrooks (X - X - 15)
t3.new_ab()
t3.pitch_list("c b")
t3.out("P3")

# 6. BOS #29 Daniel Nava (X - X - 15)
t3.new_ab()
t3.pitch_list("b c b f")
t3.hit(2)

# 7. BOS #72 Xander Bogaerts (15 - 29 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c b b")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #44 Jake Peavy
b3 = game.new_inning()

# 9. SFG #32 Ryan Vogelsong (X - X - X)
b3.new_ab()
b3.pitch_list("c b c s")
b3.out("K")

# 1. SFG #7  Grégor Blanco (X - X - X)
b3.new_ab()
b3.pitch_list("f f b b b")
b3.out("(F)F7")

# 2. SFG #19 Marco Scutaro (X - X - X)
b3.new_ab()
b3.pitch_list("c c b")
b3.out("L3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SFG #32 Ryan Vogelsong
t4 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("L8")

# 9. BOS #44 Jake Peavy (X - X - X)
t4.new_ab()
t4.pitch_list("b b f")
t4.out("G1-6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G3")


# Bot 4th
# Pitching: BOS #44 Jake Peavy
b4 = game.new_inning()

# 3. SFG #9  Brandon Belt (X - X - X)
b4.new_ab()
b4.hit(3)

# 4. SFG #28 Buster Posey (9 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b f b f f")
b4.out("G5-3")

# 5. SFG #8  Hunter Pence (9 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("f c b d s")
b4.out("K")

# 6. SFG #35 Brandon Crawford (9 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b c c t")
b4.out("KT")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SFG #32 Ryan Vogelsong
t5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G6-3")

# 4. BOS #37 Mike Carp (X - X - X)
t5.new_ab()
t5.pitch_list("c s b b b s")
t5.out("K")


# Bot 5th
# Pitching: BOS #44 Jake Peavy
b5 = game.new_inning()

# 7. SFG #22 Roger Kieschnick (X - X - X)
b5.new_ab()
b5.pitch_list("c b b f")
b5.hit(1)
b5.advance(4, "13 3B")

# 8. SFG #13 Joaquin Arias (X - X - 22)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(3, rbis=1)

# 9. SFG #32 Ryan Vogelsong (13 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b f")
b5.out("G4-3")

# 1. SFG #7  Grégor Blanco (13 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b s")
b5.out("G4-3")

# 2. SFG #19 Marco Scutaro (13 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b c c b")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SFG #32 Ryan Vogelsong
t6 = game.new_inning()

# 5. BOS #16 Will Middlebrooks (X - X - X)
t6.new_ab()
t6.pitch_list("c c b b s")
t6.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("F8")

# 7. BOS #72 Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("c c f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #44 Jake Peavy
b6 = game.new_inning()

# 3. SFG #9  Brandon Belt (X - X - X)
b6.new_ab()
b6.pitch_list("f f")
b6.hit(2)

# 4. SFG #28 Buster Posey (X - 9 - X)
b6.new_ab(is_risp=True)
b6.out("G6-3")

# 5. SFG #8  Hunter Pence (X - 9 - X)
b6.new_ab(is_risp=True)
b6.out("F9")

# Pitching change (BOS): #32 Craig Breslow replaces #44 Jake Peavy, batting 7th
b6.pitching_substitution(32)
b6.defensive_substitution(7, 32, "1")

# Defensive change (BOS): #7 Stephen Drew replaces #44 Jake Peavy (P), playing SS, batting 9th
b6.defensive_substitution(9, 7, "6")

# 6. SFG #35 Brandon Crawford (X - 9 - X)
b6.new_ab(is_risp=True)
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SFG #32 Ryan Vogelsong
t7 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.hit(2)

# 9. BOS #7  Stephen Drew (X - 3 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b b f s b s")
t7.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - 3 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.out("P6")

# 2. BOS #18 Shane Victorino (X - 3 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c b c")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #32 Craig Breslow
b7 = game.new_inning()

# 7. SFG #22 Roger Kieschnick (X - X - X)
b7.new_ab()
b7.pitch_list("f b")
b7.out("P4")

# 8. SFG #13 Joaquin Arias (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F9")

# Offensive change (SFG): Pinch-hitter #6 Brett Pill replaces #32 Ryan Vogelsong, batting 9th
b7.offensive_substitution(9, 6, "PH")

# 9. SFG #6  Brett Pill (X - X - X)
b7.new_ab()
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SFG #46 Santiago Casilla
t8 = game.new_inning()

# Pitching change (SFG): #46 Santiago Casilla replaces #32 Ryan Vogelsong, batting 9th
t8.pitching_substitution(46)
t8.defensive_substitution(9, 46, "1")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("G1-3")

# 4. BOS #37 Mike Carp (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b f s")
t8.out("K")

# 5. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.pitch_list("b s s f f b")
t8.hit(1)

# 6. BOS #29 Daniel Nava (X - X - 16)
t8.new_ab()
t8.pitch_list("f c")
t8.out("L8")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow, batting 4th
b8.pitching_substitution(36)
b8.defensive_substitution(4, 36, "1")

# Defensive change (BOS): #12 Mike Napoli replaces #32 Craig Breslow (P), playing 1B, batting 7th
b8.defensive_substitution(7, 12, "3")

# 1. SFG #7  Grégor Blanco (X - X - X)
b8.new_ab()
b8.pitch_list("b f b")
b8.out("G6-3")

# 2. SFG #19 Marco Scutaro (X - X - X)
b8.new_ab()
b8.pitch_list("c c b f")
b8.hit(1)
b8.advance(3, "9 1B")
b8.advance(4, "28 (F)SF9")

# 3. SFG #9  Brandon Belt (X - X - 19)
b8.new_ab()
b8.pitch_list("b s f f d f f")
b8.hit(1)

# 4. SFG #28 Buster Posey (19 - X - 9)
b8.new_ab(is_risp=True)
b8.pitch_list("c b")
b8.out("(F)SF9", rbis=1)

# 5. SFG #8  Hunter Pence (X - X - 9)
b8.new_ab()
b8.pitch_list("f f b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SFG #54 Sergio Romo
t9 = game.new_inning()

# Pitching change (SFG): #54 Sergio Romo replaces #46 Santiago Casilla, batting 9th
t9.pitching_substitution(54)
t9.defensive_substitution(9, 54, "1")

# 7. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("b c b c")
t9.out("G6-3")

# 8. BOS #3  David Ross (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.out("G1-3")

# 9. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G5-3")


# Bot 9th
# Pitching: BOS #56 Franklin Morales
b9 = game.new_inning()

# Pitching change (BOS): #56 Franklin Morales replaces #36 Junichi Tazawa, batting 4th
b9.pitching_substitution(56)
b9.defensive_substitution(4, 56, "1")

# 6. SFG #35 Brandon Crawford (X - X - X)
b9.new_ab()
b9.pitch_list("c b b s s")
b9.out("K")

# 7. SFG #22 Roger Kieschnick (X - X - X)
b9.new_ab()
b9.pitch_list("b b f")
b9.hit(1)
b9.advance(2, "56 BB")
b9.advance(3, "29 HBP")
b9.advance(4, "19 BB")

# 8. SFG #13 Joaquin Arias (X - X - 22)
b9.new_ab()
b9.out("L8")

# Offensive change (SFG): Pinch-hitter #56 Andres Torres replaces #54 Sergio Romo, batting 9th
b9.offensive_substitution(9, 56, "PH")

# 9. SFG #56 Andres Torres (X - X - 22)
b9.new_ab()
b9.pitch_list("1 c 1 b s b b b")
b9.reach("BB")
b9.advance(2, "29 HBP")
b9.advance(3, "19 BB")

# Offensive change (SFG): Pinch-hitter #29 Héctor Sánchez replaces #7 Grégor Blanco, batting 1st
b9.offensive_substitution(1, 29, "PH")

# 1. SFG #29 Héctor Sánchez (X - 22 - 56)
b9.new_ab(is_risp=True)
b9.pitch_list("c f b b")
b9.reach("HBP")
b9.advance(2, "19 BB")

# Pitching change (BOS): #60 Brayan Villarreal replaces #56 Franklin Morales, batting 4th
b9.pitching_substitution(60)
b9.defensive_substitution(4, 60, "1")

# 2. SFG #19 Marco Scutaro (22 - 56 - 29)
b9.new_ab(is_risp=True)
b9.pitch_list("b b b b")
b9.reach("BB", rbis=1)

# Winning team: SFG
# WP: SFG #54 Sergio Romo
game.winning_pitcher(54)

# Loser team: BOS
# LP: BOS #56 Franklin Morales
game.losing_pitcher(56, is_away_team=True)

# print(game)
game.generate_scorecard()
