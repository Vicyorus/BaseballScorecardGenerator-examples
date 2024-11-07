import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2013-06-16
# https://www.baseball-reference.com/boxes/BAL/BAL201306160.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2013/06/16/347774/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-16 13:37-16:43",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "41,311",
        "temp": "81F, Overcast",
        "wind": "9mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                10: "Jose Iglesias",
                29: "Daniel Nava",
                34: "David Ortiz",
                5: "Jonny Gomes",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                3: "David Ross",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                54: "Pedro Beato",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 30, 32, 22],
            "lineup": [
                [2, "8"],
                [10, "4"],
                [29, "9"],
                [34, "0"],
                [5, "7"],
                [37, "3"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [3, "C"],
                [18, "CF"],
                [15, "2B"],
                [12, "1B"],
            ],
            "bullpen": [40, 41, 56, 30, 32, 19, 54, 36, 22, 46],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 50,
            "roster": {
                # Lineup
                21: "Nick Markakis",
                13: "Manny Machado",
                2: "J.J. Hardy",
                10: "Adam Jones",
                19: "Chris Davis",
                32: "Matt Wieters",
                35: "Danny Valencia",
                28: "Steve Pearce",
                12: "Alexi Casilla",
                # Starting pitcher
                50: "Miguel González",
                # Bench
                3: "Ryan Flaherty",
                31: "Taylor Teagarden",
                36: "Chris Dickerson",
                9: "Nate McLouth",
                # Bullpen
                30: "Chris Tillman",
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
                [21, "9"],
                [13, "5"],
                [2, "6"],
                [10, "8"],
                [19, "3"],
                [32, "2"],
                [35, "0"],
                [28, "7"],
                [12, "4"],
            ],
            "bench": [
                [3, "2B"],
                [31, "C"],
                [36, "LF"],
                [9, "CF"],
            ],
            "bullpen": [30, 40, 66, 47, 38, 29, 56, 39, 17, 34, 43],
        },
        "umpires": {
            "HP": "David Rackley",
            "1B": "Jim Joyce",
            "2B": "Cory Blaser",
            "3B": "Jeff Nelson",
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
# Pitching: BAL #50 Miguel González
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("P6")

# 2. BOS #10 Jose Iglesias (X - X - X)
t1.new_ab()
t1.pitch_list("b f c")
t1.out("G4-3")

# 3. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("b b f c")
t1.out("F8")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. BAL #21 Nick Markakis (X - X - X)
b1.new_ab()
b1.pitch_list("s t")
b1.out("G3-1")

# 2. BAL #13 Manny Machado (X - X - X)
b1.new_ab()
b1.pitch_list("s f b b")
b1.hit(2)

# 3. BAL #2  J.J. Hardy (X - 13 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b c d f s")
b1.out("K")

# 4. BAL #10 Adam Jones (X - 13 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b f s s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #50 Miguel González
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.out("G3-1")

# 5. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("c b f s")
t2.out("K")

# 6. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
b2.new_ab()
b2.pitch_list("b f s f f s")
b2.out("K")

# 6. BAL #32 Matt Wieters (X - X - X)
b2.new_ab()
b2.pitch_list("f s")
b2.hit(1)
b2.advance(2, "35 1B")

# 7. BAL #35 Danny Valencia (X - X - 32)
b2.new_ab()
b2.pitch_list("c f")
b2.hit(1)

# 8. BAL #28 Steve Pearce (X - 32 - 35)
b2.new_ab(is_risp=True)
b2.pitch_list("d b b c c f f f s")
b2.out("K")

# 9. BAL #12 Alexi Casilla (X - 32 - 35)
b2.new_ab(is_risp=True)
b2.pitch_list("f")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #50 Miguel González
t3 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("b s b f f f b b")
t3.reach("BB")
t3.advance(2, "2 1B")

# 8. BOS #16 Will Middlebrooks (X - X - 39)
t3.new_ab()
t3.pitch_list("t b b c")
t3.out("L9")

# 9. BOS #7  Stephen Drew (X - X - 39)
t3.new_ab()
t3.pitch_list("b c")
t3.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - 39)
t3.new_ab()
t3.pitch_list("b b f")
t3.hit(1)

