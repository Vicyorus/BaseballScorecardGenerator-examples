import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2013-08-29
# https://www.baseball-reference.com/boxes/BOS/BOS201308290.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2013/08/29/348733/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-29 19:11-22:31",
        "at": "Fenway Park, Boston, MA",
        "att": "33,300",
        "temp": "62F, Cloudy",
        "wind": "11mph, In From RF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 30,
            "roster": {
                # Lineup
                9: "Nate McLouth",
                13: "Manny Machado",
                10: "Adam Jones",
                19: "Chris Davis",
                32: "Matt Wieters",
                2: "J.J. Hardy",
                21: "Nick Markakis",
                35: "Danny Valencia",
                1: "Brian Roberts",
                # Starting pitcher
                30: "Chris Tillman",
                # Bench
                24: "Wilson Betemit",
                31: "Taylor Teagarden",
                12: "Alexi Casilla",
                # Bullpen
                17: "Brian Matusz",
                50: "Miguel González",
                40: "Troy Patton",
                66: "T.J. McFarland",
                34: "Scott Feldman",
                43: "Jim Johnson",
                57: "Francisco Rodríguez",
                29: "Tommy Hunter",
                39: "Kevin Gausman",
                56: "Darren O'Day",
                25: "Bud Norris",
            },
            "lefties": [17, 40, 66],
            "lineup": [
                [9, "7"],
                [13, "5"],
                [10, "8"],
                [19, "3"],
                [32, "2"],
                [2, "6"],
                [21, "9"],
                [35, "0"],
                [1, "4"],
            ],
            "bench": [
                [24, "3B"],
                [31, "C"],
                [12, "2B"],
            ],
            "bullpen": [17, 50, 40, 66, 34, 43, 57, 29, 39, 56, 25],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
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
                16: "Will Middlebrooks",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                3: "David Ross",
                72: "Xander Bogaerts",
                12: "Mike Napoli",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                38: "Matt Thornton",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 32, 66, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "3"],
                [5, "7"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
            ],
            "bench": [
                [37, "1B"],
                [3, "C"],
                [72, "2B"],
                [12, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 36, 11, 19, 38, 22, 46],
        },
        "umpires": {
            "HP": "Tim McClelland",
            "1B": "Marty Foster",
            "2B": "Wally Bell",
            "3B": "Marvin Hudson",
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

# 1. BAL #9  Nate McLouth (X - X - X)
t1.new_ab()
t1.pitch_list("c b b s b")
t1.out("P4")

# 2. BAL #13 Manny Machado (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b b b")
t1.reach("BB")

# 3. BAL #10 Adam Jones (X - X - 13)
t1.new_ab()
t1.pitch_list("c f s")
t1.out("K")

# 4. BAL #19 Chris Davis (X - X - 13)
t1.new_ab()
t1.pitch_list("b b c s s")
t1.out("K")


# Bot 1st
# Pitching: BAL #30 Chris Tillman
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("s s b")
b1.hit(1)
b1.advance(2, "18 WP")

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab(is_risp=True)
b1.pitch_list("1 c b b f s")
b1.wp()
b1.out("K")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.out("(F)P3")

# 4. BOS #34 David Ortiz (X - 2 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b s s s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 5. BAL #32 Matt Wieters (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("L8")

# 6. BAL #2  J.J. Hardy (X - X - X)
t2.new_ab()
t2.pitch_list("b f b f b f f f")
t2.out("P4")

# 7. BAL #21 Nick Markakis (X - X - X)
t2.new_ab()
t2.pitch_list("c b s f b")
t2.out("P5")


# Bot 2nd
# Pitching: BAL #30 Chris Tillman
b2 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("s b s")
b2.hit(2)
b2.advance(4, "7 1B")

# 6. BOS #5  Jonny Gomes (X - 29 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b f f s")
b2.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - 29 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b f")
b2.out("F7")

# 8. BOS #7  Stephen Drew (X - 29 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f c b f b")
b2.hit(1, rbis=1)

# 9. BOS #16 Will Middlebrooks (X - X - 7)
b2.new_ab()
b2.pitch_list("f b c f f b 1")
b2.out("(F)P4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 8. BAL #35 Danny Valencia (X - X - X)
t3.new_ab()
t3.pitch_list("b f")
t3.hit(2)
t3.thrown_out(3, "1 FC4-5", 1, 31)

# 9. BAL #1  Brian Roberts (X - 35 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b")
t3.reach("FC4-5")
t3.advance(2, "9 BB")
t3.advance(4, "13 2B")

# 1. BAL #9  Nate McLouth (X - X - 1)
t3.new_ab()
t3.pitch_list("b b c f b b")
t3.reach("BB")
t3.advance(4, "13 2B")

# 2. BAL #13 Manny Machado (X - 1 - 9)
t3.new_ab(is_risp=True)
t3.pitch_list("b")
t3.hit(2, rbis=2)

# 3. BAL #10 Adam Jones (X - 13 - X)
t3.new_ab(is_risp=True)
t3.hit(1)

# 4. BAL #19 Chris Davis (X - 13 - 10)
t3.new_ab(is_risp=True)
t3.pitch_list("s d")
t3.out("F9")

# 5. BAL #32 Matt Wieters (X - 13 - 10)
t3.new_ab(is_risp=True)
t3.pitch_list("f s f")
t3.out("F9")


# Bot 3rd
# Pitching: BAL #30 Chris Tillman
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("P6")

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("b b c f")
b3.hit(1)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b3.new_ab()
b3.pitch_list("f 1 s b 1 f")
b3.out("F9")

# 4. BOS #34 David Ortiz (X - X - 18)
b3.new_ab()
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 6. BAL #2  J.J. Hardy (X - X - X)
t4.new_ab()
t4.pitch_list("c f b")
t4.out("F9")

# 7. BAL #21 Nick Markakis (X - X - X)
t4.new_ab()
t4.pitch_list("c s b s")
t4.out("K")

# 8. BAL #35 Danny Valencia (X - X - X)
t4.new_ab()
t4.pitch_list("b b f b")
t4.hit(2)

# 9. BAL #1  Brian Roberts (X - 35 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b b")
t4.out("G5-3")


# Bot 4th
# Pitching: BAL #30 Chris Tillman
b4 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("b b c s f f c")
b4.out("!K")

# 6. BOS #5  Jonny Gomes (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G5-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("c s b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t5.new_ab()
t5.pitch_list("c b s")
t5.out("L8")

# 2. BAL #13 Manny Machado (X - X - X)
t5.new_ab()
t5.pitch_list("b f s")
t5.out("F9")

# 3. BAL #10 Adam Jones (X - X - X)
t5.new_ab()
t5.pitch_list("b b s b b")
t5.reach("BB")
t5.advance(4, "19 2B")

# 4. BAL #19 Chris Davis (X - X - 10)
t5.new_ab()
t5.pitch_list("f c")
t5.hit(2, rbis=1)

# 5. BAL #32 Matt Wieters (X - 19 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b b f b f f")
t5.out("G6-3")


# Bot 5th
# Pitching: BAL #30 Chris Tillman
b5 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("c f f")
b5.out("F9")

# 9. BOS #16 Will Middlebrooks (X - X - X)
b5.new_ab()
b5.pitch_list("f b b c f s")
b5.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("b c s")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 6. BAL #2  J.J. Hardy (X - X - X)
t6.new_ab()
t6.pitch_list("b s f f b f")
t6.out("F8")

# 7. BAL #21 Nick Markakis (X - X - X)
t6.new_ab()
t6.out("L5")

# 8. BAL #35 Danny Valencia (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b f c")
t6.out("!K")


# Bot 6th
# Pitching: BAL #30 Chris Tillman
b6 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b")
b6.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c f s")
b6.out("K")

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.pitch_list("c s b f b")
b6.out("G4-3")

# 5. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(2)

# 6. BOS #5  Jonny Gomes (X - 29 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #38 Matt Thornton
t7 = game.new_inning()

# Pitching change (BOS): #38 Matt Thornton replaces #31 Jon Lester
t7.pitching_substitution(38)

# 9. BAL #1  Brian Roberts (X - X - X)
t7.new_ab()
t7.pitch_list("b f c f b f")
t7.out("F8")

# 1. BAL #9  Nate McLouth (X - X - X)
t7.new_ab()
t7.pitch_list("c s b b")
t7.out("G4-3")

# 2. BAL #13 Manny Machado (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.hit(1)
t7.advance(2, "10 PB")
t7.advance(3, "10 1B")

# 3. BAL #10 Adam Jones (X - X - 13)
t7.new_ab(is_risp=True)
t7.pitch_list("s")
t7.pb()
t7.hit(1)

# 4. BAL #19 Chris Davis (13 - X - 10)
t7.new_ab(is_risp=True)
t7.pitch_list("b f f")
t7.out("F8")


# Bot 7th
# Pitching: BAL #30 Chris Tillman
b7 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("b b f c")
b7.out("G3")

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("c b f b f s")
b7.out("K")

# 9. BOS #16 Will Middlebrooks (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #67 Brandon Workman
t8 = game.new_inning()

# Pitching change (BOS): #67 Brandon Workman replaces #38 Matt Thornton
t8.pitching_substitution(67)

# 5. BAL #32 Matt Wieters (X - X - X)
t8.new_ab()
t8.pitch_list("b f")
t8.out("G3")

# 6. BAL #2  J.J. Hardy (X - X - X)
t8.new_ab()
t8.pitch_list("c b c b b f b")
t8.reach("BB")
t8.advance(2, "21 G4-3")

# 7. BAL #21 Nick Markakis (X - X - 2)
t8.new_ab()
t8.pitch_list("b c 1 c f b f")
t8.out("G4-3")

# Offensive change (BAL): Pinch-hitter #24 Wilson Betemit replaces #35 Danny Valencia, batting 8th
t8.offensive_substitution(8, 24, "PH")

# 8. BAL #24 Wilson Betemit (X - 2 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b d b c")
t8.out("G3")


# Bot 8th
# Pitching: BAL #29 Tommy Hunter
b8 = game.new_inning()

# Pitching change (BAL): #29 Tommy Hunter replaces #30 Chris Tillman
b8.pitching_substitution(29)

# Defensive switch (BAL): #24 Wilson Betemit moves to DH
b8.defensive_switch(24, "0")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("c b c f b")
b8.hit(1)
b8.advance(2, "18 SB")
b8.advance(3, "15 F9")

# 2. BOS #18 Shane Victorino (X - X - 2)
b8.new_ab(is_risp=True)
b8.pitch_list("1 1 c 1 l f p s")
b8.out("K2-3")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c f")
b8.out("F9")

# Pitching change (BAL): #17 Brian Matusz replaces #29 Tommy Hunter
b8.pitching_substitution(17)

# 4. BOS #34 David Ortiz (2 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b s s s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #67 Brandon Workman
t9 = game.new_inning()

# 9. BAL #1  Brian Roberts (X - X - X)
t9.new_ab()
t9.pitch_list("c c b f s")
t9.out("K")

# 1. BAL #9  Nate McLouth (X - X - X)
t9.new_ab()
t9.pitch_list("b s b b b")
t9.reach("BB")
t9.advance(2, "13 BB")

# 2. BAL #13 Manny Machado (X - X - 9)
t9.new_ab()
t9.pitch_list("b 1 b 1 b f f f b")
t9.reach("BB")

# 3. BAL #10 Adam Jones (X - 9 - 13)
t9.new_ab(is_risp=True)
t9.pitch_list("b s s s")
t9.out("K")

# Pitching change (BOS): #32 Craig Breslow replaces #67 Brandon Workman
t9.pitching_substitution(32)

# 4. BAL #19 Chris Davis (X - 9 - 13)
t9.new_ab(is_risp=True)
t9.pitch_list("f")
t9.out("G3-1")


# Bot 9th
# Pitching: BAL #43 Jim Johnson
b9 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #17 Brian Matusz
b9.pitching_substitution(43)

# 5. BOS #29 Daniel Nava (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.thrown_out(2, "5 DP6-4-3", 1, 43)

# 6. BOS #5  Jonny Gomes (X - X - 29)
b9.new_ab()
b9.pitch_list("b f s")
b9.out("DP6-4-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b9.new_ab()
b9.pitch_list("b b s f c")
b9.out("!K")

# Winning team: BAL
# WP: BAL #30 Chris Tillman
game.winning_pitcher(30, is_away_team=True)
# SV: BAL #43 Jim Johnson
game.save_pitcher(43, is_away_team=True)

# Loser team: BOS
# LP: BOS #31 Jon Lester
game.losing_pitcher(31)

# print(game)
game.generate_scorecard()
