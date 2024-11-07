import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2013-06-29
# https://www.baseball-reference.com/boxes/BOS/BOS201306290.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2013/06/29/347956/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-29 16:09-19:14",
        "at": "Fenway Park, Boston, MA",
        "att": "37,437",
        "temp": "82F, Partly Cloudy",
        "wind": "17mph, Out To RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 32,
            "roster": {
                # Lineup
                7: "José Reyes",
                19: "José Bautista",
                10: "Edwin Encarnación",
                26: "Adam Lind",
                16: "Mark DeRosa",
                11: "Rajai Davis",
                28: "Colby Rasmus",
                9: "J.P. Arencibia",
                3: "Maicer Izturis",
                # Starting pitcher
                32: "Esmil Rogers",
                # Bench
                1: "Emilio Bonifácio",
                66: "Munenori Kawasaki",
                22: "Josh Thole",
                # Bullpen
                43: "R.A. Dickey",
                45: "Neil Wagner",
                62: "Aaron Loup",
                57: "Juan Pablo Perez",
                50: "Steve Delabar",
                67: "Chien-Ming Wang",
                56: "Mark Buehrle",
                55: "Josh Johnson",
                38: "Darren Oliver",
                29: "Dustin McGowan",
                27: "Brett Cecil",
                44: "Casey Janssen",
            },
            "lefties": [62, 57, 56, 38, 27],
            "lineup": [
                [7, "6"],
                [19, "9"],
                [10, "0"],
                [26, "3"],
                [16, "5"],
                [11, "7"],
                [28, "8"],
                [9, "2"],
                [3, "4"],
            ],
            "bench": [
                [1, "2B"],
                [66, "2B"],
                [22, "C"],
            ],
            "bullpen": [43, 45, 62, 57, 50, 67, 56, 55, 38, 29, 27, 44],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                10: "Jose Iglesias",
                76: "Jonathan Diaz",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                20: "Ryan Lavarnway",
                5: "Jonny Gomes",
                23: "Brandon Snyder",
                # Bullpen
                64: "Allen Webster",
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                46: "Ryan Dempster",
            },
            "lefties": [22, 30, 32, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [10, "6"],
                [76, "5"],
            ],
            "bench": [
                [37, "1B"],
                [20, "C"],
                [5, "LF"],
                [23, "1B"],
            ],
            "bullpen": [64, 63, 40, 41, 30, 32, 19, 31, 36, 46],
        },
        "umpires": {
            "HP": "Dan Bellino",
            "1B": "Tim Welke",
            "2B": "Mike Everitt",
            "3B": "Bruce Dreckman",
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
# Pitching: BOS #22 Felix Doubront
t1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t1.new_ab()
t1.pitch_list("b s")
t1.out("G5-3")

# 2. TOR #19 José Bautista (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")
t1.advance(2, "10 SB")
t1.thrown_out(3, "10 FC1-4-5", 2, 22)

# 3. TOR #10 Edwin Encarnación (X - X - 19)
t1.new_ab(is_risp=True)
t1.pitch_list("b b c")
t1.reach("FC1-4-5", end_base=2)
t1.advance(4, "26 1B")

# 4. TOR #26 Adam Lind (X - 10 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b s f")
t1.hit(1, rbis=1)

# 5. TOR #16 Mark DeRosa (X - X - 26)
t1.new_ab()
t1.pitch_list("c b d 1 f s")
t1.out("K")


# Bot 1st
# Pitching: TOR #32 Esmil Rogers
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c b t f")
b1.out("G3-1")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c b t f b f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 6. TOR #11 Rajai Davis (X - X - X)
t2.new_ab()
t2.pitch_list("c c f b f b")
t2.hit(2)
t2.advance(3, "28 SB")

# 7. TOR #28 Colby Rasmus (X - 11 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("f b c b c")
t2.out("!K")

# 8. TOR #9  J.P. Arencibia (11 - X - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c s s")
t2.out("K")

# 9. TOR #3  Maicer Izturis (11 - X - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c b")
t2.out("G6-3")


# Bot 2nd
# Pitching: TOR #32 Esmil Rogers
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("c c f")
b2.out("G6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c f f s")
b2.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c f f b b b b")
b2.reach("BB")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
b2.new_ab()
b2.pitch_list("c s s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t3.new_ab()
t3.pitch_list("b f b")
t3.out("(F)P3")

# 2. TOR #19 José Bautista (X - X - X)
t3.new_ab()
t3.pitch_list("c f")
t3.out("G4-3")

# 3. TOR #10 Edwin Encarnación (X - X - X)
t3.new_ab()
t3.pitch_list("c f b")
t3.out("L4")


# Bot 3rd
# Pitching: TOR #32 Esmil Rogers
b3 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("c b f b")
b3.out("G6-3")

# 9. BOS #76 Jonathan Diaz (X - X - X)
b3.new_ab()
b3.out("(F)P3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b f c")
b3.hit(1)

# 2. BOS #18 Shane Victorino (X - X - 2)
b3.new_ab()
b3.pitch_list("b c b b 1 c")
b3.out("G1-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 4. TOR #26 Adam Lind (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.hit(1)
t4.thrown_out(2, "16 DP4-6-3", 1, 22)

# 5. TOR #16 Mark DeRosa (X - X - 26)
t4.new_ab()
t4.pitch_list("b c b s")
t4.out("DP4-6-3")

# 6. TOR #11 Rajai Davis (X - X - X)
t4.new_ab()
t4.pitch_list("b s b b c b")
t4.reach("BB")
t4.thrown_out(2, "28 CS", 3, 22)

# 7. TOR #28 Colby Rasmus (X - X - 11)
t4.new_ab()
t4.pitch_list("c 1 1 1 f b")
t4.no_ab("CS")


# Bot 4th
# Pitching: TOR #32 Esmil Rogers
b4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(2)

# 4. BOS #34 David Ortiz (X - 15 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b b")
b4.out("G5-3")

# 5. BOS #12 Mike Napoli (X - 15 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c c c")
b4.out("!K")

# 6. BOS #29 Daniel Nava (X - 15 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 7. TOR #28 Colby Rasmus (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)

# 8. TOR #9  J.P. Arencibia (X - X - 28)
t5.new_ab()
t5.pitch_list("b b s f s")
t5.out("K")

# 9. TOR #3  Maicer Izturis (X - X - 28)
t5.new_ab()
t5.pitch_list("1 c f c")
t5.out("!K")

# 1. TOR #7  José Reyes (X - X - 28)
t5.new_ab()
t5.out("G4-3")


# Bot 5th
# Pitching: TOR #32 Esmil Rogers
b5 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("b s s")
b5.hit(1)
b5.advance(2, "76 WP")

# 8. BOS #10 Jose Iglesias (X - X - 39)
b5.new_ab()
b5.pitch_list("b f b 1 f b")
b5.out("L5")

# 9. BOS #76 Jonathan Diaz (X - X - 39)
b5.new_ab(is_risp=True)
b5.pitch_list("b c s b f")
b5.wp()
b5.out("L8")

# 1. BOS #2  Jacoby Ellsbury (X - 39 - X)
b5.new_ab(is_risp=True)
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 2. TOR #19 José Bautista (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.hit(4)

# 3. TOR #10 Edwin Encarnación (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G5-3")

# 4. TOR #26 Adam Lind (X - X - X)
t6.new_ab()
t6.pitch_list("c f f f b c")
t6.out("!K")

# 5. TOR #16 Mark DeRosa (X - X - X)
t6.new_ab()
t6.pitch_list("s f b b b")
t6.out("G4-3")


# Bot 6th
# Pitching: TOR #32 Esmil Rogers
b6 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(2)
b6.thrown_out(4, "15 9-2", 1, 32)

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b c b f")
b6.hit(1)
b6.advance(2, "34 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
b6.new_ab()
b6.hit(1)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
b6.new_ab(is_risp=True)
b6.pitch_list("f b b f b s")
b6.out("K")

# 6. BOS #29 Daniel Nava (X - 15 - 34)
b6.new_ab(is_risp=True)
b6.pitch_list("s b d f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Felix Doubront
t7 = game.new_inning()

# 6. TOR #11 Rajai Davis (X - X - X)
t7.new_ab()
t7.pitch_list("b c b f f b d")
t7.reach("BB")
t7.advance(2, "9 SB")

# 7. TOR #28 Colby Rasmus (X - X - 11)
t7.new_ab()
t7.pitch_list("1")
t7.out("F9")

# Pitching change (BOS): #63 Alex Wilson replaces #22 Felix Doubront
t7.pitching_substitution(63)

# 8. TOR #9  J.P. Arencibia (X - X - 11)
t7.new_ab(is_risp=True)
t7.pitch_list("1 1 c s")
t7.out("F9")

# 9. TOR #3  Maicer Izturis (X - 11 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c b f b")
t7.out("G5-3")


# Bot 7th
# Pitching: TOR #38 Darren Oliver
b7 = game.new_inning()

# Pitching change (TOR): #38 Darren Oliver replaces #32 Esmil Rogers
b7.pitching_substitution(38)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.hit(1)
b7.error(4)
b7.advance(2, "10 1B")
b7.advance(3, "10 E4")
b7.thrown_out(4, "76 FC1-2", 1, 38)

# 8. BOS #10 Jose Iglesias (X - X - 39)
b7.new_ab()
b7.hit(1)
b7.advance(2, "76 FC1-2")
b7.advance(3, "2 1B")
b7.advance(4, "18 1B")

# 9. BOS #76 Jonathan Diaz (39 - X - 10)
b7.new_ab(is_risp=True)
b7.pitch_list("c")
b7.reach("FC1-2")
b7.advance(2, "2 1B")
b7.advance(4, "18 1B")

# Pitching change (TOR): #50 Steve Delabar replaces #38 Darren Oliver
b7.pitching_substitution(50)

# 1. BOS #2  Jacoby Ellsbury (X - 10 - 76)
b7.new_ab(is_risp=True)
b7.pitch_list("b b f")
b7.hit(1)
b7.advance(2, "18 1B")

# 2. BOS #18 Shane Victorino (10 - 76 - 2)
b7.new_ab(is_risp=True)
b7.pitch_list("b")
b7.hit(1, rbis=2)

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b7.new_ab(is_risp=True)
b7.pitch_list("b c f f")
b7.out("F9")

# 4. BOS #34 David Ortiz (X - 2 - 18)
b7.new_ab(is_risp=True)
b7.pitch_list("s b f d f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #63 Alex Wilson
t8.pitching_substitution(36)

# 1. TOR #7  José Reyes (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c")
t8.hit(1)
t8.advance(4, "19 HR")

# 2. TOR #19 José Bautista (X - X - 7)
t8.new_ab()
t8.pitch_list("c d b")
t8.hit(4, rbis=2)

# 3. TOR #10 Edwin Encarnación (X - X - X)
t8.new_ab()
t8.pitch_list("s c")
t8.out("F9")

# 4. TOR #26 Adam Lind (X - X - X)
t8.new_ab()
t8.pitch_list("c f f")
t8.hit(3)

# Offensive change (TOR): Pinch-hitter #1 Emilio Bonifácio replaces #16 Mark DeRosa, batting 5th
t8.offensive_substitution(5, 1, "PH")

# 5. TOR #1  Emilio Bonifácio (26 - X - X)
t8.new_ab(is_risp=True)
t8.pitch_list("f b l d")
t8.out("G3")

# 6. TOR #11 Rajai Davis (26 - X - X)
t8.new_ab(is_risp=True)
t8.pitch_list("d")
t8.out("(F)P2")


# Bot 8th
# Pitching: TOR #50 Steve Delabar
b8 = game.new_inning()

# Defensive switch (TOR): #1 Emilio Bonifácio moves to 2B
b8.defensive_switch(1, "4")

# Defensive switch (TOR): #3 Maicer Izturis moves to 3B
b8.defensive_switch(3, "5")

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("f t s")
b8.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("c c f f b c")
b8.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("b s f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #32 Craig Breslow
t9 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
t9.pitching_substitution(32)

# 7. TOR #28 Colby Rasmus (X - X - X)
t9.new_ab()
t9.out("G4-3")

# 8. TOR #9  J.P. Arencibia (X - X - X)
t9.new_ab()
t9.pitch_list("b c f")
t9.error(3)
t9.reach("E3", end_base=2)
t9.advance("U", "7 1B")

# 9. TOR #3  Maicer Izturis (X - 9 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c f s")
t9.out("K")

# 1. TOR #7  José Reyes (X - 9 - X)
t9.new_ab(is_risp=True)
t9.hit(1, rbis=1)
t9.advance("U", "19 2B")

# 2. TOR #19 José Bautista (X - X - 7)
t9.new_ab()
t9.pitch_list("c b f b")
t9.hit(2, rbis=1)
t9.thrown_out(3, "7-6-2-5", 3, 32)


# Bot 9th
# Pitching: TOR #45 Neil Wagner
b9 = game.new_inning()

# Pitching change (TOR): #45 Neil Wagner replaces #50 Steve Delabar
b9.pitching_substitution(45)

# 8. BOS #10 Jose Iglesias (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("G6-3")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #76 Jonathan Diaz, batting 9th
b9.offensive_substitution(9, 37, "PH")

# 9. BOS #37 Mike Carp (X - X - X)
b9.new_ab()
b9.pitch_list("c t b b b b")
b9.reach("BB")
b9.thrown_out(2, "2 DP6-4-3", 2, 45)

# 1. BOS #2  Jacoby Ellsbury (X - X - 37)
b9.new_ab()
b9.pitch_list("c c")
b9.out("DP6-4-3")

# Winning team: TOR
# WP: TOR #50 Steve Delabar
game.winning_pitcher(50, is_away_team=True)

# Loser team: BOS
# LP: BOS #36 Junichi Tazawa
game.losing_pitcher(36)

# print(game)
game.generate_scorecard()
