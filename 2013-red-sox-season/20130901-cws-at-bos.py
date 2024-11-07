import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CWS @ BOS, 2013-09-01
# https://www.baseball-reference.com/boxes/BOS/BOS201309010.shtml
# https://www.mlb.com/gameday/white-sox-vs-red-sox/2013/09/01/348773/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-01 13:54-17:52 (0:19 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "37,053",
        "temp": "74F, Cloudy",
        "wind": "9mph, In From RF",
        "away": {
            "team": "Chicago White Sox",
            "starter": 64,
            "roster": {
                # Lineup
                30: "Alejandro De Aza",
                28: "Leury García",
                10: "Alexei Ramirez",
                14: "Paul Konerko",
                26: "Avisaíl García",
                7: "Jeff Keppinger",
                24: "Dayan Viciedo",
                12: "Conor Gillaspie",
                21: "Tyler Flowers",
                # Starting pitcher
                64: "André Rienzo",
                # Bench
                20: "Jordan Danks",
                15: "Gordon Beckham",
                39: "Bryan Anderson",
                44: "Adam Dunn",
                36: "Josh Phegley",
                # Bullpen
                27: "Matt Lindstrom",
                65: "Nate Jones",
                43: "Addison Reed",
                49: "Chris Sale",
                62: "Jose Quintana",
                52: "Jake Petricka",
                50: "John Danks",
                61: "Charlie Leesman",
                46: "Donnie Veal",
                33: "Dylan Axelrod",
                53: "Héctor Santiago",
                41: "David Purcey",
            },
            "lefties": [49, 62, 50, 61, 46, 53, 41],
            "lineup": [
                [30, "8"],
                [28, "4"],
                [10, "6"],
                [14, "0"],
                [26, "9"],
                [7, "3"],
                [24, "7"],
                [12, "5"],
                [21, "2"],
            ],
            "bench": [
                [20, "CF"],
                [15, "2B"],
                [39, "C"],
                [44, "LF"],
                [36, "C"],
            ],
            "bullpen": [27, 65, 43, 49, 62, 52, 50, 61, 46, 33, 53, 41],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                72: "Xander Bogaerts",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                50: "Quintin Berry",
                16: "Will Middlebrooks",
                5: "Jonny Gomes",
                3: "David Ross",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                23: "Brandon Snyder",
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
                62: "Rubby De La Rosa",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 32, 66, 31, 38],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "7"],
                [37, "3"],
                [39, "2"],
                [7, "6"],
                [72, "5"],
            ],
            "bench": [
                [50, "LF"],
                [16, "3B"],
                [5, "LF"],
                [3, "C"],
                [12, "1B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 11, 19, 38, 62, 46],
        },
        "umpires": {
            "HP": "Angel Hernandez",
            "1B": "Doug Eddings",
            "2B": "Dana DeMuth",
            "3B": "Paul Nauert",
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
# Pitching: BOS #22 Felix Doubront
t1 = game.new_inning()

# 1. CWS #30 Alejandro De Aza (X - X - X)
t1.new_ab()
t1.pitch_list("c b f f c")
t1.out("!K")

# 2. CWS #28 Leury García (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.advance(2, "14 SB")

# 3. CWS #10 Alexei Ramirez (X - X - 28)
t1.new_ab()
t1.pitch_list("1 b f b f b")
t1.out("F9")

# 4. CWS #14 Paul Konerko (X - X - 28)
t1.new_ab(is_risp=True)
t1.pitch_list("1 1 c s b b s")
t1.out("K")


# Bot 1st
# Pitching: CWS #64 André Rienzo
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c f c")
b1.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b b c")
b1.hit(1)
b1.advance(2, "34 BB")

# 4. BOS #34 David Ortiz (X - X - 15)
b1.new_ab()
b1.pitch_list("b b f 1 c f f d b")
b1.reach("BB")

# 5. BOS #29 Daniel Nava (X - 15 - 34)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 5. CWS #26 Avisaíl García (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.hit(1)
t2.thrown_out(2, "24 POCS", 2, 22)

# 6. CWS #7  Jeff Keppinger (X - X - 26)
t2.new_ab()
t2.pitch_list("c c")
t2.out("F8")

# 7. CWS #24 Dayan Viciedo (X - X - 26)
t2.new_ab()
t2.pitch_list("b 1 b s f f b")
t2.out("G6-3")


# Bot 2nd
# Pitching: CWS #64 André Rienzo
b2 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(1)
b2.advance(2, "39 BB")
b2.advance(3, "7 F9")
b2.advance(4, "2 1B")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
b2.new_ab()
b2.pitch_list("b 1 b f d b")
b2.reach("BB")
b2.advance(2, "72 SB")
b2.advance(4, "2 1B")

# 8. BOS #7  Stephen Drew (X - 37 - 39)
b2.new_ab(is_risp=True)
b2.pitch_list("d b c d")
b2.out("F9")

# 9. BOS #72 Xander Bogaerts (37 - X - 39)
b2.new_ab(is_risp=True)
b2.pitch_list("1 f 1 b c d b s")
b2.out("K")

# 1. BOS #2  Jacoby Ellsbury (37 - 39 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c b s")
b2.hit(1, rbis=2)
b2.advance(2, "T")
b2.advance(3, "15 BB")
b2.advance(4, "34 2B")

# 2. BOS #18 Shane Victorino (X - 2 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b f d b b")
b2.reach("BB")
b2.advance(2, "15 BB")
b2.advance(4, "34 2B")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b2.new_ab(is_risp=True)
b2.pitch_list("b f d f b b")
b2.reach("BB")
b2.advance(3, "34 2B")

# 4. BOS #34 David Ortiz (2 - 18 - 15)
b2.new_ab(is_risp=True)
b2.hit(2, rbis=2)

# 5. BOS #29 Daniel Nava (15 - 34 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b c c b b")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 8. CWS #12 Conor Gillaspie (X - X - X)
t3.new_ab()
t3.pitch_list("b s f b f")
t3.out("L7")

# 9. CWS #21 Tyler Flowers (X - X - X)
t3.new_ab()
t3.pitch_list("f c f b b f f s")
t3.out("K")

# 1. CWS #30 Alejandro De Aza (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b f")
t3.out("F7")


# Bot 3rd
# Pitching: CWS #64 André Rienzo
b3 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
b3.new_ab()
b3.pitch_list("c b s")
b3.out("L6")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("c b f")
b3.out("F9")

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(4)

# 9. BOS #72 Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("c f f f f c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 2. CWS #28 Leury García (X - X - X)
t4.new_ab()
t4.pitch_list("f f s")
t4.out("K")

# 3. CWS #10 Alexei Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("c f f")
t4.hit(1)
t4.advance(2, "14 1B")
t4.advance(3, "26 BB")
t4.advance(4, "7 SF8")

# 4. CWS #14 Paul Konerko (X - X - 10)
t4.new_ab()
t4.pitch_list("c f d d")
t4.hit(1)
t4.advance(2, "26 BB")
t4.advance(4, "24 2B")

# 5. CWS #26 Avisaíl García (X - 10 - 14)
t4.new_ab(is_risp=True)
t4.pitch_list("d t b b f b")
t4.reach("BB")
t4.advance(3, "24 2B")
t4.advance(4, "12 1B")

# 6. CWS #7  Jeff Keppinger (10 - 14 - 26)
t4.new_ab(is_risp=True)
t4.pitch_list("d c b f")
t4.out("SF8", rbis=1)

# 7. CWS #24 Dayan Viciedo (X - 14 - 26)
t4.new_ab(is_risp=True)
t4.pitch_list("f b s d f f")
t4.hit(2, rbis=1)
t4.advance(4, "12 1B")

# 8. CWS #12 Conor Gillaspie (26 - 24 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b t t")
t4.hit(1, rbis=2)
t4.advance(3, "21 1B")

# 9. CWS #21 Tyler Flowers (X - X - 12)
t4.new_ab()
t4.pitch_list("1 b f s b b")
t4.hit(1)
t4.advance(2, "30 BB")

# Pitching change (BOS): #67 Brandon Workman replaces #22 Felix Doubront
t4.pitching_substitution(67)

# 1. CWS #30 Alejandro De Aza (12 - X - 21)
t4.new_ab(is_risp=True)
t4.pitch_list("d b b c f b")
t4.reach("BB")

# 2. CWS #28 Leury García (12 - 21 - 30)
t4.new_ab(is_risp=True)
t4.pitch_list("b c c f s")
t4.out("K")


# Bot 4th
# Pitching: CWS #61 Charlie Leesman
b4 = game.new_inning()

# Pitching change (CWS): #61 Charlie Leesman replaces #64 André Rienzo
b4.pitching_substitution(61)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b4.new_ab()
b4.pitch_list("b b c f b b")
b4.reach("BB")
b4.advance(2, "18 SB")
b4.advance(3, "18 G3-1")
b4.error(5)
b4.advance(4, "15 E5")

# 2. BOS #18 Shane Victorino (X - X - 2)
b4.new_ab(is_risp=True)
b4.pitch_list("c b")
b4.out("G3-1")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b")
b4.hit(1)
b4.advance(2, "E5")
b4.advance("U", "34 1B")

# 4. BOS #34 David Ortiz (X - 15 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b")
b4.hit(1, rbis=1)
b4.thrown_out(2, "29 DP6-4-3", 2, 61)

# 5. BOS #29 Daniel Nava (X - X - 34)
b4.new_ab()
b4.pitch_list("b")
b4.out("DP6-4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #67 Brandon Workman
t5 = game.new_inning()

# 3. CWS #10 Alexei Ramirez (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)
t5.advance(2, "14 SB")
t5.advance(4, "14 1B")

# 4. CWS #14 Paul Konerko (X - X - 10)
t5.new_ab(is_risp=True)
t5.pitch_list("c b b c")
t5.hit(1, rbis=1)

# 5. CWS #26 Avisaíl García (X - X - 14)
t5.new_ab()
t5.pitch_list("c s f b f")
t5.out("F9")

# 6. CWS #7  Jeff Keppinger (X - X - 14)
t5.new_ab()
t5.pitch_list("b b f")
t5.out("F9")

# 7. CWS #24 Dayan Viciedo (X - X - 14)
t5.new_ab()
t5.pitch_list("b f f f")
t5.out("G4-3")


# Bot 5th
# Pitching: CWS #61 Charlie Leesman
b5 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.pitch_list("b c b c")
b5.out("F9")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("b f b")
b5.out("L5")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b f c b f f f b")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #56 Franklin Morales
t6 = game.new_inning()

# Pitching change (BOS): #56 Franklin Morales replaces #67 Brandon Workman
t6.pitching_substitution(56)

# 8. CWS #12 Conor Gillaspie (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G4-3")

# 9. CWS #21 Tyler Flowers (X - X - X)
t6.new_ab()
t6.pitch_list("c b s c")
t6.out("!K")

# 1. CWS #30 Alejandro De Aza (X - X - X)
t6.new_ab()
t6.out("L8")


# Bot 6th
# Pitching: CWS #61 Charlie Leesman
b6 = game.new_inning()

# 9. BOS #72 Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("b s")
b6.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("b b f f")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Franklin Morales
t7 = game.new_inning()

# Defensive change (BOS): #5 Jonny Gomes replaces #18 Shane Victorino (RF), playing LF, batting 2nd
t7.defensive_substitution(2, 5, "7")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
t7.defensive_switch(29, "9")

# 2. CWS #28 Leury García (X - X - X)
t7.new_ab()
t7.pitch_list("c c b b f b f")
t7.out("(F)P3")

# 3. CWS #10 Alexei Ramirez (X - X - X)
t7.new_ab()
t7.hit(1)
t7.advance(2, "14 SB")

# Pitching change (BOS): #36 Junichi Tazawa replaces #56 Franklin Morales
t7.pitching_substitution(36)

# 4. CWS #14 Paul Konerko (X - X - 10)
t7.new_ab(is_risp=True)
t7.pitch_list("b b c b b")
t7.reach("BB")

# 5. CWS #26 Avisaíl García (X - 10 - 14)
t7.new_ab(is_risp=True)
t7.pitch_list("s s b s")
t7.out("K")

# 6. CWS #7  Jeff Keppinger (X - 10 - 14)
t7.new_ab(is_risp=True)
t7.pitch_list("c f d f")
t7.out("P3")


# Bot 7th
# Pitching: CWS #61 Charlie Leesman
b7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.out("L8")

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("f c")
b7.out("G1-3")

# 5. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("b t b f f b f f f f b")
b7.reach("BB")
b7.advance(2, "37 BB")
b7.advance(3, "39 BB")

# 6. BOS #37 Mike Carp (X - X - 29)
b7.new_ab()
b7.pitch_list("b b c f b b")
b7.reach("BB")
b7.advance(2, "39 BB")

# 7. BOS #39 Jarrod Saltalamacchia (X - 29 - 37)
b7.new_ab(is_risp=True)
b7.pitch_list("c d c b b b")
b7.reach("BB")

# 8. BOS #7  Stephen Drew (29 - 37 - 39)
b7.new_ab(is_risp=True)
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
t8.pitching_substitution(32)

# 7. CWS #24 Dayan Viciedo (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("F8")

# 8. CWS #12 Conor Gillaspie (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G4-3")

# 9. CWS #21 Tyler Flowers (X - X - X)
t8.new_ab()
t8.pitch_list("b f")
t8.hit(4)

# 1. CWS #30 Alejandro De Aza (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.out("L8")


# Bot 8th
# Pitching: CWS #61 Charlie Leesman
b8 = game.new_inning()

# 9. BOS #72 Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.advance(2, "5 PB")
b8.advance(3, "5 G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - 72)
b8.new_ab()
b8.pitch_list("b f b 1")
b8.out("F8")

# Pitching change (CWS): #65 Nate Jones replaces #61 Charlie Leesman
b8.pitching_substitution(65)

# 2. BOS #5  Jonny Gomes (X - X - 72)
b8.new_ab(is_risp=True)
b8.pitch_list("1 b b c f")
b8.pb()
b8.out("G4-3")

# 3. BOS #15 Dustin Pedroia (72 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c t b")
b8.out("G1-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
t9.pitching_substitution(19)

# Defensive change (BOS): #50 Quintin Berry replaces #2 Jacoby Ellsbury (CF), playing CF, batting 1st
t9.defensive_substitution(1, 50, "8")

# 2. CWS #28 Leury García (X - X - X)
t9.new_ab()
t9.pitch_list("b s s")
t9.out("(F)P5")

# 3. CWS #10 Alexei Ramirez (X - X - X)
t9.new_ab()
t9.pitch_list("f f f s")
t9.out("K")

# 4. CWS #14 Paul Konerko (X - X - X)
t9.new_ab()
t9.pitch_list("c s b f f f")
t9.out("F8")

# Winning team: BOS
# WP: BOS #67 Brandon Workman
game.winning_pitcher(67)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: CWS
# LP: CWS #64 André Rienzo
game.losing_pitcher(64, is_away_team=True)

# print(game)
game.generate_scorecard()
