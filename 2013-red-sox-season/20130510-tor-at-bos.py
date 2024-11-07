import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2013-05-10
# https://www.baseball-reference.com/boxes/BOS/BOS201305100.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2013/05/10/347274/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-10 19:10-21:56",
        "at": "Fenway Park, Boston, MA",
        "att": "33,606",
        "temp": "72F, Partly Cloudy",
        "wind": "11mph, In From RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 34,
            "roster": {
                # Lineup
                11: "Rajai Davis",
                53: "Melky Cabrera",
                19: "José Bautista",
                10: "Edwin Encarnación",
                9: "J.P. Arencibia",
                16: "Mark DeRosa",
                13: "Brett Lawrie",
                28: "Colby Rasmus",
                3: "Maicer Izturis",
                # Starting pitcher
                34: "Ramon Ortiz",
                # Bench
                1: "Emilio Bonifácio",
                66: "Munenori Kawasaki",
                26: "Adam Lind",
                22: "Henry Blanco",
                # Bullpen
                43: "R.A. Dickey",
                62: "Aaron Loup",
                50: "Steve Delabar",
                56: "Mark Buehrle",
                37: "Mickey Storey",
                38: "Darren Oliver",
                23: "Brandon Morrow",
                49: "Brad Lincoln",
                27: "Brett Cecil",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [62, 56, 38, 27],
            "lineup": [
                [11, "0"],
                [53, "7"],
                [19, "9"],
                [10, "3"],
                [9, "2"],
                [16, "4"],
                [13, "5"],
                [28, "8"],
                [3, "6"],
            ],
            "bench": [
                [1, "2B"],
                [66, "2B"],
                [26, "1B"],
                [22, "C"],
            ],
            "bullpen": [43, 62, 50, 56, 37, 38, 23, 49, 27, 44, 32],
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
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
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
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [63, 65, 41, 30, 32, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Alan Porter",
            "1B": "Greg Gibson",
            "2B": "Hunter Wendelstedt",
            "3B": "Jerry Layne",
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

# 1. TOR #11 Rajai Davis (X - X - X)
t1.new_ab()
t1.out("F9")

# 2. TOR #53 Melky Cabrera (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G5-3")

# 3. TOR #19 José Bautista (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("F7")


# Bot 1st
# Pitching: TOR #34 Ramon Ortiz
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b b f b f")
b1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b b c f")
b1.hit(1)
b1.advance(2, "15 BB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b1.new_ab()
b1.pitch_list("b d b b")
b1.reach("BB")
b1.thrown_out(2, "34 DP4-6-3", 2, 34)

# 4. BOS #34 David Ortiz (X - 18 - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("c b s b")
b1.out("DP4-6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
t2.new_ab()
t2.out("G5-3")

# 5. TOR #9  J.P. Arencibia (X - X - X)
t2.new_ab()
t2.pitch_list("c f b f s")
t2.out("K")

# 6. TOR #16 Mark DeRosa (X - X - X)
t2.new_ab()
t2.pitch_list("c b b s b f")
t2.out("G5-3")


# Bot 2nd
# Pitching: TOR #34 Ramon Ortiz
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b c b f")
b2.out("G6-3")

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.advance(3, "39 1B")
b2.advance(4, "16 E6")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)
b2.advance(2, "16 E6")
b2.advance(3, "7 G3-1")

# 8. BOS #16 Will Middlebrooks (29 - X - 39)
b2.new_ab(is_risp=True)
b2.pitch_list("c s b b f")
b2.error(6)
b2.reach("E6", rbis=1)
b2.advance(2, "7 G3-1")

# 9. BOS #7  Stephen Drew (X - 39 - 16)
b2.new_ab(is_risp=True)
b2.pitch_list("d s")
b2.out("G3-1")

# 1. BOS #2  Jacoby Ellsbury (39 - 16 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c f f f")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 7. TOR #13 Brett Lawrie (X - X - X)
t3.new_ab()
t3.out("L5")

# 8. TOR #28 Colby Rasmus (X - X - X)
t3.new_ab()
t3.pitch_list("c b c b b f s")
t3.out("K")

# 9. TOR #3  Maicer Izturis (X - X - X)
t3.new_ab()
t3.pitch_list("c s b")
t3.out("G1-3")


# Bot 3rd
# Pitching: TOR #34 Ramon Ortiz
b3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("b b c b b")
b3.reach("BB")
b3.error(1)
b3.advance(2, "34 POE1")
b3.advance(3, "12 FC5-4")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b3.new_ab()
b3.pitch_list("b 1 1")
b3.out("F9")

# 4. BOS #34 David Ortiz (X - X - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("1 f 1 b 1 b 1 1 i i")
b3.reach("IBB")
b3.thrown_out(2, "12 FC5-4", 2, 34)

# 5. BOS #12 Mike Napoli (X - 18 - 34)
b3.new_ab(is_risp=True)
b3.pitch_list("c f b d f")
b3.reach("FC5-4")

# 6. BOS #29 Daniel Nava (18 - X - 12)
b3.new_ab(is_risp=True)
b3.pitch_list("f b")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 1. TOR #11 Rajai Davis (X - X - X)
t4.new_ab()
t4.pitch_list("b f b b f f")
t4.out("G5-3")

# 2. TOR #53 Melky Cabrera (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("F7")

# 3. TOR #19 José Bautista (X - X - X)
t4.new_ab()
t4.pitch_list("b b")
t4.out("G6-3")


# Bot 4th
# Pitching: TOR #34 Ramon Ortiz
b4 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("c c b f f b f s")
b4.out("K")

# 8. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.hit(2)

# 9. BOS #7  Stephen Drew (X - 16 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("d b c b f")
b4.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("f")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
t5.new_ab()
t5.pitch_list("c f b")
t5.out("G5-3")

# 5. TOR #9  J.P. Arencibia (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("P5")

# 6. TOR #16 Mark DeRosa (X - X - X)
t5.new_ab()
t5.pitch_list("f f b f f b b f")
t5.out("G5-3")


# Bot 5th
# Pitching: TOR #34 Ramon Ortiz
b5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("b c b b b")
b5.reach("BB")
b5.advance(2, "15 1B")
b5.advance(3, "34 FC4-6")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b5.new_ab()
b5.pitch_list("1 c 1 1 s")
b5.hit(1)
b5.thrown_out(2, "34 FC4-6", 1, 34)

# 4. BOS #34 David Ortiz (X - 18 - 15)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.reach("FC4-6")
b5.thrown_out(2, "12 DP6-4-3", 2, 34)

# 5. BOS #12 Mike Napoli (18 - X - 34)
b5.new_ab(is_risp=True)
b5.pitch_list("b b")
b5.out("DP6-4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 7. TOR #13 Brett Lawrie (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f f")
t6.out("L8")

# 8. TOR #28 Colby Rasmus (X - X - X)
t6.new_ab()
t6.pitch_list("b f b c b f")
t6.out("F9")

# 9. TOR #3  Maicer Izturis (X - X - X)
t6.new_ab()
t6.hit(2)

# Offensive change (TOR): Pinch-hitter #26 Adam Lind replaces #11 Rajai Davis, batting 1st
t6.offensive_substitution(1, 26, "PH")

# 1. TOR #26 Adam Lind (X - 3 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b b b c c s")
t6.out("K")


# Bot 6th
# Pitching: TOR #27 Brett Cecil
b6 = game.new_inning()

# Pitching change (TOR): #27 Brett Cecil replaces #34 Ramon Ortiz
b6.pitching_substitution(27)

# Defensive switch (TOR): #26 Adam Lind moves to DH
b6.defensive_switch(26, "0")

# 6. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.out("G2-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.out("P4")

# 8. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.hit(2)

# 9. BOS #7  Stephen Drew (X - 16 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b c s")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #31 Jon Lester
t7 = game.new_inning()

# 2. TOR #53 Melky Cabrera (X - X - X)
t7.new_ab()
t7.pitch_list("c f f b f")
t7.out("G6-3")

# 3. TOR #19 José Bautista (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G6-3")

# 4. TOR #10 Edwin Encarnación (X - X - X)
t7.new_ab()
t7.pitch_list("c b f b b")
t7.out("P4")


# Bot 7th
# Pitching: TOR #27 Brett Cecil
b7 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.hit(1)
b7.advance(2, "18 1B")
b7.advance(3, "15 WP")
b7.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b7.new_ab()
b7.pitch_list("c 1 b 1 f")
b7.hit(1)
b7.advance(2, "15 WP")
b7.advance(3, "15 1B")
b7.advance(4, "29 2B")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b7.new_ab(is_risp=True)
b7.pitch_list("c s b b f d")
b7.wp()
b7.hit(1, rbis=1)
b7.advance(4, "29 2B")

# 4. BOS #34 David Ortiz (18 - X - 15)
b7.new_ab(is_risp=True)
b7.pitch_list("c b 1 b f s")
b7.out("K")

# Pitching change (TOR): #37 Mickey Storey replaces #27 Brett Cecil
b7.pitching_substitution(37)

# 5. BOS #12 Mike Napoli (18 - X - 15)
b7.new_ab(is_risp=True)
b7.pitch_list("c f 1 f s")
b7.out("K")

# 6. BOS #29 Daniel Nava (18 - X - 15)
b7.new_ab(is_risp=True)
b7.pitch_list("b c b")
b7.hit(2, rbis=2)
b7.advance(4, "39 2B")

# 7. BOS #39 Jarrod Saltalamacchia (X - 29 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c s b d b")
b7.hit(2, rbis=1)

# 8. BOS #16 Will Middlebrooks (X - 39 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c f f b")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #31 Jon Lester
t8 = game.new_inning()

# 5. TOR #9  J.P. Arencibia (X - X - X)
t8.new_ab()
t8.pitch_list("c f f")
t8.out("F7")

# 6. TOR #16 Mark DeRosa (X - X - X)
t8.new_ab()
t8.out("G5-3")

# 7. TOR #13 Brett Lawrie (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("L4")


# Bot 8th
# Pitching: TOR #37 Mickey Storey
b8 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("b c f s")
b8.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("c f f")
b8.out("L8")

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("b c s")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #31 Jon Lester
t9 = game.new_inning()

# 8. TOR #28 Colby Rasmus (X - X - X)
t9.new_ab()
t9.pitch_list("f b s b f c")
t9.out("!K")

# 9. TOR #3  Maicer Izturis (X - X - X)
t9.new_ab()
t9.pitch_list("b f f b b")
t9.out("G6-3")

# 1. TOR #26 Adam Lind (X - X - X)
t9.new_ab()
t9.pitch_list("t c b b f f c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31)

# Loser team: TOR
# LP: TOR #34 Ramon Ortiz
game.losing_pitcher(34, is_away_team=True)

# print(game)
game.generate_scorecard()
