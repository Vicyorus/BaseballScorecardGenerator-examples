import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2013-07-27
# https://www.baseball-reference.com/boxes/BAL/BAL201307270.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2013/07/27/348290/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-27 19:32-23:20 (0:27 delay)",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "44,765",
        "temp": "71F, Overcast",
        "wind": "1mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 46,
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
                46: "Ryan Dempster",
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
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
            },
            "lefties": [32, 66, 31, 38, 22],
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
            "bullpen": [65, 41, 67, 32, 66, 31, 36, 19, 38, 54, 22],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 34,
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
                34: "Scott Feldman",
                # Bench
                3: "Ryan Flaherty",
                31: "Taylor Teagarden",
                12: "Alexi Casilla",
                # Bullpen
                50: "Miguel González",
                30: "Chris Tillman",
                40: "Troy Patton",
                66: "T.J. McFarland",
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
            "bullpen": [50, 30, 40, 66, 57, 29, 63, 56, 39, 17, 43, 16],
        },
        "umpires": {
            "HP": "Tim Timmons",
            "1B": "Mike Estabrook",
            "2B": "Mike Winters",
            "3B": "Laz Diaz",
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
# Pitching: BAL #34 Scott Feldman
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b b f")
t1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b f b b c")
t1.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c c b b b f f")
t1.out("G5-3")


# Bot 1st
# Pitching: BOS #46 Ryan Dempster
b1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
b1.new_ab()
b1.out("P6")

# 2. BAL #13 Manny Machado (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("(F)P2")

# 3. BAL #21 Nick Markakis (X - X - X)
b1.new_ab()
b1.pitch_list("b b b b")
b1.reach("BB")

# 4. BAL #10 Adam Jones (X - X - 21)
b1.new_ab()
b1.pitch_list("b t")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #34 Scott Feldman
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("b b f b f b")
t2.reach("BB")
t2.thrown_out(2, "37 FC4-6", 2, 34)

# 5. BOS #12 Mike Napoli (X - X - 34)
t2.new_ab()
t2.pitch_list("c s")
t2.out("(F)P3")

# 6. BOS #37 Mike Carp (X - X - 34)
t2.new_ab()
t2.reach("FC4-6")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t2.new_ab()
t2.pitch_list("b c b f")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #46 Ryan Dempster
b2 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
b2.new_ab()
b2.pitch_list("b c s b c")
b2.out("!K")

# 6. BAL #32 Matt Wieters (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.out("F7")

# 7. BAL #2  J.J. Hardy (X - X - X)
b2.new_ab()
b2.pitch_list("c f")
b2.out("G2-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #34 Scott Feldman
t3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("c b b")
t3.hit(1)
t3.advance(2, "10 G3")
t3.advance(3, "2 1B")
t3.advance(4, "18 G4-3")

# 9. BOS #10 Jose Iglesias (X - X - 7)
t3.new_ab()
t3.pitch_list("b 1 1 f")
t3.out("G3")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.hit(1)
t3.advance(2, "18 SB")
t3.advance(3, "18 G4-3")

# 2. BOS #18 Shane Victorino (7 - X - 2)
t3.new_ab(is_risp=True)
t3.pitch_list("c 1 b")
t3.out("G4-3", rbis=1)

# 3. BOS #15 Dustin Pedroia (2 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b f b f")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #46 Ryan Dempster
b3 = game.new_inning()

# 8. BAL #51 Henry Urrutia (X - X - X)
b3.new_ab()
b3.pitch_list("c b f")
b3.out("L6")

# 9. BAL #1  Brian Roberts (X - X - X)
b3.new_ab()
b3.out("L3")

# 1. BAL #9  Nate McLouth (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(2, "13 BB")

# 2. BAL #13 Manny Machado (X - X - 9)
b3.new_ab()
b3.pitch_list("1 b c p f 1 1 d f f d")
b3.reach("BB")

# 3. BAL #21 Nick Markakis (X - 9 - 13)
b3.new_ab(is_risp=True)
b3.pitch_list("f")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #34 Scott Feldman
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("c c")
t4.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("c b f t")
t4.out("KT")

# 6. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("b b f f f f b")
t4.hit(1)
t4.advance(2, "39 1B")
t4.advance(4, "7 HR")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t4.new_ab()
t4.hit(1)
t4.advance(4, "7 HR")

# 8. BOS #7  Stephen Drew (X - 37 - 39)
t4.new_ab(is_risp=True)
t4.pitch_list("b")
t4.hit(4, rbis=3)

# 9. BOS #10 Jose Iglesias (X - X - X)
t4.new_ab()
t4.pitch_list("b c f")
t4.hit(1)
t4.advance(2, "2 SB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
t4.new_ab(is_risp=True)
t4.pitch_list("1 b b")
t4.out("L3")


# Bot 4th
# Pitching: BOS #46 Ryan Dempster
b4 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.out("F9")

# 5. BAL #19 Chris Davis (X - X - X)
b4.new_ab()
b4.pitch_list("b f b f f s")
b4.out("K")

# 6. BAL #32 Matt Wieters (X - X - X)
b4.new_ab()
b4.pitch_list("c c b b")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #34 Scott Feldman
t5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("L6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("b f b b s f f b")
t5.reach("BB")

# 5. BOS #12 Mike Napoli (X - X - 34)
t5.new_ab()
t5.pitch_list("s b")
t5.out("L6")


# Bot 5th
# Pitching: BOS #46 Ryan Dempster
b5 = game.new_inning()

# 7. BAL #2  J.J. Hardy (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)
b5.advance(2, "51 1B")
b5.advance(4, "1 1B")

# 8. BAL #51 Henry Urrutia (X - X - 2)
b5.new_ab()
b5.pitch_list("t b f")
b5.hit(1)
b5.advance(3, "1 1B")

# 9. BAL #1  Brian Roberts (X - 2 - 51)
b5.new_ab(is_risp=True)
b5.pitch_list("c b b")
b5.hit(1, rbis=1)
b5.thrown_out(2, "13 DP6-4-3", 2, 46)

# 1. BAL #9  Nate McLouth (51 - X - 1)
b5.new_ab(is_risp=True)
b5.pitch_list("c s b d s")
b5.out("K")

# 2. BAL #13 Manny Machado (51 - X - 1)
b5.new_ab(is_risp=True)
b5.pitch_list("1 c 1 s b")
b5.out("DP6-4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #40 Troy Patton
t6 = game.new_inning()

# Pitching change (BAL): #40 Troy Patton replaces #34 Scott Feldman
t6.pitching_substitution(40)

# 6. BOS #37 Mike Carp (X - X - X)
t6.new_ab()
t6.pitch_list("s b b")
t6.hit(1)
t6.thrown_out(2, "39 FC5-4", 1, 40)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t6.new_ab()
t6.pitch_list("c")
t6.reach("FC5-4")
t6.advance(4, "7 HR")

# 8. BOS #7  Stephen Drew (X - X - 39)
t6.new_ab()
t6.pitch_list("b")
t6.hit(4, rbis=2)

# 9. BOS #10 Jose Iglesias (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G1-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("s f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #46 Ryan Dempster
b6 = game.new_inning()

# 3. BAL #21 Nick Markakis (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b")
b6.hit(1)
b6.advance(3, "19 1B")
b6.advance(4, "32 FC3-6")

# 4. BAL #10 Adam Jones (X - X - 21)
b6.new_ab()
b6.pitch_list("b s f s")
b6.out("K")

# 5. BAL #19 Chris Davis (X - X - 21)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1)
b6.thrown_out(2, "32 FC3-6", 2, 32)

# Pitching change (BOS): #32 Craig Breslow replaces #46 Ryan Dempster
b6.pitching_substitution(32)

# 6. BAL #32 Matt Wieters (21 - X - 19)
b6.new_ab(is_risp=True)
b6.pitch_list("b c s b f b")
b6.reach("FC3-6", rbis=1)

# 7. BAL #2  J.J. Hardy (X - X - 32)
b6.new_ab()
b6.pitch_list("c b s")
b6.out("P6")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #63 Jairo Asencio
t7 = game.new_inning()

# Pitching change (BAL): #63 Jairo Asencio replaces #40 Troy Patton
t7.pitching_substitution(63)

# 2. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("c f b b f b f")
t7.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c c s")
t7.out("K")

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("s b c c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #32 Craig Breslow
b7 = game.new_inning()

# 8. BAL #51 Henry Urrutia (X - X - X)
b7.new_ab()
b7.out("G5-3")

# 9. BAL #1  Brian Roberts (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b c f")
b7.out("F7")

# 1. BAL #9  Nate McLouth (X - X - X)
b7.new_ab()
b7.pitch_list("f")
b7.reach("HBP")

# 2. BAL #13 Manny Machado (X - X - 9)
b7.new_ab()
b7.pitch_list("b f b b")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #17 Brian Matusz
t8 = game.new_inning()

# Pitching change (BAL): #17 Brian Matusz replaces #63 Jairo Asencio
t8.pitching_substitution(17)

# 6. BOS #37 Mike Carp (X - X - X)
t8.new_ab()
t8.hit(2)
# Offensive change (BOS): Pinch-runner #29 Daniel Nava replaces #37 Mike Carp
t8.offensive_substitution(6, 29, "PR")
t8.atbase("PR")

# 7. BOS #39 Jarrod Saltalamacchia (X - 37 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c f d f b d")
t8.out("(F)P2")

# 8. BOS #7  Stephen Drew (X - 29 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("s b s c")
t8.out("!K")

# 9. BOS #10 Jose Iglesias (X - 29 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b b s")
t8.out("G6-3")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
b8.pitching_substitution(36)

# Defensive switch (BOS): #29 Daniel Nava moves to LF
b8.defensive_switch(29, "7")

# 3. BAL #21 Nick Markakis (X - X - X)
b8.new_ab()
b8.out("G3-1")

# 4. BAL #10 Adam Jones (X - X - X)
b8.new_ab()
b8.pitch_list("b b f")
b8.hit(1)
b8.advance(2, "19 BB")
b8.advance(3, "32 F9")
b8.advance("U", "2 E6")

# 5. BAL #19 Chris Davis (X - X - 10)
b8.new_ab()
b8.pitch_list("b s s b f f b b")
b8.reach("BB")
b8.advance(2, "2 E6")

# 6. BAL #32 Matt Wieters (X - 10 - 19)
b8.new_ab(is_risp=True)
b8.out("F9")

# 7. BAL #2  J.J. Hardy (10 - X - 19)
b8.new_ab(is_risp=True)
b8.pitch_list("c b s")
b8.error(6)
b8.reach("E6")

# 8. BAL #51 Henry Urrutia (X - 19 - 2)
b8.new_ab(is_risp=True)
b8.pitch_list("b b f f")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #57 Francisco Rodríguez
t9 = game.new_inning()

# Pitching change (BAL): #57 Francisco Rodríguez replaces #17 Brian Matusz
t9.pitching_substitution(57)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("b f f b t")
t9.out("KT")

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("b c s b")
t9.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("c b c b b b")
t9.reach("BB")

# Offensive change (BOS): Pinch-hitter #23 Brandon Snyder replaces #34 David Ortiz, batting 4th
t9.offensive_substitution(4, 23, "PH")

# 4. BOS #23 Brandon Snyder (X - X - 15)
t9.new_ab()
t9.out("F8")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
b9.pitching_substitution(19)

# Defensive switch (BOS): #23 Brandon Snyder moves to DH
b9.defensive_switch(23, "0")

# 9. BAL #1  Brian Roberts (X - X - X)
b9.new_ab()
b9.pitch_list("b b c s b")
b9.out("F7")

# 1. BAL #9  Nate McLouth (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(2)

# 2. BAL #13 Manny Machado (X - 9 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b c s t")
b9.out("KT")

# 3. BAL #21 Nick Markakis (X - 9 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c f b b b")
b9.out("F9")

# Winning team: BOS
# WP: BOS #46 Ryan Dempster
game.winning_pitcher(46, is_away_team=True)

# Loser team: BAL
# LP: BAL #34 Scott Feldman
game.losing_pitcher(34)

# print(game)
game.generate_scorecard()
