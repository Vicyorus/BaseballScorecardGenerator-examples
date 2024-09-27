import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ LAD, 2013-08-23
# https://www.baseball-reference.com/boxes/LAN/LAN201308230.shtml
# https://www.mlb.com/gameday/red-sox-vs-dodgers/2013/08/23/348663/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-23 22:10-00:17 +1",
        "at": "Dodger Stadium, Los Angeles, CA",
        "att": "50,240",
        "temp": "78F, Clear",
        "wind": "3mph, Varies",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                39: "Jarrod Saltalamacchia",
                29: "Daniel Nava",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                41: "John Lackey",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                72: "Xander Bogaerts",
                12: "Mike Napoli",
                # Bullpen
                67: "Brandon Workman",
                56: "Franklin Morales",
                60: "Brayan Villarreal",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "3"],
                [39, "2"],
                [29, "7"],
                [7, "6"],
                [16, "5"],
                [41, "1"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [3, "C"],
                [72, "2B"],
                [12, "1B"],
            ],
            "bullpen": [67, 56, 60, 32, 66, 44, 31, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "Los Angeles Dodgers",
            "starter": 47,
            "roster": {
                # Lineup
                25: "Carl Crawford",
                66: "Yasiel Puig",
                23: "Adrián González",
                13: "Hanley Ramirez",
                16: "Andre Ethier",
                5: "Juan Uribe",
                14: "Mark Ellis",
                18: "Tim Federowicz",
                47: "Ricky Nolasco",
                # Starting pitcher
                47: "Ricky Nolasco",
                # Bench
                6: "Jerry Hairston",
                17: "A.J. Ellis",
                7: "Nick Punto",
                55: "Skip Schumaker",
                # Bullpen
                35: "Chris Capuano",
                21: "Zack Greinke",
                43: "Brandon League",
                75: "Paco Rodríguez",
                56: "J.P. Howell",
                74: "Kenley Jansen",
                99: "Hyun Jin Ryu",
                22: "Clayton Kershaw",
                44: "Chris Withrow",
                49: "Carlos Marmol",
                0: "Brian Wilson",
                54: "Ronald Belisario",
            },
            "lefties": [35, 75, 56, 99, 22],
            "lineup": [
                [25, "7"],
                [66, "9"],
                [23, "3"],
                [13, "6"],
                [16, "8"],
                [5, "5"],
                [14, "4"],
                [18, "2"],
                [47, "1"],
            ],
            "bench": [
                [6, "2B"],
                [17, "C"],
                [7, "2B"],
                [55, "2B"],
            ],
            "bullpen": [35, 21, 43, 75, 56, 74, 99, 22, 44, 49, 0, 54],
        },
        "umpires": {
            "HP": "Gerry Davis",
            "1B": "Dan Iassogna",
            "2B": "Brian Knight",
            "3B": "Mark Carlson",
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
# Pitching: LAD #47 Ricky Nolasco
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b c b s s")
t1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b f s f")
t1.hit(1)

# 4. BOS #34 David Ortiz (X - X - 15)
t1.new_ab()
t1.pitch_list("c 1 b")
t1.out("G4-3")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. LAD #25 Carl Crawford (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("L8")

# 2. LAD #66 Yasiel Puig (X - X - X)
b1.new_ab()
b1.pitch_list("f s b s")
b1.out("K")

# 3. LAD #23 Adrián González (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f t")
b1.out("KT")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: LAD #47 Ricky Nolasco
t2 = game.new_inning()

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("F8")

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b f f")
t2.out("G6-3")

# 7. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 4. LAD #13 Hanley Ramirez (X - X - X)
b2.new_ab()
b2.out("L9")

# 5. LAD #16 Andre Ethier (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.out("F7")

# 6. LAD #5  Juan Uribe (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: LAD #47 Ricky Nolasco
t3 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("b c s c")
t3.out("!K")

# 9. BOS #41 John Lackey (X - X - X)
t3.new_ab()
t3.pitch_list("c f s")
t3.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.out("G3")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 7. LAD #14 Mark Ellis (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F8")

# 8. LAD #18 Tim Federowicz (X - X - X)
b3.new_ab()
b3.pitch_list("b s b f b")
b3.out("F9")

# 9. LAD #47 Ricky Nolasco (X - X - X)
b3.new_ab()
b3.pitch_list("c b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: LAD #47 Ricky Nolasco
t4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("c b f b s")
t4.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c b b")
t4.out("G3")

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b s f")
t4.out("F7")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 1. LAD #25 Carl Crawford (X - X - X)
b4.new_ab()
b4.pitch_list("f b f f f")
b4.hit(1)
b4.advance(2, "13 SB")
b4.advance(4, "13 HR")

# 2. LAD #66 Yasiel Puig (X - X - 25)
b4.new_ab()
b4.pitch_list("s b b s")
b4.out("P4")

# 3. LAD #23 Adrián González (X - X - 25)
b4.new_ab()
b4.pitch_list("c")
b4.out("L9")

# 4. LAD #13 Hanley Ramirez (X - X - 25)
b4.new_ab()
b4.pitch_list("c c b")
b4.hit(4, rbis=2)

# 5. LAD #16 Andre Ethier (X - X - X)
b4.new_ab()
b4.pitch_list("b f s")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: LAD #47 Ricky Nolasco
t5 = game.new_inning()

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b b f")
t5.out("L5")

# 6. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.reach("HBP")
t5.advance(2, "7 1B")

# 7. BOS #7  Stephen Drew (X - X - 29)
t5.new_ab()
t5.pitch_list("d")
t5.hit(1)
t5.thrown_out(2, "16 DP5-4-3", 2, 47)

# 8. BOS #16 Will Middlebrooks (X - 29 - 7)
t5.new_ab()
t5.pitch_list("b c")
t5.out("DP5-4-3")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 6. LAD #5  Juan Uribe (X - X - X)
b5.new_ab()
b5.pitch_list("b s f")
b5.out("G4-3")

# 7. LAD #14 Mark Ellis (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("F7")

# 8. LAD #18 Tim Federowicz (X - X - X)
b5.new_ab()
b5.pitch_list("f s b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: LAD #47 Ricky Nolasco
t6 = game.new_inning()

# 9. BOS #41 John Lackey (X - X - X)
t6.new_ab()
t6.pitch_list("c b c s")
t6.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("b c s")
t6.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("s f b")
t6.out("F9")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 9. LAD #47 Ricky Nolasco (X - X - X)
b6.new_ab()
b6.pitch_list("c s b s")
b6.out("K")

# 1. LAD #25 Carl Crawford (X - X - X)
b6.new_ab()
b6.hit(1)
b6.advance(2, "23 SB")

# 2. LAD #66 Yasiel Puig (X - X - 25)
b6.new_ab()
b6.pitch_list("b f b b")
b6.out("F9")

# 3. LAD #23 Adrián González (X - X - 25)
b6.new_ab()
b6.pitch_list("1 1 c f b b f")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: LAD #47 Ricky Nolasco
t7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.out("L8")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("c b b f b f f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #41 John Lackey
b7 = game.new_inning()

# 4. LAD #13 Hanley Ramirez (X - X - X)
b7.new_ab()
b7.out("F9")

# 5. LAD #16 Andre Ethier (X - X - X)
b7.new_ab()
b7.pitch_list("c f s")
b7.out("K2-3")

# 6. LAD #5  Juan Uribe (X - X - X)
b7.new_ab()
b7.pitch_list("b b s")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: LAD #47 Ricky Nolasco
t8 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.out("L9")

# 7. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("b b c s b f")
t8.out("G4-3")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.pitch_list("c b f")
t8.out("L6")


# Bot 8th
# Pitching: BOS #41 John Lackey
b8 = game.new_inning()

# 7. LAD #14 Mark Ellis (X - X - X)
b8.new_ab()
b8.pitch_list("c s b f b f f")
b8.out("F9")

# 8. LAD #18 Tim Federowicz (X - X - X)
b8.new_ab()
b8.pitch_list("f f")
b8.out("(F)P2")

# Offensive change (LAD): Pinch-hitter #6 Jerry Hairston replaces #47 Ricky Nolasco, batting 9th
b8.offensive_substitution(9, 6, "PH")

# 9. LAD #6  Jerry Hairston (X - X - X)
b8.new_ab()
b8.out("P5")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: LAD #74 Kenley Jansen
t9 = game.new_inning()

# Pitching change (LAD): #74 Kenley Jansen replaces #47 Ricky Nolasco, batting 9th
t9.pitching_substitution(74)
t9.defensive_substitution(9, 74, "1")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #41 John Lackey, batting 9th
t9.offensive_substitution(9, 37, "PH")

# 9. BOS #37 Mike Carp (X - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("b b c c b s")
t9.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("c s b f b f b f")
t9.out("P6")

# Winning team: LAD
# WP: LAD #47 Ricky Nolasco
game.winning_pitcher(47)
# SV: LAD #74 Kenley Jansen
game.save_pitcher(74)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
