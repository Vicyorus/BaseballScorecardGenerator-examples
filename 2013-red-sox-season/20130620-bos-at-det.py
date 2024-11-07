import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ DET, 2013-06-20
# https://www.baseball-reference.com/boxes/DET/DET201306200.shtml
# https://www.mlb.com/gameday/red-sox-vs-tigers/2013/06/20/347830/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-20 19:08-22:01",
        "at": "Comerica Park, Detroit, MI",
        "att": "36,939",
        "temp": "78F, Partly Cloudy",
        "wind": "12mph, Varies",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                16: "Will Middlebrooks",
                10: "Jose Iglesias",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [20, "2"],
                [16, "5"],
                [10, "6"],
            ],
            "bench": [
                [7, "SS"],
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
            ],
            "bullpen": [63, 40, 56, 30, 32, 31, 36, 19, 54, 22, 46],
        },
        "home": {
            "team": "Detroit Tigers",
            "starter": 52,
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
                52: "Jose Alvarez",
                # Bench
                50: "Bryan Holaday",
                39: "Ramon Santiago",
                32: "Don Kelly",
                # Bullpen
                40: "Phil Coke",
                37: "Max Scherzer",
                33: "Drew Smyly",
                53: "Joaquín Benoit",
                46: "Jose Valverde",
                58: "Doug Fister",
                21: "Rick Porcello",
                36: "Luke Putkonen",
                57: "Evan Reed",
                38: "Darin Downs",
                35: "Justin Verlander",
            },
            "lefties": [52, 40, 33, 38],
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
            ],
            "bullpen": [40, 37, 33, 53, 46, 58, 21, 36, 57, 38, 35],
        },
        "umpires": {
            "HP": "Scott Barry",
            "1B": "Mike DiMuro",
            "2B": "Ted Barrett",
            "3B": "Alfonso Márquez",
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
# Pitching: DET #52 Jose Alvarez
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F9")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c b f f b")
t1.out("P6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b c f b f c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. DET #14 Austin Jackson (X - X - X)
b1.new_ab()
b1.pitch_list("c f f b s")
b1.out("K")

# 2. DET #48 Torii Hunter (X - X - X)
b1.new_ab()
b1.pitch_list("b s")
b1.out("G5-3")

# 3. DET #24 Miguel Cabrera (X - X - X)
b1.new_ab()
b1.pitch_list("c b b s s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: DET #52 Jose Alvarez
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("c s s")
t2.out("K")

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.hit(1)
t2.thrown_out(2, "5 DP4-6-3", 2, 52)

# 6. BOS #5  Jonny Gomes (X - X - 12)
t2.new_ab()
t2.pitch_list("b c")
t2.out("DP4-6-3")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 4. DET #28 Prince Fielder (X - X - X)
b2.new_ab()
b2.pitch_list("b b c b")
b2.out("F8")

# 5. DET #41 Victor Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("b c f")
b2.out("G4-3")

# 6. DET #27 Jhonny Peralta (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: DET #52 Jose Alvarez
t3 = game.new_inning()

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t3.new_ab()
t3.pitch_list("b c b s f b")
t3.out("G5-3")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b")
t3.out("F9")

# 9. BOS #10 Jose Iglesias (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(2, "2 BB")
t3.advance(3, "18 HBP")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
t3.new_ab()
t3.pitch_list("b 1 b b b")
t3.reach("BB")
t3.advance(2, "18 HBP")

# 2. BOS #18 Shane Victorino (X - 10 - 2)
t3.new_ab(is_risp=True)
t3.pitch_list("b c c")
t3.reach("HBP")

# 3. BOS #15 Dustin Pedroia (10 - 2 - 18)
t3.new_ab(is_risp=True)
t3.pitch_list("b c")
t3.out("L9")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 7. DET #12 Andy Dirks (X - X - X)
b3.new_ab()
b3.pitch_list("b s c")
b3.out("G4-3")

# 8. DET #4  Omar Infante (X - X - X)
b3.new_ab()
b3.pitch_list("c b c b b")
b3.hit(2)

# 9. DET #55 Brayan Peña (X - 4 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c f b")
b3.out("G5-3")

# 1. DET #14 Austin Jackson (X - 4 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("s")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: DET #52 Jose Alvarez
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.hit(4)

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("b b f b s f f")
t4.out("G6-3")

# 6. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("b s s b b s")
t4.out("K")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.hit(2)

# 8. BOS #16 Will Middlebrooks (X - 20 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b f")
t4.out("G3")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 2. DET #48 Torii Hunter (X - X - X)
b4.new_ab()
b4.pitch_list("b b f")
b4.out("P3")

# 3. DET #24 Miguel Cabrera (X - X - X)
b4.new_ab()
b4.hit(2)
b4.advance(3, "41 WP")

# 4. DET #28 Prince Fielder (X - 24 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b f")
b4.out("F8")

# 5. DET #41 Victor Martinez (X - 24 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b c b f")
b4.wp()
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: DET #52 Jose Alvarez
t5 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(3)
t5.advance(4, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (10 - X - X)
t5.new_ab(is_risp=True)
t5.hit(1, rbis=1)

# 2. BOS #18 Shane Victorino (X - X - 2)
t5.new_ab()
t5.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t5.new_ab()
t5.pitch_list("1 c 1 b 1 s b f f")
t5.out("F9")

# 4. BOS #34 David Ortiz (X - X - 2)
t5.new_ab()
t5.out("F8")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 6. DET #27 Jhonny Peralta (X - X - X)
b5.new_ab()
b5.pitch_list("c s s")
b5.out("K")

# 7. DET #12 Andy Dirks (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")
b5.advance(2, "55 1B")
b5.advance(3, "14 1B")
b5.advance(4, "48 1B")

# 8. DET #4  Omar Infante (X - X - 12)
b5.new_ab()
b5.pitch_list("b 1 c b b")
b5.out("P6")

# 9. DET #55 Brayan Peña (X - X - 12)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(2, "14 1B")
b5.advance(4, "48 1B")

# 1. DET #14 Austin Jackson (X - 12 - 55)
b5.new_ab(is_risp=True)
b5.pitch_list("c")
b5.hit(1)
b5.advance(3, "48 1B")

# 2. DET #48 Torii Hunter (12 - 55 - 14)
b5.new_ab(is_risp=True)
b5.hit(1, rbis=2)

# 3. DET #24 Miguel Cabrera (14 - X - 48)
b5.new_ab(is_risp=True)
b5.pitch_list("s s f b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: DET #36 Luke Putkonen
t6 = game.new_inning()

# Pitching change (DET): #36 Luke Putkonen replaces #52 Jose Alvarez
t6.pitching_substitution(36)

# 5. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("c b b c")
t6.out("F9")

# 6. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("b c b f s")
t6.out("K")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t6.new_ab()
t6.pitch_list("f c b b b")
t6.out("G5-3")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 4. DET #28 Prince Fielder (X - X - X)
b6.new_ab()
b6.hit(1)
b6.thrown_out(2, "41 DP4-6-3", 1, 41)

# 5. DET #41 Victor Martinez (X - X - 28)
b6.new_ab()
b6.pitch_list("c f")
b6.out("DP4-6-3")

# 6. DET #27 Jhonny Peralta (X - X - X)
b6.new_ab()
b6.pitch_list("f b")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: DET #36 Luke Putkonen
t7 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b")
t7.out("F8")

# 9. BOS #10 Jose Iglesias (X - X - X)
t7.new_ab()
t7.pitch_list("b c c")
t7.out("L7")

# Pitching change (DET): #40 Phil Coke replaces #36 Luke Putkonen
t7.pitching_substitution(40)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("c c s")
t7.out("K")


# Bot 7th
# Pitching: BOS #41 John Lackey
b7 = game.new_inning()

# 7. DET #12 Andy Dirks (X - X - X)
b7.new_ab()
b7.pitch_list("f f b")
b7.hit(1)
b7.thrown_out(2, "55 FC4-6", 2, 41)

# 8. DET #4  Omar Infante (X - X - 12)
b7.new_ab()
b7.pitch_list("1")
b7.out("B1")

# 9. DET #55 Brayan Peña (X - X - 12)
b7.new_ab()
b7.reach("FC4-6")

# 1. DET #14 Austin Jackson (X - X - 55)
b7.new_ab()
b7.pitch_list("c b b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: DET #40 Phil Coke
t8 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
t8.advance(2, "15 BB")
t8.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
t8.advance(2, "34 1B")
t8.advance(3, "20 HBP")

# 4. BOS #34 David Ortiz (X - 18 - 15)
t8.new_ab(is_risp=True)
t8.pitch_list("b")
t8.hit(1, rbis=1)
t8.advance(2, "20 HBP")

# Pitching change (DET): #33 Drew Smyly replaces #40 Phil Coke
t8.pitching_substitution(33)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t8.new_ab(is_risp=True)
t8.pitch_list("c s b s")
t8.out("K")

# 6. BOS #5  Jonny Gomes (X - 15 - 34)
t8.new_ab(is_risp=True)
t8.pitch_list("f b")
t8.out("(F)P5")

# 7. BOS #20 Ryan Lavarnway (X - 15 - 34)
t8.new_ab(is_risp=True)
t8.pitch_list("b s")
t8.reach("HBP")

# 8. BOS #16 Will Middlebrooks (15 - 34 - 20)
t8.new_ab(is_risp=True)
t8.pitch_list("b c b")
t8.out("F9")


# Bot 8th
# Pitching: BOS #19 Koji Uehara
b8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #41 John Lackey
b8.pitching_substitution(19)

# 2. DET #48 Torii Hunter (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G6-3")

# 3. DET #24 Miguel Cabrera (X - X - X)
b8.new_ab()
b8.pitch_list("c s s")
b8.out("K")

# 4. DET #28 Prince Fielder (X - X - X)
b8.new_ab()
b8.pitch_list("c s b f")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: DET #33 Drew Smyly
t9 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t9.new_ab()
t9.pitch_list("b c b c f f f c")
t9.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("c f f b f f f")
t9.hit(2)
t9.advance(3, "15 SB")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b b f s")
t9.out("K")


# Bot 9th
# Pitching: BOS #40 Andrew Bailey
b9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
b9.pitching_substitution(40)

# 5. DET #41 Victor Martinez (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c b")
b9.reach("BB")
# Offensive change (DET): Pinch-runner #32 Don Kelly replaces #41 Victor Martinez
b9.offensive_substitution(5, 32, "PR")
b9.atbase("PR")
b9.advance(4, "27 HR")

# 6. DET #27 Jhonny Peralta (X - X - 41)
b9.new_ab()
b9.pitch_list("c f b")
b9.hit(4, rbis=2)

# Winning team: DET
# WP: DET #33 Drew Smyly
game.winning_pitcher(33)

# Loser team: BOS
# LP: BOS #40 Andrew Bailey
game.losing_pitcher(40, is_away_team=True)

# print(game)
game.generate_scorecard()
