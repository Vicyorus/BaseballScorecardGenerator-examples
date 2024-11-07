import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2013-06-28
# https://www.baseball-reference.com/boxes/BOS/BOS201306280.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2013/06/28/347939/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-28 19:11-22:33",
        "at": "Fenway Park, Boston, MA",
        "att": "36,383",
        "temp": "77F, Partly Cloudy",
        "wind": "18mph, Out To LF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 55,
            "roster": {
                # Lineup
                7: "José Reyes",
                19: "José Bautista",
                10: "Edwin Encarnación",
                26: "Adam Lind",
                28: "Colby Rasmus",
                11: "Rajai Davis",
                9: "J.P. Arencibia",
                3: "Maicer Izturis",
                1: "Emilio Bonifácio",
                # Starting pitcher
                55: "Josh Johnson",
                # Bench
                66: "Munenori Kawasaki",
                16: "Mark DeRosa",
                22: "Josh Thole",
                # Bullpen
                43: "R.A. Dickey",
                45: "Neil Wagner",
                62: "Aaron Loup",
                57: "Juan Pablo Perez",
                50: "Steve Delabar",
                67: "Chien-Ming Wang",
                56: "Mark Buehrle",
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
                [10, "0"],
                [26, "3"],
                [28, "8"],
                [11, "7"],
                [9, "2"],
                [3, "5"],
                [1, "4"],
            ],
            "bench": [
                [66, "2B"],
                [16, "3B"],
                [22, "C"],
            ],
            "bullpen": [43, 45, 62, 57, 50, 67, 56, 38, 29, 27, 44, 32],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 64,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                64: "Allen Webster",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [63, 40, 41, 30, 32, 31, 59, 36, 19, 22, 46],
        },
        "umpires": {
            "HP": "Bruce Dreckman",
            "1B": "Dan Bellino",
            "2B": "Tim Welke",
            "3B": "Mike Everitt",
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
# Pitching: BOS #64 Allen Webster
t1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t1.new_ab()
t1.pitch_list("b b c c s")
t1.out("K")

# 2. TOR #19 José Bautista (X - X - X)
t1.new_ab()
t1.out("F9")

# 3. TOR #10 Edwin Encarnación (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("F8")


# Bot 1st
# Pitching: TOR #55 Josh Johnson
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b c c b f s")
b1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b f b f t")
b1.out("KT")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c c")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #64 Allen Webster
t2 = game.new_inning()

# 4. TOR #26 Adam Lind (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1)
t2.thrown_out(2, "28 FC4-6", 1, 64)

# 5. TOR #28 Colby Rasmus (X - X - 26)
t2.new_ab()
t2.pitch_list("c")
t2.reach("FC4-6")
t2.thrown_out(2, "11 FC3-6", 2, 64)

# 6. TOR #11 Rajai Davis (X - X - 28)
t2.new_ab()
t2.pitch_list("c")
t2.reach("FC3-6")
t2.advance(2, "9 SB")

# 7. TOR #9  J.P. Arencibia (X - X - 11)
t2.new_ab(is_risp=True)
t2.pitch_list("b 1 b b c f f")
t2.out("G1-3")


# Bot 2nd
# Pitching: TOR #55 Josh Johnson
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b f f b")
b2.out("P5")

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f f b f b")
b2.reach("BB")
b2.advance(2, "29 1B")
b2.advance(4, "7 3B")

# 6. BOS #29 Daniel Nava (X - X - 12)
b2.new_ab()
b2.pitch_list("c b b")
b2.hit(1)
b2.advance(4, "7 3B")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - 29)
b2.new_ab(is_risp=True)
b2.pitch_list("f s s")
b2.out("K")

# 8. BOS #7  Stephen Drew (X - 12 - 29)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.hit(3, rbis=2)

# 9. BOS #10 Jose Iglesias (7 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c s f b")
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #64 Allen Webster
t3 = game.new_inning()

# 8. TOR #3  Maicer Izturis (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")

# 9. TOR #1  Emilio Bonifácio (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G3")

# 1. TOR #7  José Reyes (X - X - X)
t3.new_ab()
t3.pitch_list("b b c")
t3.hit(1)
t3.advance(2, "19 WP")

# 2. TOR #19 José Bautista (X - X - 7)
t3.new_ab(is_risp=True)
t3.pitch_list("c c b b s")
t3.wp()
t3.out("K")


