import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CWS @ BOS, 2013-08-31
# https://www.baseball-reference.com/boxes/BOS/BOS201308310.shtml
# https://www.mlb.com/gameday/white-sox-vs-red-sox/2013/08/31/348759/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-31 19:11-22:22",
        "at": "Fenway Park, Boston, MA",
        "att": "37,363",
        "temp": "82F, Partly Cloudy",
        "wind": "14mph, In From RF",
        "away": {
            "team": "Chicago White Sox",
            "starter": 50,
            "roster": {
                # Lineup
                30: "Alejandro De Aza",
                15: "Gordon Beckham",
                10: "Alexei Ramirez",
                44: "Adam Dunn",
                14: "Paul Konerko",
                26: "Avisaíl García",
                12: "Conor Gillaspie",
                20: "Jordan Danks",
                36: "Josh Phegley",
                # Starting pitcher
                50: "John Danks",
                # Bench
                28: "Leury García",
                7: "Jeff Keppinger",
                24: "Dayan Viciedo",
                21: "Tyler Flowers",
                # Bullpen
                27: "Matt Lindstrom",
                65: "Nate Jones",
                43: "Addison Reed",
                49: "Chris Sale",
                62: "Jose Quintana",
                52: "Jake Petricka",
                46: "Donnie Veal",
                33: "Dylan Axelrod",
                64: "André Rienzo",
                53: "Héctor Santiago",
                41: "David Purcey",
            },
            "lefties": [50, 49, 62, 46, 53, 41],
            "lineup": [
                [30, "7"],
                [15, "4"],
                [10, "6"],
                [44, "0"],
                [14, "3"],
                [26, "8"],
                [12, "5"],
                [20, "9"],
                [36, "2"],
            ],
            "bench": [
                [28, "OF"],
                [7, "2B"],
                [24, "LF"],
                [21, "C"],
            ],
            "bullpen": [27, 65, 43, 49, 62, 52, 46, 33, 64, 53, 41],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 44,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                16: "Will Middlebrooks",
                3: "David Ross",
                72: "Xander Bogaerts",
                # Starting pitcher
                44: "Jake Peavy",
                # Bench
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                38: "Matt Thornton",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [16, "5"],
                [3, "2"],
                [72, "6"],
            ],
            "bench": [
                [7, "SS"],
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 31, 36, 11, 19, 38, 22, 46],
        },
        "umpires": {
            "HP": "Paul Nauert",
            "1B": "Angel Hernandez",
            "2B": "Doug Eddings",
            "3B": "Dana DeMuth",
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
# Pitching: BOS #44 Jake Peavy
t1 = game.new_inning()

# 1. CWS #30 Alejandro De Aza (X - X - X)
t1.new_ab()
t1.pitch_list("b b f f b f")
t1.out("F7")

# 2. CWS #15 Gordon Beckham (X - X - X)
t1.new_ab()
t1.pitch_list("b f b f f")
t1.out("P4")

# 3. CWS #10 Alexei Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.out("F8")


# Bot 1st
# Pitching: CWS #50 John Danks
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.hit(1)
b1.advance(3, "34 E3")
b1.advance("U", "12 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab()
b1.pitch_list("c b 1 1 f d 1 f")
b1.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b1.new_ab()
b1.pitch_list("c 1 f")
b1.out("L4")

# 4. BOS #34 David Ortiz (X - X - 2)
b1.new_ab()
b1.pitch_list("1 b c")
b1.error(3)
b1.reach("E3")
b1.advance(2, "12 1B")

# 5. BOS #12 Mike Napoli (2 - X - 34)
b1.new_ab(is_risp=True)
b1.pitch_list("c b b")
b1.hit(1, rbis=1)

# 6. BOS #5  Jonny Gomes (X - 34 - 12)
b1.new_ab(is_risp=True)
b1.pitch_list("s s b")
b1.out("P6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #44 Jake Peavy
t2 = game.new_inning()

# 4. CWS #44 Adam Dunn (X - X - X)
t2.new_ab()
t2.pitch_list("s")
t2.out("F7")

# 5. CWS #14 Paul Konerko (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.out("G1-3")

# 6. CWS #26 Avisaíl García (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G4-3")


# Bot 2nd
# Pitching: CWS #50 John Danks
b2 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.out("F8")

# 8. BOS #3  David Ross (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c c f")
b2.hit(2)
b2.advance(3, "2 G4-3")

# 9. BOS #72 Xander Bogaerts (X - 3 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c f f b b f b f b")
b2.reach("BB")
b2.advance(2, "2 G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - 3 - 72)
b2.new_ab(is_risp=True)
b2.pitch_list("c")
b2.out("G4-3")

# 2. BOS #18 Shane Victorino (3 - 72 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c f f c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #44 Jake Peavy
t3 = game.new_inning()

# 7. CWS #12 Conor Gillaspie (X - X - X)
t3.new_ab()
t3.pitch_list("c b b f")
t3.hit(1)
t3.advance(3, "36 1B")
t3.advance(4, "30 FC4-6")

# 8. CWS #20 Jordan Danks (X - X - 12)
t3.new_ab()
t3.pitch_list("b s s t")
t3.out("KT")

# 9. CWS #36 Josh Phegley (X - X - 12)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)
t3.thrown_out(2, "30 FC4-6", 2, 44)

# 1. CWS #30 Alejandro De Aza (12 - X - 36)
t3.new_ab(is_risp=True)
t3.pitch_list("b")
t3.reach("FC4-6", rbis=1)
t3.advance(2, "15 SB")

# 2. CWS #15 Gordon Beckham (X - X - 30)
t3.new_ab(is_risp=True)
t3.pitch_list("b c d b")
t3.out("F7")


# Bot 3rd
# Pitching: CWS #50 John Danks
b3 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("c s b")
b3.out("P3")

# 4. BOS #34 David Ortiz (X - X - X)
b3.new_ab()
b3.out("G4-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b3.new_ab()
b3.pitch_list("b b c b")
b3.hit(2)
b3.advance(4, "5 2B")

# 6. BOS #5  Jonny Gomes (X - 12 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b c b b c")
b3.hit(2, rbis=1)

# 7. BOS #16 Will Middlebrooks (X - 5 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c f b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #44 Jake Peavy
t4 = game.new_inning()

# 3. CWS #10 Alexei Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.hit(1)
t4.advance(2, "44 SB")
t4.advance(4, "26 1B")

# 4. CWS #44 Adam Dunn (X - X - 10)
t4.new_ab()
t4.pitch_list("c f b f f s")
t4.out("K")

# 5. CWS #14 Paul Konerko (X - 10 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c s b c")
t4.out("!K")

# 6. CWS #26 Avisaíl García (X - 10 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b f")
t4.hit(1, rbis=1)
t4.advance(2, "12 SB")

# 7. CWS #12 Conor Gillaspie (X - X - 26)
t4.new_ab(is_risp=True)
t4.pitch_list("f 1 b 1 b b c f b")
t4.reach("BB")

# 8. CWS #20 Jordan Danks (X - 26 - 12)
t4.new_ab(is_risp=True)
t4.pitch_list("b b s s")
t4.out("G3")


# Bot 4th
# Pitching: CWS #50 John Danks
b4 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(2, "72 1B")
b4.advance(4, "2 2B")

# 9. BOS #72 Xander Bogaerts (X - X - 3)
b4.new_ab()
b4.pitch_list("1 b c")
b4.hit(1)
b4.advance(3, "2 2B")
b4.advance(4, "15 G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - 3 - 72)
b4.new_ab(is_risp=True)
b4.hit(2, rbis=1)
b4.advance(3, "15 G4-3")
b4.advance(4, "34 1B")

# 2. BOS #18 Shane Victorino (72 - 2 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c c b f f")
b4.out("G5-3")

# 3. BOS #15 Dustin Pedroia (72 - 2 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("3 c")
b4.out("G4-3", rbis=1)

# 4. BOS #34 David Ortiz (2 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c t")
b4.hit(1, rbis=1)

# 5. BOS #12 Mike Napoli (X - X - 34)
b4.new_ab()
b4.pitch_list("s b")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #44 Jake Peavy
t5 = game.new_inning()

# 9. CWS #36 Josh Phegley (X - X - X)
t5.new_ab()
t5.pitch_list("b c f s")
t5.out("K")

# 1. CWS #30 Alejandro De Aza (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c f")
t5.out("G4-1")

# 2. CWS #15 Gordon Beckham (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("F9")


# Bot 5th
# Pitching: CWS #50 John Danks
b5 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b5.new_ab()
b5.pitch_list("b b c")
b5.hit(1)
b5.advance(2, "16 G5-3")
b5.advance(4, "72 1B")

# 7. BOS #16 Will Middlebrooks (X - X - 5)
b5.new_ab()
b5.pitch_list("f f 1")
b5.out("G5-3")

# 8. BOS #3  David Ross (X - 5 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("f b b s d")
b5.out("L5")

# 9. BOS #72 Xander Bogaerts (X - 5 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b f b")
b5.hit(1, rbis=1)
b5.advance(2, "T")

# 1. BOS #2  Jacoby Ellsbury (X - 72 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("f d f")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #44 Jake Peavy
t6 = game.new_inning()

# 3. CWS #10 Alexei Ramirez (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f f b")
t6.out("P4")

# 4. CWS #44 Adam Dunn (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b b")
t6.out("G5-3")

# 5. CWS #14 Paul Konerko (X - X - X)
t6.new_ab()
t6.pitch_list("s f b")
t6.out("F9")


# Bot 6th
# Pitching: CWS #52 Jake Petricka
b6 = game.new_inning()

# Pitching change (CWS): #52 Jake Petricka replaces #50 John Danks
b6.pitching_substitution(52)

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.hit(1)
b6.advance(3, "34 1B")
b6.advance(4, "5 WP")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b6.new_ab()
b6.pitch_list("b c c f s")
b6.out("K")

# 4. BOS #34 David Ortiz (X - X - 18)
b6.new_ab()
b6.pitch_list("f d 1 b d f")
b6.hit(1)
b6.advance(2, "12 BB")
b6.advance(3, "5 WP")

# 5. BOS #12 Mike Napoli (18 - X - 34)
b6.new_ab(is_risp=True)
b6.pitch_list("c b b b b")
b6.reach("BB")
b6.advance(2, "5 WP")

# 6. BOS #5  Jonny Gomes (18 - 34 - 12)
b6.new_ab(is_risp=True)
b6.pitch_list("b b c c")
b6.wp()
b6.out("G1-3")

# 7. BOS #16 Will Middlebrooks (34 - 12 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b s")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #44 Jake Peavy
t7 = game.new_inning()

# 6. CWS #26 Avisaíl García (X - X - X)
t7.new_ab()
t7.pitch_list("b s")
t7.out("F9")

# 7. CWS #12 Conor Gillaspie (X - X - X)
t7.new_ab()
t7.out("F8")

# 8. CWS #20 Jordan Danks (X - X - X)
t7.new_ab()
t7.pitch_list("b f b")
t7.hit(1)

# 9. CWS #36 Josh Phegley (X - X - 20)
t7.new_ab()
t7.pitch_list("c")
t7.out("F8")


# Bot 7th
# Pitching: CWS #52 Jake Petricka
b7 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b b")
b7.reach("BB")
b7.thrown_out(2, "72 DP4-6-3", 1, 52)

# 9. BOS #72 Xander Bogaerts (X - X - 3)
b7.new_ab()
b7.pitch_list("c")
b7.out("DP4-6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b f b s f")
b7.hit(1)
b7.advance(2, "18 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b7.new_ab()
b7.pitch_list("f")
b7.hit(1)

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b7.new_ab(is_risp=True)
b7.pitch_list("f f")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #44 Jake Peavy
t8.pitching_substitution(32)

# 1. CWS #30 Alejandro De Aza (X - X - X)
t8.new_ab()
t8.pitch_list("b b f")
t8.out("G4-3")

# 2. CWS #15 Gordon Beckham (X - X - X)
t8.new_ab()
t8.pitch_list("b f b f")
t8.out("P6")

# 3. CWS #10 Alexei Ramirez (X - X - X)
t8.new_ab()
t8.pitch_list("b s f b s")
t8.out("K")


# Bot 8th
# Pitching: CWS #41 David Purcey
b8 = game.new_inning()

# Pitching change (CWS): #41 David Purcey replaces #52 Jake Petricka
b8.pitching_substitution(41)

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("c b b b f f b")
b8.reach("BB")
b8.thrown_out(2, "12 DP5-4-3", 1, 41)

# 5. BOS #12 Mike Napoli (X - X - 34)
b8.new_ab()
b8.pitch_list("b f")
b8.out("DP5-4-3")

# 6. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("f b s")
b8.out("P4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #66 Drake Britton
t9 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #32 Craig Breslow
t9.pitching_substitution(66)

# 4. CWS #44 Adam Dunn (X - X - X)
t9.new_ab()
t9.pitch_list("b f b f b b")
t9.reach("BB")

# 5. CWS #14 Paul Konerko (X - X - 44)
t9.new_ab()
t9.out("(F)P3")

# 6. CWS #26 Avisaíl García (X - X - 44)
t9.new_ab()
t9.pitch_list("f f f b t")
t9.out("KT")

# 7. CWS #12 Conor Gillaspie (X - X - 44)
t9.new_ab()
t9.out("F8")

# Winning team: BOS
# WP: BOS #44 Jake Peavy
game.winning_pitcher(44)

# Loser team: CWS
# LP: CWS #50 John Danks
game.losing_pitcher(50, is_away_team=True)

# print(game)
game.generate_scorecard()
