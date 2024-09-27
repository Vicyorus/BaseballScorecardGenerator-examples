import os
from baseball_scorecard.baseball_scorecard import Scorecard

# COL @ BOS, 2013-06-25
# https://www.baseball-reference.com/boxes/BOS/BOS201306250.shtml
# https://www.mlb.com/gameday/rockies-vs-red-sox/2013/06/25/347896/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-25 19:12-22:52",
        "at": "Fenway Park, Boston, MA",
        "att": "36,286",
        "temp": "88F, Partly Cloudy",
        "wind": "13mph, Out To RF",
        "away": {
            "team": "Colorado Rockies",
            "starter": 12,
            "roster": {
                # Lineup
                24: "Dexter Fowler",
                9: "DJ LeMahieu",
                5: "Carlos González",
                3: "Michael Cuddyer",
                17: "Todd Helton",
                20: "Wilin Rosario",
                6: "Corey Dickerson",
                28: "Nolan Arenado",
                18: "Jonathan Herrera",
                # Starting pitcher
                12: "Juan Nicasio",
                # Bench
                15: "Jordan Pacheco",
                8: "Yorvit Torrealba",
                14: "Josh Rutledge",
                21: "Tyler Colvin",
                # Bullpen
                44: "Roy Oswalt",
                34: "Matt Belisle",
                49: "Rex Brothers",
                0: "Adam Ottavino",
                32: "Tyler Chatwood",
                59: "Wilton Lopez",
                62: "Rob Scahill",
                60: "Manny Corpas",
                29: "Jorge De La Rosa",
                88: "Josh Outman",
                45: "Jhoulys Chacín",
            },
            "lefties": [49, 29, 88],
            "lineup": [
                [24, "8"],
                [9, "4"],
                [5, "7"],
                [3, "9"],
                [17, "3"],
                [20, "2"],
                [6, "0"],
                [28, "5"],
                [18, "6"],
            ],
            "bench": [
                [15, "1B"],
                [8, "C"],
                [14, "SS"],
                [21, "RF"],
            ],
            "bullpen": [44, 34, 49, 0, 32, 59, 62, 60, 29, 88, 45],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
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
                46: "Ryan Dempster",
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
                36: "Junichi Tazawa",
                64: "Allen Webster",
                19: "Koji Uehara",
                54: "Pedro Beato",
                22: "Felix Doubront",
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
            "bullpen": [63, 40, 41, 30, 32, 31, 36, 64, 19, 54, 22],
        },
        "umpires": {
            "HP": "Fieldin Culbreth",
            "1B": "Bill Welke",
            "2B": "Adrian Johnson",
            "3B": "Brian O'Nora",
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

# 1. COL #24 Dexter Fowler (X - X - X)
t1.new_ab()
t1.pitch_list("c b b c f b b")
t1.reach("BB")
t1.advance(2, "9 1B")

# 2. COL #9  DJ LeMahieu (X - X - 24)
t1.new_ab()
t1.hit(1)
t1.thrown_out(2, "3 DP6-4-3", 2, 46)

# 3. COL #5  Carlos González (X - 24 - 9)
t1.new_ab()
t1.pitch_list("b b")
t1.out("IF5")

# 4. COL #3  Michael Cuddyer (X - 24 - 9)
t1.new_ab()
t1.pitch_list("c")
t1.out("DP6-4-3")


# Bot 1st
# Pitching: COL #12 Juan Nicasio
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(2)
b1.advance(3, "18 SAC5-3")
b1.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (X - 2 - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("SAC5-3")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1, rbis=1)
b1.advance(2, "34 BB")
b1.advance(3, "12 BB")
b1.advance(4, "29 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
b1.new_ab()
b1.pitch_list("b b b b")
b1.reach("BB")
b1.advance(2, "12 BB")
b1.advance(3, "29 1B")

# 5. BOS #12 Mike Napoli (X - 15 - 34)
b1.new_ab()
b1.pitch_list("d b b c b")
b1.reach("BB")
b1.advance(2, "29 1B")

# 6. BOS #29 Daniel Nava (15 - 34 - 12)
b1.new_ab()
b1.pitch_list("c c b")
b1.hit(1, rbis=1)

# 7. BOS #39 Jarrod Saltalamacchia (34 - 12 - 29)
b1.new_ab()
b1.pitch_list("c c b s")
b1.out("K")

# 8. BOS #7  Stephen Drew (34 - 12 - 29)
b1.new_ab()
b1.pitch_list("b c f b")
b1.out("(F)P5")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 5. COL #17 Todd Helton (X - X - X)
t2.new_ab()
t2.pitch_list("f c")
t2.out("L1")

# 6. COL #20 Wilin Rosario (X - X - X)
t2.new_ab()
t2.pitch_list("b f b b")
t2.hit(4)

# 7. COL #6  Corey Dickerson (X - X - X)
t2.new_ab()
t2.pitch_list("t f f b f")
t2.out("G4-3")

# 8. COL #28 Nolan Arenado (X - X - X)
t2.new_ab()
t2.hit(2)

# 9. COL #18 Jonathan Herrera (X - 28 - X)
t2.new_ab()
t2.pitch_list("b c b")
t2.out("G4-3")


# Bot 2nd
# Pitching: COL #12 Juan Nicasio
b2 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("(F)P3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b2.new_ab()
b2.pitch_list("c s f")
b2.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b2.new_ab()
b2.pitch_list("b c c f")
b2.hit(2)
b2.advance(4, "15 2B")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(2, rbis=1)
b2.advance(4, "34 2B")

# 4. BOS #34 David Ortiz (X - 15 - X)
b2.new_ab()
b2.pitch_list("b b f")
b2.hit(2, rbis=1)
b2.advance(4, "12 1B")

# 5. BOS #12 Mike Napoli (X - 34 - X)
b2.new_ab()
b2.pitch_list("b b c c f f f b")
b2.hit(1, rbis=1)
b2.advance(3, "29 1B")

# 6. BOS #29 Daniel Nava (X - X - 12)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)

# 7. BOS #39 Jarrod Saltalamacchia (12 - X - 29)
b2.new_ab()
b2.pitch_list("b f b f f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 1. COL #24 Dexter Fowler (X - X - X)
t3.new_ab()
t3.pitch_list("c b b s b t")
t3.out("KT")

# 2. COL #9  DJ LeMahieu (X - X - X)
t3.new_ab()
t3.out("L4")

# 3. COL #5  Carlos González (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c")
t3.out("F7")


# Bot 3rd
# Pitching: COL #12 Juan Nicasio
b3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("c c")
b3.out("F7")

# 9. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("b c f")
b3.hit(1)
b3.advance(2, "2 1B")
b3.error(9)
b3.advance(3, "18 1B")
b3.advance(4, "18 E9")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b3.new_ab()
b3.pitch_list("1 b")
b3.hit(1)
b3.advance(3, "18 E9")
b3.advance("U", "15 1B")

# 2. BOS #18 Shane Victorino (X - 10 - 2)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(2, "15 1B")
b3.advance(3, "34 SB")

# 3. BOS #15 Dustin Pedroia (2 - X - 18)
b3.new_ab()
b3.pitch_list("b f b 1")
b3.hit(1, rbis=1)
b3.advance(2, "34 SB")

# Pitching change (COL): #0  Adam Ottavino replaces #12 Juan Nicasio
b3.pitching_substitution(0)

# 4. BOS #34 David Ortiz (X - 18 - 15)
b3.new_ab()
b3.pitch_list("c s f b d f f f d s")
b3.out("K")

# 5. BOS #12 Mike Napoli (18 - 15 - X)
b3.new_ab()
b3.pitch_list("b c b c")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 4. COL #3  Michael Cuddyer (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.advance(2, "17 WP")
t4.advance(4, "28 1B")

# 5. COL #17 Todd Helton (X - X - 3)
t4.new_ab()
t4.pitch_list("f b b f f f f")
t4.wp()
t4.out("F9")

# 6. COL #20 Wilin Rosario (X - 3 - X)
t4.new_ab()
t4.pitch_list("b b b c s")
t4.out("G1-3")

# 7. COL #6  Corey Dickerson (X - 3 - X)
t4.new_ab()
t4.pitch_list("c b f b f f f b f b")
t4.reach("BB")
t4.error(8)
t4.advance(2, "28 1B")
t4.advance(3, "28 E8")

# 8. COL #28 Nolan Arenado (X - 3 - 6)
t4.new_ab()
t4.hit(1, rbis=1)

# 9. COL #18 Jonathan Herrera (6 - X - 28)
t4.new_ab()
t4.pitch_list("d c")
t4.out("G5-3")


# Bot 4th
# Pitching: COL #0  Adam Ottavino
b4 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.thrown_out(2, "39 CS", 2, 0)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
b4.new_ab()
b4.pitch_list("b f b b f s")
b4.out("KDP2-6")

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("b f t b f b")
b4.hit(3)
b4.advance(4, "10 2B")

# 9. BOS #10 Jose Iglesias (7 - X - X)
b4.new_ab()
b4.pitch_list("c b f")
b4.hit(2, rbis=1)

# 1. BOS #2  Jacoby Ellsbury (X - 10 - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 1. COL #24 Dexter Fowler (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("F8")

# 2. COL #9  DJ LeMahieu (X - X - X)
t5.new_ab()
t5.pitch_list("b s b")
t5.out("L9")

# 3. COL #5  Carlos González (X - X - X)
t5.new_ab()
t5.pitch_list("c c s")
t5.out("K")


# Bot 5th
# Pitching: COL #0  Adam Ottavino
b5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("c b b f f b f b")
b5.reach("BB")

# 5. BOS #12 Mike Napoli (X - X - 34)
b5.new_ab()
b5.pitch_list("c b f f d b")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 4. COL #3  Michael Cuddyer (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c c s")
t6.out("K")

# 5. COL #17 Todd Helton (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c c")
t6.out("F7")

# 6. COL #20 Wilin Rosario (X - X - X)
t6.new_ab()
t6.pitch_list("c t b b b f")
t6.hit(1)

# 7. COL #6  Corey Dickerson (X - X - 20)
t6.new_ab()
t6.pitch_list("s s s")
t6.out("K")


# Bot 6th
# Pitching: COL #60 Manny Corpas
b6 = game.new_inning()

# Pitching change (COL): #60 Manny Corpas replaces #0  Adam Ottavino
b6.pitching_substitution(60)

# 6. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("c f s")
b6.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G4-3")

# 8. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #63 Alex Wilson
t7 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #46 Ryan Dempster
t7.pitching_substitution(63)

# 8. COL #28 Nolan Arenado (X - X - X)
t7.new_ab()
t7.hit(1)
t7.advance(4, "18 3B")

# 9. COL #18 Jonathan Herrera (X - X - 28)
t7.new_ab()
t7.pitch_list("c b f")
t7.hit(3, rbis=1)
t7.advance(4, "5 1B")

# 1. COL #24 Dexter Fowler (18 - X - X)
t7.new_ab()
t7.pitch_list("b b f s b c")
t7.out("!K")

# 2. COL #9  DJ LeMahieu (18 - X - X)
t7.new_ab()
t7.pitch_list("s f s")
t7.out("K")

# Pitching change (BOS): #32 Craig Breslow replaces #63 Alex Wilson
t7.pitching_substitution(32)

# 3. COL #5  Carlos González (18 - X - X)
t7.new_ab()
t7.hit(1, rbis=1)

# 4. COL #3  Michael Cuddyer (X - X - 5)
t7.new_ab()
t7.pitch_list("c b s f f b f f f")
t7.out("F9")


# Bot 7th
# Pitching: COL #60 Manny Corpas
b7 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.hit(1)
b7.advance(2, "2 1B")
b7.advance(3, "18 G1")
b7.advance(4, "15 SF8")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b7.new_ab()
b7.hit(1)
b7.advance(2, "18 G1")
b7.advance(4, "12 1B")

# 2. BOS #18 Shane Victorino (X - 10 - 2)
b7.new_ab()
b7.pitch_list("s b b f")
b7.out("G1")

# 3. BOS #15 Dustin Pedroia (10 - 2 - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("SF8", rbis=1)

# 4. BOS #34 David Ortiz (X - 2 - X)
b7.new_ab()
b7.pitch_list("i i i i")
b7.reach("IBB")
b7.advance(2, "12 1B")

# 5. BOS #12 Mike Napoli (X - 2 - 34)
b7.new_ab()
b7.pitch_list("b")
b7.hit(1, rbis=1)

# 6. BOS #29 Daniel Nava (X - 34 - 12)
b7.new_ab()
b7.pitch_list("b c c b b")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# 5. COL #17 Todd Helton (X - X - X)
t8.new_ab()
t8.pitch_list("f c b b f f")
t8.out("(F)P5")

# 6. COL #20 Wilin Rosario (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.hit(1)
t8.advance(3, "6 2B")

# 7. COL #6  Corey Dickerson (X - X - 20)
t8.new_ab()
t8.pitch_list("b c c f f")
t8.hit(2)

# 8. COL #28 Nolan Arenado (20 - 6 - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("F7")

# 9. COL #18 Jonathan Herrera (20 - 6 - X)
t8.new_ab()
t8.out("(F)P3")


# Bot 8th
# Pitching: COL #88 Josh Outman
b8 = game.new_inning()

# Pitching change (COL): #88 Josh Outman replaces #60 Manny Corpas
b8.pitching_substitution(88)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1)
b8.advance(2, "7 1B")
b8.advance(3, "10 WP")
b8.advance(4, "18 G5-3")

# 8. BOS #7  Stephen Drew (X - X - 39)
b8.new_ab()
b8.hit(1)
b8.advance(2, "10 WP")
b8.advance(3, "18 G5-3")

# 9. BOS #10 Jose Iglesias (X - 39 - 7)
b8.new_ab()
b8.pitch_list("b f")
b8.wp()
b8.out("F9")

# 1. BOS #2  Jacoby Ellsbury (39 - 7 - X)
b8.new_ab()
b8.pitch_list("b f b d b")
b8.reach("BB")
b8.advance(2, "18 G5-3")

# 2. BOS #18 Shane Victorino (39 - 7 - 2)
b8.new_ab()
b8.out("G5-3", rbis=1)

# 3. BOS #15 Dustin Pedroia (7 - 2 - X)
b8.new_ab()
b8.pitch_list("b b c b s s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #54 Pedro Beato
t9 = game.new_inning()

# Pitching change (BOS): #54 Pedro Beato replaces #32 Craig Breslow
t9.pitching_substitution(54)

# 1. COL #24 Dexter Fowler (X - X - X)
t9.new_ab()
t9.out("F7")

# 2. COL #9  DJ LeMahieu (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.error(5)
t9.reach("E5")
t9.advance(2, "5 DI")
t9.advance(3, "3 1B")

# 3. COL #5  Carlos González (X - X - 9)
t9.new_ab()
t9.pitch_list("b b f")
t9.out("P4")

# 4. COL #3  Michael Cuddyer (X - 9 - X)
t9.new_ab()
t9.hit(1)
t9.advance(2, "17 DI")

# 5. COL #17 Todd Helton (9 - X - 3)
t9.new_ab()
t9.pitch_list("c f b b f")
t9.out("G1-4-3")

# Winning team: BOS
# WP: BOS #46 Ryan Dempster
game.winning_pitcher(46)

# Loser team: COL
# LP: COL #12 Juan Nicasio
game.losing_pitcher(12, is_away_team=True)

# print(game)
game.generate_scorecard()
