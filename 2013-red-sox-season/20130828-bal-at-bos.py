import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2013-08-28
# https://www.baseball-reference.com/boxes/BOS/BOS201308280.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2013/08/28/348718/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-28 19:11-22:11",
        "at": "Fenway Park, Boston, MA",
        "att": "31,962",
        "temp": "65F, Partly Cloudy",
        "wind": "7mph, In From CF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 25,
            "roster": {
                # Lineup
                9: "Nate McLouth",
                13: "Manny Machado",
                19: "Chris Davis",
                10: "Adam Jones",
                21: "Nick Markakis",
                2: "J.J. Hardy",
                32: "Matt Wieters",
                24: "Wilson Betemit",
                1: "Brian Roberts",
                # Starting pitcher
                25: "Bud Norris",
                # Bench
                31: "Taylor Teagarden",
                12: "Alexi Casilla",
                35: "Danny Valencia",
                # Bullpen
                17: "Brian Matusz",
                50: "Miguel González",
                30: "Chris Tillman",
                40: "Troy Patton",
                66: "T.J. McFarland",
                34: "Scott Feldman",
                43: "Jim Johnson",
                57: "Francisco Rodríguez",
                29: "Tommy Hunter",
                39: "Kevin Gausman",
                56: "Darren O'Day",
            },
            "lefties": [17, 40, 66],
            "lineup": [
                [9, "7"],
                [13, "5"],
                [19, "3"],
                [10, "8"],
                [21, "9"],
                [2, "6"],
                [32, "2"],
                [24, "0"],
                [1, "4"],
            ],
            "bench": [
                [31, "C"],
                [12, "2B"],
                [35, "3B"],
            ],
            "bullpen": [17, 50, 30, 40, 66, 34, 43, 57, 29, 39, 56],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                72: "Xander Bogaerts",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                37: "Mike Carp",
                16: "Will Middlebrooks",
                5: "Jonny Gomes",
                3: "David Ross",
                # Bullpen
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
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
                [29, "7"],
                [12, "3"],
                [39, "2"],
                [7, "6"],
                [72, "5"],
            ],
            "bench": [
                [37, "1B"],
                [16, "3B"],
                [5, "LF"],
                [3, "C"],
            ],
            "bullpen": [67, 56, 32, 66, 44, 31, 36, 11, 19, 38, 22, 46],
        },
        "umpires": {
            "HP": "Marvin Hudson",
            "1B": "Tim McClelland",
            "2B": "Marty Foster",
            "3B": "Wally Bell",
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
# Pitching: BOS #41 John Lackey
t1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t1.new_ab()
t1.pitch_list("b f")
t1.out("G3-1")

# 2. BAL #13 Manny Machado (X - X - X)
t1.new_ab()
t1.pitch_list("f s f")
t1.hit(1)
t1.advance(4, "19 2B")

# 3. BAL #19 Chris Davis (X - X - 13)
t1.new_ab()
t1.pitch_list("b")
t1.hit(2, rbis=1)
t1.advance(3, "10 F8")

# 4. BAL #10 Adam Jones (X - 19 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c d b")
t1.out("F8")

# 5. BAL #21 Nick Markakis (19 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("f")
t1.out("(F)P5")


# Bot 1st
# Pitching: BAL #25 Bud Norris
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b f f b f f b b")
b1.reach("BB")
b1.advance(2, "18 SB")
b1.advance(3, "15 G1-3")

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab(is_risp=True)
b1.pitch_list("b c b")
b1.out("L6")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b c b d c")
b1.out("G1-3")

# 4. BOS #34 David Ortiz (2 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 6. BAL #2  J.J. Hardy (X - X - X)
t2.new_ab()
t2.pitch_list("c c s")
t2.out("K")

# 7. BAL #32 Matt Wieters (X - X - X)
t2.new_ab()
t2.pitch_list("b s s f f s")
t2.out("K")

# 8. BAL #24 Wilson Betemit (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("F9")


# Bot 2nd
# Pitching: BAL #25 Bud Norris
b2 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b c s f b s")
b2.out("K")

# 6. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("c b f b b s")
b2.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("f b b b s c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 9. BAL #1  Brian Roberts (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b b")
t3.reach("BB")
t3.advance(2, "9 SB")
t3.thrown_out(3, "13 CS", 2, 41)

# 1. BAL #9  Nate McLouth (X - X - 1)
t3.new_ab(is_risp=True)
t3.pitch_list("b b b c c f")
t3.out("(F)P5")

# 2. BAL #13 Manny Machado (X - 1 - X)
t3.new_ab()
t3.pitch_list("2 2 c")
t3.hit(4)

# 3. BAL #19 Chris Davis (X - X - X)
t3.new_ab()
t3.pitch_list("s b b s")
t3.out("L9")


# Bot 3rd
# Pitching: BAL #25 Bud Norris
b3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.advance(2, "2 1B")
b3.advance(4, "18 1B")

# 9. BOS #72 Xander Bogaerts (X - X - 7)
b3.new_ab()
b3.pitch_list("c 1")
b3.out("L8")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b3.new_ab()
b3.hit(1)
b3.advance(2, "18 1B")
b3.advance(3, "15 BB")

# 2. BOS #18 Shane Victorino (X - 7 - 2)
b3.new_ab(is_risp=True)
b3.pitch_list("b b f f")
b3.hit(1, rbis=1)
b3.advance(2, "15 BB")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("b b b b")
b3.reach("BB")

# 4. BOS #34 David Ortiz (2 - 18 - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("b b c f t")
b3.out("KT")

# 5. BOS #29 Daniel Nava (2 - 18 - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("c f c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("s b f f f f b")
t4.out("G1-3")

# 5. BAL #21 Nick Markakis (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(2)

# 6. BAL #2  J.J. Hardy (X - 21 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("s s d s")
t4.out("K")

# 7. BAL #32 Matt Wieters (X - 21 - X)
t4.new_ab(is_risp=True)
t4.out("L7")


# Bot 4th
# Pitching: BAL #25 Bud Norris
b4 = game.new_inning()

# 6. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("b f c")
b4.out("G5-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("c f b b f f f b")
b4.hit(1)
b4.thrown_out(2, "72 FC6-4", 3, 25)

# 8. BOS #7  Stephen Drew (X - X - 39)
b4.new_ab()
b4.pitch_list("c c c")
b4.out("!K")

# 9. BOS #72 Xander Bogaerts (X - X - 39)
b4.new_ab()
b4.reach("FC6-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 8. BAL #24 Wilson Betemit (X - X - X)
t5.new_ab()
t5.pitch_list("c f f s")
t5.out("K")

# 9. BAL #1  Brian Roberts (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)

# 1. BAL #9  Nate McLouth (X - X - 1)
t5.new_ab()
t5.pitch_list("1 d")
t5.out("F8")

# 2. BAL #13 Manny Machado (X - X - 1)
t5.new_ab()
t5.pitch_list("c 1")
t5.out("F9")


# Bot 5th
# Pitching: BAL #25 Bud Norris
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("F7")

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("c b b b b")
b5.reach("BB")

# 4. BOS #34 David Ortiz (X - X - 15)
b5.new_ab()
b5.pitch_list("b c")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 3. BAL #19 Chris Davis (X - X - X)
t6.new_ab()
t6.hit(4)

# 4. BAL #10 Adam Jones (X - X - X)
t6.new_ab()
t6.out("L6")

# 5. BAL #21 Nick Markakis (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("L7")

# 6. BAL #2  J.J. Hardy (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G6-3")


# Bot 6th
# Pitching: BAL #25 Bud Norris
b6 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("b c b")
b6.hit(1)
b6.thrown_out(2, "39 DP3-6-3", 2, 57)

# 6. BOS #12 Mike Napoli (X - X - 29)
b6.new_ab()
b6.pitch_list("b c b c b f f c")
b6.out("!K")

# Pitching change (BAL): #57 Francisco Rodríguez replaces #25 Bud Norris
b6.pitching_substitution(57)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
b6.new_ab()
b6.out("DP3-6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 7. BAL #32 Matt Wieters (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.out("G3")

# 8. BAL #24 Wilson Betemit (X - X - X)
t7.new_ab()
t7.out("F7")

# 9. BAL #1  Brian Roberts (X - X - X)
t7.new_ab()
t7.pitch_list("b c f")
t7.hit(1)

# 1. BAL #9  Nate McLouth (X - X - 1)
t7.new_ab()
t7.pitch_list("1 b")
t7.out("F9")


# Bot 7th
# Pitching: BAL #57 Francisco Rodríguez
b7 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("s c b")
b7.hit(2)
b7.advance(3, "2 1B")
b7.advance(4, "15 1B")

# 9. BOS #72 Xander Bogaerts (X - 7 - X)
b7.new_ab(is_risp=True)
b7.out("L4")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c f b")
b7.hit(1)
b7.advance(2, "18 SB")
b7.advance(4, "15 1B")

# Pitching change (BAL): #56 Darren O'Day replaces #57 Francisco Rodríguez
b7.pitching_substitution(56)

# 2. BOS #18 Shane Victorino (7 - X - 2)
b7.new_ab(is_risp=True)
b7.pitch_list("1 c c f")
b7.out("L4")

# 3. BOS #15 Dustin Pedroia (7 - 2 - X)
b7.new_ab(is_risp=True)
b7.hit(1, rbis=2)
b7.advance(2, "T")

# Pitching change (BAL): #17 Brian Matusz replaces #56 Darren O'Day
b7.pitching_substitution(17)

# 4. BOS #34 David Ortiz (X - 15 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b b b f")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #41 John Lackey
t8 = game.new_inning()

# Defensive change (BOS): #5 Jonny Gomes replaces #2 Jacoby Ellsbury (CF), playing LF, batting 1st
t8.defensive_substitution(1, 5, "7")

# Defensive switch (BOS): #18 Shane Victorino moves to CF
t8.defensive_switch(18, "8")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
t8.defensive_switch(29, "9")

# 2. BAL #13 Manny Machado (X - X - X)
t8.new_ab()
t8.pitch_list("b s b b f")
t8.out("P5")

# Pitching change (BOS): #32 Craig Breslow replaces #41 John Lackey
t8.pitching_substitution(32)

# 3. BAL #19 Chris Davis (X - X - X)
t8.new_ab()
t8.pitch_list("c f b f b t")
t8.out("KT")

# 4. BAL #10 Adam Jones (X - X - X)
t8.new_ab()
t8.pitch_list("f b f b")
t8.out("L6")


# Bot 8th
# Pitching: BAL #17 Brian Matusz
b8 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("c b b b s s")
b8.out("K")

# Pitching change (BAL): #29 Tommy Hunter replaces #17 Brian Matusz
b8.pitching_substitution(29)

# 6. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("f f b b c")
b8.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("b s f b b f")
b8.hit(2)
b8.advance(4, "37 1B")

# 8. BOS #7  Stephen Drew (X - 39 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("i i i i")
b8.reach("IBB")
b8.advance(3, "37 1B")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #72 Xander Bogaerts, batting 9th
b8.offensive_substitution(9, 37, "PH")

# 9. BOS #37 Mike Carp (X - 39 - 7)
b8.new_ab(is_risp=True)
b8.pitch_list("f")
b8.hit(1, rbis=1)
# Offensive change (BOS): Pinch-runner #16 Will Middlebrooks replaces #37 Mike Carp
b8.offensive_substitution(9, 16, "PR")
b8.atbase("PR")

# 1. BOS #5  Jonny Gomes (7 - X - 37)
b8.new_ab(is_risp=True)
b8.pitch_list("s")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
t9.pitching_substitution(19)

# Defensive switch (BOS): #16 Will Middlebrooks moves to 3B
t9.defensive_switch(16, "5")

# 5. BAL #21 Nick Markakis (X - X - X)
t9.new_ab()
t9.pitch_list("f s s")
t9.out("K")

# 6. BAL #2  J.J. Hardy (X - X - X)
t9.new_ab()
t9.pitch_list("b f c")
t9.out("G5-3")

# 7. BAL #32 Matt Wieters (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F9")

# Winning team: BOS
# WP: BOS #32 Craig Breslow
game.winning_pitcher(32)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: BAL
# LP: BAL #29 Tommy Hunter
game.losing_pitcher(29, is_away_team=True)

# print(game)
game.generate_scorecard()
