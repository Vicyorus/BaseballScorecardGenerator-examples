import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2013-04-10
# https://www.baseball-reference.com/boxes/BOS/BOS201304100.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2013/04/10/346859/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-10 19:09-22:45 (0:43 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "30,862",
        "temp": "53F, Cloudy",
        "wind": "11mph, In From RF",
        "away": {
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
                3: "Ryan Flaherty",
                14: "Nolan Reimold",
                # Starting pitcher
                34: "Jake Arrieta",
                # Bench
                28: "Steve Pearce",
                31: "Taylor Teagarden",
                60: "Chris Dickerson",
                12: "Alexi Casilla",
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
                [3, "4"],
                [14, "0"],
            ],
            "bench": [
                [28, "1B"],
                [31, "C"],
                [60, "LF"],
                [12, "2B"],
            ],
            "bullpen": [50, 30, 40, 66, 47, 29, 56, 39, 17, 43, 16],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
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
                46: "Ryan Dempster",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                52: "Joel Hanrahan",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
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
            "bullpen": [63, 40, 30, 91, 52, 31, 59, 36, 11, 19, 22],
        },
        "umpires": {
            "HP": "Cory Blaser",
            "1B": "Jim Joyce",
            "2B": "Jim Wolf",
            "3B": "Ed Hickox",
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
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b b f b")
t1.reach("BB")
t1.advance(3, "13 E8")
t1.advance("U", "21 G3")

# 2. BAL #13 Manny Machado (X - X - 9)
t1.new_ab()
t1.pitch_list("c c b f")
t1.error(8)
t1.reach("E8", end_base=2)
t1.advance(3, "21 G3")

# 3. BAL #21 Nick Markakis (9 - 13 - X)
t1.new_ab()
t1.pitch_list("b b c b f")
t1.out("G3", rbis=1)

# 4. BAL #10 Adam Jones (13 - X - X)
t1.new_ab()
t1.pitch_list("f b s b s")
t1.out("K")

# 5. BAL #19 Chris Davis (13 - X - X)
t1.new_ab()
t1.pitch_list("b f c b f c")
t1.out("!K")


# Bot 1st
# Pitching: BAL #34 Jake Arrieta
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c c")
b1.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G1-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c b c c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 6. BAL #32 Matt Wieters (X - X - X)
t2.new_ab()
t2.pitch_list("b s f")
t2.out("G3-1")

# 7. BAL #2  J.J. Hardy (X - X - X)
t2.new_ab()
t2.pitch_list("c f")
t2.out("G6-3")

# 8. BAL #3  Ryan Flaherty (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b f s")
t2.out("K")


# Bot 2nd
# Pitching: BAL #34 Jake Arrieta
b2 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.out("F8")

# 5. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("b c b f f f")
b2.out("F8")

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.advance(4, "39 2B")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
b2.new_ab()
b2.pitch_list("c s")
b2.hit(2, rbis=1)

# 8. BOS #7  Stephen Drew (X - 39 - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 9. BAL #14 Nolan Reimold (X - X - X)
t3.new_ab()
t3.pitch_list("b c b s f")
t3.out("P2")

# 1. BAL #9  Nate McLouth (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G4-3")

# 2. BAL #13 Manny Machado (X - X - X)
t3.new_ab()
t3.pitch_list("c f b")
t3.out("G1-3")


# Bot 3rd
# Pitching: BAL #34 Jake Arrieta
b3 = game.new_inning()

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c s b b b b")
b3.reach("BB")
b3.advance(4, "2 3B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 44)
b3.new_ab()
b3.pitch_list("1")
b3.hit(3, rbis=1)
b3.advance(4, "18 SF7")

# 2. BOS #18 Shane Victorino (2 - X - X)
b3.new_ab()
b3.pitch_list("b b 3 c f")
b3.out("SF7", rbis=1)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.advance(2, "12 BB")

# 4. BOS #12 Mike Napoli (X - X - 15)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.thrown_out(2, "16 DP4-6-3", 2, 34)

# 5. BOS #16 Will Middlebrooks (X - 15 - 12)
b3.new_ab()
b3.pitch_list("c")
b3.out("DP4-6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 3. BAL #21 Nick Markakis (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(4)

# 4. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("c s b f b d")
t4.hit(1)
t4.advance(2, "19 WP")
t4.error(7)
t4.advance("U", "32 E7")

# 5. BAL #19 Chris Davis (X - X - 10)
t4.new_ab()
t4.pitch_list("f b f b b s")
t4.wp()
t4.out("K")

# 6. BAL #32 Matt Wieters (X - 10 - X)
t4.new_ab()
t4.hit(1)
t4.advance(2, "2 BB")

# 7. BAL #2  J.J. Hardy (X - X - 32)
t4.new_ab()
t4.pitch_list("c d b 1 b b")
t4.reach("BB")
t4.thrown_out(2, "14 FC6-4", 3, 46)

# 8. BAL #3  Ryan Flaherty (X - 32 - 2)
t4.new_ab()
t4.pitch_list("c c s")
t4.out("K")

# 9. BAL #14 Nolan Reimold (X - 32 - 2)
t4.new_ab()
t4.pitch_list("s s")
t4.reach("FC6-4")


# Bot 4th
# Pitching: BAL #34 Jake Arrieta
b4 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("c b c b b f")
b4.out("L7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.hit(2)
b4.advance(3, "7 G3-1")

# 8. BOS #7  Stephen Drew (X - 39 - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G3-1")

# 9. BOS #44 Jackie Bradley Jr. (39 - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t5.new_ab()
t5.pitch_list("c s f b s")
t5.out("K")

# 2. BAL #13 Manny Machado (X - X - X)
t5.new_ab()
t5.pitch_list("c b c b s")
t5.out("K")

# 3. BAL #21 Nick Markakis (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G3")


# Bot 5th
# Pitching: BAL #34 Jake Arrieta
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c")
b5.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.out("P6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("f f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #19 Koji Uehara
t6 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #46 Ryan Dempster
t6.pitching_substitution(19)

# 4. BAL #10 Adam Jones (X - X - X)
t6.new_ab()
t6.pitch_list("f s b s")
t6.out("K")

# 5. BAL #19 Chris Davis (X - X - X)
t6.new_ab()
t6.pitch_list("s c b")
t6.out("G1-3")

# 6. BAL #32 Matt Wieters (X - X - X)
t6.new_ab()
t6.pitch_list("f b b")
t6.out("P6")


# Bot 6th
# Pitching: BAL #29 Tommy Hunter
b6 = game.new_inning()

# Pitching change (BAL): #29 Tommy Hunter replaces #34 Jake Arrieta
b6.pitching_substitution(29)

# 4. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b b s")
b6.out("K")

# 5. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("f b b f f f f f f f s")
b6.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.hit(4)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("c b s")
b6.hit(4)

# 8. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #36 Junichi Tazawa
t7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #19 Koji Uehara
t7.pitching_substitution(36)

# 7. BAL #2  J.J. Hardy (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("F7")

# 8. BAL #3  Ryan Flaherty (X - X - X)
t7.new_ab()
t7.pitch_list("b f f b t")
t7.out("KT")

# 9. BAL #14 Nolan Reimold (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c s f s")
t7.out("K")


# Bot 7th
# Pitching: BAL #40 Troy Patton
b7 = game.new_inning()

# Pitching change (BAL): #40 Troy Patton replaces #29 Tommy Hunter
b7.pitching_substitution(40)

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("c f f b")
b7.out("G3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b c f")
b7.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("c c")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #40 Andrew Bailey
t8 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #36 Junichi Tazawa
t8.pitching_substitution(40)

# 1. BAL #9  Nate McLouth (X - X - X)
t8.new_ab()
t8.pitch_list("b f f b b b")
t8.reach("BB")

# 2. BAL #13 Manny Machado (X - X - 9)
t8.new_ab()
t8.pitch_list("b")
t8.out("(F)P3")

# 3. BAL #21 Nick Markakis (X - X - 9)
t8.new_ab()
t8.pitch_list("b s c b s")
t8.out("K")

# 4. BAL #10 Adam Jones (X - X - 9)
t8.new_ab()
t8.pitch_list("f 1 b f d s")
t8.out("K")


# Bot 8th
# Pitching: BAL #56 Darren O'Day
b8 = game.new_inning()

# Pitching change (BAL): #56 Darren O'Day replaces #40 Troy Patton
b8.pitching_substitution(56)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.out("L8")

# 4. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("c s s")
b8.out("K")

# 5. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.pitch_list("c c b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #52 Joel Hanrahan
t9 = game.new_inning()

# Pitching change (BOS): #52 Joel Hanrahan replaces #40 Andrew Bailey
t9.pitching_substitution(52)

# 5. BAL #19 Chris Davis (X - X - X)
t9.new_ab()
t9.pitch_list("f f f b f")
t9.hit(4)

# 6. BAL #32 Matt Wieters (X - X - X)
t9.new_ab()
t9.pitch_list("f f s")
t9.out("K")

# 7. BAL #2  J.J. Hardy (X - X - X)
t9.new_ab()
t9.pitch_list("c s b b")
t9.out("(F)P5")

# 8. BAL #3  Ryan Flaherty (X - X - X)
t9.new_ab()
t9.pitch_list("s b b f")
t9.hit(1)
# Offensive change (BAL): Pinch-runner #12 Alexi Casilla replaces #3 Ryan Flaherty
t9.offensive_substitution(8, 12, "PR")
t9.atbase("PR")
t9.advance(2, "14 SB")
t9.advance(3, "9 BB")
t9.advance(4, "13 WP")

# 9. BAL #14 Nolan Reimold (X - X - 3)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")
# Offensive change (BAL): Pinch-runner #60 Chris Dickerson replaces #14 Nolan Reimold
t9.offensive_substitution(9, 60, "PR")
t9.atbase("PR")
t9.advance(2, "9 BB")
t9.advance(3, "13 WP")
t9.advance(4, "13 HR")

# 1. BAL #9  Nate McLouth (X - 12 - 14)
t9.new_ab()
t9.pitch_list("c b s b f b b")
t9.reach("BB")
t9.advance(2, "13 WP")
t9.advance(4, "13 HR")

# 2. BAL #13 Manny Machado (12 - 60 - 9)
t9.new_ab()
t9.pitch_list("b")
t9.wp()
t9.hit(4, rbis=3)

# Pitching change (BOS): #30 Andrew Miller replaces #52 Joel Hanrahan
t9.pitching_substitution(30)

# 3. BAL #21 Nick Markakis (X - X - X)
t9.new_ab()
t9.pitch_list("c b b c f s")
t9.out("K")


# Bot 9th
# Pitching: BAL #43 Jim Johnson
b9 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #56 Darren O'Day
b9.pitching_substitution(43)

# Defensive switch (BAL): #12 Alexi Casilla moves to 2B
b9.defensive_switch(12, "4")

# Defensive switch (BAL): #60 Chris Dickerson moves to DH
b9.defensive_switch(60, "0")

# 6. BOS #29 Daniel Nava (X - X - X)
b9.new_ab()
b9.pitch_list("c c b f b f f f")
b9.out("F8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b9.new_ab()
b9.pitch_list("b c b s b t")
b9.out("KT")

# 8. BOS #7  Stephen Drew (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("G4-3")

# Winning team: BAL
# WP: BAL #56 Darren O'Day
game.winning_pitcher(56, is_away_team=True)
# SV: BAL #43 Jim Johnson
game.save_pitcher(43, is_away_team=True)

# Loser team: BOS
# LP: BOS #52 Joel Hanrahan
game.losing_pitcher(52)

# print(game)
game.generate_scorecard()