# 2. BOS #10 Jose Iglesias (X - 39 - 2)
t3.new_ab(is_risp=True)
t3.pitch_list("b f")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 1. BAL #21 Nick Markakis (X - X - X)
b3.new_ab()
b3.pitch_list("b b s b f")
b3.hit(1)
b3.advance(2, "13 F7")
b3.advance(4, "10 2B")

# 2. BAL #13 Manny Machado (X - X - 21)
b3.new_ab()
b3.pitch_list("c f f f b")
b3.out("F7")

# 3. BAL #2  J.J. Hardy (X - 21 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c s b")
b3.out("F8")

# 4. BAL #10 Adam Jones (X - 21 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c")
b3.hit(2, rbis=1)
b3.advance(4, "19 HR")

# 5. BAL #19 Chris Davis (X - 10 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c b b b 2")
b3.hit(4, rbis=2)

# 6. BAL #32 Matt Wieters (X - X - X)
b3.new_ab()
b3.pitch_list("b s b b s f f")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #50 Miguel González
t4 = game.new_inning()

# 3. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("B1-3")

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b f b")
t4.out("F8")

# 5. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 7. BAL #35 Danny Valencia (X - X - X)
b4.new_ab()
b4.out("G5-3")

# 8. BAL #28 Steve Pearce (X - X - X)
b4.new_ab()
b4.pitch_list("b c t s")
b4.out("K")

# 9. BAL #12 Alexi Casilla (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #50 Miguel González
t5 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t5.new_ab()
t5.pitch_list("b t b b b")
t5.reach("BB")
t5.thrown_out(2, "16 DP6-4-3", 2, 50)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
t5.new_ab()
t5.pitch_list("b f b c")
t5.out("F9")

# 8. BOS #16 Will Middlebrooks (X - X - 37)
t5.new_ab()
t5.pitch_list("f b b 1")
t5.out("DP6-4-3")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 1. BAL #21 Nick Markakis (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(2)
b5.advance(4, "13 E3")

# 2. BAL #13 Manny Machado (X - 21 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c d")
b5.hit(1, rbis=1)
b5.error(3)
b5.advance(3, "E3")
b5.advance(4, "19 2B")

# 3. BAL #2  J.J. Hardy (13 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b f b f f b s")
b5.out("K")

# 4. BAL #10 Adam Jones (13 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("s d s b f f f s")
b5.out("K")

# 5. BAL #19 Chris Davis (13 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.hit(2, rbis=1)

# 6. BAL #32 Matt Wieters (X - 19 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b s d s c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #50 Miguel González
t6 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b")
t6.hit(1)
t6.advance(2, "10 E5")
t6.advance(3, "29 F7")

# 2. BOS #10 Jose Iglesias (X - X - 2)
t6.new_ab()
t6.pitch_list("c f")
t6.error(5)
t6.reach("E5")

# 3. BOS #29 Daniel Nava (X - 2 - 10)
t6.new_ab(is_risp=True)
t6.pitch_list("f f b")
t6.out("F7")

# 4. BOS #34 David Ortiz (2 - X - 10)
t6.new_ab(is_risp=True)
t6.pitch_list("f b b")
t6.out("G3")


# Bot 6th
# Pitching: BOS #54 Pedro Beato
b6 = game.new_inning()

# Pitching change (BOS): #54 Pedro Beato replaces #31 Jon Lester
b6.pitching_substitution(54)

# 7. BAL #35 Danny Valencia (X - X - X)
b6.new_ab()
b6.pitch_list("b c c b s")
b6.out("K")

# 8. BAL #28 Steve Pearce (X - X - X)
b6.new_ab()
b6.out("F7")

# 9. BAL #12 Alexi Casilla (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("P5")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #50 Miguel González
t7 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("P6")

# 6. BOS #37 Mike Carp (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(2)
t7.advance(3, "39 1B")
# Offensive change (BOS): Pinch-runner #18 Shane Victorino replaces #37 Mike Carp
t7.offensive_substitution(6, 18, "PR")
t7.atbase("PR")
t7.advance(4, "16 HR")

