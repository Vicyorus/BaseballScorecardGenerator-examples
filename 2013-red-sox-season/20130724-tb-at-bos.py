import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TB @ BOS, 2013-07-24
# https://www.baseball-reference.com/boxes/BOS/BOS201307240.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2013/07/24/348255/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-24 19:11-22:11",
        "at": "Fenway Park, Boston, MA",
        "att": "36,514",
        "temp": "82F, Partly Cloudy",
        "wind": "10mph, L To R",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 14,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                3: "Evan Longoria",
                18: "Ben Zobrist",
                9: "Wil Myers",
                30: "Luke Scott",
                1: "Sean Rodríguez",
                21: "James Loney",
                28: "José Molina",
                11: "Yunel Escobar",
                # Starting pitcher
                14: "David Price",
                # Bench
                20: "Matt Joyce",
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
                56: "Fernando Rodney",
                22: "Chris Archer",
                40: "Roberto Hernandez",
            },
            "lefties": [14, 55, 57, 54, 27],
            "lineup": [
                [8, "8"],
                [3, "5"],
                [18, "4"],
                [9, "9"],
                [30, "0"],
                [1, "7"],
                [21, "3"],
                [28, "2"],
                [11, "6"],
            ],
            "bench": [
                [20, "RF"],
                [59, "C"],
                [5, "LF"],
                [2, "2B"],
            ],
            "bullpen": [58, 55, 62, 35, 43, 57, 54, 27, 56, 22, 40],
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
                12: "Mike Napoli",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                10: "Jose Iglesias",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                29: "Daniel Nava",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                65: "Jose De La Torre",
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                46: "Ryan Dempster",
            },
            "lefties": [22, 32, 66, 31, 38],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [7, "6"],
                [39, "2"],
                [10, "5"],
            ],
            "bench": [
                [37, "1B"],
                [29, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [65, 41, 67, 32, 66, 31, 36, 19, 38, 54, 46],
        },
        "umpires": {
            "HP": "Larry Vanover",
            "1B": "Brian Gorman",
            "2B": "Manny Gonzalez",
            "3B": "Tony Randazzo",
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
t1.pitch_list("b f b f s")
t1.out("K")

# 2. TBR #3  Evan Longoria (X - X - X)
t1.new_ab()
t1.pitch_list("f b s c")
t1.out("!K")

# 3. TBR #18 Ben Zobrist (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.hit(1)
t1.advance(2, "9 BB")

# 4. TBR #9  Wil Myers (X - X - 18)
t1.new_ab()
t1.pitch_list("d 1 f b c b f f f b")
t1.reach("BB")

# 5. TBR #30 Luke Scott (X - 18 - 9)
t1.new_ab()
t1.pitch_list("c c b b b")
t1.out("G4-3")


# Bot 1st
# Pitching: TBR #14 David Price
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c f f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 6. TBR #1  Sean Rodríguez (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("G4-3")

# 7. TBR #21 James Loney (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")

# 8. TBR #28 José Molina (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")


# Bot 2nd
# Pitching: TBR #14 David Price
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)

# 5. BOS #12 Mike Napoli (X - X - 34)
b2.new_ab()
b2.pitch_list("b f f s")
b2.out("K")

# 6. BOS #5  Jonny Gomes (X - X - 34)
b2.new_ab()
b2.pitch_list("1 f c b c")
b2.out("!K")

# 7. BOS #7  Stephen Drew (X - X - 34)
b2.new_ab()
b2.pitch_list("c b")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 9. TBR #11 Yunel Escobar (X - X - X)
t3.new_ab()
t3.out("G6-3")

# 1. TBR #8  Desmond Jennings (X - X - X)
t3.new_ab()
t3.pitch_list("b c s b")
t3.hit(1)
t3.error(1)
t3.advance(2, "3 POE1")
t3.advance(3, "3 1B")
t3.advance(4, "9 1B")

# 2. TBR #3  Evan Longoria (X - X - 8)
t3.new_ab()
t3.pitch_list("1 1 b")
t3.hit(1)
t3.advance(2, "18 SAC-1")
t3.advance(4, "9 1B")

# 3. TBR #18 Ben Zobrist (8 - X - 3)
t3.new_ab()
t3.reach("SAC-1")
t3.advance(2, "9 1B")
t3.advance(3, "30 SB")
t3.advance(4, "30 SF7")

# 4. TBR #9  Wil Myers (8 - 3 - 18)
t3.new_ab()
t3.pitch_list("f b c f f")
t3.hit(1, rbis=2)
t3.advance(2, "30 SB")

# 5. TBR #30 Luke Scott (X - 18 - 9)
t3.new_ab()
t3.pitch_list("f c b")
t3.out("SF7", rbis=1)

# 6. TBR #1  Sean Rodríguez (X - 9 - X)
t3.new_ab()
t3.pitch_list("c f b c")
t3.out("!K")


# Bot 3rd
# Pitching: TBR #14 David Price
b3 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G6-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.out("G1-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 7. TBR #21 James Loney (X - X - X)
t4.new_ab()
t4.pitch_list("b b c")
t4.hit(1)
t4.thrown_out(2, "28 DP1-6-3", 1, 22)

# 8. TBR #28 José Molina (X - X - 21)
t4.new_ab()
t4.pitch_list("s")
t4.out("DP1-6-3")

# 9. TBR #11 Yunel Escobar (X - X - X)
t4.new_ab()
t4.pitch_list("f s b b b")
t4.out("G5-3")


# Bot 4th
# Pitching: TBR #14 David Price
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b b f")
b4.hit(1)
b4.thrown_out(2, "15 DP6-4-3", 1, 14)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b4.new_ab()
b4.pitch_list("f 1")
b4.out("DP6-4-3")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
t5.new_ab()
t5.pitch_list("c f b s")
t5.out("K")

# 2. TBR #3  Evan Longoria (X - X - X)
t5.new_ab()
t5.pitch_list("b b s")
t5.out("G5-3")

# 3. TBR #18 Ben Zobrist (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("F8")


# Bot 5th
# Pitching: TBR #14 David Price
b5 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("b c c b")
b5.hit(2)

# 6. BOS #5  Jonny Gomes (X - 12 - X)
b5.new_ab()
b5.out("L8")

# 7. BOS #7  Stephen Drew (X - 12 - X)
b5.new_ab()
b5.pitch_list("b f b b")
b5.out("F8")

# 8. BOS #39 Jarrod Saltalamacchia (X - 12 - X)
b5.new_ab()
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 4. TBR #9  Wil Myers (X - X - X)
t6.new_ab()
t6.pitch_list("b b s c")
t6.out("G1-3")

# 5. TBR #30 Luke Scott (X - X - X)
t6.new_ab()
t6.hit(1)

# 6. TBR #1  Sean Rodríguez (X - X - 30)
t6.new_ab()
t6.pitch_list("b")
t6.out("P3")

# 7. TBR #21 James Loney (X - X - 30)
t6.new_ab()
t6.pitch_list("c f s")
t6.out("K")


# Bot 6th
# Pitching: TBR #14 David Price
b6 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("c s b")
b6.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("c c")
b6.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b6.new_ab()
b6.pitch_list("c 1 f 1 1 b")
b6.out("G1-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Felix Doubront
t7 = game.new_inning()

# 8. TBR #28 José Molina (X - X - X)
t7.new_ab()
t7.pitch_list("b s")
t7.out("G6-3")

# 9. TBR #11 Yunel Escobar (X - X - X)
t7.new_ab()
t7.pitch_list("c b c f b")
t7.out("G6-3")

# 1. TBR #8  Desmond Jennings (X - X - X)
t7.new_ab()
t7.pitch_list("b f b b b")
t7.reach("BB")
t7.advance(2, "3 SB")

# Pitching change (BOS): #54 Pedro Beato replaces #22 Felix Doubront
t7.pitching_substitution(54)

# 2. TBR #3  Evan Longoria (X - X - 8)
t7.new_ab()
t7.pitch_list("1 1 c b s")
t7.out("F9")


# Bot 7th
# Pitching: TBR #14 David Price
b7 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("c b f f b")
b7.out("G3-1")

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.hit(4)

# 6. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("f b")
b7.out("P4")

# 7. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b")
b7.out("(F)P5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #54 Pedro Beato
t8 = game.new_inning()

# 3. TBR #18 Ben Zobrist (X - X - X)
t8.new_ab()
t8.out("F9")

# 4. TBR #9  Wil Myers (X - X - X)
t8.new_ab()
t8.pitch_list("c s")
t8.hit(1)
t8.thrown_out(2, "30 FC4-6", 2, 38)

# Pitching change (BOS): #38 Matt Thornton replaces #54 Pedro Beato
t8.pitching_substitution(38)

# 5. TBR #30 Luke Scott (X - X - 9)
t8.new_ab()
t8.pitch_list("1 b s f")
t8.reach("FC4-6")
t8.advance(2, "1 1B")
t8.advance(4, "21 1B")

# 6. TBR #1  Sean Rodríguez (X - X - 30)
t8.new_ab()
t8.pitch_list("c d 1 f")
t8.hit(1)
t8.advance(3, "21 1B")
t8.advance(4, "28 1B")

# 7. TBR #21 James Loney (X - 30 - 1)
t8.new_ab()
t8.hit(1, rbis=1)
t8.advance(2, "28 1B")

# 8. TBR #28 José Molina (1 - X - 21)
t8.new_ab()
t8.pitch_list("s b f f")
t8.hit(1, rbis=1)

# 9. TBR #11 Yunel Escobar (X - 21 - 28)
t8.new_ab()
t8.out("G3")


# Bot 8th
# Pitching: TBR #14 David Price
b8 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("c c")
b8.out("G4-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
b8.new_ab()
b8.pitch_list("b f f b s")
b8.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("c f")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #66 Drake Britton
t9 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #38 Matt Thornton
t9.pitching_substitution(66)

# 1. TBR #8  Desmond Jennings (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G5-3")

# 2. TBR #3  Evan Longoria (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.out("G6-3")

# 3. TBR #18 Ben Zobrist (X - X - X)
t9.new_ab()
t9.pitch_list("b c b s b")
t9.hit(1)

# 4. TBR #9  Wil Myers (X - X - 18)
t9.new_ab()
t9.out("G5-3")


# Bot 9th
# Pitching: TBR #14 David Price
b9 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b9.new_ab()
b9.pitch_list("b c b f")
b9.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b9.new_ab()
b9.pitch_list("c b b")
b9.out("(F)P3")

# 4. BOS #34 David Ortiz (X - X - X)
b9.new_ab()
b9.out("L6")

# Winning team: TBR
# WP: TBR #14 David Price
game.winning_pitcher(14, is_away_team=True)

# Loser team: BOS
# LP: BOS #22 Felix Doubront
game.losing_pitcher(22)

# print(game)
game.generate_scorecard()
