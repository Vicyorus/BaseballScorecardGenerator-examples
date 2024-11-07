import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2013-04-08
# https://www.baseball-reference.com/boxes/BOS/BOS201304080.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2013/04/08/346834/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-08 14:07-16:49",
        "at": "Fenway Park, Boston, MA",
        "att": "37,008",
        "temp": "59F, Cloudy",
        "wind": "8mph, In From LF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 16,
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
                28: "Steve Pearce",
                # Starting pitcher
                16: "Wei-Yin Chen",
                # Bench
                31: "Taylor Teagarden",
                14: "Nolan Reimold",
                12: "Alexi Casilla",
                # Bullpen
                50: "Miguel González",
                30: "Chris Tillman",
                40: "Troy Patton",
                66: "T.J. McFarland",
                38: "Luis Ayala",
                47: "Pedro Strop",
                29: "Tommy Hunter",
                56: "Darren O'Day",
                39: "Jason Hammel",
                17: "Brian Matusz",
                34: "Jake Arrieta",
                43: "Jim Johnson",
            },
            "lefties": [16, 40, 66, 17],
            "lineup": [
                [9, "7"],
                [13, "5"],
                [21, "9"],
                [10, "8"],
                [19, "3"],
                [32, "2"],
                [2, "6"],
                [3, "4"],
                [28, "0"],
            ],
            "bench": [
                [31, "C"],
                [14, "LF"],
                [12, "2B"],
            ],
            "bullpen": [50, 30, 40, 66, 38, 47, 29, 56, 39, 17, 34, 43],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                16: "Will Middlebrooks",
                29: "Daniel Nava",
                5: "Jonny Gomes",
                3: "David Ross",
                10: "Jose Iglesias",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                23: "Pedro Ciriaco",
                44: "Jackie Bradley Jr.",
                # Bullpen
                40: "Andrew Bailey",
                30: "Andrew Miller",
                19: "Koji Uehara",
                91: "Alfredo Aceves",
                52: "Joel Hanrahan",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
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
                [29, "7"],
                [5, "0"],
                [3, "2"],
                [10, "6"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [23, "3B"],
                [44, "CF"],
            ],
            "bullpen": [40, 30, 19, 91, 52, 31, 59, 36, 22, 46],
        },
        "umpires": {
            "HP": "Ed Hickox",
            "1B": "Cory Blaser",
            "2B": "Jim Joyce",
            "3B": "Jim Wolf",
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
# Pitching: BOS #11 Clay Buchholz
t1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t1.new_ab()
t1.pitch_list("f c b b")
t1.hit(1)

# 2. BAL #13 Manny Machado (X - X - 9)
t1.new_ab()
t1.pitch_list("1 1 1 1")
t1.out("(F)P3")

# 3. BAL #21 Nick Markakis (X - X - 9)
t1.new_ab()
t1.pitch_list("b 1 f")
t1.out("F8")

# 4. BAL #10 Adam Jones (X - X - 9)
t1.new_ab()
t1.pitch_list("b b")
t1.out("F9")


# Bot 1st
# Pitching: BAL #16 Wei-Yin Chen
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b f f b")
b1.out("P4")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c c f")
b1.out("L5")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b f b")
b1.out("G1-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #11 Clay Buchholz
t2 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")

# 6. BAL #32 Matt Wieters (X - X - 19)
t2.new_ab()
t2.pitch_list("c 1 b")
t2.out("F9")

# 7. BAL #2  J.J. Hardy (X - X - 19)
t2.new_ab()
t2.pitch_list("c c b c")
t2.out("!K")

# 8. BAL #3  Ryan Flaherty (X - X - 19)
t2.new_ab()
t2.pitch_list("c s b t")
t2.out("KT")


# Bot 2nd
# Pitching: BAL #16 Wei-Yin Chen
b2 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b c s f")
b2.out("F8")

# 5. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("F9")

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b b")
b2.reach("BB")

# 7. BOS #5  Jonny Gomes (X - X - 29)
b2.new_ab()
b2.pitch_list("b b c c b f f f f")
b2.out("P4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #11 Clay Buchholz
t3 = game.new_inning()

# 9. BAL #28 Steve Pearce (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b")
t3.out("G5-3")

# 1. BAL #9  Nate McLouth (X - X - X)
t3.new_ab()
t3.pitch_list("c f c")
t3.out("!K")

# 2. BAL #13 Manny Machado (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b c")
t3.hit(1)
t3.advance(2, "21 1B")

# 3. BAL #21 Nick Markakis (X - X - 13)
t3.new_ab()
t3.pitch_list("c b s")
t3.hit(1)

# 4. BAL #10 Adam Jones (X - 13 - 21)
t3.new_ab(is_risp=True)
t3.pitch_list("b b s s b c")
t3.out("!K")


# Bot 3rd
# Pitching: BAL #16 Wei-Yin Chen
b3 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.out("F7")

# 9. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #11 Clay Buchholz
t4 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
t4.new_ab()
t4.pitch_list("c b s f b b b")
t4.reach("BB")
t4.thrown_out(2, "32 FC4-6", 1, 11)

# 6. BAL #32 Matt Wieters (X - X - 19)
t4.new_ab()
t4.reach("FC4-6")
t4.thrown_out(2, "2 DP4-6-3", 2, 11)

# 7. BAL #2  J.J. Hardy (X - X - 32)
t4.new_ab()
t4.pitch_list("b")
t4.out("DP4-6-3")


# Bot 4th
# Pitching: BAL #16 Wei-Yin Chen
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.hit(1)
b4.thrown_out(2, "15 CS", 1, 16)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b4.new_ab()
b4.pitch_list("c b 1 1 b b b")
b4.reach("BB")
b4.thrown_out(2, "12 DP4-6-3", 2, 16)

# 4. BOS #12 Mike Napoli (X - X - 15)
b4.new_ab()
b4.pitch_list("f b s")
b4.out("DP4-6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #11 Clay Buchholz
t5 = game.new_inning()

# 8. BAL #3  Ryan Flaherty (X - X - X)
t5.new_ab()
t5.pitch_list("f b b b")
t5.out("G3-1")

# 9. BAL #28 Steve Pearce (X - X - X)
t5.new_ab()
t5.pitch_list("s f s")
t5.out("K")

# 1. BAL #9  Nate McLouth (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c f b")
t5.reach("BB")

# 2. BAL #13 Manny Machado (X - X - 9)
t5.new_ab()
t5.out("F9")


# Bot 5th
# Pitching: BAL #16 Wei-Yin Chen
b5 = game.new_inning()

# 5. BOS #16 Will Middlebrooks (X - X - X)
b5.new_ab()
b5.pitch_list("c s c")
b5.out("!K")

# 6. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("b c f f f")
b5.hit(1)

# 7. BOS #5  Jonny Gomes (X - X - 29)
b5.new_ab()
b5.pitch_list("f f t")
b5.out("KT")

# 8. BOS #3  David Ross (X - X - 29)
b5.new_ab()
b5.pitch_list("b b b f s")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #11 Clay Buchholz
t6 = game.new_inning()

# 3. BAL #21 Nick Markakis (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G3-1")

# 4. BAL #10 Adam Jones (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b b")
t6.out("L9")

# 5. BAL #19 Chris Davis (X - X - X)
t6.new_ab()
t6.pitch_list("b b f f c")
t6.out("!K")


# Bot 6th
# Pitching: BAL #16 Wei-Yin Chen
b6 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("c f b")
b6.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f")
b6.out("L8")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("b c b")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #11 Clay Buchholz
t7 = game.new_inning()

# 6. BAL #32 Matt Wieters (X - X - X)
t7.new_ab()
t7.pitch_list("b s b f b f f f b")
t7.reach("BB")
t7.advance(2, "3 G4-3")

# 7. BAL #2  J.J. Hardy (X - X - 32)
t7.new_ab()
t7.pitch_list("c s b c")
t7.out("!K")

# 8. BAL #3  Ryan Flaherty (X - X - 32)
t7.new_ab()
t7.pitch_list("f f b b")
t7.out("G4-3")

# 9. BAL #28 Steve Pearce (X - 32 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b b c f s")
t7.out("K")


# Bot 7th
# Pitching: BAL #16 Wei-Yin Chen
b7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.hit(1)
b7.advance(3, "12 2B")
b7.advance(4, "29 HR")

# 4. BOS #12 Mike Napoli (X - X - 15)
b7.new_ab()
b7.pitch_list("f b s f b 1 f")
b7.hit(2)
b7.advance(4, "29 HR")

# 5. BOS #16 Will Middlebrooks (15 - 12 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("f f b f f b s")
b7.out("K")

# 6. BOS #29 Daniel Nava (15 - 12 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f")
b7.hit(4, rbis=3)

# Pitching change (BAL): #29 Tommy Hunter replaces #16 Wei-Yin Chen
b7.pitching_substitution(29)

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #5 Jonny Gomes, batting 7th
b7.offensive_substitution(7, 37, "PH")

# 7. BOS #37 Mike Carp (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G5-3")

# 8. BOS #3  David Ross (X - X - X)
b7.new_ab()
b7.pitch_list("b f b s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #40 Andrew Bailey
t8 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #11 Clay Buchholz
t8.pitching_substitution(40)

# Defensive switch (BOS): #37 Mike Carp moves to DH
t8.defensive_switch(37, "0")

# 1. BAL #9  Nate McLouth (X - X - X)
t8.new_ab()
t8.pitch_list("c b c b f c")
t8.out("!K")

# 2. BAL #13 Manny Machado (X - X - X)
t8.new_ab()
t8.pitch_list("b c c f f s")
t8.out("K")

# 3. BAL #21 Nick Markakis (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("F8")


# Bot 8th
# Pitching: BAL #29 Tommy Hunter
b8 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b8.new_ab()
b8.pitch_list("b f c f")
b8.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("c b f")
b8.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #52 Joel Hanrahan
t9 = game.new_inning()

# Pitching change (BOS): #52 Joel Hanrahan replaces #40 Andrew Bailey
t9.pitching_substitution(52)

# 4. BAL #10 Adam Jones (X - X - X)
t9.new_ab()
t9.pitch_list("c b s")
t9.hit(4)

# 5. BAL #19 Chris Davis (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G3-1")

# 6. BAL #32 Matt Wieters (X - X - X)
t9.new_ab()
t9.pitch_list("b c c b s")
t9.out("K")

# 7. BAL #2  J.J. Hardy (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(2)

# 8. BAL #3  Ryan Flaherty (X - 2 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b b")
t9.out("(F)P5")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11)
# SV: BOS #52 Joel Hanrahan
game.save_pitcher(52)

# Loser team: BAL
# LP: BAL #16 Wei-Yin Chen
game.losing_pitcher(16, is_away_team=True)

# print(game)
game.generate_scorecard()