# 7. BOS #39 Jarrod Saltalamacchia (X - 37 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.hit(1)
t7.advance(4, "16 HR")

# 8. BOS #16 Will Middlebrooks (37 - X - 39)
t7.new_ab(is_risp=True)
t7.pitch_list("c b b")
t7.hit(4, rbis=3)

# Pitching change (BAL): #17 Brian Matusz replaces #50 Miguel González
t7.pitching_substitution(17)

# 9. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("s c")
t7.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #54 Pedro Beato
b7.pitching_substitution(36)

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
b7.defensive_switch(29, "3")

# Defensive switch (BOS): #18 Shane Victorino moves to RF
b7.defensive_switch(18, "9")

# 1. BAL #21 Nick Markakis (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.hit(2)
b7.advance(3, "13 SAC5-3")
b7.advance(4, "2 1B")

# 2. BAL #13 Manny Machado (X - 21 - X)
b7.new_ab(is_risp=True)
b7.out("SAC5-3")

# 3. BAL #2  J.J. Hardy (21 - X - X)
b7.new_ab(is_risp=True)
b7.hit(1, rbis=1)
b7.advance(3, "10 2B")

# 4. BAL #10 Adam Jones (X - X - 2)
b7.new_ab()
b7.pitch_list("s b f b f d f")
b7.hit(2)

# Pitching change (BOS): #30 Andrew Miller replaces #36 Junichi Tazawa
b7.pitching_substitution(30)

# 5. BAL #19 Chris Davis (2 - 10 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("s f s")
b7.out("K")

# 6. BAL #32 Matt Wieters (2 - 10 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("f b b s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #17 Brian Matusz
t8 = game.new_inning()

# 2. BOS #10 Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("b c b")
t8.hit(1)

# 3. BOS #29 Daniel Nava (X - X - 10)
t8.new_ab()
t8.pitch_list("f f f f b b")
t8.out("F7")

# 4. BOS #34 David Ortiz (X - X - 10)
t8.new_ab()
t8.pitch_list("f")
t8.out("L9")

# Pitching change (BAL): #29 Tommy Hunter replaces #17 Brian Matusz
t8.pitching_substitution(29)

# 5. BOS #5  Jonny Gomes (X - X - 10)
t8.new_ab()
t8.out("F9")


# Bot 8th
# Pitching: BOS #30 Andrew Miller
b8 = game.new_inning()

# 7. BAL #35 Danny Valencia (X - X - X)
b8.new_ab()
b8.pitch_list("c s f")
b8.hit(1)
b8.thrown_out(2, "28 FC4-6", 1, 30)

# 8. BAL #28 Steve Pearce (X - X - 35)
b8.new_ab()
b8.pitch_list("c")
b8.reach("FC4-6")
# Offensive change (BAL): Pinch-runner #36 Chris Dickerson replaces #28 Steve Pearce
b8.offensive_substitution(8, 36, "PR")
b8.atbase("PR")
b8.advance(3, "21 1B")

# 9. BAL #12 Alexi Casilla (X - X - 28)
b8.new_ab()
b8.out("F9")

# 1. BAL #21 Nick Markakis (X - X - 36)
b8.new_ab()
b8.hit(1)
b8.thrown_out(2, "13 FC6-4", 3, 30)

# 2. BAL #13 Manny Machado (36 - X - 21)
b8.new_ab(is_risp=True)
b8.pitch_list("f b s f")
b8.reach("FC6-4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #43 Jim Johnson
t9 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #29 Tommy Hunter
t9.pitching_substitution(43)

# Defensive switch (BAL): #36 Chris Dickerson moves to LF
t9.defensive_switch(36, "7")

# 6. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G1-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("f s b b f b")
t9.out("G4-3")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.out("F8")

# Winning team: BAL
# WP: BAL #50 Miguel González
game.winning_pitcher(50)
# SV: BAL #43 Jim Johnson
game.save_pitcher(43)

# Loser team: BOS
# LP: BOS #31 Jon Lester
game.losing_pitcher(31, is_away_team=True)

# print(game)
game.generate_scorecard()
