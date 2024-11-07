import os
from baseball_scorecard.baseball_scorecard import Scorecard

# COL @ BOS, 2013-06-26
# https://www.baseball-reference.com/boxes/BOS/BOS201306260.shtml
# https://www.mlb.com/gameday/rockies-vs-red-sox/2013/06/26/347911/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-26 16:06-18:42",
        "at": "Fenway Park, Boston, MA",
        "att": "34,632",
        "temp": "73F, Partly Cloudy",
        "wind": "7mph, In From RF",
        "away": {
            "team": "Colorado Rockies",
            "starter": 44,
            "roster": {
                # Lineup
                9: "DJ LeMahieu",
                5: "Carlos González",
                3: "Michael Cuddyer",
                20: "Wilin Rosario",
                17: "Todd Helton",
                28: "Nolan Arenado",
                21: "Tyler Colvin",
                8: "Yorvit Torrealba",
                14: "Josh Rutledge",
                # Starting pitcher
                44: "Roy Oswalt",
                # Bench
                6: "Corey Dickerson",
                15: "Jordan Pacheco",
                18: "Jonathan Herrera",
                # Bullpen
                62: "Rob Scahill",
                34: "Matt Belisle",
                49: "Rex Brothers",
                60: "Manny Corpas",
                29: "Jorge De La Rosa",
                88: "Josh Outman",
                45: "Jhoulys Chacín",
                0: "Adam Ottavino",
                32: "Tyler Chatwood",
                59: "Wilton Lopez",
                12: "Juan Nicasio",
            },
            "lefties": [49, 29, 88],
            "lineup": [
                [9, "4"],
                [5, "7"],
                [3, "9"],
                [20, "0"],
                [17, "3"],
                [28, "5"],
                [21, "8"],
                [8, "2"],
                [14, "6"],
            ],
            "bench": [
                [6, "LF"],
                [15, "1B"],
                [18, "2B"],
            ],
            "bullpen": [62, 34, 49, 60, 29, 88, 45, 0, 32, 59, 12],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
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
                41: "John Lackey",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                64: "Allen Webster",
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
            "bullpen": [63, 40, 30, 32, 31, 59, 36, 64, 19, 22, 46],
        },
        "umpires": {
            "HP": "Bill Welke",
            "1B": "Adrian Johnson",
            "2B": "Brian O'Nora",
            "3B": "Fieldin Culbreth",
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
# Pitching: BOS #41 John Lackey
t1 = game.new_inning()

# 1. COL #9  DJ LeMahieu (X - X - X)
t1.new_ab()
t1.pitch_list("c f f f b s")
t1.out("K")

# 2. COL #5  Carlos González (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.advance(2, "20 SB")
t1.advance(4, "20 1B")

# 3. COL #3  Michael Cuddyer (X - X - 5)
t1.new_ab()
t1.pitch_list("c c 1 s")
t1.out("K")

# 4. COL #20 Wilin Rosario (X - X - 5)
t1.new_ab(is_risp=True)
t1.pitch_list("s b f f")
t1.hit(1, rbis=1)

# 5. COL #17 Todd Helton (X - X - 20)
t1.new_ab()
t1.pitch_list("c s c")
t1.out("!K")


# Bot 1st
# Pitching: COL #44 Roy Oswalt
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.hit(2)
b1.advance(4, "18 1B")

# 2. BOS #18 Shane Victorino (X - 2 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.hit(1, rbis=1)
b1.advance(4, "34 2B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b1.new_ab()
b1.pitch_list("1 c f f f 1")
b1.out("F8")

# 4. BOS #34 David Ortiz (X - X - 18)
b1.new_ab()
b1.pitch_list("1 c b c b 1")
b1.hit(2, rbis=1)
b1.advance(3, "12 G6-3")
b1.advance(4, "29 1B")

# 5. BOS #12 Mike Napoli (X - 34 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b c c d d")
b1.out("G6-3")

# 6. BOS #29 Daniel Nava (34 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("d b c c d")
b1.hit(1, rbis=1)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
b1.new_ab()
b1.pitch_list("c b c b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 6. COL #28 Nolan Arenado (X - X - X)
t2.new_ab()
t2.pitch_list("c f b s")
t2.out("K")

# 7. COL #21 Tyler Colvin (X - X - X)
t2.new_ab()
t2.pitch_list("b c c f s")
t2.out("K")

# 8. COL #8  Yorvit Torrealba (X - X - X)
t2.new_ab()
t2.pitch_list("c b s c")
t2.out("!K")


# Bot 2nd
# Pitching: COL #44 Roy Oswalt
b2 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("c b f f")
b2.out("P5")

# 9. BOS #10 Jose Iglesias (X - X - X)
b2.new_ab()
b2.pitch_list("l b")
b2.out("B1")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G3-1")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 9. COL #14 Josh Rutledge (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("L4")

# 1. COL #9  DJ LeMahieu (X - X - X)
t3.new_ab()
t3.out("G6-3")

# 2. COL #5  Carlos González (X - X - X)
t3.new_ab()
t3.hit(1)

# 3. COL #3  Michael Cuddyer (X - X - 5)
t3.new_ab()
t3.pitch_list("c c f")
t3.out("F9")


# Bot 3rd
# Pitching: COL #44 Roy Oswalt
b3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.hit(1)
b3.advance(2, "15 1B")
b3.advance(3, "34 BB")
b3.advance(4, "12 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(2, "34 BB")
b3.advance(3, "12 1B")
b3.advance(4, "29 SF8")

# 4. BOS #34 David Ortiz (X - 18 - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("d d b c b")
b3.reach("BB")
b3.advance(2, "12 1B")
b3.advance(3, "29 SF8")

# 5. BOS #12 Mike Napoli (18 - 15 - 34)
b3.new_ab(is_risp=True)
b3.hit(1, rbis=1)
b3.advance(2, "29 SF8")

# 6. BOS #29 Daniel Nava (15 - 34 - 12)
b3.new_ab(is_risp=True)
b3.out("SF8", rbis=1)

# 7. BOS #39 Jarrod Saltalamacchia (34 - 12 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c s f d d s")
b3.out("K")

# 8. BOS #7  Stephen Drew (34 - 12 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("f c")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 4. COL #20 Wilin Rosario (X - X - X)
t4.new_ab()
t4.pitch_list("s f f f f b s")
t4.out("K")

# 5. COL #17 Todd Helton (X - X - X)
t4.new_ab()
t4.pitch_list("c b c b b")
t4.hit(2)

# 6. COL #28 Nolan Arenado (X - 17 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b f d f s")
t4.out("K")

# 7. COL #21 Tyler Colvin (X - 17 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c b t b b c")
t4.out("!K")


# Bot 4th
# Pitching: COL #44 Roy Oswalt
b4 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b4.new_ab()
b4.pitch_list("c c s")
b4.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.out("(F)P5")

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.out("L9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 8. COL #8  Yorvit Torrealba (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.advance(2, "9 G6-3")

# 9. COL #14 Josh Rutledge (X - X - 8)
t5.new_ab()
t5.pitch_list("c b")
t5.out("F9")

# 1. COL #9  DJ LeMahieu (X - X - 8)
t5.new_ab()
t5.pitch_list("b")
t5.out("G6-3")

# 2. COL #5  Carlos González (X - 8 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b c s b b s")
t5.out("K")


# Bot 5th
# Pitching: COL #44 Roy Oswalt
b5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b c b s")
b5.hit(1)
b5.thrown_out(2, "29 FC6", 3, 44)

# 4. BOS #34 David Ortiz (X - X - 15)
b5.new_ab()
b5.out("F9")

# 5. BOS #12 Mike Napoli (X - X - 15)
b5.new_ab()
b5.pitch_list("c 1 f f s")
b5.out("K")

# 6. BOS #29 Daniel Nava (X - X - 15)
b5.new_ab()
b5.pitch_list("b b")
b5.reach("FC6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 3. COL #3  Michael Cuddyer (X - X - X)
t6.new_ab()
t6.hit(4)

# 4. COL #20 Wilin Rosario (X - X - X)
t6.new_ab()
t6.pitch_list("f b f")
t6.hit(2)
t6.advance(3, "28 1B")

# 5. COL #17 Todd Helton (X - 20 - X)
t6.new_ab(is_risp=True)
t6.out("L7")

# 6. COL #28 Nolan Arenado (X - 20 - X)
t6.new_ab(is_risp=True)
t6.hit(1)

# 7. COL #21 Tyler Colvin (20 - X - 28)
t6.new_ab(is_risp=True)
t6.pitch_list("f b f s")
t6.out("K")

# 8. COL #8  Yorvit Torrealba (20 - X - 28)
t6.new_ab(is_risp=True)
t6.out("L8")


# Bot 6th
# Pitching: COL #44 Roy Oswalt
b6 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("c b b f b f s")
b6.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(3)
b6.thrown_out(4, "10 FC6-2", 2, 44)

# 9. BOS #10 Jose Iglesias (7 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("l f")
b6.reach("FC6-2")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b6.new_ab()
b6.pitch_list("c b f")
b6.out("P6")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 9. COL #14 Josh Rutledge (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("F9")

# 1. COL #9  DJ LeMahieu (X - X - X)
t7.new_ab()
t7.out("G1-3")

# 2. COL #5  Carlos González (X - X - X)
t7.new_ab()
t7.pitch_list("c f b s")
t7.out("K")


# Bot 7th
# Pitching: COL #59 Wilton Lopez
b7 = game.new_inning()

# Pitching change (COL): #59 Wilton Lopez replaces #44 Roy Oswalt
b7.pitching_substitution(59)

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("c f")
b7.hit(2)

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b7.new_ab(is_risp=True)
b7.out("F9")

# 4. BOS #34 David Ortiz (X - 18 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("i i i i")
b7.reach("IBB")

# 5. BOS #12 Mike Napoli (X - 18 - 34)
b7.new_ab(is_risp=True)
b7.pitch_list("f")
b7.out("(F)P2")

# 6. BOS #29 Daniel Nava (X - 18 - 34)
b7.new_ab(is_risp=True)
b7.pitch_list("c b b b f c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #41 John Lackey
t8.pitching_substitution(36)

# 3. COL #3  Michael Cuddyer (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.hit(4)

# 4. COL #20 Wilin Rosario (X - X - X)
t8.new_ab()
t8.out("G4-3")

# 5. COL #17 Todd Helton (X - X - X)
t8.new_ab()
t8.pitch_list("c c s")
t8.out("K2-3")

# 6. COL #28 Nolan Arenado (X - X - X)
t8.new_ab()
t8.out("G5-3")


# Bot 8th
# Pitching: COL #59 Wilton Lopez
b8 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("b f f b b d")
b8.reach("BB")
b8.thrown_out(2, "10 DP6-4-3", 2, 59)

# 8. BOS #7  Stephen Drew (X - X - 39)
b8.new_ab()
b8.out("L8")

# 9. BOS #10 Jose Iglesias (X - X - 39)
b8.new_ab()
b8.pitch_list("b 1 f f f d")
b8.out("DP6-4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t9.pitching_substitution(19)

# 7. COL #21 Tyler Colvin (X - X - X)
t9.new_ab()
t9.pitch_list("b s b b f f f c")
t9.out("!K")

# 8. COL #8  Yorvit Torrealba (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G6-3")

# 9. COL #14 Josh Rutledge (X - X - X)
t9.new_ab()
t9.pitch_list("c c c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #41 John Lackey
game.winning_pitcher(41)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: COL
# LP: COL #44 Roy Oswalt
game.losing_pitcher(44, is_away_team=True)

# print(game)
game.generate_scorecard()
