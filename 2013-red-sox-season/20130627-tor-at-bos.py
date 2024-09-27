import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2013-06-27
# https://www.baseball-reference.com/boxes/BOS/BOS201306270.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2013/06/27/347926/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-27 19:11-21:45",
        "at": "Fenway Park, Boston, MA",
        "att": "34,750",
        "temp": "64F, Cloudy",
        "wind": "7mph, In From RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 67,
            "roster": {
                # Lineup
                7: "José Reyes",
                19: "José Bautista",
                10: "Edwin Encarnación",
                16: "Mark DeRosa",
                53: "Melky Cabrera",
                9: "J.P. Arencibia",
                11: "Rajai Davis",
                3: "Maicer Izturis",
                1: "Emilio Bonifácio",
                # Starting pitcher
                67: "Chien-Ming Wang",
                # Bench
                26: "Adam Lind",
                28: "Colby Rasmus",
                22: "Josh Thole",
                # Bullpen
                43: "R.A. Dickey",
                45: "Neil Wagner",
                62: "Aaron Loup",
                57: "Juan Pablo Perez",
                50: "Steve Delabar",
                56: "Mark Buehrle",
                55: "Josh Johnson",
                38: "Darren Oliver",
                29: "Dustin McGowan",
                27: "Brett Cecil",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [62, 57, 56, 38, 27],
            "lineup": [
                [7, "6"],
                [19, "9"],
                [10, "3"],
                [16, "0"],
                [53, "7"],
                [9, "2"],
                [11, "8"],
                [3, "5"],
                [1, "4"],
            ],
            "bench": [
                [26, "1B"],
                [28, "CF"],
                [22, "C"],
            ],
            "bullpen": [43, 45, 62, 57, 50, 56, 55, 38, 29, 27, 44, 32],
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
                37: "Mike Carp",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                5: "Jonny Gomes",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                64: "Allen Webster",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 30, 32, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [37, "3"],
                [29, "7"],
                [39, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [5, "LF"],
                [12, "1B"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [63, 40, 41, 30, 32, 59, 36, 64, 19, 22, 46],
        },
        "umpires": {
            "HP": "Mike Everitt",
            "1B": "Bruce Dreckman",
            "2B": "Dan Bellino",
            "3B": "Tim Welke",
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

# 1. TOR #7  José Reyes (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b f b")
t1.reach("BB")
t1.thrown_out(2, "10 DP6-4-3", 2, 31)

# 2. TOR #19 José Bautista (X - X - 7)
t1.new_ab()
t1.pitch_list("b b b c")
t1.out("F7")

# 3. TOR #10 Edwin Encarnación (X - X - 7)
t1.new_ab()
t1.pitch_list("s d")
t1.out("DP6-4-3")


# Bot 1st
# Pitching: TOR #67 Chien-Ming Wang
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.out("G3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c f b")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 4. TOR #16 Mark DeRosa (X - X - X)
t2.new_ab()
t2.out("G6-3")

# 5. TOR #53 Melky Cabrera (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("L5")

# 6. TOR #9  J.P. Arencibia (X - X - X)
t2.new_ab()
t2.pitch_list("f b b f s")
t2.out("K")


# Bot 2nd
# Pitching: TOR #67 Chien-Ming Wang
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b f d")
b2.reach("BB")
b2.advance(2, "37 BB")
b2.advance(4, "29 1B")

# 5. BOS #37 Mike Carp (X - X - 34)
b2.new_ab()
b2.pitch_list("b f b b f b")
b2.reach("BB")
b2.advance(3, "29 1B")
b2.advance(4, "39 1B")

# 6. BOS #29 Daniel Nava (X - 34 - 37)
b2.new_ab()
b2.pitch_list("c f b")
b2.hit(1, rbis=1)
b2.advance(2, "39 1B")
b2.advance(4, "7 2B")

# 7. BOS #39 Jarrod Saltalamacchia (37 - X - 29)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1, rbis=1)
b2.advance(3, "7 2B")
b2.advance(4, "10 1B")

# 8. BOS #7  Stephen Drew (X - 29 - 39)
b2.new_ab()
b2.pitch_list("c c d f d")
b2.hit(2, rbis=1)
b2.advance(4, "2 1B")

# 9. BOS #10 Jose Iglesias (39 - 7 - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1, rbis=1)
b2.advance(2, "2 1B")
b2.advance(3, "18 DP4-6-3")
b2.advance(4, "15 HR")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - 10)
b2.new_ab()
b2.pitch_list("f")
b2.hit(1, rbis=1)
b2.thrown_out(2, "18 DP4-6-3", 1, 67)

# 2. BOS #18 Shane Victorino (X - 10 - 2)
b2.new_ab()
b2.pitch_list("b c b f")
b2.out("DP4-6-3")

# 3. BOS #15 Dustin Pedroia (10 - X - X)
b2.new_ab()
b2.pitch_list("s f")
b2.hit(4, rbis=2)

# Pitching change (TOR): #62 Aaron Loup replaces #67 Chien-Ming Wang
b2.pitching_substitution(62)

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("b c s b b")
b2.hit(1)

# 5. BOS #37 Mike Carp (X - X - 34)
b2.new_ab()
b2.pitch_list("b f f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 7. TOR #11 Rajai Davis (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")

# 8. TOR #3  Maicer Izturis (X - X - X)
t3.new_ab()
t3.pitch_list("c c t")
t3.out("KT")

# 9. TOR #1  Emilio Bonifácio (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")


# Bot 3rd
# Pitching: TOR #62 Aaron Loup
b3 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G4-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("c c b")
b3.out("F8")

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t4.new_ab()
t4.pitch_list("c b f")
t4.out("G6-3")

# 2. TOR #19 José Bautista (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b f b")
t4.reach("BB")
t4.thrown_out(2, "10 DP6-4-3", 2, 31)

# 3. TOR #10 Edwin Encarnación (X - X - 19)
t4.new_ab()
t4.pitch_list("c b b b")
t4.out("DP6-4-3")


# Bot 4th
# Pitching: TOR #57 Juan Pablo Perez
b4 = game.new_inning()

# Pitching change (TOR): #57 Juan Pablo Perez replaces #62 Aaron Loup
b4.pitching_substitution(57)

# 9. BOS #10 Jose Iglesias (X - X - X)
b4.new_ab()
b4.pitch_list("c f")
b4.out("L4")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b4.new_ab()
b4.pitch_list("c b s f s")
b4.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 4. TOR #16 Mark DeRosa (X - X - X)
t5.new_ab()
t5.pitch_list("c f f b b s")
t5.out("K")

# 5. TOR #53 Melky Cabrera (X - X - X)
t5.new_ab()
t5.pitch_list("b c c f")
t5.hit(1)
t5.advance(2, "11 1B")
t5.advance(4, "3 2B")

# 6. TOR #9  J.P. Arencibia (X - X - 53)
t5.new_ab()
t5.pitch_list("d")
t5.out("F8")

# 7. TOR #11 Rajai Davis (X - X - 53)
t5.new_ab()
t5.pitch_list("d s b")
t5.hit(1)
t5.advance(4, "3 2B")

# 8. TOR #3  Maicer Izturis (X - 53 - 11)
t5.new_ab()
t5.pitch_list("f s")
t5.hit(2, rbis=2)

# 9. TOR #1  Emilio Bonifácio (X - 3 - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("P6")


# Bot 5th
# Pitching: TOR #57 Juan Pablo Perez
b5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G4-3")

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b s")
b5.out("K")

# 5. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t6.new_ab()
t6.out("G5-3")

# 2. TOR #19 José Bautista (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G4-3")

# 3. TOR #10 Edwin Encarnación (X - X - X)
t6.new_ab()
t6.pitch_list("f c b f b b s")
t6.out("K")


# Bot 6th
# Pitching: TOR #57 Juan Pablo Perez
b6 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("c c b")
b6.out("G6-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.out("G5-3")

# 8. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("b c c f b f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #31 Jon Lester
t7 = game.new_inning()

# 4. TOR #16 Mark DeRosa (X - X - X)
t7.new_ab()
t7.pitch_list("s c b b s")
t7.out("K")

# 5. TOR #53 Melky Cabrera (X - X - X)
t7.new_ab()
t7.out("F9")

# 6. TOR #9  J.P. Arencibia (X - X - X)
t7.new_ab()
t7.out("P6")


# Bot 7th
# Pitching: TOR #27 Brett Cecil
b7 = game.new_inning()

# Pitching change (TOR): #27 Brett Cecil replaces #57 Juan Pablo Perez
b7.pitching_substitution(27)

# 9. BOS #10 Jose Iglesias (X - X - X)
b7.new_ab()
b7.pitch_list("c c f b s")
b7.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.out("(F)P5")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("s")
b7.hit(2)

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b7.new_ab()
b7.pitch_list("b b b c c d")
b7.reach("BB")

# 4. BOS #34 David Ortiz (X - 18 - 15)
b7.new_ab()
b7.pitch_list("f b b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #31 Jon Lester
t8 = game.new_inning()

# 7. TOR #11 Rajai Davis (X - X - X)
t8.new_ab()
t8.pitch_list("c b s")
t8.hit(1)
t8.advance(2, "3 1B")
t8.advance(3, "1 BB")
t8.advance(4, "7 SF8")

# 8. TOR #3  Maicer Izturis (X - X - 11)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(1)
t8.advance(2, "1 BB")
t8.advance(3, "19 WP")
t8.advance(4, "19 G6-3")

# Pitching change (BOS): #36 Junichi Tazawa replaces #31 Jon Lester
t8.pitching_substitution(36)

# 9. TOR #1  Emilio Bonifácio (X - 11 - 3)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
t8.advance(2, "19 WP")
t8.advance(3, "19 G6-3")

# 1. TOR #7  José Reyes (11 - 3 - 1)
t8.new_ab()
t8.pitch_list("c b")
t8.out("SF8", rbis=1)

# 2. TOR #19 José Bautista (X - 3 - 1)
t8.new_ab()
t8.pitch_list("c b")
t8.wp()
t8.out("G6-3", rbis=1)

# 3. TOR #10 Edwin Encarnación (1 - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.out("L7")


# Bot 8th
# Pitching: TOR #50 Steve Delabar
b8 = game.new_inning()

# Pitching change (TOR): #50 Steve Delabar replaces #27 Brett Cecil
b8.pitching_substitution(50)

# 5. BOS #37 Mike Carp (X - X - X)
b8.new_ab()
b8.pitch_list("b f b f")
b8.out("G3")

# 6. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("s c f f s")
b8.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("c s b")
b8.hit(2)

# 8. BOS #7  Stephen Drew (X - 39 - X)
b8.new_ab()
b8.pitch_list("b s s s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t9.pitching_substitution(19)

# Offensive change (TOR): Pinch-hitter #26 Adam Lind replaces #16 Mark DeRosa, batting 4th
t9.offensive_substitution(4, 26, "PH")

# 4. TOR #26 Adam Lind (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.out("G3")

# 5. TOR #53 Melky Cabrera (X - X - X)
t9.new_ab()
t9.pitch_list("f c f b b s")
t9.out("K")

# 6. TOR #9  J.P. Arencibia (X - X - X)
t9.new_ab()
t9.pitch_list("b b f f f s")
t9.out("K")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: TOR
# LP: TOR #67 Chien-Ming Wang
game.losing_pitcher(67, is_away_team=True)

# print(game)
game.generate_scorecard()
