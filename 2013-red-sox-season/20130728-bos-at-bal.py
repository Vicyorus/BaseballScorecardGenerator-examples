import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2013-07-28
# https://www.baseball-reference.com/boxes/BAL/BAL201307280.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2013/07/28/348305/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-28 13:39-16:37",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "32,891",
        "temp": "79F, Overcast",
        "wind": "5mph, Out To RF",
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
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                29: "Daniel Nava",
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
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [39, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [29, "LF"],
                [5, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [65, 41, 67, 32, 66, 36, 19, 38, 54, 22, 46],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 39,
            "roster": {
                # Lineup
                21: "Nick Markakis",
                13: "Manny Machado",
                19: "Chris Davis",
                10: "Adam Jones",
                32: "Matt Wieters",
                2: "J.J. Hardy",
                1: "Brian Roberts",
                25: "L.J. Hoes",
                31: "Taylor Teagarden",
                # Starting pitcher
                39: "Jason Hammel",
                # Bench
                3: "Ryan Flaherty",
                9: "Nate McLouth",
                51: "Henry Urrutia",
                12: "Alexi Casilla",
                # Bullpen
                50: "Miguel González",
                30: "Chris Tillman",
                40: "Troy Patton",
                66: "T.J. McFarland",
                34: "Scott Feldman",
                57: "Francisco Rodríguez",
                29: "Tommy Hunter",
                56: "Darren O'Day",
                17: "Brian Matusz",
                43: "Jim Johnson",
                16: "Wei-Yin Chen",
            },
            "lefties": [40, 66, 17, 16],
            "lineup": [
                [21, "9"],
                [13, "5"],
                [19, "3"],
                [10, "8"],
                [32, "0"],
                [2, "6"],
                [1, "4"],
                [25, "7"],
                [31, "2"],
            ],
            "bench": [
                [3, "2B"],
                [9, "CF"],
                [51, "OF"],
                [12, "2B"],
            ],
            "bullpen": [50, 30, 40, 66, 34, 57, 29, 56, 17, 43, 16],
        },
        "umpires": {
            "HP": "Mike Estabrook",
            "1B": "Mike Winters",
            "2B": "Laz Diaz",
            "3B": "Tim Timmons",
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
# Pitching: BAL #39 Jason Hammel
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b b c")
t1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b b c b b")
t1.reach("BB")
t1.advance(3, "34 1B")
t1.advance(4, "12 2B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t1.new_ab()
t1.pitch_list("1 b c 1 f f 1 b f b")
t1.out("F8")

# 4. BOS #34 David Ortiz (X - X - 18)
t1.new_ab()
t1.pitch_list("b f f")
t1.hit(1)
t1.advance(3, "12 2B")

# 5. BOS #12 Mike Napoli (18 - X - 34)
t1.new_ab(is_risp=True)
t1.pitch_list("b b")
t1.hit(2, rbis=1)

# 6. BOS #37 Mike Carp (34 - 12 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("s f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. BAL #21 Nick Markakis (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c s f")
b1.hit(1)
b1.advance(2, "13 G6-3")

# 2. BAL #13 Manny Machado (X - X - 21)
b1.new_ab()
b1.pitch_list("b")
b1.out("G6-3")

# 3. BAL #19 Chris Davis (X - 21 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("f b f b s")
b1.out("K")

# 4. BAL #10 Adam Jones (X - 21 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b s f b f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #39 Jason Hammel
t2 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b f c f")
t2.out("G3")

# 8. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("b c c c")
t2.out("!K")

# 9. BOS #10 Jose Iglesias (X - X - X)
t2.new_ab()
t2.pitch_list("c c b")
t2.out("G5-3")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 5. BAL #32 Matt Wieters (X - X - X)
b2.new_ab()
b2.pitch_list("f")
b2.out("G6-3")

# 6. BAL #2  J.J. Hardy (X - X - X)
b2.new_ab()
b2.pitch_list("c c s")
b2.out("K")

# 7. BAL #1  Brian Roberts (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #39 Jason Hammel
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)
t3.advance(4, "34 HR")

# 2. BOS #18 Shane Victorino (X - X - 2)
t3.new_ab()
t3.pitch_list("c 1 p 1")
t3.out("P5")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t3.new_ab()
t3.pitch_list("p")
t3.out("F8")

# 4. BOS #34 David Ortiz (X - X - 2)
t3.new_ab()
t3.pitch_list("b b")
t3.hit(4, rbis=2)

# 5. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("b b c f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 8. BAL #25 L.J. Hoes (X - X - X)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")

# 9. BAL #31 Taylor Teagarden (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.out("F9")

# 1. BAL #21 Nick Markakis (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.out("G3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #39 Jason Hammel
t4 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("b s b b b")
t4.reach("BB")
t4.advance(2, "7 BB")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t4.new_ab()
t4.pitch_list("f b")
t4.out("L8")

# 8. BOS #7  Stephen Drew (X - X - 37)
t4.new_ab()
t4.pitch_list("b b b b")
t4.reach("BB")

# 9. BOS #10 Jose Iglesias (X - 37 - 7)
t4.new_ab(is_risp=True)
t4.pitch_list("c")
t4.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - 37 - 7)
t4.new_ab(is_risp=True)
t4.pitch_list("b s f")
t4.out("F8")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 2. BAL #13 Manny Machado (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G5-3")

# 3. BAL #19 Chris Davis (X - X - X)
b4.new_ab()
b4.pitch_list("s f c")
b4.out("!K")

# 4. BAL #10 Adam Jones (X - X - X)
b4.new_ab()
b4.pitch_list("b c b")
b4.hit(1)
b4.advance(2, "32 BB")

# 5. BAL #32 Matt Wieters (X - X - 10)
b4.new_ab()
b4.pitch_list("b b b c f f b")
b4.reach("BB")

# 6. BAL #2  J.J. Hardy (X - 10 - 32)
b4.new_ab(is_risp=True)
b4.pitch_list("c")
b4.out("(F)P3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #39 Jason Hammel
t5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c b")
t5.reach("BB")
t5.thrown_out(2, "15 CS", 1, 39)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t5.new_ab()
t5.pitch_list("b b b c f f b")
t5.reach("BB")
t5.advance(2, "34 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
t5.new_ab()
t5.pitch_list("f 1 b")
t5.hit(1)
t5.thrown_out(2, "12 DP5-4-3", 2, 39)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t5.new_ab(is_risp=True)
t5.out("DP5-4-3")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 7. BAL #1  Brian Roberts (X - X - X)
b5.new_ab()
b5.pitch_list("c c b f b f f f s")
b5.out("K")

# 8. BAL #25 L.J. Hoes (X - X - X)
b5.new_ab()
b5.out("G5-3")

# 9. BAL #31 Taylor Teagarden (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.hit(1)
b5.advance(2, "21 BB")

# 1. BAL #21 Nick Markakis (X - X - 31)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")

# 2. BAL #13 Manny Machado (X - 31 - 21)
b5.new_ab(is_risp=True)
b5.pitch_list("b b f b")
b5.out("L6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #39 Jason Hammel
t6 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("b b s b f")
t6.hit(2)
t6.thrown_out(2, "7 DP4-6", 3, 66)

# Pitching change (BAL): #66 T.J. McFarland replaces #39 Jason Hammel
t6.pitching_substitution(66)

# 8. BOS #7  Stephen Drew (X - 39 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b c s f f f d")
t6.out("DP4-6")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 3. BAL #19 Chris Davis (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.error(4)
b6.reach("E4")
b6.advance(2, "10 1B")

# 4. BAL #10 Adam Jones (X - X - 19)
b6.new_ab()
b6.hit(1)
b6.thrown_out(2, "2 DP5-4-3", 2, 31)

# 5. BAL #32 Matt Wieters (X - 19 - 10)
b6.new_ab(is_risp=True)
b6.pitch_list("b b f b f f s")
b6.out("K")

# 6. BAL #2  J.J. Hardy (X - 19 - 10)
b6.new_ab(is_risp=True)
b6.pitch_list("c b f f b b")
b6.out("DP5-4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #66 T.J. McFarland
t7 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("L8")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("c f f b")
t7.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.pitch_list("b f f")
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# 7. BAL #1  Brian Roberts (X - X - X)
b7.new_ab()
b7.out("(F)P3")

# 8. BAL #25 L.J. Hoes (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G4-3")

# 9. BAL #31 Taylor Teagarden (X - X - X)
b7.new_ab()
b7.pitch_list("f s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #66 T.J. McFarland
t8 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c s")
t8.out("L7")

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(3, "12 2B")
t8.advance(4, "39 1B")

# 5. BOS #12 Mike Napoli (X - X - 34)
t8.new_ab()
t8.pitch_list("b c s b f f f d")
t8.hit(2)
t8.advance(4, "39 1B")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 6th
t8.offensive_substitution(6, 5, "PH")

# 6. BOS #5  Jonny Gomes (34 - 12 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("i i i i")
t8.reach("IBB")
t8.advance(2, "39 1B")

# 7. BOS #39 Jarrod Saltalamacchia (34 - 12 - 5)
t8.new_ab(is_risp=True)
t8.hit(1, rbis=2)

# 8. BOS #7  Stephen Drew (X - 5 - 39)
t8.new_ab(is_risp=True)
t8.pitch_list("s c b f s")
t8.out("K")

# 9. BOS #10 Jose Iglesias (X - 5 - 39)
t8.new_ab(is_risp=True)
t8.pitch_list("d f")
t8.out("G1-3")


# Bot 8th
# Pitching: BOS #38 Matt Thornton
b8 = game.new_inning()

# Pitching change (BOS): #38 Matt Thornton replaces #31 Jon Lester
b8.pitching_substitution(38)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
b8.defensive_switch(5, "7")

# 1. BAL #21 Nick Markakis (X - X - X)
b8.new_ab()
b8.pitch_list("c b b f")
b8.hit(1)
b8.thrown_out(2, "13 DP5-4-3", 1, 38)

# 2. BAL #13 Manny Machado (X - X - 21)
b8.new_ab()
b8.pitch_list("b")
b8.out("DP5-4-3")

# 3. BAL #19 Chris Davis (X - X - X)
b8.new_ab()
b8.pitch_list("s f b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #29 Tommy Hunter
t9 = game.new_inning()

# Pitching change (BAL): #29 Tommy Hunter replaces #66 T.J. McFarland
t9.pitching_substitution(29)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.hit(1)
t9.thrown_out(2, "15 DP4-6-3", 2, 29)

# 2. BOS #18 Shane Victorino (X - X - 2)
t9.new_ab()
t9.pitch_list("b b")
t9.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t9.new_ab()
t9.pitch_list("b f b")
t9.out("DP4-6-3")


# Bot 9th
# Pitching: BOS #54 Pedro Beato
b9 = game.new_inning()

# Pitching change (BOS): #54 Pedro Beato replaces #38 Matt Thornton
b9.pitching_substitution(54)

# 4. BAL #10 Adam Jones (X - X - X)
b9.new_ab()
b9.pitch_list("c f b f")
b9.out("G5-3")

# 5. BAL #32 Matt Wieters (X - X - X)
b9.new_ab()
b9.pitch_list("b c f b b")
b9.out("F8")

# 6. BAL #2  J.J. Hardy (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("P4")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31, is_away_team=True)

# Loser team: BAL
# LP: BAL #39 Jason Hammel
game.losing_pitcher(39)

# print(game)
game.generate_scorecard()
