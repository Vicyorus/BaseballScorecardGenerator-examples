import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2013-07-26
# https://www.baseball-reference.com/boxes/BAL/BAL201307260.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2013/07/26/348275/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-26 19:07-21:42",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "39,063",
        "temp": "85F, Partly Cloudy",
        "wind": "9mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                65: "Jose De La Torre",
                67: "Brandon Workman",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [65, 67, 32, 66, 31, 36, 19, 38, 54, 22, 46],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 30,
            "roster": {
                # Lineup
                9: "Nate McLouth",
                13: "Manny Machado",
                21: "Nick Markakis",
                10: "Adam Jones",
                19: "Chris Davis",
                32: "Matt Wieters",
                2: "J.J. Hardy",
                51: "Henry Urrutia",
                1: "Brian Roberts",
                # Starting pitcher
                30: "Chris Tillman",
                # Bench
                3: "Ryan Flaherty",
                31: "Taylor Teagarden",
                12: "Alexi Casilla",
                # Bullpen
                50: "Miguel González",
                40: "Troy Patton",
                66: "T.J. McFarland",
                34: "Scott Feldman",
                57: "Francisco Rodríguez",
                29: "Tommy Hunter",
                63: "Jairo Asencio",
                56: "Darren O'Day",
                39: "Jason Hammel",
                17: "Brian Matusz",
                43: "Jim Johnson",
                16: "Wei-Yin Chen",
            },
            "lefties": [40, 66, 17, 16],
            "lineup": [
                [9, "7"],
                [13, "5"],
                [21, "9"],
                [10, "8"],
                [19, "3"],
                [32, "2"],
                [2, "6"],
                [51, "0"],
                [1, "4"],
            ],
            "bench": [
                [3, "2B"],
                [31, "C"],
                [12, "2B"],
            ],
            "bullpen": [50, 40, 66, 34, 57, 29, 63, 56, 39, 17, 43, 16],
        },
        "umpires": {
            "HP": "Laz Diaz",
            "1B": "Tim Timmons",
            "2B": "Mike Estabrook",
            "3B": "Mike Winters",
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
# Pitching: BAL #30 Chris Tillman
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.hit(1)
t1.advance(2, "34 BB")
t1.advance(3, "12 BB")

# 4. BOS #34 David Ortiz (X - X - 15)
t1.new_ab()
t1.pitch_list("c 1 d b b b")
t1.reach("BB")
t1.advance(2, "12 BB")

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t1.new_ab()
t1.pitch_list("b s b b s b")
t1.reach("BB")

# 6. BOS #29 Daniel Nava (15 - 34 - 12)
t1.new_ab()
t1.pitch_list("c c s")
t1.out("K")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
b1.new_ab()
b1.pitch_list("c f s")
b1.out("K")

# 2. BAL #13 Manny Machado (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b b")
b1.out("P4")

# 3. BAL #21 Nick Markakis (X - X - X)
b1.new_ab()
b1.pitch_list("b b c")
b1.hit(1)
b1.advance(4, "10 HR")

# 4. BAL #10 Adam Jones (X - X - 21)
b1.new_ab()
b1.pitch_list("d c")
b1.hit(4, rbis=2)

# 5. BAL #19 Chris Davis (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.hit(1)

# 6. BAL #32 Matt Wieters (X - X - 19)
b1.new_ab()
b1.pitch_list("b b f f f f f b f")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #30 Chris Tillman
t2 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("c b c")
t2.out("F7")

# 8. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c")
t2.out("L7")

# 9. BOS #10 Jose Iglesias (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 7. BAL #2  J.J. Hardy (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("L7")

# 8. BAL #51 Henry Urrutia (X - X - X)
b2.new_ab()
b2.pitch_list("s b s")
b2.out("G5-3")

# 9. BAL #1  Brian Roberts (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #30 Chris Tillman
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c f b s")
t3.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b s")
t3.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("b c c f")
t3.out("G3")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
b3.new_ab()
b3.hit(3)
b3.advance(4, "13 1B")

# 2. BAL #13 Manny Machado (9 - X - X)
b3.new_ab()
b3.pitch_list("b b d s c f")
b3.hit(1, rbis=1)
b3.advance(2, "21 G3")

# 3. BAL #21 Nick Markakis (X - X - 13)
b3.new_ab()
b3.pitch_list("c")
b3.out("G3")

# 4. BAL #10 Adam Jones (X - 13 - X)
b3.new_ab()
b3.pitch_list("b b")
b3.out("G5-3")

# 5. BAL #19 Chris Davis (X - 13 - X)
b3.new_ab()
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #30 Chris Tillman
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.out("(F)P5")

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("c b b s s")
t4.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("b c b f b b")
t4.reach("BB")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t4.new_ab()
t4.pitch_list("f b b c f f b f f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 6. BAL #32 Matt Wieters (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f")
b4.out("F7")

# 7. BAL #2  J.J. Hardy (X - X - X)
b4.new_ab()
b4.pitch_list("f b b b b")
b4.reach("BB")
b4.advance(2, "51 1B")
b4.advance(3, "1 1B")
b4.thrown_out(4, "1 9-2", 2, 41)

# 8. BAL #51 Henry Urrutia (X - X - 2)
b4.new_ab()
b4.pitch_list("b f f b")
b4.hit(1)
b4.advance(3, "1 9-2")

# 9. BAL #1  Brian Roberts (X - 2 - 51)
b4.new_ab()
b4.pitch_list("b c b")
b4.hit(1)

# 1. BAL #9  Nate McLouth (51 - X - 1)
b4.new_ab()
b4.pitch_list("1")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #30 Chris Tillman
t5 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("F8")

# 9. BOS #10 Jose Iglesias (X - X - X)
t5.new_ab()
t5.pitch_list("c s b s")
t5.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(2)

# 2. BOS #18 Shane Victorino (X - 2 - X)
t5.new_ab()
t5.pitch_list("c s d b f b f")
t5.out("L8")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 2. BAL #13 Manny Machado (X - X - X)
b5.new_ab()
b5.pitch_list("b f b f")
b5.out("F9")

# 3. BAL #21 Nick Markakis (X - X - X)
b5.new_ab()
b5.pitch_list("b b c b")
b5.out("(F)P5")

# 4. BAL #10 Adam Jones (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(4)

# 5. BAL #19 Chris Davis (X - X - X)
b5.new_ab()
b5.pitch_list("b f s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #30 Chris Tillman
t6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f b")
t6.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("c s b f b f f f b t")
t6.out("KT")

# 5. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("c b b s s")
t6.out("K")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 6. BAL #32 Matt Wieters (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("(F)P5")

# 7. BAL #2  J.J. Hardy (X - X - X)
b6.new_ab()
b6.pitch_list("c b b")
b6.out("L8")

# 8. BAL #51 Henry Urrutia (X - X - X)
b6.new_ab()
b6.error(1)
b6.reach("E1", end_base=2)

# 9. BAL #1  Brian Roberts (X - 51 - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("(F)P5")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #30 Chris Tillman
t7 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("f b s s")
t7.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.out("G5-3")

# 8. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("c f f b")
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #41 John Lackey
b7 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
b7.new_ab()
b7.pitch_list("b c b")
b7.out("L4")

# 2. BAL #13 Manny Machado (X - X - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.hit(4)

# Pitching change (BOS): #66 Drake Britton replaces #41 John Lackey
b7.pitching_substitution(66)

# 3. BAL #21 Nick Markakis (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G3")

# 4. BAL #10 Adam Jones (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #29 Tommy Hunter
t8 = game.new_inning()

# Pitching change (BAL): #29 Tommy Hunter replaces #30 Chris Tillman
t8.pitching_substitution(29)

# 9. BOS #10 Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.hit(1)
t8.thrown_out(2, "15 FC5-4", 3, 29)

# 2. BOS #18 Shane Victorino (X - X - 2)
t8.new_ab()
t8.pitch_list("b")
t8.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t8.new_ab()
t8.pitch_list("c 1 b b")
t8.reach("FC5-4")


# Bot 8th
# Pitching: BOS #66 Drake Britton
b8 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
b8.new_ab()
b8.pitch_list("c b s c")
b8.out("!K")

# Pitching change (BOS): #65 Jose De La Torre replaces #66 Drake Britton
b8.pitching_substitution(65)

# 6. BAL #32 Matt Wieters (X - X - X)
b8.new_ab()
b8.pitch_list("f b s b")
b8.out("G4-3")

# 7. BAL #2  J.J. Hardy (X - X - X)
b8.new_ab()
b8.pitch_list("c f b")
b8.hit(4)

# 8. BAL #51 Henry Urrutia (X - X - X)
b8.new_ab()
b8.out("L7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #43 Jim Johnson
t9 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #29 Tommy Hunter
t9.pitching_substitution(43)

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.hit(1)
t9.thrown_out(2, "12 DP5-4-3", 1, 43)

# 5. BOS #12 Mike Napoli (X - X - 34)
t9.new_ab()
t9.pitch_list("c")
t9.out("DP5-4-3")

# 6. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("f c s")
t9.out("K")

# Winning team: BAL
# WP: BAL #30 Chris Tillman
game.winning_pitcher(30)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
