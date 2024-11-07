import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ DET, 2013-06-22
# https://www.baseball-reference.com/boxes/DET/DET201306220.shtml
# https://www.mlb.com/gameday/red-sox-vs-tigers/2013/06/22/347858/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-22 19:15-22:20",
        "at": "Comerica Park, Detroit, MI",
        "att": "42,508",
        "temp": "77F, Cloudy",
        "wind": "12mph, In From RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 64,
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
                64: "Allen Webster",
                # Bench
                16: "Will Middlebrooks",
                5: "Jonny Gomes",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 30, 32, 31, 22],
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
                [16, "3B"],
                [5, "LF"],
                [12, "1B"],
                [20, "C"],
            ],
            "bullpen": [63, 40, 41, 56, 30, 32, 31, 36, 19, 22, 46],
        },
        "home": {
            "team": "Detroit Tigers",
            "starter": 37,
            "roster": {
                # Lineup
                14: "Austin Jackson",
                48: "Torii Hunter",
                24: "Miguel Cabrera",
                28: "Prince Fielder",
                41: "Victor Martinez",
                27: "Jhonny Peralta",
                12: "Andy Dirks",
                4: "Omar Infante",
                55: "Brayan Peña",
                # Starting pitcher
                37: "Max Scherzer",
                # Bench
                50: "Bryan Holaday",
                39: "Ramon Santiago",
                32: "Don Kelly",
                34: "Avisaíl García",
                # Bullpen
                40: "Phil Coke",
                33: "Drew Smyly",
                53: "Joaquín Benoit",
                21: "Rick Porcello",
                36: "Luke Putkonen",
                52: "Jose Alvarez",
                38: "Darin Downs",
                62: "Al Alburquerque",
                58: "Doug Fister",
                57: "Evan Reed",
                35: "Justin Verlander",
            },
            "lefties": [40, 33, 52, 38],
            "lineup": [
                [14, "8"],
                [48, "9"],
                [24, "5"],
                [28, "3"],
                [41, "0"],
                [27, "6"],
                [12, "7"],
                [4, "4"],
                [55, "2"],
            ],
            "bench": [
                [50, "C"],
                [39, "SS"],
                [32, "LF"],
                [34, "RF"],
            ],
            "bullpen": [40, 33, 53, 21, 36, 52, 38, 62, 58, 57, 35],
        },
        "umpires": {
            "HP": "Ted Barrett",
            "1B": "Alfonso Márquez",
            "2B": "Scott Barry",
            "3B": "Mike DiMuro",
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
# Pitching: DET #37 Max Scherzer
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b f")
t1.hit(1)
t1.advance(3, "18 1B")
t1.advance(4, "15 DP4-6-3")

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("1 b 1 b c s f")
t1.hit(1)
t1.thrown_out(2, "15 DP4-6-3", 1, 37)

# 3. BOS #15 Dustin Pedroia (2 - X - 18)
t1.new_ab(is_risp=True)
t1.pitch_list("b f 1")
t1.out("DP4-6-3")

# 4. BOS #34 David Ortiz (X - X - X)
t1.new_ab()
t1.pitch_list("b b f")
t1.hit(4)

# 5. BOS #37 Mike Carp (X - X - X)
t1.new_ab()
t1.pitch_list("c c b b c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #64 Allen Webster
b1 = game.new_inning()

# 1. DET #14 Austin Jackson (X - X - X)
b1.new_ab()
b1.pitch_list("b c s b")
b1.hit(1)
b1.advance(2, "48 1B")
b1.advance(3, "24 BB")
b1.advance(4, "41 HR")

# 2. DET #48 Torii Hunter (X - X - 14)
b1.new_ab()
b1.pitch_list("d 1")
b1.hit(1)
b1.advance(2, "24 BB")
b1.advance(4, "41 HR")

# 3. DET #24 Miguel Cabrera (X - 14 - 48)
b1.new_ab(is_risp=True)
b1.pitch_list("b b b b")
b1.reach("BB")
b1.advance(4, "41 HR")

# 4. DET #28 Prince Fielder (14 - 48 - 24)
b1.new_ab(is_risp=True)
b1.pitch_list("s d s b d f s")
b1.out("K")

# 5. DET #41 Victor Martinez (14 - 48 - 24)
b1.new_ab(is_risp=True)
b1.pitch_list("s")
b1.hit(4, rbis=4)

# 6. DET #27 Jhonny Peralta (X - X - X)
b1.new_ab()
b1.pitch_list("b s b s f s")
b1.out("K")

# 7. DET #12 Andy Dirks (X - X - X)
b1.new_ab()
b1.pitch_list("b s")
b1.hit(1)

# 8. DET #4  Omar Infante (X - X - 12)
b1.new_ab()
b1.pitch_list("c s s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: DET #37 Max Scherzer
t2 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c c b")
t2.out("F7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G3-1")

# 8. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G3")


# Bot 2nd
# Pitching: BOS #64 Allen Webster
b2 = game.new_inning()

# 9. DET #55 Brayan Peña (X - X - X)
b2.new_ab()
b2.pitch_list("b s b f b")
b2.hit(1)
b2.thrown_out(2, "14 DP6-4-3", 1, 64)

# 1. DET #14 Austin Jackson (X - X - 55)
b2.new_ab()
b2.pitch_list("c b f b b f")
b2.out("DP6-4-3")

# 2. DET #48 Torii Hunter (X - X - X)
b2.new_ab()
b2.hit(1)
b2.thrown_out(2, "24 CS", 3, 64)

# 3. DET #24 Miguel Cabrera (X - X - 48)
b2.new_ab()
b2.pitch_list("f f b")
b2.no_ab("CS")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: DET #37 Max Scherzer
t3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("s c b b")
t3.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #64 Allen Webster
b3 = game.new_inning()

# 3. DET #24 Miguel Cabrera (X - X - X)
b3.new_ab()
b3.pitch_list("t b s s")
b3.out("K")

# 4. DET #28 Prince Fielder (X - X - X)
b3.new_ab()
b3.pitch_list("b c b f b")
b3.out("G4-3")

# 5. DET #41 Victor Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c b")
b3.reach("BB")

# 6. DET #27 Jhonny Peralta (X - X - 41)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: DET #37 Max Scherzer
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c s b")
t4.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("s b f b f b s")
t4.out("K")

# 5. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b")
t4.hit(1)
t4.error(1)
t4.advance(3, "E1")

# 6. BOS #29 Daniel Nava (37 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c c b")
t4.out("F7")


# Bot 4th
# Pitching: BOS #64 Allen Webster
b4 = game.new_inning()

# 7. DET #12 Andy Dirks (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(2, "55 SB")
b4.advance(4, "14 1B")

# 8. DET #4  Omar Infante (X - X - 12)
b4.new_ab()
b4.out("F8")

# 9. DET #55 Brayan Peña (X - X - 12)
b4.new_ab(is_risp=True)
b4.pitch_list("b s s")
b4.out("F8")

# 1. DET #14 Austin Jackson (X - 12 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("s")
b4.hit(1, rbis=1)

# 2. DET #48 Torii Hunter (X - X - 14)
b4.new_ab()
b4.pitch_list("1 1 s s")
b4.out("L5")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: DET #37 Max Scherzer
t5 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("G4-3")

# 8. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("b b f f b t")
t5.out("KT")

# 9. BOS #10 Jose Iglesias (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(1)
t5.thrown_out(2, "9-6", 3, 37)


# Bot 5th
# Pitching: BOS #64 Allen Webster
b5 = game.new_inning()

# 3. DET #24 Miguel Cabrera (X - X - X)
b5.new_ab()
b5.pitch_list("f b f")
b5.out("G6-3")

# Pitching change (BOS): #56 Franklin Morales replaces #64 Allen Webster
b5.pitching_substitution(56)

# 4. DET #28 Prince Fielder (X - X - X)
b5.new_ab()
b5.pitch_list("c b b f b b")
b5.reach("BB")
b5.advance(4, "41 2B")

# 5. DET #41 Victor Martinez (X - X - 28)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(2, rbis=1)
b5.advance(4, "27 1B")

# 6. DET #27 Jhonny Peralta (X - 41 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.hit(1, rbis=1)
b5.advance(2, "12 1B")

# 7. DET #12 Andy Dirks (X - X - 27)
b5.new_ab()
b5.pitch_list("b f s")
b5.hit(1)

# 8. DET #4  Omar Infante (X - 27 - 12)
b5.new_ab(is_risp=True)
b5.pitch_list("b c b")
b5.out("F9")

# 9. DET #55 Brayan Peña (X - 27 - 12)
b5.new_ab(is_risp=True)
b5.pitch_list("c f")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: DET #37 Max Scherzer
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c c")
t6.hit(2)

# 2. BOS #18 Shane Victorino (X - 2 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c f b s")
t6.out("K")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c")
t6.out("F9")

# 4. BOS #34 David Ortiz (X - 2 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b s b c b")
t6.out("F8")


# Bot 6th
# Pitching: BOS #56 Franklin Morales
b6 = game.new_inning()

# 1. DET #14 Austin Jackson (X - X - X)
b6.new_ab()
b6.pitch_list("c c s")
b6.out("K")

# 2. DET #48 Torii Hunter (X - X - X)
b6.new_ab()
b6.pitch_list("c s s")
b6.out("K")

# 3. DET #24 Miguel Cabrera (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)

# 4. DET #28 Prince Fielder (X - X - 24)
b6.new_ab()
b6.pitch_list("b c b")
b6.out("L7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: DET #37 Max Scherzer
t7 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
t7.new_ab()
t7.pitch_list("c b f b s")
t7.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b")
t7.out("F9")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("f b b c f b c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #56 Franklin Morales
b7 = game.new_inning()

# 5. DET #41 Victor Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b b")
b7.reach("BB")
b7.advance(4, "4 HR")

# 6. DET #27 Jhonny Peralta (X - X - 41)
b7.new_ab()
b7.pitch_list("f b s s")
b7.out("K")

# 7. DET #12 Andy Dirks (X - X - 41)
b7.new_ab()
b7.pitch_list("f t s")
b7.out("K")

# 8. DET #4  Omar Infante (X - X - 41)
b7.new_ab()
b7.pitch_list("c")
b7.hit(4, rbis=2)

# Pitching change (BOS): #63 Alex Wilson replaces #56 Franklin Morales
b7.pitching_substitution(63)

# 9. DET #55 Brayan Peña (X - X - X)
b7.new_ab()
b7.pitch_list("c f")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: DET #62 Al Alburquerque
t8 = game.new_inning()

# Pitching change (DET): #62 Al Alburquerque replaces #37 Max Scherzer
t8.pitching_substitution(62)

# 8. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("b c b b b")
t8.reach("BB")
t8.advance(2, "10 1B")

# 9. BOS #10 Jose Iglesias (X - X - 7)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - 7 - 10)
t8.new_ab(is_risp=True)
t8.pitch_list("b c c")
t8.out("F7")

# 2. BOS #18 Shane Victorino (X - 7 - 10)
t8.new_ab(is_risp=True)
t8.pitch_list("c f s")
t8.out("K")

# 3. BOS #15 Dustin Pedroia (X - 7 - 10)
t8.new_ab(is_risp=True)
t8.pitch_list("b f b f")
t8.out("F8")


# Bot 8th
# Pitching: BOS #63 Alex Wilson
b8 = game.new_inning()

# 1. DET #14 Austin Jackson (X - X - X)
b8.new_ab()
b8.pitch_list("c b b")
b8.hit(1)
b8.advance(2, "48 1B")
b8.advance(3, "24 BB")
b8.advance(4, "28 DP6-4-3")

# 2. DET #48 Torii Hunter (X - X - 14)
b8.new_ab()
b8.pitch_list("b f s")
b8.hit(1)
b8.advance(2, "24 BB")
b8.advance(3, "28 DP6-4-3")

# 3. DET #24 Miguel Cabrera (X - 14 - 48)
b8.new_ab(is_risp=True)
b8.pitch_list("b c s b f f f b b")
b8.reach("BB")
b8.thrown_out(2, "28 DP6-4-3", 1, 63)

# 4. DET #28 Prince Fielder (14 - 48 - 24)
b8.new_ab(is_risp=True)
b8.pitch_list("b")
b8.out("DP6-4-3")

# 5. DET #41 Victor Martinez (48 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("d c c b")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: DET #36 Luke Putkonen
t9 = game.new_inning()

# Pitching change (DET): #36 Luke Putkonen replaces #62 Al Alburquerque
t9.pitching_substitution(36)

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.hit(1)
t9.thrown_out(2, "37 FC4-6", 1, 36)

# 5. BOS #37 Mike Carp (X - X - 34)
t9.new_ab()
t9.pitch_list("b b f c")
t9.reach("FC4-6")
t9.advance(2, "29 1B")
t9.advance(4, "39 1B")

# 6. BOS #29 Daniel Nava (X - X - 37)
t9.new_ab()
t9.pitch_list("f")
t9.hit(1)
t9.advance(2, "39 1B")

# 7. BOS #39 Jarrod Saltalamacchia (X - 37 - 29)
t9.new_ab(is_risp=True)
t9.pitch_list("b b t")
t9.hit(1, rbis=1)
t9.thrown_out(2, "7 DP4-6-3", 2, 36)

# 8. BOS #7  Stephen Drew (X - 29 - 39)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b f")
t9.out("DP4-6-3")

# Winning team: DET
# WP: DET #37 Max Scherzer
game.winning_pitcher(37)

# Loser team: BOS
# LP: BOS #64 Allen Webster
game.losing_pitcher(64, is_away_team=True)

# print(game)
game.generate_scorecard()
