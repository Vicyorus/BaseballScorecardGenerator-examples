import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2013-06-14
# https://www.baseball-reference.com/boxes/BAL/BAL201306140.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2013/06/14/347744/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-14 19:07-21:50",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "39,158",
        "temp": "79F, Partly Cloudy",
        "wind": "8mph, In From LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                37: "Mike Carp",
                29: "Daniel Nava",
                10: "Jose Iglesias",
                16: "Will Middlebrooks",
                3: "David Ross",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                62: "Rubby De La Rosa",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [37, "3"],
                [29, "7"],
                [10, "6"],
                [16, "5"],
                [3, "2"],
            ],
            "bench": [
                [7, "SS"],
                [39, "C"],
                [12, "1B"],
                [5, "LF"],
            ],
            "bullpen": [40, 41, 56, 30, 32, 19, 62, 31, 36, 22],
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
                36: "Chris Dickerson",
                3: "Ryan Flaherty",
                # Starting pitcher
                30: "Chris Tillman",
                # Bench
                28: "Steve Pearce",
                31: "Taylor Teagarden",
                12: "Alexi Casilla",
                35: "Danny Valencia",
                # Bullpen
                50: "Miguel González",
                40: "Troy Patton",
                66: "T.J. McFarland",
                47: "Pedro Strop",
                38: "Freddy Garcia",
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
                [32, "2"],
                [2, "6"],
                [36, "0"],
                [3, "4"],
            ],
            "bench": [
                [28, "1B"],
                [31, "C"],
                [12, "2B"],
                [35, "3B"],
            ],
            "bullpen": [50, 40, 66, 47, 38, 29, 56, 39, 17, 34, 43],
        },
        "umpires": {
            "HP": "Cory Blaser",
            "1B": "Jeff Nelson",
            "2B": "David Rackley",
            "3B": "Jim Joyce",
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
t1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.hit(1)
t1.advance(2, "34 BB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t1.new_ab()
t1.pitch_list("c 1 f f f")
t1.out("F9")

# 4. BOS #34 David Ortiz (X - X - 18)
t1.new_ab()
t1.pitch_list("c b b 1 b b")
t1.reach("BB")

# 5. BOS #37 Mike Carp (X - 18 - 34)
t1.new_ab()
t1.pitch_list("s b b")
t1.out("F9")


# Bot 1st
# Pitching: BOS #46 Ryan Dempster
b1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("F7")

# 2. BAL #13 Manny Machado (X - X - X)
b1.new_ab()
b1.pitch_list("b f b")
b1.hit(2)
b1.advance(3, "21 G3")

# 3. BAL #21 Nick Markakis (X - 13 - X)
b1.new_ab()
b1.pitch_list("c b d")
b1.out("G3")

# 4. BAL #10 Adam Jones (13 - X - X)
b1.new_ab()
b1.pitch_list("d b b c")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #30 Chris Tillman
t2 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b f f b b")
t2.reach("BB")

# 7. BOS #10 Jose Iglesias (X - X - 29)
t2.new_ab()
t2.pitch_list("l f")
t2.out("L5")

# 8. BOS #16 Will Middlebrooks (X - X - 29)
t2.new_ab()
t2.pitch_list("t f f")
t2.out("L9")

# 9. BOS #3  David Ross (X - X - 29)
t2.new_ab()
t2.pitch_list("c b f f")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #46 Ryan Dempster
b2 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(4)

# 6. BAL #32 Matt Wieters (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F9")

# 7. BAL #2  J.J. Hardy (X - X - X)
b2.new_ab()
b2.pitch_list("b f c b")
b2.out("G5-3")

# 8. BAL #36 Chris Dickerson (X - X - X)
b2.new_ab()
b2.pitch_list("b f c f f c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #30 Chris Tillman
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c b")
t3.reach("BB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t3.new_ab()
t3.out("(F)P3")

# 4. BOS #34 David Ortiz (X - X - 18)
t3.new_ab()
t3.pitch_list("1 d")
t3.out("F7")


# Bot 3rd
# Pitching: BOS #46 Ryan Dempster
b3 = game.new_inning()

# 9. BAL #3  Ryan Flaherty (X - X - X)
b3.new_ab()
b3.out("G4-3")

# 1. BAL #9  Nate McLouth (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b f b")
b3.reach("BB")
b3.advance(2, "13 1B")
b3.advance(3, "21 F8")
b3.advance(4, "10 1B")

# 2. BAL #13 Manny Machado (X - X - 9)
b3.new_ab()
b3.pitch_list("1 c c d 1 1")
b3.hit(1)
b3.advance(2, "10 1B")

# 3. BAL #21 Nick Markakis (X - 9 - 13)
b3.new_ab()
b3.pitch_list("c b")
b3.out("F8")

# 4. BAL #10 Adam Jones (9 - X - 13)
b3.new_ab()
b3.hit(1, rbis=1)

# 5. BAL #19 Chris Davis (X - 13 - 10)
b3.new_ab()
b3.pitch_list("b c f")
b3.out("L4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #30 Chris Tillman
t4 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("b f b s b b")
t4.reach("BB")
t4.advance(2, "29 G3")
t4.advance(3, "10 1B")

# 6. BOS #29 Daniel Nava (X - X - 37)
t4.new_ab()
t4.pitch_list("b f b f")
t4.out("G3")

# 7. BOS #10 Jose Iglesias (X - 37 - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)

# 8. BOS #16 Will Middlebrooks (37 - X - 10)
t4.new_ab()
t4.pitch_list("b b c b 1")
t4.out("F9")

# 9. BOS #3  David Ross (37 - X - 10)
t4.new_ab()
t4.pitch_list("b s f 1 s")
t4.out("K")


# Bot 4th
# Pitching: BOS #46 Ryan Dempster
b4 = game.new_inning()

# 6. BAL #32 Matt Wieters (X - X - X)
b4.new_ab()
b4.pitch_list("f b b")
b4.out("G1-3")

# 7. BAL #2  J.J. Hardy (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b c b")
b4.reach("BB")
b4.advance(2, "36 WP")

# 8. BAL #36 Chris Dickerson (X - X - 2)
b4.new_ab()
b4.pitch_list("b c b b s s")
b4.wp()
b4.out("K")

# 9. BAL #3  Ryan Flaherty (X - 2 - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("G3-1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #30 Chris Tillman
t5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.pitch_list("b c c b f s")
t5.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("b b c b")
t5.out("G6-3")


# Bot 5th
# Pitching: BOS #46 Ryan Dempster
b5 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")
b5.advance(2, "21 SB")
b5.advance(3, "21 G3")

# 2. BAL #13 Manny Machado (X - X - 9)
b5.new_ab()
b5.pitch_list("1 c b 1 f f b t")
b5.out("KT")

# 3. BAL #21 Nick Markakis (X - X - 9)
b5.new_ab()
b5.pitch_list("p")
b5.out("G3")

# 4. BAL #10 Adam Jones (9 - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #30 Chris Tillman
t6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("b c b b")
t6.out("F9")

# 5. BOS #37 Mike Carp (X - X - X)
t6.new_ab()
t6.pitch_list("b b c c b")
t6.out("F8")

# 6. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #46 Ryan Dempster
b6 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
b6.new_ab()
b6.pitch_list("b f s s")
b6.out("K")

# 6. BAL #32 Matt Wieters (X - X - X)
b6.new_ab()
b6.out("G4-3")

# 7. BAL #2  J.J. Hardy (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #30 Chris Tillman
t7 = game.new_inning()

# 7. BOS #10 Jose Iglesias (X - X - X)
t7.new_ab()
t7.pitch_list("c c f")
t7.hit(2)

# Pitching change (BAL): #56 Darren O'Day replaces #30 Chris Tillman
t7.pitching_substitution(56)

# 8. BOS #16 Will Middlebrooks (X - 10 - X)
t7.new_ab()
t7.pitch_list("f b")
t7.out("P4")

# 9. BOS #3  David Ross (X - 10 - X)
t7.new_ab()
t7.pitch_list("s c f b b s")
t7.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - 10 - X)
t7.new_ab()
t7.out("F8")


# Bot 7th
# Pitching: BOS #46 Ryan Dempster
b7 = game.new_inning()

# 8. BAL #36 Chris Dickerson (X - X - X)
b7.new_ab()
b7.pitch_list("f b f f")
b7.out("G4-3")

# 9. BAL #3  Ryan Flaherty (X - X - X)
b7.new_ab()
b7.pitch_list("f")
b7.out("F7")

# 1. BAL #9  Nate McLouth (X - X - X)
b7.new_ab()
b7.pitch_list("b c b")
b7.out("(F)F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #29 Tommy Hunter
t8 = game.new_inning()

# Pitching change (BAL): #29 Tommy Hunter replaces #56 Darren O'Day
t8.pitching_substitution(29)

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("c f f b f")
t8.out("P4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c c")
t8.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b")
t8.out("F8")


# Bot 8th
# Pitching: BOS #46 Ryan Dempster
b8 = game.new_inning()

# 2. BAL #13 Manny Machado (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(2)
b8.advance(3, "21 G4-3")

# 3. BAL #21 Nick Markakis (X - 13 - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G4-3")

# 4. BAL #10 Adam Jones (13 - X - X)
b8.new_ab()
b8.pitch_list("f s b d b f")
b8.out("G4-3")

# 5. BAL #19 Chris Davis (13 - X - X)
b8.new_ab()
b8.pitch_list("i i i i")
b8.reach("IBB")
b8.advance(2, "32 BB")

# 6. BAL #32 Matt Wieters (13 - X - 19)
b8.new_ab()
b8.pitch_list("b c b d b")
b8.reach("BB")

# Pitching change (BOS): #19 Koji Uehara replaces #46 Ryan Dempster
b8.pitching_substitution(19)

# 7. BAL #2  J.J. Hardy (13 - 19 - 32)
b8.new_ab()
b8.pitch_list("c s t")
b8.out("KT")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #43 Jim Johnson
t9 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #29 Tommy Hunter
t9.pitching_substitution(43)

# 5. BOS #37 Mike Carp (X - X - X)
t9.new_ab()
t9.pitch_list("c t b c")
t9.out("!K")

# 6. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.reach("HBP")
t9.thrown_out(2, "10 DP6-4-3", 2, 43)

# 7. BOS #10 Jose Iglesias (X - X - 29)
t9.new_ab()
t9.out("DP6-4-3")

# Winning team: BAL
# WP: BAL #30 Chris Tillman
game.winning_pitcher(30)
# SV: BAL #43 Jim Johnson
game.save_pitcher(43)

# Loser team: BOS
# LP: BOS #46 Ryan Dempster
game.losing_pitcher(46, is_away_team=True)

# print(game)
game.generate_scorecard()
