import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TB, 2013-06-11
# https://www.baseball-reference.com/boxes/TBA/TBA201306110.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2013/06/11/347706/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-11 19:12-22:18",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "16,870",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                7: "Stephen Drew",
                3: "David Ross",
                10: "Jose Iglesias",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                16: "Will Middlebrooks",
                5: "Jonny Gomes",
                # Bullpen
                65: "Jose De La Torre",
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 30, 32, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [7, "6"],
                [3, "2"],
                [10, "5"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [16, "3B"],
                [5, "LF"],
            ],
            "bullpen": [65, 40, 41, 56, 30, 32, 19, 36, 22, 46],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 40,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                1: "Sean Rodríguez",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                11: "Yunel Escobar",
                21: "James Loney",
                19: "Ryan Roberts",
                28: "José Molina",
                20: "Matt Joyce",
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
                23: "Jake Odorizzi",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                56: "Fernando Rodney",
                22: "Chris Archer",
            },
            "lefties": [55, 57, 54, 27],
            "lineup": [
                [8, "8"],
                [1, "7"],
                [18, "9"],
                [3, "5"],
                [11, "6"],
                [21, "3"],
                [19, "4"],
                [28, "2"],
                [20, "0"],
            ],
            "bench": [
                [30, "DH"],
                [59, "C"],
                [5, "LF"],
                [2, "2B"],
            ],
            "bullpen": [58, 55, 62, 35, 43, 23, 57, 54, 27, 56, 22],
        },
        "umpires": {
            "HP": "Chris Guccione",
            "1B": "Ron Kulpa",
            "2B": "Phil Cuzzi",
            "3B": "Tom Hallion",
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
# Pitching: TBR #40 Roberto Hernandez
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.advance(2, "18 SB")
t1.advance(3, "18 1B")
t1.advance(4, "15 (F)SF9")

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("b b c")
t1.hit(1)
t1.advance(2, "34 SB")

# 3. BOS #15 Dustin Pedroia (2 - X - 18)
t1.new_ab()
t1.pitch_list("c f b")
t1.out("(F)SF9", rbis=1)

# 4. BOS #34 David Ortiz (X - X - 18)
t1.new_ab()
t1.pitch_list("b c f b d s")
t1.out("K")

# 5. BOS #12 Mike Napoli (X - 18 - X)
t1.new_ab()
t1.pitch_list("b c b b f f")
t1.out("G5-3")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
b1.new_ab()
b1.pitch_list("c b c")
b1.hit(1)
b1.advance(2, "1 BB")
b1.advance(3, "18 DP4-6-3")
b1.advance(4, "21 BB")

# 2. TBR #1  Sean Rodríguez (X - X - 8)
b1.new_ab()
b1.pitch_list("b c b b b")
b1.reach("BB")
b1.thrown_out(2, "18 DP4-6-3", 1, 31)

# 3. TBR #18 Ben Zobrist (X - 8 - 1)
b1.new_ab()
b1.out("DP4-6-3")

# 4. TBR #3  Evan Longoria (8 - X - X)
b1.new_ab()
b1.pitch_list("b b b b")
b1.reach("BB")
b1.advance(2, "11 BB")
b1.advance(3, "21 BB")

# 5. TBR #11 Yunel Escobar (8 - X - 3)
b1.new_ab()
b1.pitch_list("b c b b b")
b1.reach("BB")
b1.advance(2, "21 BB")

# 6. TBR #21 James Loney (8 - 3 - 11)
b1.new_ab()
b1.pitch_list("b b c t b b")
b1.reach("BB", rbis=1)

# 7. TBR #19 Ryan Roberts (3 - 11 - 21)
b1.new_ab()
b1.out("G1-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #40 Roberto Hernandez
t2 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b f")
t2.hit(1)
t2.thrown_out(2, "7 DP4-6-3", 1, 40)

# 7. BOS #7  Stephen Drew (X - X - 29)
t2.new_ab()
t2.pitch_list("c s b")
t2.out("DP4-6-3")

# 8. BOS #3  David Ross (X - X - X)
t2.new_ab()
t2.pitch_list("b b c s s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 8. TBR #28 José Molina (X - X - X)
b2.new_ab()
b2.pitch_list("c c b f c")
b2.out("!K")

# 9. TBR #20 Matt Joyce (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("F8")

# 1. TBR #8  Desmond Jennings (X - X - X)
b2.new_ab()
b2.pitch_list("b b c")
b2.hit(4)

# 2. TBR #1  Sean Rodríguez (X - X - X)
b2.new_ab()
b2.pitch_list("s b b t b")
b2.out("L9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #40 Roberto Hernandez
t3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t3.new_ab()
t3.pitch_list("b f f")
t3.hit(1)
t3.advance(2, "2 FC3")
t3.advance(3, "18 SAC1-3")
t3.advance(4, "12 1B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
t3.new_ab()
t3.pitch_list("1 b")
t3.reach("FC3")
t3.advance(2, "18 SAC1-3")
t3.advance(4, "12 1B")

# 2. BOS #18 Shane Victorino (X - 10 - 2)
t3.new_ab()
t3.out("SAC1-3")

# 3. BOS #15 Dustin Pedroia (10 - 2 - X)
t3.new_ab()
t3.pitch_list("f f s")
t3.out("K")

# 4. BOS #34 David Ortiz (10 - 2 - X)
t3.new_ab()
t3.pitch_list("b b i i")
t3.reach("IBB")
t3.advance(2, "12 1B")

# 5. BOS #12 Mike Napoli (10 - 2 - 34)
t3.new_ab()
t3.pitch_list("s")
t3.hit(1, rbis=2)

# 6. BOS #29 Daniel Nava (X - 34 - 12)
t3.new_ab()
t3.out("L8")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 3. TBR #18 Ben Zobrist (X - X - X)
b3.new_ab()
b3.pitch_list("c c")
b3.hit(1)
b3.advance(2, "11 BB")
b3.advance(4, "19 1B")

# 4. TBR #3  Evan Longoria (X - X - 18)
b3.new_ab()
b3.pitch_list("b s f c")
b3.out("!K")

# 5. TBR #11 Yunel Escobar (X - X - 18)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.advance(2, "19 1B")
b3.advance(4, "28 1B")

# 6. TBR #21 James Loney (X - 18 - 11)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")

# 7. TBR #19 Ryan Roberts (X - 18 - 11)
b3.new_ab()
b3.pitch_list("s c")
b3.hit(1, rbis=1)
b3.advance(2, "28 1B")
b3.advance(3, "20 1B")

# 8. TBR #28 José Molina (X - 11 - 19)
b3.new_ab()
b3.hit(1, rbis=1)
b3.advance(2, "20 1B")

# 9. TBR #20 Matt Joyce (X - 19 - 28)
b3.new_ab()
b3.pitch_list("b 2 b f c")
b3.hit(1)
b3.thrown_out(2, "8 FC6-4", 3, 31)

# 1. TBR #8  Desmond Jennings (19 - 28 - 20)
b3.new_ab()
b3.pitch_list("b d")
b3.reach("FC6-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #40 Roberto Hernandez
t4 = game.new_inning()

# 7. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("c b s s")
t4.out("K")

# 8. BOS #3  David Ross (X - X - X)
t4.new_ab()
t4.pitch_list("f s b f b b s")
t4.out("K")

# 9. BOS #10 Jose Iglesias (X - X - X)
t4.new_ab()
t4.pitch_list("b b c c f c")
t4.out("!K")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 2. TBR #1  Sean Rodríguez (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("P6")

# 3. TBR #18 Ben Zobrist (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b")
b4.out("P4")

# 4. TBR #3  Evan Longoria (X - X - X)
b4.new_ab()
b4.hit(4)

# 5. TBR #11 Yunel Escobar (X - X - X)
b4.new_ab()
b4.pitch_list("b c c")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #40 Roberto Hernandez
t5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.pitch_list("c b b s f")
t5.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.out("L7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 6. TBR #21 James Loney (X - X - X)
b5.new_ab()
b5.out("L6")

# 7. TBR #19 Ryan Roberts (X - X - X)
b5.new_ab()
b5.pitch_list("c b b b c b")
b5.reach("BB")
b5.advance(2, "28 BB")
b5.thrown_out(3, "20 CS", 2, 31)

# 8. TBR #28 José Molina (X - X - 19)
b5.new_ab()
b5.pitch_list("b f b b b")
b5.reach("BB")
b5.advance(4, "20 HR")

# 9. TBR #20 Matt Joyce (X - 19 - 28)
b5.new_ab()
b5.pitch_list("b n b c")
b5.hit(4, rbis=2)

# Pitching change (BOS): #65 Jose De La Torre replaces #31 Jon Lester
b5.pitching_substitution(65)

# 1. TBR #8  Desmond Jennings (X - X - X)
b5.new_ab()
b5.pitch_list("b c f b b")
b5.hit(4)

# 2. TBR #1  Sean Rodríguez (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")

# 3. TBR #18 Ben Zobrist (X - X - 1)
b5.new_ab()
b5.pitch_list("c")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #40 Roberto Hernandez
t6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.hit(1)
t6.advance(2, "7 BB")

# 5. BOS #12 Mike Napoli (X - X - 34)
t6.new_ab()
t6.pitch_list("b c f s")
t6.out("K")

# 6. BOS #29 Daniel Nava (X - X - 34)
t6.new_ab()
t6.pitch_list("c b c f")
t6.out("F8")

# 7. BOS #7  Stephen Drew (X - X - 34)
t6.new_ab()
t6.pitch_list("b b b c c b")
t6.reach("BB")

# 8. BOS #3  David Ross (X - 34 - 7)
t6.new_ab()
t6.pitch_list("c s")
t6.out("(F)P3")


# Bot 6th
# Pitching: BOS #65 Jose De La Torre
b6 = game.new_inning()

# 4. TBR #3  Evan Longoria (X - X - X)
b6.new_ab()
b6.pitch_list("c s b b s")
b6.out("K")

# 5. TBR #11 Yunel Escobar (X - X - X)
b6.new_ab()
b6.out("(F)F9")

# 6. TBR #21 James Loney (X - X - X)
b6.new_ab()
b6.pitch_list("c s")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #40 Roberto Hernandez
t7 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t7.new_ab()
t7.pitch_list("c f b")
t7.hit(1)
t7.thrown_out(2, "2 DP3-6-3", 1, 40)

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
t7.new_ab()
t7.pitch_list("b")
t7.out("DP3-6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("P6")


# Bot 7th
# Pitching: BOS #65 Jose De La Torre
b7 = game.new_inning()

# 7. TBR #19 Ryan Roberts (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G5-3")

# 8. TBR #28 José Molina (X - X - X)
b7.new_ab()
b7.pitch_list("c f f f s")
b7.out("K")

# 9. TBR #20 Matt Joyce (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c b")
b7.reach("BB")
b7.error(2)
b7.advance(2, "8 SB")
b7.advance(3, "8 E2")

# 1. TBR #8  Desmond Jennings (X - X - 20)
b7.new_ab()
b7.pitch_list("b f b c b")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #40 Roberto Hernandez
t8 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c b f f")
t8.reach("HBP")
t8.advance(2, "34 1B")
t8.advance(3, "29 G1-3")

# 4. BOS #34 David Ortiz (X - X - 15)
t8.new_ab()
t8.pitch_list("b c b")
t8.hit(1)
t8.advance(2, "29 G1-3")

# Pitching change (TBR): #62 Joel Peralta replaces #40 Roberto Hernandez
t8.pitching_substitution(62)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t8.new_ab()
t8.pitch_list("s c f s")
t8.out("K")

# 6. BOS #29 Daniel Nava (X - 15 - 34)
t8.new_ab()
t8.pitch_list("b c b c")
t8.out("G1-3")

# 7. BOS #7  Stephen Drew (15 - 34 - X)
t8.new_ab()
t8.out("F8")


# Bot 8th
# Pitching: BOS #65 Jose De La Torre
b8 = game.new_inning()

# 2. TBR #1  Sean Rodríguez (X - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.hit(1)
b8.thrown_out(2, "18 CS", 1, 65)

# 3. TBR #18 Ben Zobrist (X - X - 1)
b8.new_ab()
b8.pitch_list("s b s b 1 1 d b")
b8.reach("BB")

# 4. TBR #3  Evan Longoria (X - X - 18)
b8.new_ab()
b8.pitch_list("s f c")
b8.out("!K")

# 5. TBR #11 Yunel Escobar (X - X - 18)
b8.new_ab()
b8.pitch_list("1")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #57 Jake McGee
t9 = game.new_inning()

# Pitching change (TBR): #57 Jake McGee replaces #62 Joel Peralta
t9.pitching_substitution(57)

# Defensive change (TBR): #5 Sam Fuld replaces #1 Sean Rodríguez (LF), playing LF, batting 2nd
t9.defensive_substitution(2, 5, "7")

# 8. BOS #3  David Ross (X - X - X)
t9.new_ab()
t9.pitch_list("c s f b b")
t9.out("F8")

# 9. BOS #10 Jose Iglesias (X - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b")
t9.hit(1)

# 2. BOS #18 Shane Victorino (X - X - 2)
t9.new_ab()
t9.pitch_list("c f f")
t9.out("P6")

# Winning team: TBR
# WP: TBR #40 Roberto Hernandez
game.winning_pitcher(40)

# Loser team: BOS
# LP: BOS #31 Jon Lester
game.losing_pitcher(31, is_away_team=True)

# print(game)
game.generate_scorecard()