# Bot 3rd
# Pitching: TOR #55 Josh Johnson
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b f")
b3.hit(1)
b3.advance(2, "18 PB")
b3.advance(4, "12 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b3.new_ab(is_risp=True)
b3.pitch_list("1 c 1 b f b s")
b3.pb()
b3.out("K")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c b b f")
b3.out("L7")

# 4. BOS #34 David Ortiz (X - 2 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("i i i i")
b3.reach("IBB")
b3.advance(2, "12 1B")
b3.advance(3, "29 1B")
b3.thrown_out(4, "29 9-2", 3, 55)

# 5. BOS #12 Mike Napoli (X - 2 - 34)
b3.new_ab(is_risp=True)
b3.pitch_list("b s c")
b3.hit(1, rbis=1)
b3.advance(3, "29 9-2")

# 6. BOS #29 Daniel Nava (X - 34 - 12)
b3.new_ab(is_risp=True)
b3.pitch_list("d f d")
b3.hit(1)


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #64 Allen Webster
t4 = game.new_inning()

# 3. TOR #10 Edwin Encarnación (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b b")
t4.reach("BB")
t4.error(6)
t4.advance(2, "28 E6")
t4.advance(3, "11 FC6-4")

# 4. TOR #26 Adam Lind (X - X - 10)
t4.new_ab()
t4.pitch_list("c b b f s")
t4.out("K")

# 5. TOR #28 Colby Rasmus (X - X - 10)
t4.new_ab()
t4.reach("FC6")
t4.thrown_out(2, "11 FC6-4", 2, 64)

# 6. TOR #11 Rajai Davis (X - 10 - 28)
t4.new_ab(is_risp=True)
t4.pitch_list("c f")
t4.reach("FC6-4")
t4.thrown_out(2, "9 FC4-6", 3, 64)

# 7. TOR #9  J.P. Arencibia (10 - X - 11)
t4.new_ab(is_risp=True)
t4.pitch_list("b 1")
t4.reach("FC4-6")


# Bot 4th
# Pitching: TOR #55 Josh Johnson
b4 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("c s s")
b4.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("b b f")
b4.hit(2)
# Offensive change (BOS): Pinch-runner #23 Brandon Snyder replaces #7 Stephen Drew
b4.offensive_substitution(8, 23, "PR")
b4.atbase("PR")
b4.advance(3, "10 1B")
b4.advance(4, "2 1B")

# 9. BOS #10 Jose Iglesias (X - 7 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b")
b4.hit(1)
b4.advance(2, "2 SB")
b4.advance(4, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (23 - X - 10)
b4.new_ab(is_risp=True)
b4.pitch_list("b d f 1 b c")
b4.hit(1, rbis=2)
b4.thrown_out(1, "18 KDP2", 3, 62)

# Pitching change (TOR): #62 Aaron Loup replaces #55 Josh Johnson
b4.pitching_substitution(62)

# 2. BOS #18 Shane Victorino (X - X - 2)
b4.new_ab()
b4.pitch_list("s f b d s")
b4.out("KDP2")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #64 Allen Webster
t5 = game.new_inning()

# Defensive switch (BOS): #23 Brandon Snyder moves to 3B
t5.defensive_switch(23, "5")

# Defensive switch (BOS): #10 Jose Iglesias moves to SS
t5.defensive_switch(10, "6")

# 8. TOR #3  Maicer Izturis (X - X - X)
t5.new_ab()
t5.pitch_list("b b c")
t5.hit(1)
t5.advance(2, "1 BB")
t5.advance(3, "7 FC5-4")
t5.advance(4, "19 1B")

# 9. TOR #1  Emilio Bonifácio (X - X - 3)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")
t5.thrown_out(2, "7 FC5-4", 1, 64)

# 1. TOR #7  José Reyes (X - 3 - 1)
t5.new_ab(is_risp=True)
t5.pitch_list("b c c d b")
t5.reach("FC5-4")
t5.advance(3, "19 1B")
t5.advance(4, "10 1B")

# 2. TOR #19 José Bautista (3 - X - 7)
t5.new_ab(is_risp=True)
t5.pitch_list("c d b b f")
t5.hit(1, rbis=1)
t5.advance(3, "10 1B")
t5.advance(4, "26 SF8")

# 3. TOR #10 Edwin Encarnación (7 - X - 19)
t5.new_ab(is_risp=True)
t5.pitch_list("s f")
t5.hit(1, rbis=1)

# 4. TOR #26 Adam Lind (19 - X - 10)
t5.new_ab(is_risp=True)
t5.out("SF8", rbis=1)

# 5. TOR #28 Colby Rasmus (X - X - 10)
t5.new_ab()
t5.pitch_list("f b b")
t5.out("F8")


# Bot 5th
# Pitching: TOR #62 Aaron Loup
b5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("c f b")
b5.hit(1)
b5.advance(2, "34 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
b5.new_ab()
b5.pitch_list("f")
b5.hit(1)
b5.thrown_out(2, "29 DP6-4-3", 2, 62)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
b5.new_ab(is_risp=True)
b5.pitch_list("b b")
b5.out("L8")

# 6. BOS #29 Daniel Nava (X - 15 - 34)
b5.new_ab(is_risp=True)
b5.pitch_list("f b f b f")
b5.out("DP6-4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #64 Allen Webster
t6 = game.new_inning()

# 6. TOR #11 Rajai Davis (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.hit(1)
t6.advance(2, "9 SB")
t6.advance(3, "9 G3")
t6.advance(4, "3 SF7")

# 7. TOR #9  J.P. Arencibia (X - X - 11)
t6.new_ab(is_risp=True)
t6.pitch_list("f b 1 c")
t6.out("G3")

# 8. TOR #3  Maicer Izturis (11 - X - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b b b c")
t6.out("SF7", rbis=1)

# 9. TOR #1  Emilio Bonifácio (X - X - X)
t6.new_ab()
t6.pitch_list("c s b b b")
t6.out("G3")


# Bot 6th
# Pitching: TOR #62 Aaron Loup
b6 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("F9")

# Pitching change (TOR): #45 Neil Wagner replaces #62 Aaron Loup
b6.pitching_substitution(45)

# 8. BOS #23 Brandon Snyder (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("F8")

# 9. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("c c")
b6.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b6.new_ab()
b6.pitch_list("c f b f 1 f b f")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #40 Andrew Bailey
t7 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #64 Allen Webster
t7.pitching_substitution(40)

# 1. TOR #7  José Reyes (X - X - X)
t7.new_ab()
t7.pitch_list("c f f b s")
t7.out("K")

# 2. TOR #19 José Bautista (X - X - X)
t7.new_ab()
t7.pitch_list("b f c s")
t7.out("K")

# 3. TOR #10 Edwin Encarnación (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(4)

# Pitching change (BOS): #30 Andrew Miller replaces #40 Andrew Bailey
t7.pitching_substitution(30)

# 4. TOR #26 Adam Lind (X - X - X)
t7.new_ab()
t7.pitch_list("b f c s")
t7.out("K")


# Bot 7th
# Pitching: TOR #45 Neil Wagner
b7 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(1)
b7.advance(2, "15 1B")
b7.advance(3, "12 WP")
b7.advance(4, "5 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b7.new_ab()
b7.pitch_list("c")
b7.hit(1)
b7.advance(2, "12 WP")
b7.advance(3, "5 1B")
b7.advance(4, "39 BB")

# Pitching change (TOR): #27 Brett Cecil replaces #45 Neil Wagner
b7.pitching_substitution(27)

# 4. BOS #34 David Ortiz (X - 18 - 15)
b7.new_ab(is_risp=True)
b7.pitch_list("c c f c")
b7.out("!K")

# 5. BOS #12 Mike Napoli (X - 18 - 15)
b7.new_ab(is_risp=True)
b7.pitch_list("d s b d d")
b7.wp()
b7.reach("BB")
b7.advance(2, "5 1B")
b7.advance(3, "39 BB")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #29 Daniel Nava, batting 6th
b7.offensive_substitution(6, 5, "PH")

# 6. BOS #5  Jonny Gomes (18 - 15 - 12)
b7.new_ab(is_risp=True)
b7.pitch_list("b b c b")
b7.hit(1, rbis=1)
b7.advance(2, "39 BB")

# Pitching change (TOR): #38 Darren Oliver replaces #27 Brett Cecil
b7.pitching_substitution(38)

# 7. BOS #39 Jarrod Saltalamacchia (15 - 12 - 5)
b7.new_ab(is_risp=True)
b7.pitch_list("d b b c b")
b7.reach("BB", rbis=1)

# 8. BOS #23 Brandon Snyder (12 - 5 - 39)
b7.new_ab(is_risp=True)
b7.pitch_list("c s b s")
b7.out("K")

# 9. BOS #10 Jose Iglesias (12 - 5 - 39)
b7.new_ab(is_risp=True)
b7.pitch_list("b b c b c")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #30 Andrew Miller
t8 = game.new_inning()

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t8.defensive_switch(5, "7")

# 5. TOR #28 Colby Rasmus (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.out("P3")

# 6. TOR #11 Rajai Davis (X - X - X)
t8.new_ab()
t8.pitch_list("c c b")
t8.hit(1)
t8.thrown_out(2, "9 DP6-4-3", 2, 30)

# 7. TOR #9  J.P. Arencibia (X - X - 11)
t8.new_ab()
t8.pitch_list("b f 1 b c 1 f f f")
t8.out("DP6-4-3")


# Bot 8th
# Pitching: TOR #44 Casey Janssen
b8 = game.new_inning()

# Pitching change (TOR): #44 Casey Janssen replaces #38 Darren Oliver
b8.pitching_substitution(44)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("P6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.hit(3)

# 4. BOS #34 David Ortiz (15 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b f s b b f")
b8.out("G3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #30 Andrew Miller
t9.pitching_substitution(19)

# 8. TOR #3  Maicer Izturis (X - X - X)
t9.new_ab()
t9.pitch_list("c s b f f c")
t9.out("!K")

# 9. TOR #1  Emilio Bonifácio (X - X - X)
t9.new_ab()
t9.pitch_list("f b f f f f f s")
t9.out("K")

# 1. TOR #7  José Reyes (X - X - X)
t9.new_ab()
t9.out("G6-3")

# Winning team: BOS
# WP: BOS #30 Andrew Miller
game.winning_pitcher(30)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: TOR
# LP: TOR #45 Neil Wagner
game.losing_pitcher(45, is_away_team=True)

# print(game)
game.generate_scorecard()
