import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TB @ BOS, 2013-07-23
# https://www.baseball-reference.com/boxes/BOS/BOS201307230.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2013/07/23/348240/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-23 19:12-22:18",
        "at": "Fenway Park, Boston, MA",
        "att": "34,609",
        "temp": "72F, Cloudy",
        "wind": "6mph, In From LF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 40,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                9: "Wil Myers",
                20: "Matt Joyce",
                11: "Yunel Escobar",
                21: "James Loney",
                28: "José Molina",
                1: "Sean Rodríguez",
                # Starting pitcher
                40: "Roberto Hernandez",
                # Bench
                30: "Luke Scott",
                59: "Jose Lobaton",
                5: "Sam Fuld",
                2: "Kelly Johnson",
                # Bullpen
                58: "Jeremy Hellickson",
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                14: "David Price",
                56: "Fernando Rodney",
                22: "Chris Archer",
            },
            "lefties": [55, 57, 54, 27, 14],
            "lineup": [
                [8, "8"],
                [18, "4"],
                [3, "5"],
                [9, "9"],
                [20, "0"],
                [11, "6"],
                [21, "3"],
                [28, "2"],
                [1, "7"],
            ],
            "bench": [
                [30, "DH"],
                [59, "C"],
                [5, "LF"],
                [2, "2B"],
            ],
            "bullpen": [58, 55, 62, 35, 43, 57, 54, 27, 14, 56, 22],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                18: "Shane Victorino",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                65: "Jose De La Torre",
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                66: "Drake Britton",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 32, 66, 38, 22],
            "lineup": [
                [18, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [39, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [2, "CF"],
                [5, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [65, 41, 67, 32, 66, 36, 19, 38, 54, 22, 46],
        },
        "umpires": {
            "HP": "Tony Randazzo",
            "1B": "Larry Vanover",
            "2B": "Brian Gorman",
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
# Pitching: BOS #31 Jon Lester
t1 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
t1.new_ab()
t1.pitch_list("b b c c f b s")
t1.out("K")

# 2. TBR #18 Ben Zobrist (X - X - X)
t1.new_ab()
t1.pitch_list("b f")
t1.out("F9")

# 3. TBR #3  Evan Longoria (X - X - X)
t1.new_ab()
t1.pitch_list("b s c c")
t1.out("!K")


# Bot 1st
# Pitching: TBR #40 Roberto Hernandez
b1 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f b f f f f f")
b1.out("F9")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("b c c b f f b")
b1.out("G3-1")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 4. TBR #9  Wil Myers (X - X - X)
t2.new_ab()
t2.hit(4)

# 5. TBR #20 Matt Joyce (X - X - X)
t2.new_ab()
t2.pitch_list("f b")
t2.out("F7")

# 6. TBR #11 Yunel Escobar (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("G6-3")

# 7. TBR #21 James Loney (X - X - X)
t2.new_ab()
t2.pitch_list("b f")
t2.hit(1)

# 8. TBR #28 José Molina (X - X - 21)
t2.new_ab()
t2.pitch_list("c c d s")
t2.out("K")


# Bot 2nd
# Pitching: TBR #40 Roberto Hernandez
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("b b c f f f")
b2.hit(1)
b2.advance(2, "12 1B")
b2.thrown_out(3, "12 7-6", 1, 40)

# 5. BOS #12 Mike Napoli (X - X - 34)
b2.new_ab()
b2.pitch_list("c s f b")
b2.hit(1)
b2.advance(2, "T")
b2.advance(4, "37 1B")

# 6. BOS #37 Mike Carp (X - 12 - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1, rbis=1)
b2.advance(2, "39 BB")
b2.advance(3, "7 F8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
b2.new_ab()
b2.pitch_list("b d f b b")
b2.reach("BB")

# 8. BOS #7  Stephen Drew (X - 37 - 39)
b2.new_ab()
b2.pitch_list("s c b")
b2.out("F8")

# 9. BOS #10 Jose Iglesias (37 - X - 39)
b2.new_ab()
b2.pitch_list("f")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 9. TBR #1  Sean Rodríguez (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("G5-3")

# 1. TBR #8  Desmond Jennings (X - X - X)
t3.new_ab()
t3.pitch_list("b f b c")
t3.hit(1)

# 2. TBR #18 Ben Zobrist (X - X - 8)
t3.new_ab()
t3.pitch_list("b c b f b s")
t3.out("K")

# 3. TBR #3  Evan Longoria (X - X - 8)
t3.new_ab()
t3.pitch_list("b")
t3.out("G4-3")


# Bot 3rd
# Pitching: TBR #40 Roberto Hernandez
b3 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.hit(2)
b3.advance(3, "29 F9")
b3.advance(4, "34 SB")

# 2. BOS #29 Daniel Nava (X - 18 - X)
b3.new_ab()
b3.pitch_list("f b")
b3.out("F9")

# 3. BOS #15 Dustin Pedroia (18 - X - X)
b3.new_ab()
b3.pitch_list("c f b")
b3.reach("HBP")
b3.advance(2, "34 SB")
b3.advance(3, "34 G4-3")

# 4. BOS #34 David Ortiz (18 - X - 15)
b3.new_ab()
b3.pitch_list("f f b b")
b3.out("G4-3")

# 5. BOS #12 Mike Napoli (15 - X - X)
b3.new_ab()
b3.pitch_list("c c")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 4. TBR #9  Wil Myers (X - X - X)
t4.new_ab()
t4.hit(2)
t4.advance(3, "11 F8")

# 5. TBR #20 Matt Joyce (X - 9 - X)
t4.new_ab()
t4.pitch_list("b f b s s")
t4.out("K")

# 6. TBR #11 Yunel Escobar (X - 9 - X)
t4.new_ab()
t4.pitch_list("b c c f d f")
t4.out("F8")

# 7. TBR #21 James Loney (9 - X - X)
t4.new_ab()
t4.pitch_list("f s s")
t4.out("K")


# Bot 4th
# Pitching: TBR #40 Roberto Hernandez
b4 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.pitch_list("c b s s")
b4.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(2)
b4.advance(3, "7 G3")

# 8. BOS #7  Stephen Drew (X - 39 - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G3")

# 9. BOS #10 Jose Iglesias (39 - X - X)
b4.new_ab()
b4.pitch_list("c b b s")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 8. TBR #28 José Molina (X - X - X)
t5.new_ab()
t5.pitch_list("b c f f f s")
t5.out("K")

# 9. TBR #1  Sean Rodríguez (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.hit(1)

# 1. TBR #8  Desmond Jennings (X - X - 1)
t5.new_ab()
t5.pitch_list("b f b s f b f s")
t5.out("K")

# 2. TBR #18 Ben Zobrist (X - X - 1)
t5.new_ab()
t5.pitch_list("f f b")
t5.out("F9")


# Bot 5th
# Pitching: TBR #40 Roberto Hernandez
b5 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c b f b")
b5.out("G3")

# 2. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("b c c")
b5.hit(2)
b5.advance(3, "15 WP")
b5.advance(4, "15 SF9")

# 3. BOS #15 Dustin Pedroia (X - 29 - X)
b5.new_ab()
b5.pitch_list("c s b b")
b5.wp()
b5.out("SF9", rbis=1)

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.thrown_out(2, "12 FC5-4", 3, 40)

# 5. BOS #12 Mike Napoli (X - X - 34)
b5.new_ab()
b5.reach("FC5-4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 3. TBR #3  Evan Longoria (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(4)

# 4. TBR #9  Wil Myers (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.out("L7")

# 5. TBR #20 Matt Joyce (X - X - X)
t6.new_ab()
t6.pitch_list("b b f")
t6.out("G3-1")

# 6. TBR #11 Yunel Escobar (X - X - X)
t6.new_ab()
t6.pitch_list("c f")
t6.out("F9")


# Bot 6th
# Pitching: TBR #54 Alex Torres
b6 = game.new_inning()

# Pitching change (TBR): #54 Alex Torres replaces #40 Roberto Hernandez
b6.pitching_substitution(54)

# 6. BOS #37 Mike Carp (X - X - X)
b6.new_ab()
b6.pitch_list("f b f b c")
b6.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("b c s b")
b6.hit(1)

# 8. BOS #7  Stephen Drew (X - X - 39)
b6.new_ab()
b6.pitch_list("b f b 1 s b s")
b6.out("K")

# 9. BOS #10 Jose Iglesias (X - X - 39)
b6.new_ab()
b6.pitch_list("b b 1")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #31 Jon Lester
t7 = game.new_inning()

# 7. TBR #21 James Loney (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("L7")

# 8. TBR #28 José Molina (X - X - X)
t7.new_ab()
t7.pitch_list("b f")
t7.hit(2)

# Pitching change (BOS): #38 Matt Thornton replaces #31 Jon Lester
t7.pitching_substitution(38)

# 9. TBR #1  Sean Rodríguez (X - 28 - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G5-3")

# Pitching change (BOS): #36 Junichi Tazawa replaces #38 Matt Thornton
t7.pitching_substitution(36)

# 1. TBR #8  Desmond Jennings (X - 28 - X)
t7.new_ab()
t7.pitch_list("c c s")
t7.out("K")


# Bot 7th
# Pitching: TBR #54 Alex Torres
b7 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c")
b7.out("P4")

# 2. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("c b c")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Defensive change (BOS): #5 Jonny Gomes replaces #37 Mike Carp (LF), playing LF, batting 6th
t8.defensive_substitution(6, 5, "7")

# 2. TBR #18 Ben Zobrist (X - X - X)
t8.new_ab()
t8.pitch_list("c b f f b f f c")
t8.out("!K")

# 3. TBR #3  Evan Longoria (X - X - X)
t8.new_ab()
t8.pitch_list("s b s t")
t8.out("KT")

# 4. TBR #9  Wil Myers (X - X - X)
t8.new_ab()
t8.pitch_list("c b s f")
t8.out("G4-3")


# Bot 8th
# Pitching: TBR #35 Jamey Wright
b8 = game.new_inning()

# Pitching change (TBR): #35 Jamey Wright replaces #54 Alex Torres
b8.pitching_substitution(35)

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.out("G4-3")

# Pitching change (TBR): #43 Kyle Farnsworth replaces #35 Jamey Wright
b8.pitching_substitution(43)

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("c s b")
b8.hit(2)
b8.advance(3, "5 1B")
b8.advance(4, "7 1B")

# 6. BOS #5  Jonny Gomes (X - 12 - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1)
b8.advance(3, "7 1B")
b8.advance(4, "10 E6")

# 7. BOS #39 Jarrod Saltalamacchia (12 - X - 5)
b8.new_ab()
b8.pitch_list("f f s")
b8.out("K")

# 8. BOS #7  Stephen Drew (12 - X - 5)
b8.new_ab()
b8.hit(1, rbis=1)
b8.advance(2, "10 SB")
b8.advance(4, "10 E6")

# 9. BOS #10 Jose Iglesias (5 - X - 7)
b8.new_ab()
b8.pitch_list("b b c")
b8.hit(1, rbis=2)
b8.error(6)
b8.advance(3, "E6")

# 1. BOS #18 Shane Victorino (10 - X - X)
b8.new_ab()
b8.pitch_list("c d s b")
b8.out("G3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t9.pitching_substitution(19)

# 5. TBR #20 Matt Joyce (X - X - X)
t9.new_ab()
t9.pitch_list("t b b s b s")
t9.out("K")

# 6. TBR #11 Yunel Escobar (X - X - X)
t9.new_ab()
t9.out("F9")

# 7. TBR #21 James Loney (X - X - X)
t9.new_ab()
t9.pitch_list("c b f s")
t9.out("K")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31)

# Loser team: TBR
# LP: TBR #40 Roberto Hernandez
game.losing_pitcher(40, is_away_team=True)

# print(game)
game.generate_scorecard()
