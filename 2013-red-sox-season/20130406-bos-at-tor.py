import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2013-04-06
# https://www.baseball-reference.com/boxes/TOR/TOR201304060.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2013/04/06/346817/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-06 13:07-15:45",
        "at": "Rogers Centre, Toronto, ON",
        "att": "45,797",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                16: "Will Middlebrooks",
                5: "Jonny Gomes",
                3: "David Ross",
                44: "Jackie Bradley Jr.",
                23: "Pedro Ciriaco",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                10: "Jose Iglesias",
                # Bullpen
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
                46: "Ryan Dempster",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [16, "5"],
                [5, "0"],
                [3, "2"],
                [44, "7"],
                [23, "6"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
                [10, "2B"],
            ],
            "bullpen": [40, 30, 91, 52, 31, 59, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 48,
            "roster": {
                # Lineup
                7: "José Reyes",
                11: "Rajai Davis",
                53: "Melky Cabrera",
                10: "Edwin Encarnación",
                26: "Adam Lind",
                9: "J.P. Arencibia",
                16: "Mark DeRosa",
                28: "Colby Rasmus",
                1: "Emilio Bonifácio",
                # Starting pitcher
                48: "J.A. Happ",
                # Bench
                3: "Maicer Izturis",
                22: "Henry Blanco",
                19: "José Bautista",
                # Bullpen
                43: "R.A. Dickey",
                62: "Aaron Loup",
                50: "Steve Delabar",
                56: "Mark Buehrle",
                55: "Josh Johnson",
                54: "Dave Bush",
                38: "Darren Oliver",
                23: "Brandon Morrow",
                27: "Brett Cecil",
                21: "Sergio Santos",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [48, 62, 56, 38, 27],
            "lineup": [
                [7, "6"],
                [11, "9"],
                [53, "7"],
                [10, "3"],
                [26, "0"],
                [9, "2"],
                [16, "5"],
                [28, "8"],
                [1, "4"],
            ],
            "bench": [
                [3, "3B"],
                [22, "C"],
                [19, "RF"],
            ],
            "bullpen": [43, 62, 50, 56, 55, 54, 38, 23, 27, 21, 44, 32],
        },
        "umpires": {
            "HP": "John Hirschbeck",
            "1B": "Bob Davidson",
            "2B": "Jim Reynolds",
            "3B": "James Hoye",
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
# Pitching: TOR #48 J.A. Happ
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c c b b b")
t1.hit(2)
t1.advance(3, "12 SB")

# 2. BOS #18 Shane Victorino (X - 2 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b s f f")
t1.out("P4")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c d b s s")
t1.out("K")

# 4. BOS #12 Mike Napoli (X - 2 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b c b b c c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.hit(1)
b1.advance(2, "11 SB")

# 2. TOR #11 Rajai Davis (X - X - 7)
b1.new_ab(is_risp=True)
b1.pitch_list("b c f b b c")
b1.out("!K")

# 3. TOR #53 Melky Cabrera (X - 7 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("f b b c b f f")
b1.out("G1-3")

# 4. TOR #10 Edwin Encarnación (X - 7 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #48 J.A. Happ
t2 = game.new_inning()

# 5. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("b c b s b")
t2.out("F9")

# 6. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("c c f")
t2.out("G6-3")

# 7. BOS #3  David Ross (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G6-3")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 5. TOR #26 Adam Lind (X - X - X)
b2.new_ab()
b2.pitch_list("c b c")
b2.out("G1-3")

# 6. TOR #9  J.P. Arencibia (X - X - X)
b2.new_ab()
b2.pitch_list("c b s b c")
b2.out("!K")

# 7. TOR #16 Mark DeRosa (X - X - X)
b2.new_ab()
b2.pitch_list("c b s s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #48 J.A. Happ
t3 = game.new_inning()

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c b s b b s")
t3.out("K")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(3, "2 WP")
t3.thrown_out(4, "2 FC3-2", 2, 48)

# 1. BOS #2  Jacoby Ellsbury (X - X - 23)
t3.new_ab(is_risp=True)
t3.pitch_list("c c b")
t3.wp()
t3.reach("FC3-2")
t3.advance(2, "18 SB")

# 2. BOS #18 Shane Victorino (X - X - 2)
t3.new_ab(is_risp=True)
t3.pitch_list("1 b b b b")
t3.reach("BB")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t3.new_ab(is_risp=True)
t3.pitch_list("c f f b b b")
t3.out("(F)P5")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 8. TOR #28 Colby Rasmus (X - X - X)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")

# 9. TOR #1  Emilio Bonifácio (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c c")
b3.out("G3")

# 1. TOR #7  José Reyes (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.hit(1)
b3.advance(2, "11 1B")

# 2. TOR #11 Rajai Davis (X - X - 7)
b3.new_ab()
b3.pitch_list("1 1")
b3.hit(1)

# 3. TOR #53 Melky Cabrera (X - 7 - 11)
b3.new_ab(is_risp=True)
b3.pitch_list("b b c c s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #48 J.A. Happ
t4 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("b s c s")
t4.out("K")

# 5. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("c f s")
t4.out("K")

# 6. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("f c b b s")
t4.out("K")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("L9")

# 5. TOR #26 Adam Lind (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)
b4.advance(4, "9 HR")

# 6. TOR #9  J.P. Arencibia (X - X - 26)
b4.new_ab()
b4.pitch_list("b c b")
b4.hit(4, rbis=2)

# 7. TOR #16 Mark DeRosa (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("G1-3")

# 8. TOR #28 Colby Rasmus (X - X - X)
b4.new_ab()
b4.pitch_list("s c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #48 J.A. Happ
t5 = game.new_inning()

# 7. BOS #3  David Ross (X - X - X)
t5.new_ab()
t5.pitch_list("f s")
t5.out("F9")

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b")
t5.out("G3")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t5.new_ab()
t5.pitch_list("c b s b f b f")
t5.out("L9")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 9. TOR #1  Emilio Bonifácio (X - X - X)
b5.new_ab()
b5.pitch_list("c f c")
b5.out("!K")

# Pitching change (BOS): #91 Alfredo Aceves replaces #41 John Lackey
b5.pitching_substitution(91)

# 1. TOR #7  José Reyes (X - X - X)
b5.new_ab()
b5.pitch_list("c b f b f b b")
b5.reach("BB")
b5.advance(2, "53 1B")

# 2. TOR #11 Rajai Davis (X - X - 7)
b5.new_ab()
b5.pitch_list("b c 1 f")
b5.out("F9")

# 3. TOR #53 Melky Cabrera (X - X - 7)
b5.new_ab()
b5.pitch_list("1")
b5.hit(1)

# 4. TOR #10 Edwin Encarnación (X - 7 - 53)
b5.new_ab(is_risp=True)
b5.pitch_list("c")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #48 J.A. Happ
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("b c f b")
t6.out("L7")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("b b c f f b b")
t6.reach("BB")
t6.thrown_out(2, "15 CS", 2, 50)

# Pitching change (TOR): #50 Steve Delabar replaces #48 J.A. Happ
t6.pitching_substitution(50)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t6.new_ab()
t6.pitch_list("b s s s")
t6.out("K")


# Bot 6th
# Pitching: BOS #91 Alfredo Aceves
b6 = game.new_inning()

# 5. TOR #26 Adam Lind (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")
b6.advance(2, "16 SB")
b6.advance(4, "28 HR")

# 6. TOR #9  J.P. Arencibia (X - X - 26)
b6.new_ab()
b6.pitch_list("f s c")
b6.out("!K")

# 7. TOR #16 Mark DeRosa (X - X - 26)
b6.new_ab(is_risp=True)
b6.pitch_list("s b b f d b")
b6.reach("BB")
b6.advance(4, "28 HR")

# 8. TOR #28 Colby Rasmus (X - 26 - 16)
b6.new_ab(is_risp=True)
b6.pitch_list("b 2 b")
b6.hit(4, rbis=3)

# 9. TOR #1  Emilio Bonifácio (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.out("F7")

# 1. TOR #7  José Reyes (X - X - X)
b6.new_ab()
b6.pitch_list("f f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #50 Steve Delabar
t7 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("c s f s")
t7.out("K")

# 5. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("s")
t7.out("F9")

# 6. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #91 Alfredo Aceves
b7 = game.new_inning()

# 2. TOR #11 Rajai Davis (X - X - X)
b7.new_ab()
b7.out("F9")

# 3. TOR #53 Melky Cabrera (X - X - X)
b7.new_ab()
b7.pitch_list("b c f b s")
b7.out("K")

# 4. TOR #10 Edwin Encarnación (X - X - X)
b7.new_ab()
b7.pitch_list("c c c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #62 Aaron Loup
t8 = game.new_inning()

# Pitching change (TOR): #62 Aaron Loup replaces #50 Steve Delabar
t8.pitching_substitution(62)

# 7. BOS #3  David Ross (X - X - X)
t8.new_ab()
t8.pitch_list("b b c f c")
t8.out("!K")

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("c f c")
t8.out("!K")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G1-3")


# Bot 8th
# Pitching: BOS #91 Alfredo Aceves
b8 = game.new_inning()

# 5. TOR #26 Adam Lind (X - X - X)
b8.new_ab()
b8.out("F7")

# 6. TOR #9  J.P. Arencibia (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b")
b8.hit(2)

# 7. TOR #16 Mark DeRosa (X - 9 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c s d c")
b8.out("!K")

# 8. TOR #28 Colby Rasmus (X - 9 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c c b")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #21 Sergio Santos
t9 = game.new_inning()

# Pitching change (TOR): #21 Sergio Santos replaces #62 Aaron Loup
t9.pitching_substitution(21)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("c b f b b")
t9.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("b b c s c")
t9.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)

# 4. BOS #12 Mike Napoli (X - X - 15)
t9.new_ab()
t9.out("F8")

# Winning team: TOR
# WP: TOR #48 J.A. Happ
game.winning_pitcher(48)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
