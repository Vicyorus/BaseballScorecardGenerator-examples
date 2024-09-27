import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ SF, 2013-08-19
# https://www.baseball-reference.com/boxes/SFN/SFN201308190.shtml
# https://www.mlb.com/gameday/red-sox-vs-giants/2013/08/19/348600/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-19 22:16-01:15 +1",
        "at": "AT&T Park, San Francisco, CA",
        "att": "41,585",
        "temp": "64F, Partly Cloudy",
        "wind": "18mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                39: "Jarrod Saltalamacchia",
                29: "Daniel Nava",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                31: "Jon Lester",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                72: "Xander Bogaerts",
                12: "Mike Napoli",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                60: "Brayan Villarreal",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 32, 66, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "3"],
                [39, "2"],
                [29, "7"],
                [7, "6"],
                [16, "5"],
                [31, "1"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [3, "C"],
                [72, "2B"],
                [12, "1B"],
            ],
            "bullpen": [41, 67, 56, 60, 32, 66, 44, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "San Francisco Giants",
            "starter": 55,
            "roster": {
                # Lineup
                56: "Andres Torres",
                19: "Marco Scutaro",
                9: "Brandon Belt",
                28: "Buster Posey",
                8: "Hunter Pence",
                48: "Pablo Sandoval",
                23: "Jeff Francoeur",
                35: "Brandon Crawford",
                55: "Tim Lincecum",
                # Starting pitcher
                55: "Tim Lincecum",
                # Bench
                29: "Héctor Sánchez",
                6: "Brett Pill",
                22: "Roger Kieschnick",
                13: "Joaquin Arias",
                7: "Grégor Blanco",
                # Bullpen
                40: "Madison Bumgarner",
                32: "Ryan Vogelsong",
                75: "Barry Zito",
                50: "Jose Mijares",
                49: "Javier López",
                43: "Sandy Rosario",
                34: "Guillermo Moscoso",
                18: "Matt Cain",
                46: "Santiago Casilla",
                54: "Sergio Romo",
            },
            "lefties": [40, 75, 50, 49],
            "lineup": [
                [56, "8"],
                [19, "4"],
                [9, "3"],
                [28, "2"],
                [8, "9"],
                [48, "5"],
                [23, "7"],
                [35, "6"],
                [55, "1"],
            ],
            "bench": [
                [29, "C"],
                [6, "1B"],
                [22, "LF"],
                [13, "3B"],
                [7, "CF"],
            ],
            "bullpen": [40, 32, 75, 50, 49, 43, 34, 18, 46, 54],
        },
        "umpires": {
            "HP": "Tim Welke",
            "1B": "Mike Everitt",
            "2B": "Dan Bellino",
            "3B": "Bruce Dreckman",
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
# Pitching: SFG #55 Tim Lincecum
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b b f c")
t1.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(2)

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
t1.new_ab()
t1.pitch_list("c t c")
t1.out("!K")

# 4. BOS #34 David Ortiz (X - 18 - X)
t1.new_ab()
t1.pitch_list("b b f")
t1.out("G3")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. SFG #56 Andres Torres (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("F9")

# 2. SFG #19 Marco Scutaro (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("F9")

# 3. SFG #9  Brandon Belt (X - X - X)
b1.new_ab()
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: SFG #55 Tim Lincecum
t2 = game.new_inning()

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.advance(2, "29 BB")
t2.advance(3, "7 1B")
t2.advance(4, "16 SF9")

# 6. BOS #29 Daniel Nava (X - X - 39)
t2.new_ab()
t2.pitch_list("b b b c b")
t2.reach("BB")
t2.advance(2, "7 1B")
t2.advance(3, "16 SF9")
t2.advance(4, "31 BLK")

# 7. BOS #7  Stephen Drew (X - 39 - 29)
t2.new_ab()
t2.pitch_list("c s b")
t2.hit(1)
t2.advance(2, "31 BLK")
t2.advance(3, "31 SAC1-4")
t2.advance(4, "18 1B")

# 8. BOS #16 Will Middlebrooks (39 - 29 - 7)
t2.new_ab()
t2.pitch_list("c")
t2.out("SF9", rbis=1)

# 9. BOS #31 Jon Lester (29 - X - 7)
t2.new_ab()
t2.pitch_list("n b")
t2.balk()
t2.out("SAC1-4")

# 1. BOS #2  Jacoby Ellsbury (7 - X - X)
t2.new_ab()
t2.pitch_list("f d c f b f b f f n")
t2.error(2)
t2.reach("CI")
t2.advance(3, "18 1B")

# 2. BOS #18 Shane Victorino (7 - X - 2)
t2.new_ab()
t2.pitch_list("c 1 b f 1")
t2.hit(1, rbis=1)

# 3. BOS #15 Dustin Pedroia (2 - X - 18)
t2.new_ab()
t2.pitch_list("f f f")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 4. SFG #28 Buster Posey (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b f")
b2.out("F7")

# 5. SFG #8  Hunter Pence (X - X - X)
b2.new_ab()
b2.pitch_list("b s b b f")
b2.out("G4-3")

# 6. SFG #48 Pablo Sandoval (X - X - X)
b2.new_ab()
b2.pitch_list("b f b c f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: SFG #55 Tim Lincecum
t3 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t3.new_ab()
t3.pitch_list("b b b")
t3.out("G4-3")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("b b s b f b")
t3.reach("BB")
t3.advance(2, "29 1B")
t3.advance(3, "7 G4-3")

# 6. BOS #29 Daniel Nava (X - X - 39)
t3.new_ab()
t3.pitch_list("c c")
t3.hit(1)
t3.advance(2, "7 G4-3")

# 7. BOS #7  Stephen Drew (X - 39 - 29)
t3.new_ab()
t3.pitch_list("c f")
t3.out("G4-3")

# 8. BOS #16 Will Middlebrooks (39 - 29 - X)
t3.new_ab()
t3.pitch_list("i i i i")
t3.reach("IBB")

# 9. BOS #31 Jon Lester (39 - 29 - 16)
t3.new_ab()
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 7. SFG #23 Jeff Francoeur (X - X - X)
b3.new_ab()
b3.pitch_list("c t s")
b3.out("K")

# 8. SFG #35 Brandon Crawford (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("F7")

# 9. SFG #55 Tim Lincecum (X - X - X)
b3.new_ab()
b3.pitch_list("c b b c f f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: SFG #55 Tim Lincecum
t4 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t4.new_ab()
t4.pitch_list("c f f")
t4.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.hit(1)
t4.thrown_out(2, "15 DP6-4-3", 2, 55)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t4.new_ab()
t4.pitch_list("b b")
t4.out("DP6-4-3")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 1. SFG #56 Andres Torres (X - X - X)
b4.new_ab()
b4.hit(1)
b4.thrown_out(2, "9 FC4-6", 2, 31)

# 2. SFG #19 Marco Scutaro (X - X - 56)
b4.new_ab()
b4.pitch_list("b c b f")
b4.out("F8")

# 3. SFG #9  Brandon Belt (X - X - 56)
b4.new_ab()
b4.pitch_list("c s")
b4.reach("FC4-6")

# 4. SFG #28 Buster Posey (X - X - 9)
b4.new_ab()
b4.pitch_list("f b s b f")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: SFG #55 Tim Lincecum
t5 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.out("G3")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("b s f c")
t5.out("!K")

# 6. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("c b b")
t5.hit(1)
t5.advance(4, "7 2B")

# 7. BOS #7  Stephen Drew (X - X - 29)
t5.new_ab()
t5.pitch_list("1 b b f s d")
t5.hit(2, rbis=1)

# 8. BOS #16 Will Middlebrooks (X - 7 - X)
t5.new_ab()
t5.pitch_list("i i i i")
t5.reach("IBB")

# 9. BOS #31 Jon Lester (X - 7 - 16)
t5.new_ab()
t5.pitch_list("b c f c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 5. SFG #8  Hunter Pence (X - X - X)
b5.new_ab()
b5.pitch_list("f s b b")
b5.error(6)
b5.reach("E6")
b5.thrown_out(2, "48 DP4-6-3", 1, 31)

# 6. SFG #48 Pablo Sandoval (X - X - 8)
b5.new_ab()
b5.pitch_list("b")
b5.out("DP4-6-3")

# 7. SFG #23 Jeff Francoeur (X - X - X)
b5.new_ab()
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: SFG #55 Tim Lincecum
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("b f c")
t6.hit(1)
t6.advance(2, "18 HBP")
t6.advance(3, "15 DP4-6-3")
t6.advance(4, "34 WP")

# Pitching change (SFG): #34 Guillermo Moscoso replaces #55 Tim Lincecum, batting 7th
t6.pitching_substitution(34)
t6.defensive_substitution(7, 34, "1")

# Defensive change (SFG): #6 Brett Pill replaces #55 Tim Lincecum (P), playing LF, batting 9th
t6.defensive_substitution(9, 6, "7")

# 2. BOS #18 Shane Victorino (X - X - 2)
t6.new_ab()
t6.pitch_list("c d 1")
t6.reach("HBP")
t6.thrown_out(2, "15 DP4-6-3", 1, 34)

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t6.new_ab()
t6.pitch_list("c f")
t6.out("DP4-6-3")

# 4. BOS #34 David Ortiz (2 - X - X)
t6.new_ab()
t6.pitch_list("b b b c t s")
t6.wp()
t6.out("K")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 8. SFG #35 Brandon Crawford (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b c")
b6.out("F8")

# 9. SFG #6  Brett Pill (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")
b6.advance(2, "56 1B")

# 1. SFG #56 Andres Torres (X - X - 6)
b6.new_ab()
b6.hit(1)

# 2. SFG #19 Marco Scutaro (X - 6 - 56)
b6.new_ab()
b6.pitch_list("c b")
b6.out("L9")

# 3. SFG #9  Brandon Belt (X - 6 - 56)
b6.new_ab()
b6.pitch_list("f b f f")
b6.out("L7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: SFG #34 Guillermo Moscoso
t7 = game.new_inning()

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("c c s")
t7.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c c f f")
t7.out("F7")

# 7. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("s f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# 4. SFG #28 Buster Posey (X - X - X)
b7.new_ab()
b7.pitch_list("b s c f f")
b7.hit(1)
b7.thrown_out(2, "48 FC5-4", 2, 31)

# 5. SFG #8  Hunter Pence (X - X - 28)
b7.new_ab()
b7.out("F8")

# 6. SFG #48 Pablo Sandoval (X - X - 28)
b7.new_ab()
b7.pitch_list("f b")
b7.reach("FC5-4")

# 7. SFG #23 Jeff Francoeur (X - X - 48)
b7.new_ab()
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: SFG #34 Guillermo Moscoso
t8 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.pitch_list("b f c")
t8.out("L7")

# 9. BOS #31 Jon Lester (X - X - X)
t8.new_ab()
t8.pitch_list("c c f f f b")
t8.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #31 Jon Lester
b8 = game.new_inning()

# 8. SFG #35 Brandon Crawford (X - X - X)
b8.new_ab()
b8.out("F8")

# 9. SFG #6  Brett Pill (X - X - X)
b8.new_ab()
b8.pitch_list("c b s b b f f b")
b8.reach("BB")
b8.advance(2, "56 1B")

# 1. SFG #56 Andres Torres (X - X - 6)
b8.new_ab()
b8.pitch_list("f")
b8.hit(1)
b8.thrown_out(2, "19 DP6-3", 2, 31)

# 2. SFG #19 Marco Scutaro (X - 6 - 56)
b8.new_ab()
b8.pitch_list("c f b")
b8.out("DP6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: SFG #50 Jose Mijares
t9 = game.new_inning()

# Pitching change (SFG): #50 Jose Mijares replaces #34 Guillermo Moscoso, batting 7th
t9.pitching_substitution(50)
t9.defensive_substitution(7, 50, "1")

# Defensive change (SFG): #13 Joaquin Arias replaces #48 Pablo Sandoval (3B), playing 3B, batting 6th
t9.defensive_substitution(6, 13, "5")

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("b c b f f b")
t9.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("b s b")
t9.hit(3)
t9.advance(4, "39 2B")

# 4. BOS #34 David Ortiz (15 - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")

# 5. BOS #39 Jarrod Saltalamacchia (15 - X - X)
t9.new_ab()
t9.pitch_list("b c b")
t9.hit(2, rbis=1)
t9.advance(4, "29 1B")

# 6. BOS #29 Daniel Nava (X - 39 - X)
t9.new_ab()
t9.pitch_list("c b t")
t9.hit(1, rbis=1)

# 7. BOS #7  Stephen Drew (X - X - 29)
t9.new_ab()
t9.pitch_list("f f")
t9.out("(F)P5")


# Bot 9th
# Pitching: BOS #31 Jon Lester
b9 = game.new_inning()

# Defensive change (BOS): #37 Mike Carp replaces #34 David Ortiz (1B), playing 1B, batting 4th
b9.defensive_substitution(4, 37, "3")

# 3. SFG #9  Brandon Belt (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("F8")

# 4. SFG #28 Buster Posey (X - X - X)
b9.new_ab()
b9.pitch_list("b f b b")
b9.hit(1)
b9.advance(2, "8 1B")

# 5. SFG #8  Hunter Pence (X - X - 28)
b9.new_ab()
b9.hit(1)

# Pitching change (BOS): #67 Brandon Workman replaces #31 Jon Lester, batting 9th
b9.pitching_substitution(67)
b9.defensive_substitution(9, 67, "1")

# 6. SFG #13 Joaquin Arias (X - 28 - 8)
b9.new_ab()
b9.pitch_list("f b b f f s")
b9.out("K")

# Offensive change (SFG): Pinch-hitter #29 Héctor Sánchez replaces #50 Jose Mijares, batting 7th
b9.offensive_substitution(7, 29, "PH")

# 7. SFG #29 Héctor Sánchez (X - 28 - 8)
b9.new_ab()
b9.pitch_list("b c f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31, is_away_team=True)

# Loser team: SFG
# LP: SFG #55 Tim Lincecum
game.losing_pitcher(55)

# print(game)
game.generate_scorecard()
