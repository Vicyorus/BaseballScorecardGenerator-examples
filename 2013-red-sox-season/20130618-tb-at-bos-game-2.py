import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TB @ BOS, 2013-06-18
# https://www.baseball-reference.com/boxes/BOS/BOS201306182.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2013/06/18/347811/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-18 20:07-22:34",
        "at": "Fenway Park, Boston, MA",
        "att": "32,156",
        "temp": "59F, Cloudy",
        "wind": "7mph, In From CF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 23,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                1: "Sean Rodríguez",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                11: "Yunel Escobar",
                9: "Wil Myers",
                30: "Luke Scott",
                59: "Jose Lobaton",
                2: "Kelly Johnson",
                # Starting pitcher
                23: "Jake Odorizzi",
                # Bench
                28: "José Molina",
                21: "James Loney",
                20: "Matt Joyce",
                5: "Sam Fuld",
                # Bullpen
                58: "Jeremy Hellickson",
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                52: "Josh Lueke",
                56: "Fernando Rodney",
                22: "Chris Archer",
                40: "Roberto Hernandez",
            },
            "lefties": [55, 57, 54, 27],
            "lineup": [
                [8, "8"],
                [1, "3"],
                [18, "4"],
                [3, "5"],
                [11, "6"],
                [9, "9"],
                [30, "0"],
                [59, "2"],
                [2, "7"],
            ],
            "bench": [
                [28, "C"],
                [21, "1B"],
                [20, "RF"],
                [5, "LF"],
            ],
            "bullpen": [58, 55, 62, 35, 43, 57, 54, 27, 52, 56, 22, 40],
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
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                16: "Will Middlebrooks",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                91: "Alfredo Aceves",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                54: "Pedro Beato",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 30, 32, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "3"],
                [5, "7"],
                [39, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [37, "1B"],
                [16, "3B"],
                [12, "1B"],
                [20, "C"],
            ],
            "bullpen": [63, 40, 41, 56, 30, 32, 91, 31, 36, 19, 54, 46],
        },
        "umpires": {
            "HP": "Brian Knight",
            "1B": "Dan Iassogna",
            "2B": "Mark Carlson",
            "3B": "Lance Barrett",
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

# 1. TBR #8  Desmond Jennings (X - X - X)
t1.new_ab()
t1.hit(1)
t1.advance(2, "3 WP")

# 2. TBR #1  Sean Rodríguez (X - X - 8)
t1.new_ab()
t1.pitch_list("1 c b")
t1.out("F7")

# 3. TBR #18 Ben Zobrist (X - X - 8)
t1.new_ab()
t1.pitch_list("c")
t1.out("F9")

# 4. TBR #3  Evan Longoria (X - X - 8)
t1.new_ab()
t1.pitch_list("s b s b b s")
t1.wp()
t1.out("K")


# Bot 1st
# Pitching: TBR #23 Jake Odorizzi
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c c b")
b1.out("G1-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("L8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 5. TBR #11 Yunel Escobar (X - X - X)
t2.new_ab()
t2.out("F8")

# 6. TBR #9  Wil Myers (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "30 G3")

# 7. TBR #30 Luke Scott (X - X - 9)
t2.new_ab()
t2.pitch_list("c b b")
t2.out("G3")

# 8. TBR #59 Jose Lobaton (X - 9 - X)
t2.new_ab()
t2.pitch_list("s b s f c")
t2.out("!K")


# Bot 2nd
# Pitching: TBR #23 Jake Odorizzi
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.out("F7")

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c b f b")
b2.hit(4)

# 6. BOS #5  Jonny Gomes (X - X - X)
b2.new_ab()
b2.pitch_list("b b f c f c")
b2.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("b s c b")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 9. TBR #2  Kelly Johnson (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.thrown_out(2, "1 DP4-6-3", 2, 22)

# 1. TBR #8  Desmond Jennings (X - X - 2)
t3.new_ab()
t3.out("F9")

# 2. TBR #1  Sean Rodríguez (X - X - 2)
t3.new_ab()
t3.pitch_list("b b c b c f")
t3.out("DP4-6-3")


# Bot 3rd
# Pitching: TBR #23 Jake Odorizzi
b3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("b c b")
b3.out("(F)P5")

# 9. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("b b c")
b3.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("f b b")
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 3. TBR #18 Ben Zobrist (X - X - X)
t4.new_ab()
t4.pitch_list("f b b")
t4.out("G5-3")

# 4. TBR #3  Evan Longoria (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G5-3")

# 5. TBR #11 Yunel Escobar (X - X - X)
t4.new_ab()
t4.pitch_list("s b b b f")
t4.out("F9")


# Bot 4th
# Pitching: TBR #23 Jake Odorizzi
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b f b b c s")
b4.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("f f")
b4.hit(1)
b4.advance(2, "34 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
b4.new_ab()
b4.pitch_list("b b t")
b4.hit(1)

# 5. BOS #29 Daniel Nava (X - 15 - 34)
b4.new_ab()
b4.pitch_list("b f b f b")
b4.out("F8")

# 6. BOS #5  Jonny Gomes (X - 15 - 34)
b4.new_ab()
b4.pitch_list("s d b f")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 6. TBR #9  Wil Myers (X - X - X)
t5.new_ab()
t5.pitch_list("b f b s b c")
t5.out("!K")

# 7. TBR #30 Luke Scott (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("F8")

# 8. TBR #59 Jose Lobaton (X - X - X)
t5.new_ab()
t5.pitch_list("s c b b s")
t5.out("K")


# Bot 5th
# Pitching: TBR #23 Jake Odorizzi
b5 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c")
b5.out("F7")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b c c b")
b5.hit(2)
b5.advance(3, "10 1B")

# 9. BOS #10 Jose Iglesias (X - 7 - X)
b5.new_ab()
b5.pitch_list("c c d b")
b5.hit(1)
b5.thrown_out(2, "2 DP6-3", 2, 23)

# 1. BOS #2  Jacoby Ellsbury (7 - X - 10)
b5.new_ab()
b5.pitch_list("1 f b f")
b5.out("DP6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 9. TBR #2  Kelly Johnson (X - X - X)
t6.new_ab()
t6.pitch_list("b b f")
t6.out("G3-1")

# 1. TBR #8  Desmond Jennings (X - X - X)
t6.new_ab()
t6.pitch_list("c b c b f")
t6.out("F8")

# 2. TBR #1  Sean Rodríguez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("(F)P2")


# Bot 6th
# Pitching: TBR #23 Jake Odorizzi
b6 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b c")
b6.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("b c b b f")
b6.out("G5-3")

# Pitching change (TBR): #54 Alex Torres replaces #23 Jake Odorizzi
b6.pitching_substitution(54)

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.hit(2)

# 5. BOS #29 Daniel Nava (X - 34 - X)
b6.new_ab()
b6.pitch_list("f c")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Felix Doubront
t7 = game.new_inning()

# 3. TBR #18 Ben Zobrist (X - X - X)
t7.new_ab()
t7.out("F8")

# 4. TBR #3  Evan Longoria (X - X - X)
t7.new_ab()
t7.pitch_list("c b c f b")
t7.out("F9")

# 5. TBR #11 Yunel Escobar (X - X - X)
t7.new_ab()
t7.pitch_list("b s c c")
t7.out("!K")


# Bot 7th
# Pitching: TBR #54 Alex Torres
b7 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("b f f s")
b7.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("b f b s f b b")
b7.reach("BB")

# 8. BOS #7  Stephen Drew (X - X - 39)
b7.new_ab()
b7.out("F7")

# 9. BOS #10 Jose Iglesias (X - X - 39)
b7.new_ab()
b7.pitch_list("c")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #22 Felix Doubront
t8 = game.new_inning()

# 6. TBR #9  Wil Myers (X - X - X)
t8.new_ab()
t8.out("F9")

# 7. TBR #30 Luke Scott (X - X - X)
t8.new_ab()
t8.pitch_list("c b s b s")
t8.out("K")

# Offensive change (TBR): Pinch-hitter #20 Matt Joyce replaces #59 Jose Lobaton, batting 8th
t8.offensive_substitution(8, 20, "PH")

# 8. TBR #20 Matt Joyce (X - X - X)
t8.new_ab()
t8.pitch_list("b b f b")
t8.out("P4")


# Bot 8th
# Pitching: TBR #54 Alex Torres
b8 = game.new_inning()

# Defensive change (TBR): #28 José Molina replaces #20 Matt Joyce (PH), playing C, batting 8th
b8.defensive_substitution(8, 28, "2")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("f b s")
b8.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("b c b f b b")
b8.reach("BB")

# 4. BOS #34 David Ortiz (X - X - 15)
b8.new_ab()
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #22 Felix Doubront
t9.pitching_substitution(40)

# 9. TBR #2  Kelly Johnson (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(4)

# 1. TBR #8  Desmond Jennings (X - X - X)
t9.new_ab()
t9.pitch_list("b c c b")
t9.out("F9")

# Offensive change (TBR): Pinch-hitter #21 James Loney replaces #1 Sean Rodríguez, batting 2nd
t9.offensive_substitution(2, 21, "PH")

# 2. TBR #21 James Loney (X - X - X)
t9.new_ab()
t9.pitch_list("b f")
t9.out("G4-3")

# 3. TBR #18 Ben Zobrist (X - X - X)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")
t9.thrown_out(2, "3 FC5-4", 3, 40)

# 4. TBR #3  Evan Longoria (X - X - 18)
t9.new_ab()
t9.pitch_list("c b f 1")
t9.reach("FC5-4")


# Bot 9th
# Pitching: TBR #62 Joel Peralta
b9 = game.new_inning()

# Pitching change (TBR): #62 Joel Peralta replaces #54 Alex Torres
b9.pitching_substitution(62)

# Defensive switch (TBR): #21 James Loney moves to 1B
b9.defensive_switch(21, "3")

# 5. BOS #29 Daniel Nava (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c b")
b9.reach("BB")
b9.advance(4, "5 HR")

# 6. BOS #5  Jonny Gomes (X - X - 29)
b9.new_ab()
b9.pitch_list("1")
b9.hit(4, rbis=2)

# Winning team: BOS
# WP: BOS #40 Andrew Bailey
game.winning_pitcher(40)

# Loser team: TBR
# LP: TBR #62 Joel Peralta
game.losing_pitcher(62, is_away_team=True)

# print(game)
game.generate_scorecard()
