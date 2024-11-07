import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2013-04-11
# https://www.baseball-reference.com/boxes/BOS/BOS201304110.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2013/04/11/346874/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-11 19:10-22:25",
        "at": "Fenway Park, Boston, MA",
        "att": "27,704",
        "temp": "45F, Cloudy",
        "wind": "5mph, In From RF",
        "away": {
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
                60: "Chris Dickerson",
                12: "Alexi Casilla",
                # Starting pitcher
                30: "Chris Tillman",
                # Bench
                28: "Steve Pearce",
                3: "Ryan Flaherty",
                31: "Taylor Teagarden",
                14: "Nolan Reimold",
                # Bullpen
                50: "Miguel González",
                40: "Troy Patton",
                66: "T.J. McFarland",
                47: "Pedro Strop",
                29: "Tommy Hunter",
                56: "Darren O'Day",
                39: "Jason Hammel",
                17: "Brian Matusz",
                34: "Jake Arrieta",
                43: "Jim Johnson",
                16: "Wei-Yin Chen",
            },
            "lefties": [40, 66, 17, 16],
            "lineup": [
                [9, "7"],
                [13, "5"],
                [21, "0"],
                [10, "8"],
                [19, "3"],
                [32, "2"],
                [2, "6"],
                [60, "9"],
                [12, "4"],
            ],
            "bench": [
                [28, "1B"],
                [3, "2B"],
                [31, "C"],
                [14, "LF"],
            ],
            "bullpen": [50, 40, 66, 47, 29, 56, 39, 17, 34, 43, 16],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 91,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                16: "Will Middlebrooks",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                44: "Jackie Bradley Jr.",
                # Starting pitcher
                91: "Alfredo Aceves",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                52: "Joel Hanrahan",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [16, "5"],
                [29, "0"],
                [39, "2"],
                [7, "6"],
                [44, "7"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [63, 40, 30, 52, 31, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Jim Joyce",
            "1B": "Jim Wolf",
            "2B": "Ed Hickox",
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
# Pitching: BOS #91 Alfredo Aceves
t1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t1.new_ab()
t1.out("F8")

# 2. BAL #13 Manny Machado (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.hit(2)
t1.thrown_out(3, "9-4-5", 2, 91)

# 3. BAL #21 Nick Markakis (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("F7")


# Bot 1st
# Pitching: BAL #30 Chris Tillman
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b b f c b")
b1.hit(1)
b1.thrown_out(2, "18 FC4-6", 1, 30)

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab()
b1.pitch_list("b c b 1 b 1")
b1.reach("FC4-6")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b1.new_ab()
b1.pitch_list("c b d f 1 t")
b1.out("KT")

# 4. BOS #12 Mike Napoli (X - X - 18)
b1.new_ab()
b1.pitch_list("c b b")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #91 Alfredo Aceves
t2 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
t2.new_ab()
t2.out("G1-3")

# 5. BAL #19 Chris Davis (X - X - X)
t2.new_ab()
t2.pitch_list("b b b")
t2.hit(4)

# 6. BAL #32 Matt Wieters (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")

# 7. BAL #2  J.J. Hardy (X - X - 32)
t2.new_ab()
t2.pitch_list("c b c s")
t2.out("K")

# 8. BAL #60 Chris Dickerson (X - X - 32)
t2.new_ab()
t2.pitch_list("f b 1 b f t")
t2.out("KT")


# Bot 2nd
# Pitching: BAL #30 Chris Tillman
b2 = game.new_inning()

# 5. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.out("L9")

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c f s")
b2.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #91 Alfredo Aceves
t3 = game.new_inning()

# 9. BAL #12 Alexi Casilla (X - X - X)
t3.new_ab()
t3.out("B1-3")

# 1. BAL #9  Nate McLouth (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.thrown_out(2, "13 FC5-4", 2, 91)

# 2. BAL #13 Manny Machado (X - X - 9)
t3.new_ab()
t3.pitch_list("b 1 b")
t3.reach("FC5-4")

# 3. BAL #21 Nick Markakis (X - X - 13)
t3.new_ab()
t3.pitch_list("1 f")
t3.out("G1-3")


# Bot 3rd
# Pitching: BAL #30 Chris Tillman
b3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("b b c b b")
b3.reach("BB")
b3.advance(3, "18 1B")
b3.advance(4, "15 1B")

# 9. BOS #44 Jackie Bradley Jr. (X - X - 7)
b3.new_ab()
b3.pitch_list("b 1 b c 1 1 f s")
b3.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b3.new_ab()
b3.pitch_list("f f b d b c")
b3.out("!K")

# 2. BOS #18 Shane Victorino (X - X - 7)
b3.new_ab()
b3.pitch_list("b c")
b3.hit(1)
b3.advance(2, "15 1B")
b3.advance(4, "12 1B")

# 3. BOS #15 Dustin Pedroia (7 - X - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("c b 1 f")
b3.hit(1, rbis=1)
b3.advance(3, "12 1B")

# 4. BOS #12 Mike Napoli (X - 18 - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("f f b f f b b f")
b3.hit(1, rbis=1)

# 5. BOS #16 Will Middlebrooks (15 - X - 12)
b3.new_ab(is_risp=True)
b3.pitch_list("f c f")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #91 Alfredo Aceves
t4 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("c c f b f f b f s")
t4.out("K")

# 5. BAL #19 Chris Davis (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c b")
t4.reach("BB")
t4.advance(3, "2 1B")

# 6. BAL #32 Matt Wieters (X - X - 19)
t4.new_ab()
t4.pitch_list("b")
t4.out("F7")

# 7. BAL #2  J.J. Hardy (X - X - 19)
t4.new_ab()
t4.pitch_list("b c")
t4.hit(1)
t4.advance(2, "60 BB")

# 8. BAL #60 Chris Dickerson (19 - X - 2)
t4.new_ab(is_risp=True)
t4.pitch_list("b f 1 s b d f b")
t4.reach("BB")

# 9. BAL #12 Alexi Casilla (19 - 2 - 60)
t4.new_ab(is_risp=True)
t4.pitch_list("c f c")
t4.out("!K")


# Bot 4th
# Pitching: BAL #30 Chris Tillman
b4 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("b b f")
b4.out("F7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("c b s c")
b4.out("!K")

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("f b c b b b")
b4.reach("BB")
b4.thrown_out(2, "44 FC5-4", 3, 30)

# 9. BOS #44 Jackie Bradley Jr. (X - X - 7)
b4.new_ab()
b4.pitch_list("b f s")
b4.reach("FC5-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #91 Alfredo Aceves
t5 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G4-3")

# 2. BAL #13 Manny Machado (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)
t5.advance(2, "21 G5-3")
t5.advance(4, "10 1B")

# 3. BAL #21 Nick Markakis (X - X - 13)
t5.new_ab()
t5.pitch_list("d c 1 d f b")
t5.out("G5-3")

# 4. BAL #10 Adam Jones (X - 13 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b c")
t5.hit(1, rbis=1)

# 5. BAL #19 Chris Davis (X - X - 10)
t5.new_ab()
t5.pitch_list("f f")
t5.out("G3-5-3")


# Bot 5th
# Pitching: BAL #30 Chris Tillman
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.out("F7")

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("P6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b c b f f b f")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #59 Clayton Mortensen
t6 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #91 Alfredo Aceves
t6.pitching_substitution(59)

# 6. BAL #32 Matt Wieters (X - X - X)
t6.new_ab()
t6.pitch_list("f b")
t6.out("F9")

# 7. BAL #2  J.J. Hardy (X - X - X)
t6.new_ab()
t6.pitch_list("b c f b b f")
t6.out("G5-3")

# 8. BAL #60 Chris Dickerson (X - X - X)
t6.new_ab()
t6.pitch_list("f f")
t6.out("P5")


# Bot 6th
# Pitching: BAL #30 Chris Tillman
b6 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1)
b6.advance(2, "29 1B")

# 5. BOS #16 Will Middlebrooks (X - X - 12)
b6.new_ab()
b6.pitch_list("b")
b6.out("F9")

# 6. BOS #29 Daniel Nava (X - X - 12)
b6.new_ab()
b6.hit(1)

# Pitching change (BAL): #17 Brian Matusz replaces #30 Chris Tillman
b6.pitching_substitution(17)

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - 29)
b6.new_ab(is_risp=True)
b6.pitch_list("b b d c f s")
b6.out("K")

# 8. BOS #7  Stephen Drew (X - 12 - 29)
b6.new_ab(is_risp=True)
b6.pitch_list("c c b d b c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #59 Clayton Mortensen
t7 = game.new_inning()

# 9. BAL #12 Alexi Casilla (X - X - X)
t7.new_ab()
t7.pitch_list("c c s")
t7.out("K2-3")

# 1. BAL #9  Nate McLouth (X - X - X)
t7.new_ab()
t7.pitch_list("c f b b")
t7.out("P6")

# 2. BAL #13 Manny Machado (X - X - X)
t7.new_ab()
t7.pitch_list("c b b")
t7.hit(1)
t7.advance(2, "21 BB")
t7.advance(4, "10 2B")

# Pitching change (BOS): #30 Andrew Miller replaces #59 Clayton Mortensen
t7.pitching_substitution(30)

# 3. BAL #21 Nick Markakis (X - X - 13)
t7.new_ab()
t7.pitch_list("b c s b b b")
t7.reach("BB")
t7.advance(3, "10 2B")

# Pitching change (BOS): #19 Koji Uehara replaces #30 Andrew Miller
t7.pitching_substitution(19)

# 4. BAL #10 Adam Jones (X - 13 - 21)
t7.new_ab(is_risp=True)
t7.hit(2, rbis=1)

# 5. BAL #19 Chris Davis (21 - 10 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("i i i i")
t7.reach("IBB")

# 6. BAL #32 Matt Wieters (21 - 10 - 19)
t7.new_ab(is_risp=True)
t7.pitch_list("c f")
t7.out("F7")


# Bot 7th
# Pitching: BAL #47 Pedro Strop
b7 = game.new_inning()

# Pitching change (BAL): #47 Pedro Strop replaces #17 Brian Matusz
b7.pitching_substitution(47)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #44 Jackie Bradley Jr., batting 9th
b7.offensive_substitution(9, 5, "PH")

# 9. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("b b c s")
b7.out("L5")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.out("G1-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("c b s")
b7.hit(1)
b7.thrown_out(2, "15 FC4-6", 3, 47)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b7.new_ab()
b7.pitch_list("c 1 1 f")
b7.reach("FC4-6")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #19 Koji Uehara
t8.pitching_substitution(36)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t8.defensive_switch(5, "7")

# 7. BAL #2  J.J. Hardy (X - X - X)
t8.new_ab()
t8.pitch_list("f f b c")
t8.out("!K")

# 8. BAL #60 Chris Dickerson (X - X - X)
t8.new_ab()
t8.pitch_list("c s b f f")
t8.hit(1)
t8.thrown_out(2, "12 FC4-6", 2, 36)

# 9. BAL #12 Alexi Casilla (X - X - 60)
t8.new_ab()
t8.pitch_list("1")
t8.reach("FC4-6")
t8.advance(2, "9 WP")

# 1. BAL #9  Nate McLouth (X - X - 12)
t8.new_ab(is_risp=True)
t8.pitch_list("b b c c d")
t8.wp()
t8.out("G4-3")


# Bot 8th
# Pitching: BAL #56 Darren O'Day
b8 = game.new_inning()

# Pitching change (BAL): #56 Darren O'Day replaces #47 Pedro Strop
b8.pitching_substitution(56)

# 4. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("f s")
b8.out("P6")

# 5. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.pitch_list("b s f")
b8.out("L4")

# 6. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #63 Alex Wilson
t9 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #36 Junichi Tazawa
t9.pitching_substitution(63)

# 2. BAL #13 Manny Machado (X - X - X)
t9.new_ab()
t9.pitch_list("b b f b b")
t9.reach("BB")
t9.thrown_out(2, "21 DP6-4-3", 1, 63)

# 3. BAL #21 Nick Markakis (X - X - 13)
t9.new_ab()
t9.pitch_list("b b c")
t9.out("DP6-4-3")

# 4. BAL #10 Adam Jones (X - X - X)
t9.new_ab()
t9.pitch_list("c s s")
t9.out("K")


# Bot 9th
# Pitching: BAL #43 Jim Johnson
b9 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #56 Darren O'Day
b9.pitching_substitution(43)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b9.new_ab()
b9.pitch_list("b b f c f b c")
b9.out("!K")

# 8. BOS #7  Stephen Drew (X - X - X)
b9.new_ab()
b9.pitch_list("f b b")
b9.hit(1)

# 9. BOS #5  Jonny Gomes (X - X - 7)
b9.new_ab()
b9.pitch_list("b c f f s")
b9.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b9.new_ab()
b9.pitch_list("b")
b9.out("L7")

# Winning team: BAL
# WP: BAL #17 Brian Matusz
game.winning_pitcher(17, is_away_team=True)
# SV: BAL #43 Jim Johnson
game.save_pitcher(43, is_away_team=True)

# Loser team: BOS
# LP: BOS #59 Clayton Mortensen
game.losing_pitcher(59)

# print(game)
game.generate_scorecard()
