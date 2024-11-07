import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2013-04-07
# https://www.baseball-reference.com/boxes/TOR/TOR201304070.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2013/04/07/346831/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-07 13:08-15:52",
        "at": "Rogers Centre, Toronto, ON",
        "att": "41,168",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                16: "Will Middlebrooks",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                44: "Jackie Bradley Jr.",
                10: "Jose Iglesias",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                3: "David Ross",
                37: "Mike Carp",
                23: "Pedro Ciriaco",
                5: "Jonny Gomes",
                # Bullpen
                40: "Andrew Bailey",
                30: "Andrew Miller",
                19: "Koji Uehara",
                91: "Alfredo Aceves",
                52: "Joel Hanrahan",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
                11: "Clay Buchholz",
            },
            "lefties": [31, 30, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "0"],
                [16, "5"],
                [29, "3"],
                [39, "2"],
                [44, "7"],
                [10, "6"],
            ],
            "bench": [
                [3, "C"],
                [37, "1B"],
                [23, "3B"],
                [5, "LF"],
            ],
            "bullpen": [40, 30, 19, 91, 52, 59, 36, 22, 46, 11],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 43,
            "roster": {
                # Lineup
                7: "José Reyes",
                11: "Rajai Davis",
                53: "Melky Cabrera",
                10: "Edwin Encarnación",
                9: "J.P. Arencibia",
                16: "Mark DeRosa",
                3: "Maicer Izturis",
                22: "Henry Blanco",
                1: "Emilio Bonifácio",
                # Starting pitcher
                43: "R.A. Dickey",
                # Bench
                26: "Adam Lind",
                28: "Colby Rasmus",
                19: "José Bautista",
                # Bullpen
                62: "Aaron Loup",
                50: "Steve Delabar",
                56: "Mark Buehrle",
                55: "Josh Johnson",
                54: "Dave Bush",
                38: "Darren Oliver",
                23: "Brandon Morrow",
                27: "Brett Cecil",
                21: "Sergio Santos",
                48: "J.A. Happ",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [62, 56, 38, 27, 48],
            "lineup": [
                [7, "6"],
                [11, "9"],
                [53, "7"],
                [10, "3"],
                [9, "0"],
                [16, "5"],
                [3, "4"],
                [22, "2"],
                [1, "8"],
            ],
            "bench": [
                [26, "1B"],
                [28, "CF"],
                [19, "RF"],
            ],
            "bullpen": [62, 50, 56, 55, 54, 38, 23, 27, 21, 48, 44, 32],
        },
        "umpires": {
            "HP": "Bob Davidson",
            "1B": "Jim Reynolds",
            "2B": "James Hoye",
            "3B": "John Hirschbeck",
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
# Pitching: TOR #43 R.A. Dickey
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(2)
t1.advance(3, "18 1B")
t1.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (X - 2 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("l b f b")
t1.hit(1)
t1.advance(2, "15 1B")
t1.advance(4, "12 2B")

# 3. BOS #15 Dustin Pedroia (2 - X - 18)
t1.new_ab(is_risp=True)
t1.pitch_list("1 s s f")
t1.hit(1, rbis=1)
t1.advance(4, "12 2B")

# 4. BOS #12 Mike Napoli (X - 18 - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("b s b c f f")
t1.hit(2, rbis=2)
t1.advance(4, "16 HR")

# 5. BOS #16 Will Middlebrooks (X - 12 - X)
t1.new_ab(is_risp=True)
t1.hit(4, rbis=2)

# 6. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("F7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("L9")

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("b c s b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G4-3")

# 2. TOR #11 Rajai Davis (X - X - X)
b1.new_ab()
b1.pitch_list("c f s")
b1.out("K")

# 3. TOR #53 Melky Cabrera (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #43 R.A. Dickey
t2 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t2.new_ab()
t2.pitch_list("b b f c")
t2.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
t2.new_ab()
t2.pitch_list("1 f b f")
t2.out("P5")

# 2. BOS #18 Shane Victorino (X - X - 10)
t2.new_ab()
t2.pitch_list("1 b c f s")
t2.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - 10)
t2.new_ab()
t2.pitch_list("f s b s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
b2.new_ab()
b2.pitch_list("c c s")
b2.out("K")

# 5. TOR #9  J.P. Arencibia (X - X - X)
b2.new_ab()
b2.hit(1)
b2.advance(2, "3 1B")

# 6. TOR #16 Mark DeRosa (X - X - 9)
b2.new_ab()
b2.pitch_list("b")
b2.out("F9")

# 7. TOR #3  Maicer Izturis (X - X - 9)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)

# 8. TOR #22 Henry Blanco (X - 9 - 3)
b2.new_ab(is_risp=True)
b2.pitch_list("s s f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #43 R.A. Dickey
t3 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c s c")
t3.out("!K")

# 5. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(2)
t3.advance(3, "29 PB")
t3.advance("U", "29 SF9")

# 6. BOS #29 Daniel Nava (X - 16 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b c f")
t3.pb()
t3.out("SF9", rbis=1)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.out("F8")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 9. TOR #1  Emilio Bonifácio (X - X - X)
b3.new_ab()
b3.pitch_list("b c b s f c")
b3.out("!K")

# 1. TOR #7  José Reyes (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.thrown_out(2, "11 FC5-4", 2, 31)

# 2. TOR #11 Rajai Davis (X - X - 7)
b3.new_ab()
b3.pitch_list("b")
b3.reach("FC5-4")

# 3. TOR #53 Melky Cabrera (X - X - 11)
b3.new_ab()
b3.pitch_list("b")
b3.out("(F)P3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #43 R.A. Dickey
t4 = game.new_inning()

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.out("G2-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
t4.new_ab()
t4.pitch_list("b b f b")
t4.hit(2)
t4.advance(4, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 10 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b t")
t4.hit(1, rbis=1)
t4.advance(2, "T")
t4.advance(3, "12 SB")

# 2. BOS #18 Shane Victorino (X - 2 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b c b b")
t4.reach("BB")
t4.advance(2, "12 SB")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t4.new_ab(is_risp=True)
t4.pitch_list("c f s")
t4.out("K")

# 4. BOS #12 Mike Napoli (X - 2 - 18)
t4.new_ab(is_risp=True)
t4.pitch_list("c f f d")
t4.out("G1-3")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("G6-3")

# 5. TOR #9  J.P. Arencibia (X - X - X)
b4.new_ab()
b4.pitch_list("c f s")
b4.out("K")

# 6. TOR #16 Mark DeRosa (X - X - X)
b4.new_ab()
b4.pitch_list("b b c f b f f f")
b4.reach("HBP")

# 7. TOR #3  Maicer Izturis (X - X - 16)
b4.new_ab()
b4.pitch_list("c b")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #43 R.A. Dickey
t5 = game.new_inning()

# 5. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c s")
t5.hit(4)

# 6. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("L3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("c b b")
t5.out("G5-3")

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c s b b b b")
t5.reach("BB")

# Pitching change (TOR): #54 Dave Bush replaces #43 R.A. Dickey
t5.pitching_substitution(54)

# 9. BOS #10 Jose Iglesias (X - X - 44)
t5.new_ab()
t5.pitch_list("f b")
t5.out("F9")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 8. TOR #22 Henry Blanco (X - X - X)
b5.new_ab()
b5.pitch_list("b f b c b")
b5.out("F8")

# 9. TOR #1  Emilio Bonifácio (X - X - X)
b5.new_ab()
b5.pitch_list("s c b f")
b5.hit(1)
b5.advance(2, "7 G5-3")

# 1. TOR #7  José Reyes (X - X - 1)
b5.new_ab()
b5.out("G5-3")

# 2. TOR #11 Rajai Davis (X - 1 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b f b f f f")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #54 Dave Bush
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("c s")
t6.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("b c c")
t6.hit(1)

# 4. BOS #12 Mike Napoli (X - X - 15)
t6.new_ab()
t6.pitch_list("c f f")
t6.out("F9")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 3. TOR #53 Melky Cabrera (X - X - X)
b6.new_ab()
b6.pitch_list("c f b")
b6.out("(F)P3")

# 4. TOR #10 Edwin Encarnación (X - X - X)
b6.new_ab()
b6.pitch_list("b c c b")
b6.out("F7")

# 5. TOR #9  J.P. Arencibia (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #54 Dave Bush
t7 = game.new_inning()

# 5. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c")
t7.hit(4)

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(4)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("c b c f c")
t7.out("!K")

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G6-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("F7")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# 6. TOR #16 Mark DeRosa (X - X - X)
b7.new_ab()
b7.pitch_list("t s b s")
b7.out("K")

# 7. TOR #3  Maicer Izturis (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G4-3")

# 8. TOR #22 Henry Blanco (X - X - X)
b7.new_ab()
b7.pitch_list("b b f f")
b7.hit(1)

# 9. TOR #1  Emilio Bonifácio (X - X - 22)
b7.new_ab()
b7.pitch_list("b f c")
b7.out("L4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #54 Dave Bush
t8 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c f b f f f b b")
t8.hit(4)

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #18 Shane Victorino, batting 2nd
t8.offensive_substitution(2, 37, "PH")

# 2. BOS #37 Mike Carp (X - X - X)
t8.new_ab()
t8.out("L6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("b f b b b")
t8.reach("BB")
t8.advance(4, "12 HR")

# 4. BOS #12 Mike Napoli (X - X - 15)
t8.new_ab()
t8.pitch_list("b b")
t8.hit(4, rbis=2)

# 5. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.out("F7")

# Pitching change (TOR): #27 Brett Cecil replaces #54 Dave Bush
t8.pitching_substitution(27)

# 6. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t8.new_ab()
t8.pitch_list("c")
t8.out("F9")


# Bot 8th
# Pitching: BOS #59 Clayton Mortensen
b8 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #31 Jon Lester
b8.pitching_substitution(59)

# Defensive switch (BOS): #37 Mike Carp moves to 1B
b8.defensive_switch(37, "3")

# Defensive change (BOS): #23 Pedro Ciriaco replaces #15 Dustin Pedroia (2B), playing 2B, batting 3rd
b8.defensive_substitution(3, 23, "4")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
b8.defensive_switch(29, "9")

# 1. TOR #7  José Reyes (X - X - X)
b8.new_ab()
b8.pitch_list("c s")
b8.hit(1)
b8.thrown_out(2, "11 FC6-4", 1, 59)

# 2. TOR #11 Rajai Davis (X - X - 7)
b8.new_ab()
b8.pitch_list("b")
b8.reach("FC6-4")

# 3. TOR #53 Melky Cabrera (X - X - 11)
b8.new_ab()
b8.pitch_list("f b f d b c")
b8.out("!K")

# 4. TOR #10 Edwin Encarnación (X - X - 11)
b8.new_ab()
b8.pitch_list("s f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #27 Brett Cecil
t9 = game.new_inning()

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("b c c s")
t9.out("K")

# 9. BOS #10 Jose Iglesias (X - X - X)
t9.new_ab()
t9.pitch_list("b c b b c s")
t9.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")


# Bot 9th
# Pitching: BOS #59 Clayton Mortensen
b9 = game.new_inning()

# 5. TOR #9  J.P. Arencibia (X - X - X)
b9.new_ab()
b9.pitch_list("b b f c s")
b9.out("K")

# 6. TOR #16 Mark DeRosa (X - X - X)
b9.new_ab()
b9.pitch_list("b b f s b")
b9.out("G6-3")

# 7. TOR #3  Maicer Izturis (X - X - X)
b9.new_ab()
b9.pitch_list("s b b")
b9.hit(1)

# 8. TOR #22 Henry Blanco (X - X - 3)
b9.new_ab()
b9.pitch_list("f s d b f c")
b9.out("!K")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31, is_away_team=True)

# Loser team: TOR
# LP: TOR #43 R.A. Dickey
game.losing_pitcher(43)

# print(game)
game.generate_scorecard()
