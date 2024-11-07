import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2013-06-15
# https://www.baseball-reference.com/boxes/BAL/BAL201306150.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2013/06/15/347759/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-15 16:06-18:54",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "42,422",
        "temp": "81F, Partly Cloudy",
        "wind": "5mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                37: "Mike Carp",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                3: "David Ross",
                16: "Will Middlebrooks",
                29: "Daniel Nava",
                12: "Mike Napoli",
                # Bullpen
                40: "Andrew Bailey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                62: "Rubby De La Rosa",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [37, "3"],
                [5, "7"],
                [39, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [3, "C"],
                [16, "3B"],
                [29, "LF"],
                [12, "1B"],
            ],
            "bullpen": [40, 56, 30, 32, 19, 62, 31, 36, 22, 46],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 38,
            "roster": {
                # Lineup
                9: "Nate McLouth",
                13: "Manny Machado",
                21: "Nick Markakis",
                10: "Adam Jones",
                19: "Chris Davis",
                32: "Matt Wieters",
                2: "J.J. Hardy",
                3: "Ryan Flaherty",
                31: "Taylor Teagarden",
                # Starting pitcher
                38: "Freddy Garcia",
                # Bench
                28: "Steve Pearce",
                36: "Chris Dickerson",
                12: "Alexi Casilla",
                35: "Danny Valencia",
                # Bullpen
                50: "Miguel González",
                30: "Chris Tillman",
                40: "Troy Patton",
                66: "T.J. McFarland",
                47: "Pedro Strop",
                29: "Tommy Hunter",
                56: "Darren O'Day",
                39: "Jason Hammel",
                17: "Brian Matusz",
                34: "Jake Arrieta",
                43: "Jim Johnson",
            },
            "lefties": [40, 66, 17],
            "lineup": [
                [9, "7"],
                [13, "5"],
                [21, "9"],
                [10, "8"],
                [19, "3"],
                [32, "0"],
                [2, "6"],
                [3, "4"],
                [31, "2"],
            ],
            "bench": [
                [28, "1B"],
                [36, "LF"],
                [12, "2B"],
                [35, "3B"],
            ],
            "bullpen": [50, 30, 40, 66, 47, 29, 56, 39, 17, 34, 43],
        },
        "umpires": {
            "HP": "Jeff Nelson",
            "1B": "David Rackley",
            "2B": "Jim Joyce",
            "3B": "Cory Blaser",
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
# Pitching: BAL #38 Freddy Garcia
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c f b")
t1.out("P6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("P6")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(4, "13 2B")

# 2. BAL #13 Manny Machado (X - X - 9)
b1.new_ab()
b1.pitch_list("1 b f")
b1.hit(2, rbis=1)
b1.advance(3, "21 1B")
b1.advance(4, "10 1B")

# 3. BAL #21 Nick Markakis (X - 13 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("s")
b1.hit(1)
b1.advance(2, "10 WP")
b1.advance(3, "19 G4-3")

# 4. BAL #10 Adam Jones (13 - X - 21)
b1.new_ab(is_risp=True)
b1.pitch_list("f b s b")
b1.wp()
b1.hit(1, rbis=1)
b1.advance(2, "19 G4-3")

# 5. BAL #19 Chris Davis (X - 21 - 10)
b1.new_ab(is_risp=True)
b1.pitch_list("f b c b")
b1.out("G4-3")

# 6. BAL #32 Matt Wieters (21 - 10 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b f c f")
b1.out("P6")

# 7. BAL #2  J.J. Hardy (21 - 10 - X)
b1.new_ab(is_risp=True)
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #38 Freddy Garcia
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(3)

# 5. BOS #37 Mike Carp (34 - X - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b d b c f b")
t2.reach("BB")

# 6. BOS #5  Jonny Gomes (34 - X - 37)
t2.new_ab(is_risp=True)
t2.pitch_list("c d")
t2.out("(F)P3")

# 7. BOS #39 Jarrod Saltalamacchia (34 - X - 37)
t2.new_ab(is_risp=True)
t2.pitch_list("b b c f s")
t2.out("K")

# 8. BOS #7  Stephen Drew (34 - X - 37)
t2.new_ab(is_risp=True)
t2.pitch_list("b d b c c")
t2.out("P6")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 8. BAL #3  Ryan Flaherty (X - X - X)
b2.new_ab()
b2.pitch_list("b f f b c")
b2.out("!K")

# 9. BAL #31 Taylor Teagarden (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b s")
b2.out("K")

# 1. BAL #9  Nate McLouth (X - X - X)
b2.new_ab()
b2.pitch_list("b b c")
b2.out("G3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #38 Freddy Garcia
t3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t3.new_ab()
t3.pitch_list("c b c")
t3.hit(1)
t3.thrown_out(2, "2 DP4-6-3", 1, 38)

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
t3.new_ab()
t3.pitch_list("1 b b f 1")
t3.out("DP4-6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b t s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 2. BAL #13 Manny Machado (X - X - X)
b3.new_ab()
b3.hit(1)
b3.thrown_out(2, "21 CS", 1, 41)

# 3. BAL #21 Nick Markakis (X - X - 13)
b3.new_ab()
b3.pitch_list("b f b s b")
b3.out("P6")

# 4. BAL #10 Adam Jones (X - X - X)
b3.new_ab()
b3.out("P4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #38 Freddy Garcia
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("b c b c f")
t4.hit(1)
t4.advance(2, "34 SB")
t4.advance(4, "37 HR")

# 4. BOS #34 David Ortiz (X - X - 15)
t4.new_ab()
t4.pitch_list("f s 1 s")
t4.out("K")

# 5. BOS #37 Mike Carp (X - 15 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b f b b")
t4.hit(4, rbis=2)

# 6. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.hit(1)
t4.advance(4, "7 2B")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 5)
t4.new_ab()
t4.out("F8")

# 8. BOS #7  Stephen Drew (X - X - 5)
t4.new_ab()
t4.hit(2, rbis=1)
t4.advance(3, "T")

# 9. BOS #10 Jose Iglesias (7 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c f f f b")
t4.out("G5-3")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
b4.new_ab()
b4.pitch_list("b f f c")
b4.out("!K")

# 6. BAL #32 Matt Wieters (X - X - X)
b4.new_ab()
b4.pitch_list("b b c c b f")
b4.out("G4-3")

# 7. BAL #2  J.J. Hardy (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b s b")
b4.reach("BB")

# 8. BAL #3  Ryan Flaherty (X - X - 2)
b4.new_ab()
b4.pitch_list("b f b")
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #38 Freddy Garcia
t5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.hit(1)
t5.advance(2, "18 SB")
t5.advance(3, "18 SAC1-3")
t5.advance(4, "15 G6-3")

# 2. BOS #18 Shane Victorino (X - X - 2)
t5.new_ab(is_risp=True)
t5.pitch_list("b 1 1 b b c")
t5.out("SAC1-3")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c b")
t5.out("G6-3", rbis=1)

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("F7")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 9. BAL #31 Taylor Teagarden (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1)
b5.advance(3, "9 E4")

# 1. BAL #9  Nate McLouth (X - X - 31)
b5.new_ab()
b5.pitch_list("d b c s d")
b5.error(4)
b5.reach("E4")
b5.thrown_out(2, "13 CS", 1, 41)

# 2. BAL #13 Manny Machado (31 - X - 9)
b5.new_ab(is_risp=True)
b5.pitch_list("c b f")
b5.out("G1-3")

# 3. BAL #21 Nick Markakis (31 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("f")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #38 Freddy Garcia
t6 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
t6.new_ab()
t6.out("G3")

# 6. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("c s b")
t6.hit(4)

# Pitching change (BAL): #66 T.J. McFarland replaces #38 Freddy Garcia
t6.pitching_substitution(66)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("c f s")
t6.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("c s c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
b6.new_ab()
b6.pitch_list("b b f f s")
b6.out("K")

# 5. BAL #19 Chris Davis (X - X - X)
b6.new_ab()
b6.out("F8")

# 6. BAL #32 Matt Wieters (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #66 T.J. McFarland
t7 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t7.new_ab()
t7.pitch_list("c s s")
t7.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b")
t7.out("F7")

# 2. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.pitch_list("c b f f b")
t7.hit(1)
t7.advance(2, "15 SB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t7.new_ab(is_risp=True)
t7.pitch_list("b 1 c")
t7.out("G1-3")


# Bot 7th
# Pitching: BOS #41 John Lackey
b7 = game.new_inning()

# 7. BAL #2  J.J. Hardy (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(1)
b7.thrown_out(1, "3 DP3", 2, 41)

# 8. BAL #3  Ryan Flaherty (X - X - 2)
b7.new_ab()
b7.pitch_list("1 b")
b7.out("DP3")

# 9. BAL #31 Taylor Teagarden (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #66 T.J. McFarland
t8 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.out("F7")

# 5. BOS #37 Mike Carp (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G6-3")

# 6. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("s b s b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #19 Koji Uehara
b8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #41 John Lackey
b8.pitching_substitution(19)

# 1. BAL #9  Nate McLouth (X - X - X)
b8.new_ab()
b8.pitch_list("c c b f f t")
b8.out("KT")

# 2. BAL #13 Manny Machado (X - X - X)
b8.new_ab()
b8.pitch_list("b c s b t")
b8.out("KT")

# 3. BAL #21 Nick Markakis (X - X - X)
b8.new_ab()
b8.pitch_list("b c f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #66 T.J. McFarland
t9 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("b s")
t9.out("G4-3")

# 8. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("c f c")
t9.out("!K")

# 9. BOS #10 Jose Iglesias (X - X - X)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")
t9.thrown_out(2, "2 CS", 3, 66)

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
t9.new_ab()
t9.pitch_list("1 1 1 c")
t9.no_ab("CS")


# Bot 9th
# Pitching: BOS #40 Andrew Bailey
b9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
b9.pitching_substitution(40)

# 4. BAL #10 Adam Jones (X - X - X)
b9.new_ab()
b9.pitch_list("c s b b f b")
b9.hit(1)
b9.advance(4, "32 HR")

# 5. BAL #19 Chris Davis (X - X - 10)
b9.new_ab()
b9.pitch_list("f f s")
b9.out("K")

# 6. BAL #32 Matt Wieters (X - X - 10)
b9.new_ab()
b9.pitch_list("b b f")
b9.hit(4, rbis=2)

# 7. BAL #2  J.J. Hardy (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
# Offensive change (BAL): Pinch-runner #12 Alexi Casilla replaces #2 J.J. Hardy
b9.offensive_substitution(7, 12, "PR")
b9.atbase("PR")
b9.thrown_out(1, "3 DP9-3", 3, 40)

# 8. BAL #3  Ryan Flaherty (X - X - 2)
b9.new_ab()
b9.pitch_list("1 f b c")
b9.out("DP9-3")

# Winning team: BOS
# WP: BOS #41 John Lackey
game.winning_pitcher(41, is_away_team=True)
# SV: BOS #40 Andrew Bailey
game.save_pitcher(40, is_away_team=True)

# Loser team: BAL
# LP: BAL #38 Freddy Garcia
game.losing_pitcher(38)

# print(game)
game.generate_scorecard()
