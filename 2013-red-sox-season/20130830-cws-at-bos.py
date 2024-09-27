import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CWS @ BOS, 2013-08-30
# https://www.baseball-reference.com/boxes/BOS/BOS201308300.shtml
# https://www.mlb.com/gameday/white-sox-vs-red-sox/2013/08/30/348743/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-30 19:13-22:22",
        "at": "Fenway Park, Boston, MA",
        "att": "36,063",
        "temp": "82F, Partly Cloudy",
        "wind": "11mph, In From RF",
        "away": {
            "team": "Chicago White Sox",
            "starter": 53,
            "roster": {
                # Lineup
                30: "Alejandro De Aza",
                15: "Gordon Beckham",
                10: "Alexei Ramirez",
                44: "Adam Dunn",
                14: "Paul Konerko",
                26: "Avisaíl García",
                7: "Jeff Keppinger",
                24: "Dayan Viciedo",
                36: "Josh Phegley",
                # Starting pitcher
                53: "Héctor Santiago",
                # Bench
                20: "Jordan Danks",
                28: "Leury García",
                21: "Tyler Flowers",
                12: "Conor Gillaspie",
                # Bullpen
                27: "Matt Lindstrom",
                65: "Nate Jones",
                43: "Addison Reed",
                49: "Chris Sale",
                62: "Jose Quintana",
                52: "Jake Petricka",
                50: "John Danks",
                46: "Donnie Veal",
                33: "Dylan Axelrod",
                64: "André Rienzo",
                41: "David Purcey",
            },
            "lefties": [53, 49, 62, 50, 46, 41],
            "lineup": [
                [30, "8"],
                [15, "4"],
                [10, "6"],
                [44, "0"],
                [14, "3"],
                [26, "9"],
                [7, "5"],
                [24, "7"],
                [36, "2"],
            ],
            "bench": [
                [20, "CF"],
                [28, "OF"],
                [21, "C"],
                [12, "3B"],
            ],
            "bullpen": [27, 65, 43, 49, 62, 52, 50, 46, 33, 64, 41],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                5: "Jonny Gomes",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                37: "Mike Carp",
                29: "Daniel Nava",
                3: "David Ross",
                72: "Xander Bogaerts",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                38: "Matt Thornton",
                22: "Felix Doubront",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [5, "7"],
                [12, "3"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
            ],
            "bench": [
                [37, "1B"],
                [29, "LF"],
                [3, "C"],
                [72, "2B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 11, 19, 38, 22],
        },
        "umpires": {
            "HP": "Dana DeMuth",
            "1B": "Paul Nauert",
            "2B": "Angel Hernandez",
            "3B": "Doug Eddings",
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

# 1. CWS #30 Alejandro De Aza (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b b f b")
t1.reach("BB")
t1.advance(2, "15 SB")
t1.advance(3, "10 DP6-4-3")

# 2. CWS #15 Gordon Beckham (X - X - 30)
t1.new_ab()
t1.pitch_list("b f b c b b")
t1.reach("BB")
t1.thrown_out(2, "10 DP6-4-3", 1, 46)

# 3. CWS #10 Alexei Ramirez (X - 30 - 15)
t1.new_ab()
t1.out("DP6-4-3")

# 4. CWS #44 Adam Dunn (30 - X - X)
t1.new_ab()
t1.pitch_list("b s c d d s")
t1.out("K")


# Bot 1st
# Pitching: CWS #53 Héctor Santiago
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b b c b f s")
b1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f f b b")
b1.reach("BB")
b1.advance(2, "15 SB")
b1.thrown_out(3, "34 FC4-5", 2, 53)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b1.new_ab()
b1.pitch_list("b b 1 f 1 b f f f f b")
b1.reach("BB")
b1.advance(2, "34 FC4-5")

# 4. BOS #34 David Ortiz (X - 18 - 15)
b1.new_ab()
b1.pitch_list("c")
b1.reach("FC4-5")

# 5. BOS #5  Jonny Gomes (X - 15 - 34)
b1.new_ab()
b1.pitch_list("b")
b1.out("P6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 5. CWS #14 Paul Konerko (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("L8")

# 6. CWS #26 Avisaíl García (X - X - X)
t2.new_ab()
t2.pitch_list("b b c f f s")
t2.out("K")

# 7. CWS #7  Jeff Keppinger (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b")
t2.out("G6-3")


# Bot 2nd
# Pitching: CWS #53 Héctor Santiago
b2 = game.new_inning()

# 6. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b c c")
b2.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.out("F8")

# 8. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("b f b")
b2.hit(1)
b2.thrown_out(2, "16 FC4-6", 3, 53)

# 9. BOS #16 Will Middlebrooks (X - X - 7)
b2.new_ab()
b2.pitch_list("b c b")
b2.reach("FC4-6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 8. CWS #24 Dayan Viciedo (X - X - X)
t3.new_ab()
t3.pitch_list("c b b f")
t3.out("G5-3")

# 9. CWS #36 Josh Phegley (X - X - X)
t3.new_ab()
t3.pitch_list("b c s s")
t3.out("K")

# 1. CWS #30 Alejandro De Aza (X - X - X)
t3.new_ab()
t3.pitch_list("b b")
t3.out("L4")


# Bot 3rd
# Pitching: CWS #53 Héctor Santiago
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("s c b b f")
b3.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(2, "34 BB")
b3.advance(3, "5 HBP")
b3.advance(4, "12 BB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b3.new_ab()
b3.pitch_list("f b 1 b c")
b3.out("P6")

# 4. BOS #34 David Ortiz (X - X - 18)
b3.new_ab()
b3.pitch_list("b c b b b")
b3.reach("BB")
b3.advance(2, "5 HBP")
b3.advance(3, "12 BB")

# 5. BOS #5  Jonny Gomes (X - 18 - 34)
b3.new_ab()
b3.reach("HBP")
b3.advance(2, "12 BB")

# 6. BOS #12 Mike Napoli (18 - 34 - 5)
b3.new_ab()
b3.pitch_list("d b b c b")
b3.reach("BB", rbis=1)

# 7. BOS #39 Jarrod Saltalamacchia (34 - 5 - 12)
b3.new_ab()
b3.pitch_list("b b s b t")
b3.out("P5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 2. CWS #15 Gordon Beckham (X - X - X)
t4.new_ab()
t4.pitch_list("b b f c b")
t4.out("L6")

# 3. CWS #10 Alexei Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("c f")
t4.out("G4-3")

# 4. CWS #44 Adam Dunn (X - X - X)
t4.new_ab()
t4.pitch_list("c f s")
t4.out("K")


# Bot 4th
# Pitching: CWS #53 Héctor Santiago
b4 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("c c b b s")
b4.out("K")

# 9. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("b b b b")
b4.reach("BB")
b4.advance(2, "2 SB")
b4.advance(3, "2 G6-3")
b4.advance(4, "18 1B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b4.new_ab()
b4.pitch_list("c b 1 b")
b4.out("G6-3")

# 2. BOS #18 Shane Victorino (16 - X - X)
b4.new_ab()
b4.pitch_list("c f b")
b4.hit(1, rbis=1)
b4.advance(3, "15 2B")
b4.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b4.new_ab()
b4.pitch_list("1 c")
b4.hit(2)
b4.advance(4, "34 1B")

# 4. BOS #34 David Ortiz (18 - 15 - X)
b4.new_ab()
b4.pitch_list("c b b s f b")
b4.hit(1, rbis=2)
b4.thrown_out(2, "5 FC5-4", 3, 52)

# Pitching change (CWS): #52 Jake Petricka replaces #53 Héctor Santiago
b4.pitching_substitution(52)

# 5. BOS #5  Jonny Gomes (X - X - 34)
b4.new_ab()
b4.pitch_list("b b c s f")
b4.reach("FC5-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 5. CWS #14 Paul Konerko (X - X - X)
t5.new_ab()
t5.hit(2)
t5.advance(3, "26 1B")
t5.thrown_out(4, "7 FC5-2", 1, 46)

# 6. CWS #26 Avisaíl García (X - 14 - X)
t5.new_ab()
t5.pitch_list("f")
t5.hit(1)
t5.advance(2, "7 FC5-2")
t5.advance(4, "24 1B")

# 7. CWS #7  Jeff Keppinger (14 - X - 26)
t5.new_ab()
t5.pitch_list("b c")
t5.reach("FC5-2")
t5.advance(2, "24 1B")
t5.advance(3, "36 F8")

# 8. CWS #24 Dayan Viciedo (X - 26 - 7)
t5.new_ab()
t5.pitch_list("d c s b")
t5.hit(1, rbis=1)

# 9. CWS #36 Josh Phegley (X - 7 - 24)
t5.new_ab()
t5.pitch_list("b")
t5.out("F8")

# 1. CWS #30 Alejandro De Aza (7 - X - 24)
t5.new_ab()
t5.pitch_list("c")
t5.out("G6-3")


# Bot 5th
# Pitching: CWS #52 Jake Petricka
b5 = game.new_inning()

# 6. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.out("G4-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("c s b f s")
b5.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("s f")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 2. CWS #15 Gordon Beckham (X - X - X)
t6.new_ab()
t6.pitch_list("f s c")
t6.out("!K")

# 3. CWS #10 Alexei Ramirez (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("L6")

# 4. CWS #44 Adam Dunn (X - X - X)
t6.new_ab()
t6.pitch_list("b f b b b")
t6.reach("BB")

# 5. CWS #14 Paul Konerko (X - X - 44)
t6.new_ab()
t6.pitch_list("b s")
t6.out("P4")


# Bot 6th
# Pitching: CWS #41 David Purcey
b6 = game.new_inning()

# Pitching change (CWS): #41 David Purcey replaces #52 Jake Petricka
b6.pitching_substitution(41)

# 9. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("b c s b")
b6.hit(1)
b6.advance(2, "2 WP")
b6.advance(3, "34 BB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b6.new_ab()
b6.pitch_list("l 1 s b s")
b6.wp()
b6.out("K")

# 2. BOS #18 Shane Victorino (X - 16 - X)
b6.new_ab()
b6.pitch_list("c f")
b6.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - 16 - X)
b6.new_ab()
b6.pitch_list("i i i i")
b6.reach("IBB")
b6.advance(2, "34 BB")

# 4. BOS #34 David Ortiz (X - 16 - 15)
b6.new_ab()
b6.pitch_list("b f d f b b")
b6.reach("BB")

# 5. BOS #5  Jonny Gomes (16 - 15 - 34)
b6.new_ab()
b6.pitch_list("b c b f b f f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #46 Ryan Dempster
t7 = game.new_inning()

# 6. CWS #26 Avisaíl García (X - X - X)
t7.new_ab()
t7.pitch_list("f b")
t7.hit(4)

# 7. CWS #7  Jeff Keppinger (X - X - X)
t7.new_ab()
t7.pitch_list("f b b b f")
t7.out("G6-3")

# 8. CWS #24 Dayan Viciedo (X - X - X)
t7.new_ab()
t7.pitch_list("f b t")
t7.hit(1)
t7.advance(4, "30 3B")

# Pitching change (BOS): #36 Junichi Tazawa replaces #46 Ryan Dempster
t7.pitching_substitution(36)

# 9. CWS #36 Josh Phegley (X - X - 24)
t7.new_ab()
t7.out("L7")

# 1. CWS #30 Alejandro De Aza (X - X - 24)
t7.new_ab()
t7.hit(3, rbis=1)

# 2. CWS #15 Gordon Beckham (30 - X - X)
t7.new_ab()
t7.pitch_list("d s b")
t7.out("F8")


# Bot 7th
# Pitching: CWS #41 David Purcey
b7 = game.new_inning()

# 6. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c")
b7.out("F8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.out("L5")

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("f b s b f")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# 3. CWS #10 Alexei Ramirez (X - X - X)
t8.new_ab()
t8.pitch_list("b f")
t8.out("G1-3")

# Pitching change (BOS): #56 Franklin Morales replaces #36 Junichi Tazawa
t8.pitching_substitution(56)

# 4. CWS #44 Adam Dunn (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G3-1")

# Pitching change (BOS): #19 Koji Uehara replaces #56 Franklin Morales
t8.pitching_substitution(19)

# 5. CWS #14 Paul Konerko (X - X - X)
t8.new_ab()
t8.pitch_list("c s")
t8.out("F7")


# Bot 8th
# Pitching: CWS #27 Matt Lindstrom
b8 = game.new_inning()

# Pitching change (CWS): #27 Matt Lindstrom replaces #41 David Purcey
b8.pitching_substitution(27)

# 9. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.out("G1-6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("b s c b")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# 6. CWS #26 Avisaíl García (X - X - X)
t9.new_ab()
t9.pitch_list("c b f s")
t9.out("K")

# 7. CWS #7  Jeff Keppinger (X - X - X)
t9.new_ab()
t9.pitch_list("b c f f f s")
t9.out("K")

# 8. CWS #24 Dayan Viciedo (X - X - X)
t9.new_ab()
t9.pitch_list("c b s")
t9.out("G6-3")

# Winning team: BOS
# WP: BOS #46 Ryan Dempster
game.winning_pitcher(46)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: CWS
# LP: CWS #53 Héctor Santiago
game.losing_pitcher(53, is_away_team=True)

# print(game)
game.generate_scorecard()
