import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ DET, 2013-06-21
# https://www.baseball-reference.com/boxes/DET/DET201306210.shtml
# https://www.mlb.com/gameday/red-sox-vs-tigers/2013/06/21/347842/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-21 19:08-22:24",
        "at": "Comerica Park, Detroit, MI",
        "att": "41,126",
        "temp": "82F, Partly Cloudy",
        "wind": "10mph, In From RF",
        "away": {
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
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                16: "Will Middlebrooks",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 30, 32, 22],
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
                [16, "3B"],
                [5, "LF"],
                [20, "C"],
            ],
            "bullpen": [63, 40, 41, 56, 30, 32, 36, 19, 54, 22, 46],
        },
        "home": {
            "team": "Detroit Tigers",
            "starter": 58,
            "roster": {
                # Lineup
                4: "Omar Infante",
                48: "Torii Hunter",
                24: "Miguel Cabrera",
                28: "Prince Fielder",
                41: "Victor Martinez",
                27: "Jhonny Peralta",
                34: "Avisaíl García",
                12: "Andy Dirks",
                55: "Brayan Peña",
                # Starting pitcher
                58: "Doug Fister",
                # Bench
                50: "Bryan Holaday",
                39: "Ramon Santiago",
                14: "Austin Jackson",
                32: "Don Kelly",
                # Bullpen
                40: "Phil Coke",
                33: "Drew Smyly",
                53: "Joaquín Benoit",
                21: "Rick Porcello",
                36: "Luke Putkonen",
                52: "Jose Alvarez",
                38: "Darin Downs",
                37: "Max Scherzer",
                62: "Al Alburquerque",
                57: "Evan Reed",
                35: "Justin Verlander",
            },
            "lefties": [40, 33, 52, 38],
            "lineup": [
                [4, "4"],
                [48, "9"],
                [24, "5"],
                [28, "3"],
                [41, "0"],
                [27, "6"],
                [34, "8"],
                [12, "7"],
                [55, "2"],
            ],
            "bench": [
                [50, "C"],
                [39, "SS"],
                [14, "CF"],
                [32, "LF"],
            ],
            "bullpen": [40, 33, 53, 21, 36, 52, 38, 37, 62, 57, 35],
        },
        "umpires": {
            "HP": "Mike DiMuro",
            "1B": "Ted Barrett",
            "2B": "Alfonso Márquez",
            "3B": "Scott Barry",
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
# Pitching: DET #58 Doug Fister
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("G1-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c")
t1.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(1)
t1.thrown_out(2, "34 DP3-6-1", 2, 58)

# 4. BOS #34 David Ortiz (X - X - 15)
t1.new_ab()
t1.pitch_list("b c")
t1.out("DP3-6-1")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. DET #4  Omar Infante (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F9")

# 2. DET #48 Torii Hunter (X - X - X)
b1.new_ab()
b1.pitch_list("b f f b")
b1.hit(2)
b1.advance(3, "24 1B")

# 3. DET #24 Miguel Cabrera (X - 48 - X)
b1.new_ab()
b1.pitch_list("c d")
b1.hit(1)
b1.thrown_out(2, "28 DP6-4-3", 2, 31)

# 4. DET #28 Prince Fielder (48 - X - 24)
b1.new_ab()
b1.pitch_list("b s")
b1.out("DP6-4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: DET #58 Doug Fister
t2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("s b")
t2.hit(1)
t2.advance(2, "29 G4-3")
t2.advance(3, "39 G3")

# 6. BOS #29 Daniel Nava (X - X - 12)
t2.new_ab()
t2.pitch_list("c b b f f")
t2.out("G4-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - X)
t2.new_ab()
t2.pitch_list("b f b")
t2.out("G3")

# 8. BOS #7  Stephen Drew (12 - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("F7")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 5. DET #41 Victor Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.hit(1)
b2.advance(2, "27 1B")
b2.advance(4, "55 1B")

# 6. DET #27 Jhonny Peralta (X - X - 41)
b2.new_ab()
b2.pitch_list("d d")
b2.hit(1)
b2.advance(3, "55 1B")

# 7. DET #34 Avisaíl García (X - 41 - 27)
b2.new_ab()
b2.pitch_list("f d s b s")
b2.out("K")

# 8. DET #12 Andy Dirks (X - 41 - 27)
b2.new_ab()
b2.pitch_list("f b f d")
b2.out("F8")

# 9. DET #55 Brayan Peña (X - 41 - 27)
b2.new_ab()
b2.pitch_list("c b b b c f")
b2.hit(1, rbis=1)
b2.thrown_out(2, "4 FC4", 3, 31)

# 1. DET #4  Omar Infante (27 - X - 55)
b2.new_ab()
b2.pitch_list("b c")
b2.reach("FC4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: DET #58 Doug Fister
t3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t3.new_ab()
t3.pitch_list("c f")
t3.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.advance(3, "18 1B")
t3.advance(4, "15 G5-3")

# 2. BOS #18 Shane Victorino (X - X - 2)
t3.new_ab()
t3.pitch_list("b c 1")
t3.hit(1)
t3.advance(2, "15 G5-3")

# 3. BOS #15 Dustin Pedroia (2 - X - 18)
t3.new_ab()
t3.pitch_list("1 c b")
t3.out("G5-3", rbis=1)

# 4. BOS #34 David Ortiz (X - 18 - X)
t3.new_ab()
t3.pitch_list("i i i i")
t3.reach("IBB")

# 5. BOS #12 Mike Napoli (X - 18 - 34)
t3.new_ab()
t3.pitch_list("s d b")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 2. DET #48 Torii Hunter (X - X - X)
b3.new_ab()
b3.pitch_list("b b f b")
b3.out("P4")

# 3. DET #24 Miguel Cabrera (X - X - X)
b3.new_ab()
b3.pitch_list("b c b s f b b")
b3.reach("BB")
b3.thrown_out(2, "28 DP4-6-3", 2, 31)

# 4. DET #28 Prince Fielder (X - X - 24)
b3.new_ab()
b3.pitch_list("b b c")
b3.out("DP4-6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: DET #58 Doug Fister
t4 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("b c c")
t4.out("F7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("b c f f")
t4.hit(1)
t4.advance(2, "7 1B")
t4.advance(3, "10 1B")
t4.advance(4, "2 2B")

# 8. BOS #7  Stephen Drew (X - X - 39)
t4.new_ab()
t4.pitch_list("f b b f")
t4.hit(1)
t4.advance(2, "10 1B")
t4.advance(4, "2 2B")

# 9. BOS #10 Jose Iglesias (X - 39 - 7)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.advance(3, "2 2B")
t4.advance(4, "18 1B")

# 1. BOS #2  Jacoby Ellsbury (39 - 7 - 10)
t4.new_ab()
t4.hit(2, rbis=2)
t4.advance(4, "18 1B")

# 2. BOS #18 Shane Victorino (10 - 2 - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(1, rbis=2)
t4.advance(2, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t4.new_ab()
t4.pitch_list("c f b 1")
t4.hit(1)
t4.thrown_out(2, "34 DP4-6-3", 2, 38)

# Pitching change (DET): #38 Darin Downs replaces #58 Doug Fister
t4.pitching_substitution(38)

# 4. BOS #34 David Ortiz (X - 18 - 15)
t4.new_ab()
t4.out("DP4-6-3")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 5. DET #41 Victor Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.out("G5-3")

# 6. DET #27 Jhonny Peralta (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("P3")

# 7. DET #34 Avisaíl García (X - X - X)
b4.new_ab()
b4.pitch_list("b f t f f")
b4.out("G3-1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: DET #38 Darin Downs
t5 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.hit(1)
t5.thrown_out(1, "29 DP9-3", 2, 38)

# 6. BOS #29 Daniel Nava (X - X - 12)
t5.new_ab()
t5.pitch_list("c")
t5.out("DP9-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("c b s s")
t5.out("K")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 8. DET #12 Andy Dirks (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(4)

# 9. DET #55 Brayan Peña (X - X - X)
b5.new_ab()
b5.hit(1)
b5.advance(2, "48 1B")
b5.advance(4, "24 HR")

# 1. DET #4  Omar Infante (X - X - 55)
b5.new_ab()
b5.pitch_list("c b t")
b5.out("P4")

# 2. DET #48 Torii Hunter (X - X - 55)
b5.new_ab()
b5.pitch_list("f c")
b5.hit(1)
b5.advance(4, "24 HR")

# 3. DET #24 Miguel Cabrera (X - 55 - 48)
b5.new_ab()
b5.hit(4, rbis=3)

# 4. DET #28 Prince Fielder (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("F8")

# 5. DET #41 Victor Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")

# 6. DET #27 Jhonny Peralta (X - X - 41)
b5.new_ab()
b5.pitch_list("b c b")
b5.out("(F)F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: DET #38 Darin Downs
t6 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("f c b b")
t6.out("G4-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
t6.new_ab()
t6.pitch_list("b c b f")
t6.hit(3)
t6.advance(4, "18 1B")

# 1. BOS #2  Jacoby Ellsbury (10 - X - X)
t6.new_ab()
t6.pitch_list("c c s")
t6.out("K")

# 2. BOS #18 Shane Victorino (10 - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1, rbis=1)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t6.new_ab()
t6.pitch_list("c 1 1 f 1")
t6.out("G6-3")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 7. DET #34 Avisaíl García (X - X - X)
b6.new_ab()
b6.pitch_list("c b f s")
b6.out("K")

# 8. DET #12 Andy Dirks (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")

# 9. DET #55 Brayan Peña (X - X - 12)
b6.new_ab()
b6.pitch_list("b c b f s")
b6.out("K")

# Pitching change (BOS): #36 Junichi Tazawa replaces #31 Jon Lester
b6.pitching_substitution(36)

# 1. DET #4  Omar Infante (X - X - 12)
b6.new_ab()
b6.pitch_list("l")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: DET #40 Phil Coke
t7 = game.new_inning()

# Pitching change (DET): #40 Phil Coke replaces #38 Darin Downs
t7.pitching_substitution(40)

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("b f b c")
t7.out("G4-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("s")
t7.out("G5-3")

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("s s s")
t7.out("K")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# 2. DET #48 Torii Hunter (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.out("G4-3")

# 3. DET #24 Miguel Cabrera (X - X - X)
b7.new_ab()
b7.pitch_list("s b")
b7.hit(1)

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
b7.pitching_substitution(32)

# 4. DET #28 Prince Fielder (X - X - 24)
b7.new_ab()
b7.out("F8")

# 5. DET #41 Victor Martinez (X - X - 24)
b7.new_ab()
b7.pitch_list("b f b c f")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: DET #40 Phil Coke
t8 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("b b s b b")
t8.reach("BB")
t8.advance(3, "7 2B")
t8.advance(4, "18 FC6")

# 8. BOS #7  Stephen Drew (X - X - 39)
t8.new_ab()
t8.pitch_list("b b l")
t8.hit(2)
t8.advance(3, "18 FC6")
t8.advance(4, "34 WP")

# Pitching change (DET): #62 Al Alburquerque replaces #40 Phil Coke
t8.pitching_substitution(62)

# 9. BOS #10 Jose Iglesias (39 - 7 - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (39 - 7 - X)
t8.new_ab()
t8.pitch_list("i i i i")
t8.reach("IBB")
t8.advance(2, "18 FC6")
t8.advance(3, "34 WP")

# 2. BOS #18 Shane Victorino (39 - 7 - 2)
t8.new_ab()
t8.pitch_list("c")
t8.reach("FC6", rbis=1)
t8.advance(2, "34 WP")

# 3. BOS #15 Dustin Pedroia (7 - 2 - 18)
t8.new_ab()
t8.pitch_list("c s f")
t8.out("IF4")

# 4. BOS #34 David Ortiz (7 - 2 - 18)
t8.new_ab()
t8.pitch_list("c b i i i")
t8.wp()
t8.reach("IBB")

# 5. BOS #12 Mike Napoli (2 - 18 - 34)
t8.new_ab()
t8.pitch_list("b b s b")
t8.out("(F)P2")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# 6. DET #27 Jhonny Peralta (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.out("G5-3")

# 7. DET #34 Avisaíl García (X - X - X)
b8.new_ab()
b8.pitch_list("c f b b f f")
b8.out("L8")

# 8. DET #12 Andy Dirks (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")

# 9. DET #55 Brayan Peña (X - X - 12)
b8.new_ab()
b8.pitch_list("c c f")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: DET #57 Evan Reed
t9 = game.new_inning()

# Pitching change (DET): #57 Evan Reed replaces #62 Al Alburquerque
t9.pitching_substitution(57)

# 6. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("c b b c c")
t9.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("b t c f s")
t9.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("c c b b")
t9.hit(1)
t9.error(8)
t9.advance(2, "10 1B")
t9.advance("U", "10 E8")

# 9. BOS #10 Jose Iglesias (X - X - 7)
t9.new_ab()
t9.hit(1)
t9.advance(2, "E8")

# 1. BOS #2  Jacoby Ellsbury (X - 10 - X)
t9.new_ab()
t9.out("L9")


# Bot 9th
# Pitching: BOS #30 Andrew Miller
b9 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #32 Craig Breslow
b9.pitching_substitution(30)

# 1. DET #4  Omar Infante (X - X - X)
b9.new_ab()
b9.pitch_list("b c f f f f s")
b9.out("K")

# 2. DET #48 Torii Hunter (X - X - X)
b9.new_ab()
b9.pitch_list("b b c b b")
b9.reach("BB")
b9.advance(3, "24 1B")
b9.advance(4, "28 FC4-6")

# 3. DET #24 Miguel Cabrera (X - X - 48)
b9.new_ab()
b9.hit(1)
b9.thrown_out(2, "28 FC4-6", 2, 30)

# 4. DET #28 Prince Fielder (48 - X - 24)
b9.new_ab()
b9.pitch_list("c s d f")
b9.reach("FC4-6", rbis=1)

# 5. DET #41 Victor Martinez (X - X - 28)
b9.new_ab()
b9.pitch_list("c b b c")
b9.out("G4-3")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31, is_away_team=True)

# Loser team: DET
# LP: DET #58 Doug Fister
game.losing_pitcher(58)

# print(game)
game.generate_scorecard()
